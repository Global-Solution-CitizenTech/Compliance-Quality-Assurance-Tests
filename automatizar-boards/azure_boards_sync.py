#!/usr/bin/env python3
"""
ZelaFix - Sincronizador de Backlog (Wrapper de Compatibilidade)
Redireciona para o motor unificado SyncEngine e parser_backlog.
"""

import sys

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from sync_engine import SyncEngine
from parser_backlog import parse_backlog_markdown, clean_title

# Mantém compatibilidade com importações antigas
__all__ = ["SyncEngine", "parse_backlog_markdown", "clean_title"]

if __name__ == "__main__":
    from run_sync import main
    main()
