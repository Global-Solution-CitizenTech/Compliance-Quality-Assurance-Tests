#!/usr/bin/env python3
"""
ZelaFix - Motor Central de Sincronização, Commits e Governança
Orquestra as operações de Backlogs, Rastreamento de Commits Git e Governança Scrum.
"""

import sys
import os
import re
import html
import subprocess
from typing import Dict, Any, List, Optional, Tuple

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from config import (
    AZURE_ORG, AZURE_PROJECT, AZURE_PAT, GITHUB_ORG,
    DISCIPLINES, TEAM_MEMBERS
)
from azure_client import AzureClient
from parser_backlog import (
    parse_backlog_markdown,
    clean_title,
    validate_backlog_document,
    BacklogValidationError,
)


class SyncEngine:
    """Motor unificado de operações do Azure Boards para o ZelaFix."""

    def __init__(self, client: Optional[AzureClient] = None):
        self.client = client or AzureClient(AZURE_ORG, AZURE_PROJECT, AZURE_PAT)
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.backlogs_dir = os.path.join(self.script_dir, "backlog-materias")
        self.root_dir = os.path.dirname(os.path.dirname(self.script_dir))

    # =========================================================================
    # 1. SINCRONIZAÇÃO DE BACKLOGS (ÉPICOS, FEATURES E PBIS)
    # =========================================================================
    def sync_discipline(self, discipline_key: str, dry_run: bool = False) -> Dict[str, int]:
        """Sincroniza o backlog de uma matéria específica."""
        d_info = DISCIPLINES.get(discipline_key.lower())
        if not d_info:
            raise ValueError(f"Disciplina '{discipline_key}' não encontrada. Opções: {list(DISCIPLINES.keys())}")

        file_path = os.path.join(self.backlogs_dir, d_info["file"])
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Arquivo de backlog não encontrado: {file_path}")

        exact_tag_only = True
        doc = parse_backlog_markdown(
            file_path,
            strict=True,
            required_tag=d_info["tag"],
            exact_tag_only=exact_tag_only,
        )
        stats = {"epics": 0, "features": 0, "pbis": 0, "errors": 0}

        prefix = "[DRY-RUN] " if dry_run else ""
        print(f"\n========================================================")
        print(f"🚀 {prefix}Sincronizando: {d_info['name']}")
        print(f"🏷️ Tag: [{d_info['tag']}] | 📅 Iteração: [{AZURE_PROJECT}\\{d_info['iteration']}]")
        print(f"👤 Responsável: {d_info['owner_name']} ({d_info['owner_email']})")
        print(f"========================================================")

        iteration_path = f"{AZURE_PROJECT}\\{d_info['iteration']}"
        item_tags = [d_info["tag"]]
        owner_email = d_info["owner_email"]

        # 1. Cria o Epic
        epic = doc.epic
        epic_title = clean_title(epic.title)
        print(f"\n👑 Criando Epic: {epic_title} ({epic.effort} SP | BV: {epic.business_value})")

        epic_res = self.client.create_work_item(
            work_item_type="Epic",
            title=epic_title,
            description=epic.description,
            acceptance_criteria=epic.acceptance_criteria,
            priority=epic.priority,
            effort=epic.effort,
            business_value=epic.business_value,
            start_date=epic.start_date,
            target_date=epic.target_date,
            tags=item_tags,
            iteration_path=iteration_path,
            assigned_to=owner_email,
            state="In Progress",
            dry_run=dry_run
        )
        epic_id = epic_res.get("id", 1000)
        stats["epics"] += 1
        print(f"   └── ✅ Epic #{epic_id} criado com sucesso!")

        # 2. Cria as Features vinculadas ao Epic
        for f_idx, feat in enumerate(epic.features, 1):
            feat_title = clean_title(feat.title)
            print(f"\n   🏆 [{f_idx}/{len(epic.features)}] Feature: {feat_title} ({feat.effort} SP | BV: {feat.business_value})")

            relations = []
            if not dry_run:
                relations.append({
                    "rel": "System.LinkTypes.Hierarchy-Reverse",
                    "url": f"{self.client.base_url}/_apis/wit/workitems/{epic_id}",
                    "attributes": {"comment": f"Vinculado ao Epic #{epic_id}"}
                })

            feat_res = self.client.create_work_item(
                work_item_type="Feature",
                title=feat_title,
                description=feat.description,
                acceptance_criteria=feat.acceptance_criteria,
                priority=feat.priority,
                effort=feat.effort,
                business_value=feat.business_value,
                start_date=feat.start_date,
                target_date=feat.target_date,
                tags=item_tags,
                iteration_path=iteration_path,
                assigned_to=owner_email,
                state="In Progress",
                relations=relations,
                dry_run=dry_run
            )
            feat_id = feat_res.get("id", 2000 + f_idx)
            stats["features"] += 1
            print(f"       └── ✅ Feature #{feat_id} vinculada ao Epic #{epic_id}")

            # 3. Cria os PBIs vinculados à Feature
            for p_idx, pbi in enumerate(feat.pbis, 1):
                pbi_title = clean_title(pbi.title)
                print(f"       ├── 📄 [{p_idx}/{len(feat.pbis)}] PBI: {pbi_title} ({pbi.story_points} SP | BV: {pbi.business_value})")

                pbi_relations = []
                if not dry_run:
                    pbi_relations.append({
                        "rel": "System.LinkTypes.Hierarchy-Reverse",
                        "url": f"{self.client.base_url}/_apis/wit/workitems/{feat_id}",
                        "attributes": {"comment": f"Vinculado à Feature #{feat_id}"}
                    })

                pbi_res = self.client.create_work_item(
                    work_item_type="Product Backlog Item",
                    title=pbi_title,
                    description=pbi.description,
                    acceptance_criteria=pbi.acceptance_criteria,
                    priority=pbi.priority,
                    effort=pbi.story_points,
                    business_value=pbi.business_value,
                    tags=item_tags,
                    iteration_path=iteration_path,
                    assigned_to=owner_email,
                    state="Committed",
                    relations=pbi_relations,
                    dry_run=dry_run
                )
                stats["pbis"] += 1

        print(f"\n✨ {prefix}Disciplina {d_info['name']} sincronizada com sucesso!")
        return stats

    def sync_all_disciplines(self, dry_run: bool = False) -> Dict[str, int]:
        """Sincroniza os backlogs de todas as 7 disciplinas."""
        totals = {"epics": 0, "features": 0, "pbis": 0}
        for key in DISCIPLINES.keys():
            res = self.sync_discipline(key, dry_run=dry_run)
            totals["epics"] += res["epics"]
            totals["features"] += res["features"]
            totals["pbis"] += res["pbis"]

        print("\n========================================================")
        print("🎉 SINCRONIZAÇÃO TOTAL CONCLUÍDA!")
        print(f"👑 Epics    : {totals['epics']}")
        print(f"🏆 Features : {totals['features']}")
        print(f"📄 PBIs     : {totals['pbis']}")
        print("========================================================\n")
        return totals

    # =========================================================================
    # 1.1 ATUALIZAÇÃO INTELIGENTE DE BACKLOGS (SMART UPSERT)
    # =========================================================================
    def _normalize_html(self, text: Optional[str]) -> str:
        if not text:
            return ""
        # Decodifica entidades HTML para evitar falsos positivos (&quot;, &#x27;, etc.)
        s = html.unescape(text)
        # Normaliza tags self-closing do Azure DevOps (ex: <br/> vs <br>)
        s = re.sub(r"<br\s*/?>", "<br>", s, flags=re.IGNORECASE)
        # Remove espaços supérfluos adjacentes a tags
        s = re.sub(r"\s+<", "<", s)
        s = re.sub(r">\s+", ">", s)
        # Normaliza espaços múltiplos
        return re.sub(r"\s+", " ", s).strip()

    def _build_upsert_patch(
        self,
        current_wi: Dict[str, Any],
        title: str,
        description: str,
        acceptance_criteria: str,
        effort: Optional[float],
        priority: int,
        business_value: int,
        start_date: Optional[str],
        target_date: Optional[str],
        tags: List[str],
        iteration_path: str,
        assigned_to: str,
        state: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        fields = current_wi.get("fields", {})
        patch = []

        # 1. Título
        curr_title = clean_title(fields.get("System.Title", ""))
        target_title = clean_title(title)
        if target_title and target_title != curr_title:
            patch.append({"op": "add", "path": "/fields/System.Title", "value": target_title})

        # 2. Descrição (User Story)
        if self._normalize_html(description) != self._normalize_html(fields.get("System.Description", "")):
            patch.append({"op": "add", "path": "/fields/System.Description", "value": description})

        # 3. Critérios de Aceite
        if self._normalize_html(acceptance_criteria) != self._normalize_html(fields.get("Microsoft.VSTS.Common.AcceptanceCriteria", "")):
            patch.append({"op": "add", "path": "/fields/Microsoft.VSTS.Common.AcceptanceCriteria", "value": acceptance_criteria})

        # 4. Esforço / Story Points
        if effort is not None and effort > 0:
            curr_effort = float(fields.get("Microsoft.VSTS.Scheduling.Effort", 0) or 0)
            if round(curr_effort, 2) != round(float(effort), 2):
                patch.append({"op": "add", "path": "/fields/Microsoft.VSTS.Scheduling.Effort", "value": float(effort)})

        # 5. Prioridade
        curr_prio = int(fields.get("Microsoft.VSTS.Common.Priority", 0) or 0)
        if curr_prio != int(priority):
            patch.append({"op": "add", "path": "/fields/Microsoft.VSTS.Common.Priority", "value": int(priority)})

        # 6. Business Value
        curr_bv = int(fields.get("Microsoft.VSTS.Common.BusinessValue", 0) or 0)
        if curr_bv != int(business_value):
            patch.append({"op": "add", "path": "/fields/Microsoft.VSTS.Common.BusinessValue", "value": int(business_value)})

        # 7. Datas
        if start_date:
            curr_sd = (fields.get("Microsoft.VSTS.Scheduling.StartDate", "") or "")[:10]
            if curr_sd != start_date:
                patch.append({"op": "add", "path": "/fields/Microsoft.VSTS.Scheduling.StartDate", "value": f"{start_date}T00:00:00Z"})
        if target_date:
            curr_td = (fields.get("Microsoft.VSTS.Scheduling.TargetDate", "") or "")[:10]
            if curr_td != target_date:
                patch.append({"op": "add", "path": "/fields/Microsoft.VSTS.Scheduling.TargetDate", "value": f"{target_date}T00:00:00Z"})

        # 8. Iteração
        curr_iter = fields.get("System.IterationPath", "")
        if curr_iter != iteration_path:
            patch.append({"op": "add", "path": "/fields/System.IterationPath", "value": iteration_path})

        # 9. Atribuição
        curr_assigned = fields.get("System.AssignedTo")
        assigned_val = curr_assigned.get("uniqueName") or curr_assigned.get("displayName") if isinstance(curr_assigned, dict) else str(curr_assigned or "")
        if assigned_to and assigned_val != assigned_to:
            patch.append({"op": "add", "path": "/fields/System.AssignedTo", "value": assigned_to})

        # 10. Tags
        curr_tags = sorted([t.strip() for t in (fields.get("System.Tags", "") or "").split(";") if t.strip()])
        expected_tags = sorted([t.strip() for t in tags if t.strip()])
        if curr_tags != expected_tags:
            op = "replace" if fields.get("System.Tags") else "add"
            patch.append({"op": op, "path": "/fields/System.Tags", "value": "; ".join(expected_tags)})

        # 11. Estado
        if state and fields.get("System.State") != state:
            patch.append({"op": "add", "path": "/fields/System.State", "value": state})

        return patch

    def _ensure_parent_link(self, child_wi: Dict[str, Any], parent_id: int) -> Optional[Dict[str, Any]]:
        relations = child_wi.get("relations") or []
        for r in relations:
            if r.get("rel") == "System.LinkTypes.Hierarchy-Reverse" and str(parent_id) in r.get("url", ""):
                return None
        return {
            "op": "add",
            "path": "/relations/-",
            "value": {
                "rel": "System.LinkTypes.Hierarchy-Reverse",
                "url": f"{self.client.base_url}/_apis/wit/workitems/{parent_id}",
                "attributes": {"comment": f"Vinculado ao pai #{parent_id}"}
            }
        }

    def _build_commit_link_ops(self, wi: Dict[str, Any], commits: List[Tuple[str, str]], repo_name: str) -> List[Dict[str, Any]]:
        if not commits:
            return []
        relations = wi.get("relations") or []
        existing_urls = {r.get("url", "").lower() for r in relations}
        patch = []
        for sha, msg in commits:
            sha_clean = sha.strip()
            already_linked = any(sha_clean.lower() in u for u in existing_urls)
            if already_linked:
                continue

            if repo_name == "Java-Advanced":
                proj_id = "8ab7cd90-8fe0-4879-8e32-8d20a047dfb5"
                repo_id = "fa53ca63-cd58-4070-9aba-7b307a38f670"
                art_url = f"vstfs:///Git/Commit/{proj_id}%2F{repo_id}%2F{sha_clean}"
                patch.append({
                    "op": "add",
                    "path": "/relations/-",
                    "value": {
                        "rel": "ArtifactLink",
                        "url": art_url,
                        "attributes": {"name": "Fixed in Commit", "comment": f"Commit {sha_clean[:7]}: {msg}"}
                    }
                })
            else:
                commit_url = f"https://github.com/{GITHUB_ORG}/{repo_name}/commit/{sha_clean}"
                patch.append({
                    "op": "add",
                    "path": "/relations/-",
                    "value": {
                        "rel": "Hyperlink",
                        "url": commit_url,
                        "attributes": {"comment": f"Commit {sha_clean[:7]}: {msg}"}
                    }
                })
        return patch

    def update_discipline(self, discipline_key: str, dry_run: bool = False) -> Dict[str, int]:
        """Sincroniza e atualiza com inteligência (Upsert) os itens de uma disciplina específica."""
        d_info = DISCIPLINES.get(discipline_key.lower())
        if not d_info:
            raise ValueError(f"Disciplina '{discipline_key}' não encontrada. Opções: {list(DISCIPLINES.keys())}")

        file_path = os.path.join(self.backlogs_dir, d_info["file"])
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Arquivo de backlog não encontrado: {file_path}")

        exact_tag_only = True
        doc = parse_backlog_markdown(
            file_path,
            strict=True,
            required_tag=d_info["tag"],
            exact_tag_only=exact_tag_only,
        )

        prefix = "[DRY-RUN] " if dry_run else ""
        print(f"\n========================================================")
        print(f"🔄 {prefix}Smart Upsert (Atualização Inteligente): {d_info['name']}")
        print(f"🏷️ Tag: [{d_info['tag']}] | 📅 Iteração: [{AZURE_PROJECT}\\{d_info['iteration']}]")
        print(f"👤 Responsável: {d_info['owner_name']} ({d_info['owner_email']})")
        print(f"========================================================")

        iteration_path = f"{AZURE_PROJECT}\\{d_info['iteration']}"
        item_tags = [d_info["tag"]]
        owner_email = d_info["owner_email"]
        repo_name = d_info["repo"]

        stats = {"updated": 0, "created": 0, "unchanged": 0, "commits_linked": 0}

        # 1. Trata o Epic
        epic = doc.epic
        epic_title = clean_title(epic.title)
        epic_id = epic.azure_id
        curr_epic = self.client.get_work_item(epic_id) if epic_id else None

        if curr_epic:
            patch = self._build_upsert_patch(
                curr_epic, epic_title, epic.description, epic.acceptance_criteria,
                epic.effort, epic.priority, epic.business_value, epic.start_date,
                epic.target_date, item_tags, iteration_path, owner_email, state="In Progress"
            )
            if patch:
                self.client.update_work_item(epic_id, patch, dry_run=dry_run)
                stats["updated"] += 1
                print(f"👑 Epic #{epic_id}: 🔄 Atualizado ({len(patch)} alterações)")
            else:
                stats["unchanged"] += 1
                print(f"👑 Epic #{epic_id}: ⏺️ Inalterado (já sincronizado)")
        else:
            print(f"👑 Epic: 🆕 Criando novo item '{epic_title}'...")
            epic_res = self.client.create_work_item(
                work_item_type="Epic",
                title=epic_title,
                description=epic.description,
                acceptance_criteria=epic.acceptance_criteria,
                priority=epic.priority,
                effort=epic.effort,
                business_value=epic.business_value,
                start_date=epic.start_date,
                target_date=epic.target_date,
                tags=item_tags,
                iteration_path=iteration_path,
                assigned_to=owner_email,
                state="In Progress",
                dry_run=dry_run
            )
            epic_id = epic_res.get("id", 1000)
            stats["created"] += 1
            print(f"   └── ✅ Epic #{epic_id} criado com sucesso!")

        # 2. Trata as Features
        for feat in epic.features:
            feat_title = clean_title(feat.title)
            feat_id = feat.azure_id
            curr_feat = self.client.get_work_item(feat_id) if feat_id else None

            if curr_feat:
                patch = self._build_upsert_patch(
                    curr_feat, feat_title, feat.description, feat.acceptance_criteria,
                    feat.effort, feat.priority, feat.business_value, feat.start_date,
                    feat.target_date, item_tags, iteration_path, owner_email, state="In Progress"
                )
                parent_op = self._ensure_parent_link(curr_feat, epic_id)
                if parent_op:
                    patch.append(parent_op)

                if patch:
                    self.client.update_work_item(feat_id, patch, dry_run=dry_run)
                    stats["updated"] += 1
                    print(f"   🏆 Feature #{feat_id}: 🔄 Atualizada ({len(patch)} alterações)")
                else:
                    stats["unchanged"] += 1
                    print(f"   🏆 Feature #{feat_id}: ⏺️ Inalterada")
            else:
                print(f"   🏆 Feature: 🆕 Criando '{feat_title}' vinculada ao Epic #{epic_id}...")
                feat_relations = [{
                    "rel": "System.LinkTypes.Hierarchy-Reverse",
                    "url": f"{self.client.base_url}/_apis/wit/workitems/{epic_id}",
                    "attributes": {"comment": f"Vinculado ao Epic #{epic_id}"}
                }]
                feat_res = self.client.create_work_item(
                    work_item_type="Feature",
                    title=feat_title,
                    description=feat.description,
                    acceptance_criteria=feat.acceptance_criteria,
                    priority=feat.priority,
                    effort=feat.effort,
                    business_value=feat.business_value,
                    start_date=feat.start_date,
                    target_date=feat.target_date,
                    tags=item_tags,
                    iteration_path=iteration_path,
                    assigned_to=owner_email,
                    state="In Progress",
                    relations=feat_relations,
                    dry_run=dry_run
                )
                feat_id = feat_res.get("id", 2000)
                stats["created"] += 1
                print(f"       └── ✅ Feature #{feat_id} criada!")

            # 3. Trata os PBIs vinculados à Feature
            for pbi in feat.pbis:
                pbi_title = clean_title(pbi.title)
                pbi_id = pbi.azure_id
                curr_pbi = self.client.get_work_item(pbi_id) if pbi_id else None

                if curr_pbi:
                    patch = self._build_upsert_patch(
                        curr_pbi, pbi_title, pbi.description, pbi.acceptance_criteria,
                        pbi.story_points, pbi.priority, pbi.business_value, None,
                        None, item_tags, iteration_path, owner_email, state="Committed"
                    )
                    parent_op = self._ensure_parent_link(curr_pbi, feat_id)
                    if parent_op:
                        patch.append(parent_op)

                    commit_ops = self._build_commit_link_ops(curr_pbi, pbi.linked_commits, repo_name)
                    if commit_ops:
                        patch.extend(commit_ops)
                        stats["commits_linked"] += len(commit_ops)

                    if patch:
                        self.client.update_work_item(pbi_id, patch, dry_run=dry_run)
                        stats["updated"] += 1
                        print(f"       ├── 📄 PBI #{pbi_id}: 🔄 Atualizado ({len(patch)} alterações)")
                    else:
                        stats["unchanged"] += 1
                        print(f"       ├── 📄 PBI #{pbi_id}: ⏺️ Inalterado")
                else:
                    print(f"       ├── 📄 PBI: 🆕 Criando '{pbi_title}' vinculado à Feature #{feat_id}...")
                    pbi_relations = [{
                        "rel": "System.LinkTypes.Hierarchy-Reverse",
                        "url": f"{self.client.base_url}/_apis/wit/workitems/{feat_id}",
                        "attributes": {"comment": f"Vinculado à Feature #{feat_id}"}
                    }]
                    pbi_res = self.client.create_work_item(
                        work_item_type="Product Backlog Item",
                        title=pbi_title,
                        description=pbi.description,
                        acceptance_criteria=pbi.acceptance_criteria,
                        priority=pbi.priority,
                        effort=pbi.story_points,
                        business_value=pbi.business_value,
                        tags=item_tags,
                        iteration_path=iteration_path,
                        assigned_to=owner_email,
                        state="Committed",
                        relations=pbi_relations,
                        dry_run=dry_run
                    )
                    pbi_id = pbi_res.get("id", 3000)
                    stats["created"] += 1
                    print(f"           └── ✅ PBI #{pbi_id} criado!")

        print(f"\n✨ {prefix}Disciplina {d_info['name']} sincronizada: "
              f"{stats['updated']} atualizados | {stats['created']} criados | "
              f"{stats['unchanged']} inalterados | {stats['commits_linked']} commits vinculados.")
        return stats

    def update_all_disciplines(self, dry_run: bool = False) -> Dict[str, int]:
        """Sincroniza e atualiza com inteligência (Upsert) todas as 7 disciplinas."""
        totals = {"updated": 0, "created": 0, "unchanged": 0, "commits_linked": 0}
        for key in DISCIPLINES.keys():
            res = self.update_discipline(key, dry_run=dry_run)
            for k in totals:
                totals[k] += res.get(k, 0)

        prefix = "[DRY-RUN] " if dry_run else ""
        print("\n========================================================")
        print(f"🎉 {prefix}SMART UPSERT TOTAL CONCLUÍDO (7 DISCIPLINAS)!")
        print(f"🔄 Itens Atualizados : {totals['updated']}")
        print(f"🆕 Itens Criados     : {totals['created']}")
        print(f"⏺️ Itens Inalterados : {totals['unchanged']}")
        print(f"🔗 Commits Vinculados: {totals['commits_linked']}")
        print("========================================================\n")
        return totals

    # =========================================================================
    # 2. RASTREABILIDADE MULTI-REPO DE COMMITS GIT
    # =========================================================================
    def scan_and_link_commits(self, dry_run: bool = False) -> Dict[str, int]:
        """Varre os 7 repositórios locais e vincula os commits ao Azure Boards."""
        prefix = "[DRY-RUN] " if dry_run else ""
        print("\n================================================================================")
        print(f"🔍 {prefix}ESCANEANDO OS 7 REPOSITÓRIOS PARA RASTREAMENTO DE COMMITS")
        print(f"📁 Diretório Base: {self.root_dir}")
        print("================================================================================")

        total_commits = 0
        linked_commits = 0

        for key, d_info in DISCIPLINES.items():
            repo_path = os.path.join(self.root_dir, d_info["repo"])
            if not os.path.exists(repo_path):
                continue

            print(f"\n📂 [{d_info['name']}] - {d_info['repo']}")

            try:
                cmd = ["git", "-C", repo_path, "log", "-n", "3", "--pretty=format:%h|%s"]
                output = subprocess.check_output(cmd, encoding="utf-8", errors="ignore")
                lines = [l.strip() for l in output.split("\n") if l.strip()]
            except Exception as e:
                print(f"  ⚠️ Erro ao ler git log: {e}")
                continue

            print(f"  🔎 Encontrados {len(lines)} commits recentes:")

            disc_items = []
            if not dry_run:
                wiql = f"Select [System.Id] From WorkItems Where [System.TeamProject] = '{AZURE_PROJECT}' and [System.Tags] Contains '{d_info['tag']}'"
                disc_items = self.client.query_wiql(wiql)

            for line in lines:
                sha, msg = line.split("|", 1)
                total_commits += 1
                commit_url = f"https://github.com/{GITHUB_ORG}/{d_info['repo']}/commit/{sha}"
                print(f"    • {sha} — {msg}")
                print(f"      🔗 {commit_url}")

                matches = re.findall(r"AB#(\d+)", msg, re.IGNORECASE)
                target_ids = [int(m) for m in matches] if matches else ([disc_items[0]] if disc_items else [])

                for tid in target_ids:
                    comment = f"Commit {sha}: {msg} ({d_info['repo']})"
                    ok = self.client.link_commit(tid, commit_url, comment, dry_run=dry_run)
                    if ok:
                        linked_commits += 1
                        print(f"  ✅ Commit vinculado ao Work Item #{tid}!")

        print("\n" + "="*80)
        print(f"✨ {prefix}Commits identificados: {total_commits} | Vínculos processados: {linked_commits}")
        print("="*80 + "\n")
        return {"total": total_commits, "linked": linked_commits}

    # =========================================================================
    # 3. GOVERNANÇA DE RESPONSÁVEIS E ESTADOS
    # =========================================================================
    def apply_governance(self, dry_run: bool = False) -> int:
        """Aplica atribuição dos integrantes e estados In Progress / Committed."""
        prefix = "[DRY-RUN] " if dry_run else ""
        print("\n================================================================================")
        print(f"👤 {prefix}APLICANDO GOVERNANÇA, RESPONSÁVEIS E ESTADOS NO AZURE BOARDS")
        print("================================================================================")

        ids = self.client.query_wiql(f"Select [System.Id] From WorkItems Where [System.TeamProject] = '{AZURE_PROJECT}'")
        if not ids:
            print("ℹ️ Nenhum Work Item encontrado no projeto.")
            return 0

        items = self.client.get_batch(ids, fields=["System.Id", "System.Title", "System.WorkItemType", "System.Tags", "System.State"])
        updated = 0

        tag_to_owner = {d["tag"]: d["owner_email"] for d in DISCIPLINES.values()}

        for it in items:
            iid = it["id"]
            fields = it["fields"]
            wtype = fields.get("System.WorkItemType")
            tags = fields.get("System.Tags", "")
            state = fields.get("System.State", "")

            patch = []

            # 1. Responsável
            target_owner = None
            for tag, owner_email in tag_to_owner.items():
                if tag in tags:
                    target_owner = owner_email
                    break

            if target_owner:
                patch.append({"op": "add", "path": "/fields/System.AssignedTo", "value": target_owner})

            # 2. State
            if wtype in ["Epic", "Feature"] and state != "In Progress":
                patch.append({"op": "add", "path": "/fields/System.State", "value": "In Progress"})
            elif wtype == "Product Backlog Item" and state != "Committed":
                patch.append({"op": "add", "path": "/fields/System.State", "value": "Committed"})

            # 3. Remove GS 2026/2 de títulos se presente
            title = fields.get("System.Title", "")
            if "GS 2026/2 - " in title:
                patch.append({"op": "add", "path": "/fields/System.Title", "value": title.replace("GS 2026/2 - ", "").strip()})

            if patch:
                ok = self.client.update_work_item(iid, patch, dry_run=dry_run)
                if ok:
                    updated += 1

        print(f"✨ {prefix}Governança aplicada: {updated}/{len(ids)} itens atualizados.")
        print("================================================================================\n")
        return updated

    # =========================================================================
    # 4. DASHBOARD DE STATUS DO PROJETO
    # =========================================================================
    def get_project_status(self) -> Dict[str, Any]:
        """Consulta e exibe a visão consolidada de saúde do Azure Boards."""
        ids = self.client.query_wiql(f"Select [System.Id] From WorkItems Where [System.TeamProject] = '{AZURE_PROJECT}'")
        items = self.client.get_batch(ids, fields=["System.Id", "System.WorkItemType", "System.State", "System.AssignedTo"])

        types_count = {}
        states_count = {}
        assigned_count = {}

        for it in items:
            f = it["fields"]
            wtype = f.get("System.WorkItemType", "Outro")
            st = f.get("System.State", "Indefinido")
            assigned = f.get("System.AssignedTo", {}).get("displayName", "Não atribuído") if isinstance(f.get("System.AssignedTo"), dict) else str(f.get("System.AssignedTo", "N/A"))

            types_count[wtype] = types_count.get(wtype, 0) + 1
            states_count[st] = states_count.get(st, 0) + 1
            assigned_count[assigned] = assigned_count.get(assigned, 0) + 1

        print("\n================================================================================")
        print(f"📊 PAINEL DE CONTROLE AZURE BOARDS: {AZURE_PROJECT} ({AZURE_ORG})")
        print("================================================================================")
        print(f"📦 Total de Work Items: {len(ids)}\n")

        print("🏷️ Distribuição por Tipo:")
        for t, count in sorted(types_count.items()):
            print(f"   • {t:22}: {count}")

        print("\n🚦 Distribuição por Estado:")
        for s, count in sorted(states_count.items()):
            print(f"   • {s:22}: {count}")

        print("\n👥 Distribuição por Responsável:")
        for a, count in sorted(assigned_count.items()):
            print(f"   • {a:35}: {count}")

        print("================================================================================\n")
        return {"total": len(ids), "types": types_count, "states": states_count, "members": assigned_count}

    # =========================================================================
    # 5. VALIDAÇÃO ESTRITA DOS BACKLOGS (CONTRATO DE CAMPOS OBRIGATÓRIOS)
    # =========================================================================
    def validate_all_backlogs(self) -> bool:
        """Valida localmente todos os 7 arquivos de backlog contra o contrato mínimo obrigatório."""
        print("\n🔎 Validando contrato obrigatório de todos os 7 backlogs...")
        all_ok = True
        for key, d_info in DISCIPLINES.items():
            file_path = os.path.join(self.backlogs_dir, d_info["file"])
            if not os.path.exists(file_path):
                print(f"  ❌ [{key}] Arquivo não encontrado: {file_path}")
                all_ok = False
                continue
            doc = parse_backlog_markdown(file_path)
            exact_tag_only = True
            errors = validate_backlog_document(
                doc,
                required_tag=d_info["tag"],
                exact_tag_only=exact_tag_only,
            )
            if errors:
                all_ok = False
                print(f"  ❌ [{key}] {d_info['file']} — {len(errors)} erro(s):")
                for err in errors:
                    print(f"     • {err}")
            else:
                pbis_count = sum(len(f.pbis) for f in doc.epic.features)
                print(
                    f"  ✅ [{key:10s}] {d_info['file']} | Epic ({doc.epic.start_date}..{doc.epic.target_date}) "
                    f"| {len(doc.epic.features)} Features | {pbis_count} PBIs | {doc.epic.effort:.0f} SP"
                )
        return all_ok

    # =========================================================================
    # 6. LIMPEZA TOTAL DO BOARD
    # =========================================================================
    def clean_board(self, destroy: bool = True) -> int:
        """Limpa todos os Work Items do projeto com segurança."""
        ids = self.client.query_wiql(f"Select [System.Id] From WorkItems Where [System.TeamProject] = '{AZURE_PROJECT}'")
        print(f"🗑️ Encontrados {len(ids)} itens para remoção no projeto {AZURE_PROJECT}...")
        deleted = 0
        for iid in ids:
            ok = self.client.delete_work_item(iid, destroy=destroy)
            if ok:
                deleted += 1
        print(f"✨ Limpeza concluída: {deleted}/{len(ids)} itens removidos.")
        return deleted
