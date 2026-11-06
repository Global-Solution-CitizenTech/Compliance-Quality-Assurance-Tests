#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🏛️ CitizenTech — Azure Boards Git Commit Linking CLI
=============================================================================
Utilitário para vincular commits dos 7 repositórios do CitizenTech aos
Work Items (Epics, Features, PBIs e Tasks) no Azure Boards via REST API.

FIAP Global Solution 2026/2 — CitizenTech
Disciplina: Compliance, Quality Assurance & Tests
=============================================================================
"""

import os
import sys
import json
import base64
import argparse
import subprocess
import urllib.request
import urllib.parse
import urllib.error
from typing import Dict, List, Optional, Tuple

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def load_env_file() -> dict:
    candidates = [
        os.path.join(os.path.dirname(__file__), ".env"),
        os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"),
        os.path.join(os.getcwd(), ".env")
    ]
    env_vars = {}
    for p in candidates:
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        env_vars[k.strip()] = v.strip().strip("'\"")
            break
    return env_vars


REPOS_CONFIG = {
    "Mobile-Application-Development": {
        "discipline": "Mobile Application Development",
        "tag": "Mobile",
        "github_repo": "Mobile-Application-Development"
    },
    "Java-Advanced": {
        "discipline": "Java Advanced",
        "tag": "JavaAdvanced",
        "github_repo": "Java-Advanced"
    },
    "Database-Advanced": {
        "discipline": "Database Advanced",
        "tag": "Database",
        "github_repo": "Database-Advanced"
    },
    "Advanced-Business-Development-with-Dot-Net": {
        "discipline": "Advanced Business Development with .NET",
        "tag": "DotNet",
        "github_repo": "Advanced-Business-Development-with-Dot-Net"
    },
    "DevOps-Tools-Cloud-Computing": {
        "discipline": "DevOps Tools & Cloud Computing",
        "tag": "DevOps",
        "github_repo": "DevOps-Tools-Cloud-Computing"
    },
    "Disruptive-Architectures-IoT-IoB-IA": {
        "discipline": "Disruptive Architectures (IoT & IA)",
        "tag": "DisruptiveArchitectures",
        "github_repo": "Disruptive-Architectures-IoT-IoB-IA"
    },
    "Compliance-Quality-Assurance-Tests": {
        "discipline": "Compliance, Quality Assurance & Tests",
        "tag": "Compliance",
        "github_repo": "Compliance-Quality-Assurance-Tests"
    }
}


class AzureCommitLinker:
    def __init__(self, organization: str, project: str, pat: str, github_org: str = "Global-Solution-CitizenTech"):
        self.organization = organization.strip()
        self.project = project.strip()
        self.pat = pat.strip()
        self.github_org = github_org.strip()
        self.auth_header = "Basic " + base64.b64encode(f":{self.pat}".encode("utf-8")).decode("utf-8")

    def _request(self, url: str, method: str = "GET", body: Optional[list] = None, patch_content_type: bool = False) -> Optional[dict]:
        content_type = "application/json-patch+json" if patch_content_type else "application/json"
        data = json.dumps(body).encode("utf-8") if body is not None else None
        req = urllib.request.Request(url, data=data, method=method, headers={
            "Authorization": self.auth_header,
            "Content-Type": content_type,
            "Accept": "application/json"
        })
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                content = resp.read().decode("utf-8")
                return json.loads(content) if content else {}
        except urllib.error.HTTPError as e:
            err_msg = e.read().decode("utf-8", errors="ignore")
            print(f"❌ [HTTP Error {e.code}] {url}\n{err_msg[:250]}")
            return None
        except Exception as e:
            print(f"❌ [Erro de Conexão] {e}")
            return None

    def get_work_item(self, wi_id: int) -> Optional[dict]:
        url = f"https://dev.azure.com/{self.organization}/_apis/wit/workitems/{wi_id}?$expand=relations&api-version=7.1-preview.3"
        return self._request(url)

    def query_work_items_by_tag(self, tag: str) -> List[int]:
        url = f"https://dev.azure.com/{self.organization}/{self.project}/_apis/wit/wiql?api-version=7.1-preview.2"
        query = {
            "query": f"Select [System.Id], [System.Title], [System.WorkItemType] From WorkItems Where [System.TeamProject] = @project And [System.Tags] Contains '{tag}' Order By [System.Id] Asc"
        }
        res = self._request(url, method="POST", body=query)
        if not res or "workItems" not in res:
            return []
        return [item["id"] for item in res.get("workItems", [])]

    def link_commit_to_work_item(self, wi_id: int, commit_url: str, comment: str = "", dry_run: bool = False) -> bool:
        if dry_run:
            print(f"  [DRY-RUN] Vincularia commit {commit_url} ao Work Item #{wi_id}")
            return True

        wi = self.get_work_item(wi_id)
        if not wi:
            print(f"  ⚠️ Work Item #{wi_id} não encontrado no Azure Boards.")
            return False

        # Verifica se o link já existe nas relations
        relations = wi.get("relations", []) or []
        for rel in relations:
            if rel.get("url") == commit_url:
                print(f"  ℹ️ Commit já vinculado ao Work Item #{wi_id}.")
                return True

        patch_doc = [
            {
                "op": "add",
                "path": "/relations/-",
                "value": {
                    "rel": "Hyperlink",
                    "url": commit_url,
                    "attributes": {
                        "comment": comment or "Commit rastreado via automação de QA"
                    }
                }
            }
        ]

        url = f"https://dev.azure.com/{self.organization}/_apis/wit/workitems/{wi_id}?api-version=7.1-preview.3"
        res = self._request(url, method="PATCH", body=patch_doc, patch_content_type=True)
        if res:
            title = res.get("fields", {}).get("System.Title", f"#{wi_id}")
            print(f"  ✅ Commit vinculado com sucesso ao Work Item #{wi_id} ({title})!")
            return True
        return False


def get_repo_commits(repo_path: str, max_commits: int = 5) -> List[Dict[str, str]]:
    """Obtém os últimos commits de um repositório git local."""
    if not os.path.exists(os.path.join(repo_path, ".git")):
        return []
    try:
        cmd = ["git", "-C", repo_path, "log", f"-n{max_commits}", "--format=%H|%h|%s|%an|%ad"]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        lines = res.stdout.strip().split("\n")
        commits = []
        for l in lines:
            if not l.strip():
                continue
            parts = l.split("|", 4)
            if len(parts) >= 3:
                full_sha = parts[0]
                short_sha = parts[1]
                subject = parts[2]
                commits.append({
                    "sha": full_sha,
                    "short_sha": short_sha,
                    "subject": subject
                })
        return commits
    except Exception as e:
        print(f"⚠️ Erro ao ler git log de {repo_path}: {e}")
        return []


def print_commit_guidelines():
    print("""
