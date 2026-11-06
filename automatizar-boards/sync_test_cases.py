#!/usr/bin/env python3
"""
ZelaFix - Sincronizador de Casos de Teste (Wrapper de Compatibilidade)
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


def main():
    parser = argparse.ArgumentParser(description="ZelaFix - Sincronização de Casos de Testes no Azure Boards")
    parser.add_argument("--sync-azure", "-s", action="store_true", help="Cria os casos de teste no Azure Boards")
    parser.add_argument("--dry-run", "-d", action="store_true", help="Modo simulação")
    parser.add_argument("--export-all", "-e", action="store_true", help="Exporta matriz e plano em Markdown")
    args = parser.parse_args()

    engine = SyncEngine()

    if args.export_all or (not args.sync_azure and not args.dry_run):
        engine.export_test_documentation()

    if args.sync_azure or args.dry_run:
        engine.sync_test_cases(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
