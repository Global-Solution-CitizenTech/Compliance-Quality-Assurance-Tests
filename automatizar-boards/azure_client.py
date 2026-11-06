#!/usr/bin/env python3
"""
ZelaFix - Cliente Unificado da API REST do Azure DevOps
Centraliza todas as chamadas HTTP (WIQL, CRUD de Work Items, Vínculos de Hierarquia, Testes e Commits).
"""

import sys
import os
import base64
import requests
from typing import Dict, Any, List, Optional, Tuple

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


class AzureClient:
    """Cliente HTTP centralizado para automação do Azure Boards / Azure DevOps."""

    def __init__(self, organization: str, project: str, pat: str):
        self.org = organization.strip()
        self.project = project.strip()
        self.pat = pat.strip()

        self.base_url = f"https://dev.azure.com/{self.org}/{self.project}"
        self.org_url = f"https://dev.azure.com/{self.org}"

        # Configura sessão com autenticação básica do PAT
        self.session = requests.Session()
        auth_str = base64.b64encode(f":{self.pat}".encode("utf-8")).decode("utf-8")
        self.session.headers.update({
            "Authorization": f"Basic {auth_str}",
            "Accept": "application/json"
        })

    def check_connection(self) -> Tuple[bool, str]:
        """Verifica a conectividade e autenticação com o Azure DevOps."""
        url = f"{self.base_url}/_apis/wit/workitemtypes?api-version=7.0"
        try:
            res = self.session.get(url, timeout=15)
            if res.status_code == 200:
                types = [t.get("name") for t in res.json().get("value", [])]
                return True, f"Conexão OK ({len(types)} tipos disponíveis)"
            return False, f"Falha HTTP {res.status_code}: {res.text[:150]}"
        except Exception as e:
            return False, f"Exceção de rede: {e}"

    def query_wiql(self, wiql_query: str) -> List[int]:
        """Executa uma consulta WIQL e retorna a lista de IDs dos Work Items."""
        url = f"{self.base_url}/_apis/wit/wiql?api-version=7.0"
        res = self.session.post(url, json={"query": wiql_query}, headers={"Content-Type": "application/json"}, timeout=20)
        if res.status_code == 200:
            return [it["id"] for it in res.json().get("workItems", [])]
        return []

    def get_work_item(self, item_id: int, expand: str = "all") -> Optional[Dict[str, Any]]:
        """Busca um Work Item por ID com campos e relações."""
        url = f"{self.org_url}/_apis/wit/workitems/{item_id}?$expand={expand}&api-version=7.0"
        res = self.session.get(url, timeout=15)
        if res.status_code == 200:
            return res.json()
        return None

    def get_batch(self, ids: List[int], fields: Optional[List[str]] = None) -> List[Dict[str, Any]]:
        """Busca múltiplos Work Items em lote."""
        if not ids:
            return []
        url = f"{self.base_url}/_apis/wit/workitemsbatch?api-version=7.0"
        payload: Dict[str, Any] = {"ids": ids}
        if fields:
            payload["fields"] = fields
        res = self.session.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=30)
        if res.status_code == 200:
            return res.json().get("value", [])
        return []

    def create_work_item(
        self,
        work_item_type: str,
        title: str,
        description: str = "",
        acceptance_criteria: str = "",
        priority: int = 2,
        effort: Optional[float] = None,
        business_value: Optional[int] = None,
        start_date: Optional[str] = None,
        target_date: Optional[str] = None,
        tags: Optional[List[str]] = None,
        iteration_path: Optional[str] = None,
        assigned_to: Optional[str] = None,
        state: Optional[str] = None,
        extra_fields: Optional[Dict[str, Any]] = None,
        relations: Optional[List[Dict[str, Any]]] = None,
        dry_run: bool = False
    ) -> Dict[str, Any]:
        """Cria um Work Item com suporte a todos os campos do processo Scrum."""
        if dry_run:
            return {"id": 9999, "fields": {"System.Title": title, "System.WorkItemType": work_item_type}}

        url = f"{self.base_url}/_apis/wit/workitems/${work_item_type}?api-version=7.0"
        patch_doc = [
            {"op": "add", "path": "/fields/System.Title", "value": title}
        ]

        if description:
            patch_doc.append({"op": "add", "path": "/fields/System.Description", "value": description})
        if acceptance_criteria:
            patch_doc.append({"op": "add", "path": "/fields/Microsoft.VSTS.Common.AcceptanceCriteria", "value": acceptance_criteria})
        if priority:
            patch_doc.append({"op": "add", "path": "/fields/Microsoft.VSTS.Common.Priority", "value": int(priority)})
        if effort is not None and effort > 0:
            patch_doc.append({"op": "add", "path": "/fields/Microsoft.VSTS.Scheduling.Effort", "value": float(effort)})
        if business_value is not None and business_value > 0:
            patch_doc.append({"op": "add", "path": "/fields/Microsoft.VSTS.Common.BusinessValue", "value": int(business_value)})
        if start_date:
            patch_doc.append({"op": "add", "path": "/fields/Microsoft.VSTS.Scheduling.StartDate", "value": f"{start_date}T00:00:00Z"})
        if target_date:
            patch_doc.append({"op": "add", "path": "/fields/Microsoft.VSTS.Scheduling.TargetDate", "value": f"{target_date}T00:00:00Z"})
        if tags:
            patch_doc.append({"op": "add", "path": "/fields/System.Tags", "value": "; ".join(tags)})
        if iteration_path:
            patch_doc.append({"op": "add", "path": "/fields/System.IterationPath", "value": iteration_path})
        if assigned_to:
            patch_doc.append({"op": "add", "path": "/fields/System.AssignedTo", "value": assigned_to})
        if state:
            patch_doc.append({"op": "add", "path": "/fields/System.State", "value": state})

        if extra_fields:
            for k, v in extra_fields.items():
                patch_doc.append({"op": "add", "path": f"/fields/{k}", "value": v})

        if relations:
            for rel in relations:
                patch_doc.append({"op": "add", "path": "/relations/-", "value": rel})

        headers = {"Content-Type": "application/json-patch+json"}
        res = self.session.post(url, json=patch_doc, headers=headers, timeout=25)
        if res.status_code in (200, 201):
            return res.json()
        
        # Fallback se a iteração der 400
        if iteration_path and res.status_code == 400 and "IterationPath" in res.text:
            patch_doc = [p for p in patch_doc if p.get("path") != "/fields/System.IterationPath"]
            retry_res = self.session.post(url, json=patch_doc, headers=headers, timeout=25)
            if retry_res.status_code in (200, 201):
                return retry_res.json()

        raise RuntimeError(f"Erro ao criar {work_item_type} '{title}': HTTP {res.status_code} - {res.text[:200]}")

    def update_work_item(self, item_id: int, patch_ops: List[Dict[str, Any]], dry_run: bool = False) -> bool:
        """Aplica alterações parciais via JSON Patch em um Work Item existente."""
        if dry_run or not patch_ops:
            return True
        url = f"{self.org_url}/_apis/wit/workitems/{item_id}?api-version=7.0"
        headers = {"Content-Type": "application/json-patch+json"}
        res = self.session.patch(url, json=patch_ops, headers=headers, timeout=20)
        return res.status_code == 200

    def delete_work_item(self, item_id: int, destroy: bool = True) -> bool:
        """Remove um Work Item por ID."""
        destroy_str = "true" if destroy else "false"
        url = f"{self.org_url}/_apis/wit/workitems/{item_id}?destroy={destroy_str}&api-version=7.0"
        res = self.session.delete(url, timeout=20)
        return res.status_code in (200, 204)

    def link_parent_child(self, child_id: int, parent_id: int, dry_run: bool = False) -> bool:
        """Vincula um item filho ao seu item pai (Hierarchy-Reverse)."""
        if dry_run:
            return True
        parent_url = f"{self.base_url}/_apis/wit/workitems/{parent_id}"
        patch = [{
            "op": "add",
            "path": "/relations/-",
            "value": {
                "rel": "System.LinkTypes.Hierarchy-Reverse",
                "url": parent_url,
                "attributes": {"comment": "Vínculo hierárquico automatizado ZelaFix"}
            }
        }]
        return self.update_work_item(child_id, patch)

    def link_tested_by(self, test_case_id: int, feature_id: int, dry_run: bool = False) -> bool:
        """Vincula um Test Case a uma Feature (Microsoft.VSTS.Common.TestedBy-Reverse)."""
        if dry_run:
            return True
        feat_url = f"{self.base_url}/_apis/wit/workitems/{feature_id}"
        patch = [{
            "op": "add",
            "path": "/relations/-",
            "value": {
                "rel": "Microsoft.VSTS.Common.TestedBy-Reverse",
                "url": feat_url,
                "attributes": {"comment": f"Test Case vinculado à Feature #{feature_id}"}
            }
        }]
        return self.update_work_item(test_case_id, patch)

    def link_commit(self, work_item_id: int, commit_url: str, comment: str, dry_run: bool = False) -> bool:
        """Vincula um commit Git (Hyperlink) a um Work Item."""
        if dry_run:
            return True
        patch = [{
            "op": "add",
            "path": "/relations/-",
            "value": {
                "rel": "Hyperlink",
                "url": commit_url,
                "attributes": {"comment": comment}
            }
        }]
        return self.update_work_item(work_item_id, patch)

    def get_team_members(self) -> List[Dict[str, Any]]:
        """Retorna os integrantes do time do projeto."""
        t_url = f"{self.org_url}/_apis/projects/{self.project}/teams?api-version=7.0"
        res = self.session.get(t_url, timeout=15)
        if res.status_code != 200:
            return []
        teams = res.json().get("value", [])
        if not teams:
            return []
        team_id = teams[0]["id"]
        m_url = f"{self.org_url}/_apis/projects/{self.project}/teams/{team_id}/members?api-version=7.0"
        m_res = self.session.get(m_url, timeout=15)
        if m_res.status_code == 200:
            return [m.get("identity", {}) for m in m_res.json().get("value", [])]
        return []

    def get_iterations(self) -> List[Dict[str, str]]:
        """Retorna as iterações (Sprints) configuradas no projeto."""
        url = f"{self.base_url}/_apis/work/teamsettings/iterations?api-version=7.0"
        res = self.session.get(url, timeout=15)
        if res.status_code == 200:
            return [{"name": it.get("name"), "path": it.get("path")} for it in res.json().get("value", [])]
        return []
