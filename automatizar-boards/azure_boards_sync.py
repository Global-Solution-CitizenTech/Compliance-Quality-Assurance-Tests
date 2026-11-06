import sys
import os
import time
import json
import base64
import subprocess
import urllib.request
import urllib.parse
import urllib.error
import html
from typing import Dict, Any, Optional, List, Tuple
from parser_backlog import BacklogDocument, clean_title

# Garante suporte a UTF-8 no terminal Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def get_discipline_tag(discipline: str) -> str:
    """Retorna a tag única e padronizada para a matéria."""
    d = (discipline or "").lower()
    if "compliance" in d or "qa" in d:
        return "Compliance"
    if "java" in d:
        return "JavaAdvanced"
    if "mobile" in d:
        return "Mobile"
    if ".net" in d or "dot" in d:
        return "DotNet"
    if "data" in d or "banco" in d:
        return "Database"
    if "devops" in d or "cloud" in d:
        return "DevOps"
    if "disruptive" in d or "iot" in d or "iob" in d or "arquitetura" in d:
        return "DisruptiveArchitectures"
    if "test" in d:
        return "Compliance"
    return "GlobalSolution2"


def get_discipline_iteration_path(discipline: str, project_name: str = "ZelaFix") -> str:
    """
    Retorna o IterationPath oficial no Azure Boards para Global Solution 2:
    - Sprint 1 (2026-11-04 a 2026-11-11): Mobile, Java Advanced, Database Advanced, DotNet
    - Sprint 2 (2026-11-12 a 2026-11-19): DevOps Tools, Disruptive Architectures, Compliance
    """
    d = (discipline or "").lower()
    if any(k in d for k in ["mobile", "java", "database", "data", "banco", "plsql", ".net", "dotnet"]):
        return f"{project_name}\\Sprint 1"
    if any(k in d for k in ["devops", "cloud", "disruptive", "iot", "ia", "iob", "compliance", "qa", "test"]):
        return f"{project_name}\\Sprint 2"
    return f"{project_name}\\Sprint 1"


DISCIPLINE_OWNERS = {
    "Mobile": "RM562290@fiap.com.br",               # Luna de Carvalho Guimarães
    "DotNet": "MR563428@fiap.com.br",               # Gustavo Okada / MR563428
    "DevOps": "RM564836@fiap.com.br",               # Milton Jakson de Sousa Marcelino
    "Database": "RM566422@fiap.com.br",             # Lucas Barros Gouveia
    "DisruptiveArchitectures": "RM561432@fiap.com.br", # Enzo Okuizumi
    "Compliance": "RM561432@fiap.com.br",           # Enzo Okuizumi
    "JavaAdvanced": "RM561432@fiap.com.br"          # Enzo Okuizumi
}


