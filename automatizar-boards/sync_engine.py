#!/usr/bin/env python3
"""
ZelaFix - Motor Central de Sincronização, Commits e Governança
Orquestra as operações de Backlogs, Rastreamento de Commits Git e Governança Scrum.
"""

import sys
import os
import re
import subprocess
from typing import Dict, Any, List, Optional

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
from parser_backlog import parse_backlog_markdown, clean_title


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

        doc = parse_backlog_markdown(file_path)
        stats = {"epics": 0, "features": 0, "pbis": 0, "errors": 0}

        prefix = "[DRY-RUN] " if dry_run else ""
        print(f"\n========================================================")
        print(f"🚀 {prefix}Sincronizando: {d_info['name']}")
        print(f"🏷️ Tag: [{d_info['tag']}] | 📅 Iteração: [{AZURE_PROJECT}\\{d_info['iteration']}]")
        print(f"👤 Responsável: {d_info['owner_name']} ({d_info['owner_email']})")
        print(f"========================================================")

        iteration_path = f"{AZURE_PROJECT}\\{d_info['iteration']}"
        item_tags = [d_info["tag"], "ZelaFix"]
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
    # 5. LIMPEZA TOTAL DO BOARD
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
