#!/usr/bin/env python3
"""
ZelaFix - Orquestrador Unificado do Azure Boards (CLI Principal)
Ponto de entrada único para Carga de Backlogs, Casos de Testes, Commits e Governança Scrum.
"""

import sys
import argparse

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from config import AZURE_ORG, AZURE_PROJECT, DISCIPLINES
from sync_engine import SyncEngine
from install_git_hooks import install_hooks


def print_banner():
    banner = f"""
================================================================================
🚀 ZELAFIX AZURE BOARDS AUTOMATION CLI (FIAP 2TDSPG)
🏛️ Organização: {AZURE_ORG} | Projeto: {AZURE_PROJECT}
================================================================================
"""
    print(banner)


def main():
    parser = argparse.ArgumentParser(
        description="ZelaFix - Automação Completa de Backlogs, QA e Governança para Azure Boards",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de Uso:
  python run_sync.py --all                    # Importa os backlogs das 7 disciplinas
  python run_sync.py --discipline mobile      # Importa somente uma disciplina
  python run_sync.py --test-cases             # Cria os 20 Test Cases vinculados às Features
  python run_sync.py --commits                # Varre os 7 repositórios locais e vincula commits
  python run_sync.py --govern                 # Aplica atribuição de responsáveis e estados
  python run_sync.py --status                 # Exibe o painel de saúde e métricas do projeto
  python run_sync.py --full                   # Executa o pipeline completo (carga, testes, commits, docs)
  python run_sync.py --dry-run --all          # Simula a importação sem alterar o Azure
        """
    )

    parser.add_argument("--all", "-a", action="store_true", help="Importar backlogs das 7 disciplinas")
    parser.add_argument("--discipline", "-d", type=str, choices=list(DISCIPLINES.keys()), help="Importar disciplina específica")
    parser.add_argument("--test-cases", "-t", action="store_true", help="Sincronizar os 20 Casos de Teste Caixa-Preta")
    parser.add_argument("--commits", "-c", action="store_true", help="Escanear os 7 repositórios e vincular commits")
    parser.add_argument("--govern", "-g", action="store_true", help="Aplicar governança de responsáveis e estados (In Progress/Committed)")
    parser.add_argument("--docs", action="store_true", help="Gerar documentação Markdown da Matriz e do Plano de Testes")
    parser.add_argument("--hooks", action="store_true", help="Instalar post-commit hooks nos 7 repositórios locais")
    parser.add_argument("--status", "-s", action="store_true", help="Exibir resumo consolidado de saúde dos Work Items")
    parser.add_argument("--clean", action="store_true", help="Limpar todos os Work Items do projeto com segurança")
    parser.add_argument("--check-auth", action="store_true", help="Verificar conexão e permissões no Azure DevOps")
    parser.add_argument("--full", action="store_true", help="Executar pipeline completo de ponta a ponta")
    parser.add_argument("--dry-run", action="store_true", help="Modo simulação (não grava na nuvem)")

    args = parser.parse_args()

    # Se nenhum argumento for passado, exibe o status por padrão
    if not any([args.all, args.discipline, args.test_cases, args.commits, args.govern, args.docs, args.hooks, args.status, args.clean, args.check_auth, args.full]):
        print_banner()
        engine = SyncEngine()
        engine.get_project_status()
        print("💡 Dica: Use 'python run_sync.py --help' para listar todos os comandos disponíveis.")
        return

    print_banner()
    engine = SyncEngine()

    if args.check_auth:
        ok, msg = engine.client.check_connection()
        print(f"📡 Status da Conexão: {'✅ SUCESSO' if ok else '❌ FALHA'}")
        print(f"ℹ️ Detalhes: {msg}\n")
        return

    if args.clean:
        confirm = input("⚠️ ATENÇÃO: Deseja realmente remover todos os Work Items do projeto? (s/N): ").strip().lower()
        if confirm == "s":
            engine.clean_board()
        else:
            print("Operação de limpeza cancelada.")
        return

    if args.full:
        print("🚀 Executando Pipeline Completo de Homologação ZelaFix...")
        engine.sync_all_disciplines(dry_run=args.dry_run)
        engine.sync_test_cases(dry_run=args.dry_run)
        engine.scan_and_link_commits(dry_run=args.dry_run)
        engine.apply_governance(dry_run=args.dry_run)
        engine.export_test_documentation()
        engine.get_project_status()
        return

    if args.all:
        engine.sync_all_disciplines(dry_run=args.dry_run)

    if args.discipline:
        engine.sync_discipline(args.discipline, dry_run=args.dry_run)

    if args.test_cases:
        engine.sync_test_cases(dry_run=args.dry_run)

    if args.commits:
        engine.scan_and_link_commits(dry_run=args.dry_run)

    if args.govern:
        engine.apply_governance(dry_run=args.dry_run)

    if args.docs:
        engine.export_test_documentation()

    if args.hooks:
        install_hooks()

    if args.status:
        engine.get_project_status()


if __name__ == "__main__":
    main()
