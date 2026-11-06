#!/usr/bin/env python3
"""
ZelaFix - Instalador de Git Hooks para Automação de Commits no Azure Boards
Instala um hook 'post-commit' em cada um dos 7 repositórios locais para que,
ao commitar com 'AB#<ID>', o vínculo com o Azure Boards seja realizado automaticamente.
"""

import sys
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
import os
import stat

REPOSITORIES = [
    "Mobile-Application-Development",
    "Java-Advanced",
    "Database-Advanced",
    "Advanced-Business-Development-with-Dot-Net",
    "DevOps-Tools-Cloud-Computing",
    "Disruptive-Architectures-IoT-IoB-IA",
    "Compliance-Quality-Assurance-Tests"
]

HOOK_SCRIPT = """#!/bin/sh
# Auto-link commit to Azure Boards
COMMIT_HASH=$(git rev-parse HEAD)
REPO_NAME=$(basename -s .git `git config --get remote.origin.url 2>/dev/null || pwd`)
COMMIT_MSG=$(git log -1 --pretty=%B)

# Verifica se contem tag AB#
if echo "$COMMIT_MSG" | grep -qE "AB#[0-9]+"; then
    echo "[ZelaFix QA Hook] Detectada tag AB# no commit $COMMIT_HASH ($REPO_NAME). Vinculando ao Azure Boards..."
    # Localiza o script link_commits.py
    SCRIPT_PATH="$(git rev-parse --show-toplevel)/../Compliance-Quality-Assurance-Tests/automatizar-boards/link_commits.py"
    if [ -f "$SCRIPT_PATH" ]; then
        python "$SCRIPT_PATH" --scan-all > /dev/null 2>&1 &
    fi
fi
"""

def install_hooks():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print("================================================================================")
    print("🔧 INSTALADOR DE GIT HOOKS (POST-COMMIT) - ZELAFIX")
    print(f"📁 Diretório Base: {base_dir}")
    print("================================================================================")
    
    installed = 0
    for repo in REPOSITORIES:
        repo_dir = os.path.join(base_dir, repo)
        hooks_dir = os.path.join(repo_dir, ".git", "hooks")
        
        if not os.path.exists(hooks_dir):
            print(f"⚠️  [.git/hooks não encontrado]: {repo} (pulado)")
            continue
            
        hook_file = os.path.join(hooks_dir, "post-commit")
        try:
            with open(hook_file, "w", encoding="utf-8") as f:
                f.write(HOOK_SCRIPT)
            # Permissão de execução no Linux/mac/Git Bash
            st = os.stat(hook_file)
            os.chmod(hook_file, st.st_mode | stat.S_IEXEC)
            print(f"✅ Hook instalado com sucesso em: {repo}")
            installed += 1
        except Exception as e:
            print(f"❌ Erro ao instalar hook em {repo}: {e}")
            
    print("================================================================================")
    print(f"🎉 Concluído: {installed}/{len(REPOSITORIES)} repositórios configurados com post-commit hook!")
    print("Sempre que commitar com 'AB#<ID>', o vínculo será acionado automaticamente.")
    print("================================================================================")

if __name__ == "__main__":
    install_hooks()