=============================================================================
📘 GUIA OFICIAL DE MENSAGENS DE COMMIT COM RASTREABILIDADE AZURE BOARDS
=============================================================================
Para que o Azure DevOps e GitHub vinculem automaticamente seus commits aos
Work Items sem necessidade de scripts manuais, use a sintaxe nativa:

1. Vincular commit ao Work Item (Ex: PBI #1005):
   git commit -m "feat(mobile): implementa tela de login AB#1005"
   git commit -m "fix(database): corrige sequence de chamados AB#1012"

2. Resolver ou fechar uma Task automaticamente no commit:
   git commit -m "feat(java): endpoint de consulta de chamados Fixes AB#1020"

3. Vincular múltiplos Work Items:
   git commit -m "feat: integração entre mobile e java AB#1005 AB#1020"

💡 A tag 'AB#<ID>' é o padrão internacional do Azure Boards para rastrear
commits em repositórios GitHub e Azure Repos!
=============================================================================
""")


def scan_and_link(linker: AzureCommitLinker, root_dir: str, dry_run: bool = False, max_commits: int = 3):
    print("\n" + "="*80)
    print("🔍 ESCANEANDO OS 7 REPOSITÓRIOS PARA RASTREAMENTO DE COMMITS")
    print(f"📁 Diretório Base: {root_dir}")
    print("="*80)

    total_commits_found = 0
    total_linked = 0

    for folder_name, cfg in REPOS_CONFIG.items():
        repo_dir = os.path.normpath(os.path.join(root_dir, folder_name))
        print(f"\n📂 [{cfg['discipline']}] - {folder_name}")

        if not os.path.exists(repo_dir):
            print(f"  ⚠️ Diretório do repositório não encontrado: {repo_dir}")
            continue

        commits = get_repo_commits(repo_dir, max_commits=max_commits)
        if not commits:
            print("  ⚪ Nenhum commit encontrado no repositório.")
            continue

        print(f"  🔎 Encontrados {len(commits)} commits recentes:")
        total_commits_found += len(commits)

        # Busca work items correspondentes à matéria no Azure Boards se PAT disponível
        work_item_ids = []
        if linker.pat:
            work_item_ids = linker.query_work_items_by_tag(cfg["tag"])
            if work_item_ids:
                print(f"  🏷️ Work Items encontrados com a tag [{cfg['tag']}]: {work_item_ids}")

        for c in commits:
            commit_url = f"https://github.com/{linker.github_org}/{cfg['github_repo']}/commit/{c['sha']}"
            comment = f"Commit [{cfg['tag']}]: {c['short_sha']} - {c['subject']}"
            print(f"    • {c['short_sha']} — {c['subject']}")
            print(f"      🔗 {commit_url}")

            # Se o commit message possui AB#<id>, vincula diretamente a esse ID específico
            import re
            explicit_matches = re.findall(r"AB#(\d+)", c["subject"], re.IGNORECASE)
            target_ids = [int(m) for m in explicit_matches]

            # Se não houver AB# explícito, mas encontramos work items da matéria, vincula ao primeiro PBI/Feature
            if not target_ids and work_item_ids:
                target_ids = [work_item_ids[0]]

            if target_ids and linker.pat:
                for tid in target_ids:
                    ok = linker.link_commit_to_work_item(tid, commit_url, comment, dry_run=dry_run)
                    if ok:
                        total_linked += 1

    print("\n" + "="*80)
    print(f"✨ RESUMO DO RASTREAMENTO DE COMMITS:")
    print(f"• Commits identificados : {total_commits_found}")
    print(f"• Vínculos processados  : {total_linked}")
    print("="*80 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="CitizenTech - Vinculação de Commits Git ao Azure Boards",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--scan-all", "-s", action="store_true", help="Escaneia os 7 repositórios e vincula commits aos Work Items")
    parser.add_argument("--repo", "-r", type=str, help="Nome do repositório específico (ex: Mobile-Application-Development)")
    parser.add_argument("--commit", type=str, help="Hash SHA completo ou curto do commit")
    parser.add_argument("--item-id", "-i", type=int, help="ID do Work Item no Azure Boards")
    parser.add_argument("--dry-run", "-d", action="store_true", help="Simula sem enviar alterações à API do Azure DevOps")
    parser.add_argument("--guide", "-g", action="store_true", help="Exibe boas práticas e sintaxe de commits rastreáveis")
    parser.add_argument("--org", type=str, default=None, help="Organização no Azure DevOps")
    parser.add_argument("--project", type=str, default=None, help="Projeto no Azure DevOps")
    parser.add_argument("--pat", type=str, default=None, help="Personal Access Token")
    parser.add_argument("--github-org", type=str, default=None, help="Organização no GitHub")

    args = parser.parse_args()

    if args.guide:
        print_commit_guidelines()
        return

    env_vars = load_env_file()
    org = args.org or os.getenv("AZURE_DEVOPS_ORG") or env_vars.get("AZURE_DEVOPS_ORG", "ZelaFixGS")
    project = args.project or os.getenv("AZURE_DEVOPS_PROJECT") or env_vars.get("AZURE_DEVOPS_PROJECT", "ZelaFix")
    pat = args.pat or os.getenv("AZURE_DEVOPS_PAT") or env_vars.get("AZURE_DEVOPS_PAT", "")
    github_org = args.github_org or os.getenv("GITHUB_ORG") or env_vars.get("GITHUB_ORG", "Global-Solution-CitizenTech")

    linker = AzureCommitLinker(organization=org, project=project, pat=pat, github_org=github_org)

    # Diretório raiz com os 7 repositórios (pai de Compliance-Quality-Assurance-Tests)
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    if args.item_id and args.commit and args.repo:
        full_url = f"https://github.com/{github_org}/{args.repo}/commit/{args.commit}"
        print(f"🔗 Vinculando commit {args.commit} ({args.repo}) ao Work Item #{args.item_id}...")
        linker.link_commit_to_work_item(args.item_id, full_url, dry_run=args.dry_run)
    else:
        # Padrão: scan all
        scan_and_link(linker, base_dir, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