class AzureBoardsClient:
    def __init__(self, organization: str, project: str, pat: Optional[str] = None):
        self.organization = organization.strip()
        self.project = project.strip()
        self.pat = (pat or "").strip()
        self.bearer_token: Optional[str] = None
        self._simulated_id_counter = 1000

    def _get_auth_headers(self) -> Dict[str, str]:
        """Obtém cabeçalhos de autenticação via PAT ou Bearer Token do Azure CLI."""
        if self.pat:
            auth_str = f":{self.pat}"
            b64_auth = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
            return {
                "Authorization": f"Basic {b64_auth}",
                "Content-Type": "application/json-patch+json",
                "Accept": "application/json"
            }
        
        if not self.bearer_token:
            self.bearer_token = self._fetch_azure_cli_token()
        
        if self.bearer_token:
            return {
                "Authorization": f"Bearer {self.bearer_token}",
                "Content-Type": "application/json-patch+json",
                "Accept": "application/json"
            }

        raise ValueError(
            "Nenhuma credencial encontrada!\n"
            "Por favor, configure o seu Personal Access Token (PAT) no arquivo .env (AZURE_DEVOPS_PAT=...)\n"
            "Ou faça login no terminal com: az login"
        )

    def _fetch_azure_cli_token(self) -> Optional[str]:
        """Extrai o Bearer token para Azure DevOps a partir da sessão do Azure CLI."""
        try:
            cmd = ["az", "account", "get-access-token", "--resource", "499b84ac-1321-427f-aa17-267ca6975798", "-o", "json"]
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
            data = json.loads(result.stdout)
            return data.get("accessToken")
        except Exception:
            return None

    def check_connection(self) -> Tuple[bool, str]:
        """Verifica se a conexão com o projeto no Azure Boards está ativa e autorizada."""
        url = f"https://dev.azure.com/{self.organization}/{self.project}/_apis/wit/workitemtypes?api-version=7.1-preview.2"
        headers = self._get_auth_headers()
        headers["Content-Type"] = "application/json"

        req = urllib.request.Request(url, headers=headers, method="GET")
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                if resp.status == 200:
                    data = json.loads(resp.read().decode("utf-8"))
                    types = [t.get("name") for t in data.get("value", [])]
                    return True, f"Conexão estabelecida com sucesso! Tipos disponíveis: {', '.join(types[:5])}"
                return False, f"Resposta inesperada do servidor: HTTP {resp.status}"
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="ignore")
            return False, f"HTTP Error {e.code}: {e.reason}\nDetalhes: {err_body[:200]}"
        except Exception as e:
            return False, f"Erro ao conectar: {str(e)}"

    def create_work_item(
        self,
        work_item_type: str,
        title: str,
        description: str = "",
        acceptance_criteria: str = "",
        start_date: Optional[str] = None,
        target_date: Optional[str] = None,
        activity: Optional[str] = None,
        remaining_work: Optional[float] = None,
        priority: int = 2,
        effort: Optional[float] = None,
        business_value: Optional[int] = None,
        value_area: str = "Business",
        tags: Optional[List[str]] = None,
        iteration_path: Optional[str] = None,
        parent_id: Optional[int] = None,
        assigned_to: Optional[str] = None,
        state: Optional[str] = None,
        dry_run: bool = False
    ) -> Dict[str, Any]:
        """
        Cria um Work Item no Azure Boards com campos dedicados (Description, Acceptance Criteria, Effort, Business Value, Dates, Activity, IterationPath).
        """
        clean_item_title = clean_title(title)
        
        if dry_run:
            self._simulated_id_counter += 1
            sim_id = self._simulated_id_counter
            return {
                "id": sim_id,
                "url": f"https://dev.azure.com/{self.organization}/{self.project}/_workitems/edit/{sim_id}",
                "fields": {
                    "System.Title": clean_item_title,
                    "System.WorkItemType": work_item_type,
                    "System.IterationPath": iteration_path or self.project
                }
            }

        url = f"https://dev.azure.com/{self.organization}/{self.project}/_apis/wit/workitems/${urllib.parse.quote(work_item_type)}?api-version=7.1-preview.3"
        headers = self._get_auth_headers()

        patch_document = [
            {
                "op": "add",
                "path": "/fields/System.Title",
                "value": clean_item_title
            }
        ]

        if description:
            patch_document.append({
                "op": "add",
                "path": "/fields/System.Description",
                "value": description
            })

        if acceptance_criteria and work_item_type in ["Epic", "Feature", "Product Backlog Item"]:
            patch_document.append({
                "op": "add",
                "path": "/fields/Microsoft.VSTS.Common.AcceptanceCriteria",
                "value": acceptance_criteria
            })

        if priority:
            patch_document.append({
                "op": "add",
                "path": "/fields/Microsoft.VSTS.Common.Priority",
                "value": int(priority)
            })

        if effort is not None and effort > 0 and work_item_type in ["Epic", "Feature", "Product Backlog Item"]:
            patch_document.append({
                "op": "add",
                "path": "/fields/Microsoft.VSTS.Scheduling.Effort",
                "value": float(effort)
            })

        if business_value is not None and business_value > 0 and work_item_type in ["Epic", "Feature", "Product Backlog Item"]:
            patch_document.append({
                "op": "add",
                "path": "/fields/Microsoft.VSTS.Common.BusinessValue",
                "value": int(business_value)
            })

        if work_item_type in ["Epic", "Feature", "Product Backlog Item"]:
            patch_document.append({
                "op": "add",
                "path": "/fields/Microsoft.VSTS.Common.ValueArea",
                "value": value_area
            })

        if start_date and work_item_type in ["Epic", "Feature"]:
            patch_document.append({
                "op": "add",
                "path": "/fields/Microsoft.VSTS.Scheduling.StartDate",
                "value": f"{start_date}T00:00:00Z"
            })

        if target_date and work_item_type in ["Epic", "Feature"]:
            patch_document.append({
                "op": "add",
                "path": "/fields/Microsoft.VSTS.Scheduling.TargetDate",
                "value": f"{target_date}T00:00:00Z"
            })

        if work_item_type == "Task":
            if activity:
                patch_document.append({
                    "op": "add",
                    "path": "/fields/Microsoft.VSTS.Common.Activity",
                    "value": activity
                })
            if remaining_work is not None and remaining_work > 0:
                patch_document.append({
                    "op": "add",
                    "path": "/fields/Microsoft.VSTS.Scheduling.RemainingWork",
                    "value": float(remaining_work)
                })

        if tags:
            patch_document.append({
                "op": "add",
                "path": "/fields/System.Tags",
                "value": "; ".join(tags)
            })

        if iteration_path:
            patch_document.append({
                "op": "add",
                "path": "/fields/System.IterationPath",
                "value": iteration_path
            })

        if assigned_to:
            patch_document.append({
                "op": "add",
                "path": "/fields/System.AssignedTo",
                "value": assigned_to
            })

        if state:
            patch_document.append({
                "op": "add",
                "path": "/fields/System.State",
                "value": state
            })

        if parent_id:
            parent_url = f"https://dev.azure.com/{self.organization}/{self.project}/_apis/wit/workitems/{parent_id}"
            patch_document.append({
                "op": "add",
                "path": "/relations/-",
                "value": {
                    "rel": "System.LinkTypes.Hierarchy-Reverse",
                    "url": parent_url,
                    "attributes": {
                        "comment": "Vinculado automaticamente via automação CitizenTech"
                    }
                }
            })

        req_body = json.dumps(patch_document).encode("utf-8")

        max_retries = 3
        for attempt in range(1, max_retries + 1):
            try:
                req = urllib.request.Request(url, data=req_body, headers=headers, method="POST")
                with urllib.request.urlopen(req, timeout=45) as resp:
                    res_data = json.loads(resp.read().decode("utf-8"))
                    time.sleep(0.08)
                    return res_data
            except urllib.error.HTTPError as e:
                err_msg = e.read().decode("utf-8", errors="ignore")
                # Se falhar por causa do IterationPath inexistente, tenta remover o campo e enviar na raiz
                if "IterationPath" in err_msg or "TF400898" in err_msg or e.code == 400:
                    patch_doc_no_iter = [op for op in patch_document if op.get("path") != "/fields/System.IterationPath"]
                    req_no_iter = urllib.request.Request(url, data=json.dumps(patch_doc_no_iter).encode("utf-8"), headers=headers, method="POST")
                    try:
                        with urllib.request.urlopen(req_no_iter, timeout=45) as resp2:
                            return json.loads(resp2.read().decode("utf-8"))
                    except Exception:
                        pass
                raise RuntimeError(f"Falha ao criar [{work_item_type}] '{clean_item_title}' (HTTP {e.code}): {err_msg}")
            except Exception as e:
                if attempt < max_retries:
                    time.sleep(1.5 * attempt)
                    continue
                raise RuntimeError(f"Erro inesperado ao criar [{work_item_type}] '{clean_item_title}': {str(e)}")

    def link_commit(self, work_item_id: int, commit_url: str, comment: str = "", dry_run: bool = False) -> bool:
        """Adiciona vínculo de hyperlink do commit no GitHub ao Work Item."""
        if dry_run:
            print(f"  [DRY-RUN] Vincularia {commit_url} ao item #{work_item_id}")
            return True

        url = f"https://dev.azure.com/{self.organization}/_apis/wit/workitems/{work_item_id}?api-version=7.1-preview.3"
        headers = self._get_auth_headers()
        patch_document = [
            {
                "op": "add",
                "path": "/relations/-",
                "value": {
                    "rel": "Hyperlink",
                    "url": commit_url,
                    "attributes": {"comment": comment or "Commit rastreado"}
                }
            }
        ]
        req_body = json.dumps(patch_document).encode("utf-8")
        req = urllib.request.Request(url, data=req_body, headers=headers, method="PATCH")
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.status in (200, 201)
        except Exception as e:
            print(f"⚠️ Erro ao vincular commit ao Work Item #{work_item_id}: {e}")
            return False

    def sync_backlog(self, doc: BacklogDocument, dry_run: bool = False) -> Dict[str, Any]:
        """
        Sincroniza um documento de backlog completo (Epic ➔ Features ➔ PBIs ➔ Tasks).
        Mantém estritamente UMA ÚNICA tag padronizada por matéria e o IterationPath correto.
        """
        prefix = "[DRY-RUN] " if dry_run else ""
        discipline_tag = get_discipline_tag(doc.discipline)
        item_tags = [discipline_tag, "ZelaFix"]
        iteration_path = get_discipline_iteration_path(doc.discipline, self.project)

        print(f"\n========================================================")
        print(f"🚀 {prefix}Iniciando Sincronização: {doc.discipline}")
        print(f"🏷️ Tag Única da Matéria: [{discipline_tag}]")
        print(f"📅 Iteration Path: [{iteration_path}]")
        print(f"🏛️ Organização: {self.organization} | Projeto: {self.project}")
        print(f"========================================================")

        stats = {"epics": 0, "features": 0, "pbis": 0, "tasks": 0, "errors": 0}
        owner = DISCIPLINE_OWNERS.get(discipline_tag, "RM561432@fiap.com.br")

        # 1. Cria o Epic
        epic = doc.epic
        date_str = f" | Dates: {epic.start_date} -> {epic.target_date}" if epic.start_date and epic.target_date else ""
        print(f"\n👑 Criando Epic: {epic.title} (Effort: {epic.effort} SP | Business Value: {epic.business_value}{date_str} | Tag: {discipline_tag} | Iteration: {iteration_path})")

        epic_res = self.create_work_item(
            work_item_type="Epic",
            title=epic.title,
            description=epic.description,
            acceptance_criteria=epic.acceptance_criteria,
            start_date=epic.start_date,
            target_date=epic.target_date,
            priority=epic.priority,
            effort=epic.effort,
            business_value=epic.business_value,
            tags=item_tags,
            iteration_path=iteration_path,
            assigned_to=owner,
            state="In Progress",
            dry_run=dry_run
        )
        epic_id = epic_res.get("id")
        stats["epics"] += 1
        print(f"   └── ✅ Epic #{epic_id} criado com sucesso!")

        # 2. Cria as Features
        for f_idx, feat in enumerate(epic.features, 1):
            feat_date_str = f" | Dates: {feat.start_date} -> {feat.target_date}" if feat.start_date and feat.target_date else ""
            print(f"\n   🏆 [{f_idx}/{len(epic.features)}] Criando Feature: {feat.title} (Effort: {feat.effort} SP | Business Value: {feat.business_value}{feat_date_str})")
            feat_res = self.create_work_item(
                work_item_type="Feature",
                title=feat.title,
                description=feat.description,
                acceptance_criteria=feat.acceptance_criteria,
                start_date=feat.start_date,
                target_date=feat.target_date,
                priority=feat.priority,
                effort=feat.effort,
                business_value=feat.business_value,
                tags=item_tags,
                iteration_path=iteration_path,
                parent_id=epic_id,
                assigned_to=owner,
                state="In Progress",
                dry_run=dry_run
            )
            feat_id = feat_res.get("id")
            stats["features"] += 1
            print(f"       └── ✅ Feature #{feat_id} vinculada ao Epic #{epic_id}")

            # 3. Cria os PBIs
            for p_idx, pbi in enumerate(feat.pbis, 1):
                print(f"       ├── 📄 [{p_idx}/{len(feat.pbis)}] PBI: {pbi.title} ({pbi.story_points} SP | Prio {pbi.priority} | BV: {pbi.business_value})")
                pbi_res = self.create_work_item(
                    work_item_type="Product Backlog Item",
                    title=pbi.title,
                    description=pbi.description,
                    acceptance_criteria=pbi.acceptance_criteria,
                    priority=pbi.priority,
                    effort=pbi.story_points,
                    business_value=pbi.business_value,
                    tags=item_tags,
                    iteration_path=iteration_path,
                    parent_id=feat_id,
                    assigned_to=owner,
                    state="Committed",
                    dry_run=dry_run
                )
                pbi_id = pbi_res.get("id")
                stats["pbis"] += 1

                # 4. Cria as Tasks
                for t_idx, task in enumerate(pbi.tasks, 1):
                    rem_str = f" | {task.remaining_work}h" if task.remaining_work else ""
                    print(f"           🔨 [{t_idx}/{len(pbi.tasks)}] Task: {task.title} (Activity: {task.activity}{rem_str})")
                    task_res = self.create_work_item(
                        work_item_type="Task",
                        title=task.title,
                        description=task.description,
                        activity=task.activity,
                        remaining_work=task.remaining_work,
                        tags=item_tags,
                        iteration_path=iteration_path,
                        parent_id=pbi_id,
                        dry_run=dry_run
                    )
                    stats["tasks"] += 1

        print(f"\n✨ {prefix}Concluído com Sucesso!")
        print(f"📊 Resumo: {stats['epics']} Epics, {stats['features']} Features, {stats['pbis']} PBIs, {stats['tasks']} Tasks criados.")
        return stats
