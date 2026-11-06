#!/usr/bin/env python3
"""
ZelaFix - Rastreamento e Vínculo de Commits Git (Wrapper de Compatibilidade)
Redireciona para o motor unificado SyncEngine.
"""

import sys
import argparse

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from sync_engine import SyncEngine


def print_commit_guidelines():
    print("""
=============================================================================
📘 GUIA OFICIAL DE MENSAGENS DE COMMIT COM RASTREABILIDADE AZURE BOARDS
=============================================================================
Para que o Azure DevOps e GitHub vinculem seus commits aos Work Items:

1. Vincular commit ao Work Item (Ex: PBI #5):
   git commit -m "feat(mobile): implementa tela de login AB#5"

2. Resolver ou fechar uma tarefa automaticamente:
   git commit -m "fix(database): corrige sequence de chamados Fixes AB#38"

3. Vincular múltiplos itens:
   git commit -m "feat: integração entre mobile e java AB#5 AB#16"

💡 A tag 'AB#<ID>' é o padrão internacional do Azure Boards para rastreabilidade!
=============================================================================
""")


def main():
    parser = argparse.ArgumentParser(description="ZelaFix - Vinculação de Commits Git ao Azure Boards")
    parser.add_argument("--scan-all", "-s", action="store_true", help="Varre os 7 repositórios e vincula commits")
    parser.add_argument("--dry-run", "-d", action="store_true", help="Modo simulação")
    parser.add_argument("--guide", "-g", action="store_true", help="Exibe guia de boas práticas de commits")
    args = parser.parse_args()

    if args.guide:
        print_commit_guidelines()
        return

    engine = SyncEngine()
    engine.scan_and_link_commits(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
