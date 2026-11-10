#!/usr/bin/env python3
"""
ZelaFix - Sincronizador de Iteration Paths no Azure Boards
Atribui cada Work Item (Epic, Feature, PBI) à iteração correspondente:
- Semana 1: Mobile, Java Advanced, Database Advanced
- Semana 2: DevOps Tools, .NET, Disruptive Architectures, Compliance
"""

import sys
import os
import argparse
from typing import Dict, Any, Optional

# Garante suporte a UTF-8 no terminal Windows
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from azure_client import AzureClient
from config import AZURE_ORG, AZURE_PROJECT, AZURE_PAT, DISCIPLINES


def classify_discipline_from_tags_or_title(tags: str, title: str) -> Optional[str]:
    """Identifica a matéria a partir das tags oficiais ou do título."""
    t_str = (tags or "").lower()

    if "mobile" in t_str:
        return "mobile"
    if "javaadvanced" in t_str or "java" in t_str:
        return "java"
    if "database" in t_str:
        return "database"
    if "devops" in t_str:
        return "devops"
    if "disruptivearchitectures" in t_str or "disruptive" in t_str or "iot" in t_str:
        return "iot"
    if "dotnet" in t_str or ".net" in t_str:
        return "dotnet"
    if "compliance" in t_str or "qa" in t_str:
        return "compliance"

    title_lower = (title or "").lower()
    if "mobile" in title_lower:
        return "mobile"
    if "java" in title_lower or "spring" in title_lower:
        return "java"
    if "database" in title_lower or "oracle" in title_lower or "pl/sql" in title_lower:
        return "database"
    if "devops" in title_lower or "cloud" in title_lower:
        return "devops"
    if "disruptive" in title_lower or "iot" in title_lower:
        return "iot"
    if ".net" in title_lower or "dotnet" in title_lower:
        return "dotnet"
    if "compliance" in title_lower or "quality assurance" in title_lower:
        return "compliance"

    return None


class AzureIterationManager:
    def __init__(self, client: Optional[AzureClient] = None):
        self.client = client or AzureClient(AZURE_ORG, AZURE_PROJECT, AZURE_PAT)
        self.project = AZURE_PROJECT

    def sync_all_iterations(self, filter_discipline: Optional[str] = None, dry_run: bool = False) -> Dict[str, int]:
        prefix = "[DRY-RUN] " if dry_run else ""
        print(f"\n========================================================")
        print(f"🔄 {prefix}Sincronizador de Iteration Paths no Azure Boards")
        print(f"🏛️ Organização: {AZURE_ORG} | Projeto: {self.project}")
        print(f"📅 Semana 1 (04/11 a 11/11): Mobile, Java Advanced, Database Advanced")
        print(f"📅 Semana 2 (12/11 a 19/11): DevOps Tools, .NET, Disruptive Architectures, Compliance")
        print(f"========================================================\n")

        ids = self.client.query_wiql(f"Select [System.Id] From WorkItems Where [System.TeamProject] = '{self.project}'")
        items = self.client.get_batch(ids, fields=["System.Id", "System.WorkItemType", "System.Title", "System.IterationPath", "System.Tags"])
        print(f"🔍 Total de Work Items encontrados no projeto: {len(items)}\n")

        stats = {
            "semana1_updated": 0,
            "semana2_updated": 0,
            "already_correct": 0,
            "unmapped": 0,
            "errors": 0
        }

        for item in items:
            i_id = item["id"]
            fields = item.get("fields", {})
            w_type = fields.get("System.WorkItemType", "Item")
            title = fields.get("System.Title", "")
            tags = fields.get("System.Tags", "")
            current_path = fields.get("System.IterationPath", "")

            disc = classify_discipline_from_tags_or_title(tags, title)
            if not disc or disc not in DISCIPLINES:
                print(f"⚠️ Item #{i_id} ({w_type}): '{title}' (sem matéria identificada)")
                stats["unmapped"] += 1
                continue

            if filter_discipline and filter_discipline.lower() not in disc:
                continue

            rel_iter = DISCIPLINES[disc]["iteration"]
            target_path = f"{self.project}\\{rel_iter}"

            if current_path == target_path:
                stats["already_correct"] += 1
                continue

            is_sem1 = "Semana 1" in target_path
            target_label = "Semana 1" if is_sem1 else "Semana 2"

            if dry_run:
                print(f"   [DRY-RUN] #{i_id:03d} ({w_type:20s}): '{title[:45]}...' ➔ {target_label} ({target_path})")
                if is_sem1:
                    stats["semana1_updated"] += 1
                else:
                    stats["semana2_updated"] += 1
            else:
                patch = [{"op": "replace", "path": "/fields/System.IterationPath", "value": target_path}]
                ok = self.client.update_work_item(i_id, patch)
                if ok:
                    print(f"   ✅ #{i_id:03d} ({w_type:20s}): '{title[:45]}...' ➔ {target_label}")
                    if is_sem1:
                        stats["semana1_updated"] += 1
                    else:
                        stats["semana2_updated"] += 1
                else:
                    print(f"   ❌ Erro ao atualizar #{i_id}")
                    stats["errors"] += 1

        print(f"\n========================================================")
        print(f"✨ {prefix}Relatório Final de Sincronização de Iterações:")
        print(f"   • Atualizados para Semana 1: {stats['semana1_updated']}")
        print(f"   • Atualizados para Semana 2: {stats['semana2_updated']}")
        print(f"   • Já estavam no caminho correto: {stats['already_correct']}")
        print(f"   • Não mapeados / Ignorados: {stats['unmapped']}")
        print(f"   • Erros de atualização: {stats['errors']}")
        print(f"========================================================\n")
        return stats


def main():
    parser = argparse.ArgumentParser(description="Atualiza e padroniza os IterationPaths no Azure Boards")
    parser.add_argument("--dry-run", "-d", action="store_true", help="Simula as alterações sem modificar a nuvem")
    parser.add_argument("--discipline", "-m", type=str, default=None, help="Filtra por matéria específica (ex: mobile, java, database, devops)")
    args = parser.parse_args()

    manager = AzureIterationManager()
    manager.sync_all_iterations(filter_discipline=args.discipline, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
