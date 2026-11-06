#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🏛️ CitizenTech — Orquestrador de Sincronização Azure Boards
=============================================================================
Importador automático de Backlog Scrum (Epic -> Feature -> PBI -> Task),
vínculo de commits Git de todos os 7 repositórios e Casos de Testes.

FIAP Global Solution 2026/2 — CitizenTech
Disciplina: Compliance, Quality Assurance & Tests
=============================================================================
"""

import sys
import os
import argparse
from typing import List

# Garante suporte a UTF-8 no terminal Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Adiciona diretório atual ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from parser_backlog import parse_backlog_markdown
from azure_boards_sync import AzureBoardsClient
from link_commits import AzureCommitLinker, scan_and_link
from sync_test_cases import sync_test_cases_to_azure, export_test_matrix_md, export_test_plan_md


def load_env_file(env_path: str = None) -> dict:
    """Lê arquivo .env simples sem depender de bibliotecas externas."""
    candidates = [
        env_path,
        os.path.join(os.path.dirname(__file__), ".env"),
        os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"),
        os.path.join(os.getcwd(), ".env")
    ]
    env_vars = {}
    for p in candidates:
        if p and os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    k, v = line.split("=", 1)
                    env_vars[k.strip()] = v.strip().strip("'\"")
            break
    return env_vars


BACKLOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "backlog-materias")

ALL_DISCIPLINE_FILES = [
    (os.path.join(BACKLOG_DIR, "BACKLOG_MOBILE.md"), "Mobile Application Development"),
    (os.path.join(BACKLOG_DIR, "BACKLOG_JAVA_ADVANCED.md"), "Java Advanced"),
    (os.path.join(BACKLOG_DIR, "BACKLOG_DOT_NET.md"), "Advanced Business Development with .NET"),
    (os.path.join(BACKLOG_DIR, "BACKLOG_DATABASE_ADVANCED.md"), "Database Advanced"),
    (os.path.join(BACKLOG_DIR, "BACKLOG_DEVOPS.md"), "DevOps Tools & Cloud Computing"),
    (os.path.join(BACKLOG_DIR, "BACKLOG_DISRUPTIVE_ARCHITECTURES.md"), "Disruptive Architectures (IoT & IA)"),
    (os.path.join(BACKLOG_DIR, "BACKLOG_COMPLIANCE.md"), "Compliance, Quality Assurance & Tests")
]


def main():
    parser = argparse.ArgumentParser(
        description="CitizenTech - Automação de Backlog & QA para Azure Boards (Epic -> Feature -> PBI -> Task -> Test Case -> Commits)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  1. Testar conexão com Azure DevOps:
     python run_sync.py --check-auth

  2. Simular importação de todos os 7 backlogs (Dry-Run):
     python run_sync.py --all --dry-run

  3. Importar uma matéria específica:
     python run_sync.py --file BACKLOG_MOBILE.md --dry-run
     python run_sync.py --file BACKLOG_COMPLIANCE.md

  4. Importar todas as matérias de uma vez no Board unificado:
     python run_sync.py --all

  5. Vincular commits Git dos 7 repositórios aos Work Items:
     python run_sync.py --link-commits
     python run_sync.py --link-commits --dry-run

  6. Sincronizar os 20 Casos de Testes no Azure Boards / Test Plans:
     python run_sync.py --sync-test-cases
     python run_sync.py --sync-test-cases --dry-run
        """
    )

    parser.add_argument("--file", "-f", type=str, default=None, help="Caminho ou nome do arquivo de backlog (em backlog-materias/)")
    parser.add_argument("--all", "-a", action="store_true", help="Importar backlogs de todas as 7 disciplinas do CitizenTech")
    parser.add_argument("--dry-run", "-d", action="store_true", help="Modo simulação: executa o parser e exibe a hierarquia sem criar nada na nuvem")
    parser.add_argument("--check-auth", "-c", action="store_true", help="Valida se as credenciais e o projeto do Azure DevOps estão acessíveis")
    parser.add_argument("--link-commits", "-l", action="store_true", help="Escaneia os 7 repositórios git e vincula os commits aos Work Items")
    parser.add_argument("--sync-test-cases", "-t", action="store_true", help="Sincroniza a suíte de 20 casos de testes (caixa-preta) no Azure")
    parser.add_argument("--org", type=str, default=None, help="Nome da organização Azure DevOps (Ex: ZelaFixGS)")
    parser.add_argument("--project", type=str, default=None, help="Nome do projeto Azure DevOps (Ex: CitizenTech)")
    parser.add_argument("--pat", type=str, default=None, help="Personal Access Token (PAT) do Azure DevOps")

    args = parser.parse_args()

    # Carrega variáveis do arquivo .env se existirem
    env_vars = load_env_file()
    org = args.org or os.getenv("AZURE_DEVOPS_ORG") or env_vars.get("AZURE_DEVOPS_ORG", "ZelaFixGS")
    project = args.project or os.getenv("AZURE_DEVOPS_PROJECT") or env_vars.get("AZURE_DEVOPS_PROJECT", "ZelaFix")
    pat = args.pat or os.getenv("AZURE_DEVOPS_PAT") or env_vars.get("AZURE_DEVOPS_PAT", "")
    github_org = env_vars.get("GITHUB_ORG", "ZelaFixGS")

    client = AzureBoardsClient(organization=org, project=project, pat=pat)

    if args.check_auth:
        print(f"\n🔍 Verificando conexão com Azure DevOps...")
        print(f"🏛️ Organização: {org}")
        print(f"📁 Projeto: {project}")
        ok, msg = client.check_connection()
        if ok:
            print(f"✅ {msg}")
        else:
            print(f"❌ Falha de autenticação / conexão:\n{msg}")
            print("\n💡 Dica: Verifique se o seu PAT está preenchido no arquivo .env com permissão 'Work Items (Read & Write)'.")
        return

    # Execução de Casos de Teste isolada
    if args.sync_test_cases:
        sync_test_cases_to_azure(org=org, project=project, pat=pat, dry_run=args.dry_run)
        return

    # Execução de Vínculo de Commits isolada
    if args.link_commits:
        base_repos_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        linker = AzureCommitLinker(organization=org, project=project, pat=pat, github_org=github_org)
        scan_and_link(linker, base_repos_dir, dry_run=args.dry_run)
        return

    # Modo de execução de Backlogs: Todos ou Arquivo Único
    if args.all:
        print(f"\n🚀 Modo Selecionado: IMPORTAÇÃO TOTAL DE TODAS AS 7 DISCIPLINAS (CITIZENTECH)")
        total_stats = {"epics": 0, "features": 0, "pbis": 0, "tasks": 0}
        
        for full_path, disc_name in ALL_DISCIPLINE_FILES:
            if not os.path.exists(full_path):
                print(f"⚠️ Arquivo não encontrado: {full_path} (pulando...)")
                continue
            
            doc = parse_backlog_markdown(full_path)
            stats = client.sync_backlog(doc, dry_run=args.dry_run)
            for k in total_stats:
                total_stats[k] += stats.get(k, 0)

        print(f"\n========================================================")
        print(f"🎉 FINAL DA CARGA TOTAL CONSOLIDADA!")
        print(f"👑 Epics: {total_stats['epics']}")
        print(f"🏆 Features: {total_stats['features']}")
        print(f"📄 PBIs: {total_stats['pbis']}")
        print(f"🔨 Tasks: {total_stats['tasks']}")
        print(f"========================================================\n")

    elif args.file:
        target_path = args.file
        if not os.path.exists(target_path):
            # Tenta dentro da pasta backlog-materias
            candidate = os.path.join(BACKLOG_DIR, args.file)
            if os.path.exists(candidate):
                target_path = candidate
            else:
                candidate2 = os.path.join(os.path.dirname(__file__), args.file)
                if os.path.exists(candidate2):
                    target_path = candidate2
                else:
                    print(f"❌ Erro: Arquivo de backlog não encontrado: {args.file}")
                    return

        doc = parse_backlog_markdown(target_path)
        client.sync_backlog(doc, dry_run=args.dry_run)
    else:
        # Se nenhum argumento for passado, exibe menu / ajuda
        parser.print_help()


if __name__ == "__main__":
    main()
