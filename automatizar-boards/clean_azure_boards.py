#!/usr/bin/env python3
"""
ZelaFix - Limpeza de Boards (Wrapper de Compatibilidade)
Redireciona para o motor unificado SyncEngine.
"""

import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from sync_engine import SyncEngine


def main():
    confirm = input("⚠️ ATENÇÃO: Deseja realmente remover todos os Work Items do projeto? (s/N): ").strip().lower()
    if confirm == "s":
        engine = SyncEngine()
        engine.clean_board()
    else:
        print("Operação de limpeza cancelada.")


if __name__ == "__main__":
    main()
