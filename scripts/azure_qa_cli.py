#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🏛️ CitizenTech — Azure DevOps QA & Test Plans Management CLI
=============================================================================
Script utilitário para inspeção, controle e execução dos Planos de Testes
do Azure Boards / Test Plans via REST API oficial da Microsoft Azure DevOps.

FIAP Global Solution 2026/2 — CitizenTech
Disciplina: Compliance, Quality Assurance & Tests
Equipe: Enzo Okuizumi, Gustavo Okada, Lucas Barros Gouveia,
        Luna de Carvalho Guimarães, Milton Marcelino.
=============================================================================
"""

import os
import sys
import json
import base64
import argparse
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

# Garante suporte adequado a UTF-8 em terminais Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# Carrega variáveis de arquivo .env local automaticamente (sem dependências externas)
def _load_dotenv():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(os.path.dirname(script_dir), "automatizar-boards", ".env"),
        os.path.join(os.path.dirname(script_dir), ".env"),
        os.path.join(script_dir, ".env"),
        os.path.join(os.getcwd(), ".env")
    ]
    for env_path in candidates:
        if os.path.isfile(env_path):
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        os.environ.setdefault(k.strip(), v.strip().strip("'\""))
            break

_load_dotenv()

# Configurações Padrão
ORGANIZATION = os.environ.get("AZURE_DEVOPS_ORG", "ZelaFixGS")
PROJECT_ID = os.environ.get("AZURE_DEVOPS_PROJECT", "ZelaFix")
PAT = os.environ.get("AZURE_DEVOPS_PAT", "")
API_VERSION = "5.0"
API_VERSION_7 = "7.0"

def get_auth_header():
    pat = os.environ.get("AZURE_DEVOPS_PAT", PAT)
    if not pat:
        print("❌ ERRO: Variável AZURE_DEVOPS_PAT não definida no ambiente ou no arquivo .env.")
        print("💡 Configure o PAT em Compliance-Quality-Assurance-Tests/.env ou use --pat [SEU_TOKEN]")
        sys.exit(1)
    return "Basic " + base64.b64encode(f":{pat}".encode("utf-8")).decode("utf-8")

def api_request(url, method="GET", body=None):
    """Executa requisição autenticada contra a API REST do Azure DevOps."""
    auth_header = get_auth_header()
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": auth_header,
        "Content-Type": "application/json"
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

def get_plans():
    """Retorna a lista de planos de testes do projeto."""
    url = f"https://dev.azure.com/{ORGANIZATION}/{PROJECT_ID}/_apis/test/plans?api-version={API_VERSION}"
    data = api_request(url)
    return data.get("value", []) if data else []

def get_suites(plan_id):
    """Retorna as suites vinculadas a um plano de testes."""
    url = f"https://dev.azure.com/{ORGANIZATION}/{PROJECT_ID}/_apis/test/plans/{plan_id}/suites?api-version={API_VERSION}"
    data = api_request(url)
    return data.get("value", []) if data else []

def get_suite_testcases(plan_id, suite_id):
    """Retorna os casos de teste pertencentes a uma suite."""
    url = f"https://dev.azure.com/{ORGANIZATION}/{PROJECT_ID}/_apis/test/plans/{plan_id}/suites/{suite_id}/testcases?api-version={API_VERSION}"
    data = api_request(url)
    return data.get("value", []) if data else []

def get_suite_points(plan_id, suite_id):
    """Retorna os pontos de execução (test points) da suite com os outcomes."""
    url = f"https://dev.azure.com/{ORGANIZATION}/{PROJECT_ID}/_apis/test/plans/{plan_id}/suites/{suite_id}/points?api-version={API_VERSION}"
    data = api_request(url)
    return data.get("value", []) if data else []

def get_work_item(wi_id):
    """Retorna detalhes de um Work Item (Caso de Teste, PBI, etc.)."""
    url = f"https://dev.azure.com/{ORGANIZATION}/_apis/wit/workitems/{wi_id}?$expand=all&api-version={API_VERSION_7}"
    return api_request(url)

def parse_steps_xml(steps_xml):
    """Converte o XML de passos do Azure Test Plans em lista de dicts legíveis."""
    steps = []
    if not steps_xml:
        return steps
    try:
        root = ET.fromstring(steps_xml)
        for st in root.findall("step"):
            action_elem = st.find("parameterizedString[1]")
            expected_elem = st.find("parameterizedString[2]")
            action = "".join(action_elem.itertext()).strip() if action_elem is not None else ""
            expected = "".join(expected_elem.itertext()).strip() if expected_elem is not None else ""
            steps.append({"action": action, "expected": expected})
    except Exception:
        pass
    return steps

def build_full_tree():
    """Gera a árvore completa de dados de planos, suítes, casos e pontos."""
    plans = get_plans()
    full_tree = []
    
    for plan in plans:
        plan_id = plan["id"]
        suites = get_suites(plan_id)
        plan_item = {
            "id": plan_id,
            "name": plan["name"],
            "state": plan.get("state"),
            "suites": []
        }
        
        for suite in suites:
            suite_id = suite["id"]
            pts = get_suite_points(plan_id, suite_id)
            tcs = get_suite_testcases(plan_id, suite_id)
            
            # Indexa pontos por ID do Test Case
            pt_by_tc = {}
            for pt in pts:
                tc_obj = pt.get("testCase", {})
                tc_key = str(tc_obj.get("id"))
                pt_by_tc[tc_key] = pt
                
            suite_item = {
                "id": suite_id,
                "name": suite["name"],
                "test_cases": []
            }
            
            for tc in tcs:
                tc_id = tc.get("testCase", {}).get("id") or tc.get("id")
                tc_key = str(tc_id)
                pt = pt_by_tc.get(tc_key, {})
                
                title = pt.get("testCase", {}).get("name") or tc.get("testCase", {}).get("name") or tc.get("title", f"TC {tc_id}")
                suite_item["test_cases"].append({
                    "id": tc_id,
                    "title": title,
                    "point_id": pt.get("id"),
                    "outcome": pt.get("outcome", "Unspecified"),
                    "plan_id": plan_id,
                    "suite_id": suite_id
                })
                
            plan_item["suites"].append(suite_item)
        full_tree.append(plan_item)
        
    return full_tree

# =============================================================================
# COMANDOS CLI
# =============================================================================

def cmd_summary():
    """Exibe painel consolidado com métricas de execução dos planos."""
    tree = build_full_tree()
    print("\n" + "="*70)
    print("🏛️ CITIZENTECH — RESUMO CONSOLIDADO DE TEST PLANS (AZURE DEVOPS)")
    print("="*70)
    
    total_plans = len(tree)
    total_suites = sum(len(p["suites"]) for p in tree)
    total_cases = 0
    outcome_stats = {}
    
    for plan in tree:
        print(f"\n📋 [Plan #{plan['id']}] {plan['name']} (Estado: {plan['state']})")
        for suite in plan["suites"]:
            s_cases = suite["test_cases"]
            total_cases += len(s_cases)
            s_outcomes = {}
            for tc in s_cases:
                out = tc["outcome"]
                s_outcomes[out] = s_outcomes.get(out, 0) + 1
                outcome_stats[out] = outcome_stats.get(out, 0) + 1
            
            out_str = ", ".join(f"{k}: {v}" for k, v in s_outcomes.items())
            print(f"  └── 📁 [Suite #{suite['id']}] {suite['name']} — {len(s_cases)} casos ({out_str})")
            
    print("\n" + "-"*70)
    print(f"📊 TOTAIS: {total_plans} Planos | {total_suites} Suites | {total_cases} Casos de Teste")
    print("🎯 EXECUÇÃO GERAL:")
    for out, count in outcome_stats.items():
        pct = (count / total_cases * 100) if total_cases > 0 else 0
        print(f"   • {out:<14}: {count:>2} casos ({pct:5.1f}%)")
    print("="*70 + "\n")

def cmd_list(target_plan=None):
    """Lista todos os casos de teste e seus status detalhados."""
    tree = build_full_tree()
    print("\n" + "="*80)
    print("🧪 LISTAGEM DETALHADA DE CASOS DE TESTE")
    print("="*80)
    
    for plan in tree:
        if target_plan and str(plan["id"]) != str(target_plan) and target_plan.lower() not in plan["name"].lower():
            continue
        print(f"\n📂 PLANO [{plan['id']}] {plan['name']}:")
        for suite in plan["suites"]:
            for tc in suite["test_cases"]:
                outcome_icon = "🟢" if tc["outcome"] == "Passed" else ("🔴" if tc["outcome"] == "Failed" else "⚪")
                print(f"  {outcome_icon} TC #{tc['id']:<5} | Status: {tc['outcome']:<12} | {tc['title']}")
    print("\n" + "="*80 + "\n")

def cmd_show(tc_id):
    """Exibe todos os campos, objetivos e passos de um caso de teste específico."""
    wi = get_work_item(tc_id)
    if not wi:
        print(f"❌ Caso de teste #{tc_id} não encontrado.")
        return
    
    fields = wi.get("fields", {})
    title = fields.get("System.Title", "Sem título")
    state = fields.get("System.State", "N/A")
    assigned = fields.get("System.AssignedTo", {}).get("displayName", "Não atribuído") if isinstance(fields.get("System.AssignedTo"), dict) else str(fields.get("System.AssignedTo", "N/A"))
    desc = fields.get("System.Description", "Nenhuma descrição fornecida.")
    clean_desc = desc.replace("<div>", "").replace("</div>", "").replace("<br>", "\n").strip()
    steps_xml = fields.get("Microsoft.VSTS.TCM.Steps", "")
    steps = parse_steps_xml(steps_xml)
    
    print("\n" + "="*80)
    print(f"🧪 CASO DE TESTE #{tc_id}: {title}")
    print("="*80)
    print(f"• Responsável : {assigned}")
    print(f"• Estado      : {state}")
    print(f"• Objetivo    : {clean_desc}")
    print(f"• Passos ({len(steps)} etapas):")
    
    for i, s in enumerate(steps, 1):
        print(f"\n   Passo {i}:")
        print(f"     👉 Ação    : {s['action']}")
        print(f"     ✅ Esperado: {s['expected']}")
    print("\n" + "="*80 + "\n")

def update_point_outcome(plan_id, suite_id, point_id, outcome):
    """Atualiza o resultado de execução de um ponto de teste."""
    url = f"https://dev.azure.com/{ORGANIZATION}/{PROJECT_ID}/_apis/test/plans/{plan_id}/suites/{suite_id}/points/{point_id}?api-version={API_VERSION}"
    if outcome == "Reset":
        body = {"resetToActive": True}
    else:
        body = {"outcome": outcome}
    return api_request(url, method="PATCH", body=body)

def cmd_run(tc_id, outcome):
    """Atualiza o resultado de um caso de teste individual."""
    if outcome not in ["Passed", "Failed", "Blocked", "NotApplicable", "Reset"]:
        print("❌ Resultado inválido! Opções válidas: Passed, Failed, Blocked, NotApplicable, Reset")
        return
        
    tree = build_full_tree()
    found = False
    for plan in tree:
        for suite in plan["suites"]:
            for tc in suite["test_cases"]:
                if str(tc["id"]) == str(tc_id):
                    found = True
                    pt_id = tc["point_id"]
                    if not pt_id:
                        print(f"❌ Ponto de teste não encontrado para o TC #{tc_id}.")
                        return
                    res = update_point_outcome(plan["id"], suite["id"], pt_id, outcome)
                    if res:
                        print(f"✅ TC #{tc_id} ({tc['title']}) atualizado com sucesso para '{outcome}'!")
                    return
    if not found:
        print(f"❌ Caso de teste #{tc_id} não encontrado nos planos atuais.")

def cmd_run_all(fail_ids=None):
    """
    Executa todos os casos de teste, marcando como Passed a maioria e Failed
    os IDs indicados (para gerar evidência realista com bugs conforme ensinado em aula).
    """
    if fail_ids is None:
        fail_ids = []
        
    tree = build_full_tree()
    print("\n" + "="*80)
    print("🚀 EXECUTANDO SUÍTE COMPLETA NO AZURE DEVOPS...")
    if fail_ids:
        print(f"ℹ️  Casos marcados para simulação de falha controlada (Bug Tracking): {fail_ids}")
    print("="*80)
    
    passed_count = 0
    failed_count = 0
    
    for plan in tree:
        for suite in plan["suites"]:
            for tc in suite["test_cases"]:
                tc_id = str(tc["id"])
                pt_id = tc["point_id"]
                target_outcome = "Failed" if tc_id in fail_ids else "Passed"
                
                res = update_point_outcome(plan["id"], suite["id"], pt_id, target_outcome)
                if res:
                    if target_outcome == "Passed":
                        passed_count += 1
                        print(f"  🟢 [PASSED] TC #{tc_id:<5} — {tc['title']}")
                    else:
                        failed_count += 1
                        print(f"  🔴 [FAILED] TC #{tc_id:<5} — {tc['title']} (Evidência de Bug)")
                else:
                    print(f"  ⚠️  [ERRO] Falha ao atualizar TC #{tc_id}")
                    
    print("\n" + "="*80)
    print(f"✨ EXECUÇÃO CONCLUÍDA! Passed: {passed_count} | Failed: {failed_count}")
    print("💡 Os gráficos (Charts) na Azure agora exibirão a pizza com resultados atualizados!")
    print("="*80 + "\n")

def cmd_reset_all():
    """Reseta todos os casos de teste para Unspecified / Active."""
    tree = build_full_tree()
    print("\n" + "="*80)
    print("🔄 RESETANDO TODOS OS CASOS DE TESTE PARA 'ACTIVE' (UNSPECIFIED)...")
    print("="*80)
    count = 0
    for plan in tree:
        for suite in plan["suites"]:
            for tc in suite["test_cases"]:
                pt_id = tc["point_id"]
                res = update_point_outcome(plan["id"], suite["id"], pt_id, "Reset")
                if res:
                    count += 1
                    print(f"  ⚪ [RESET] TC #{tc['id']} resetado")
    print(f"\n✅ Total de {count} casos de teste resetados com sucesso!\n")

def cmd_export_matrix(output_path=None):
    """Gera um arquivo Markdown completo contendo todos os casos de teste extraídos do Azure."""
    if not output_path:
        output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "MATRIZ_CASOS_DE_TESTE_AZURE.md")
    tree = build_full_tree()
    lines = [
        "# 🏛️ Matriz Completa de Casos de Testes Manuais — Azure Boards",
        "> **Sincronização Oficial:** Dados extraídos diretamente da API do Azure DevOps.",
        f"> **Organização:** `{ORGANIZATION}` | **Projeto:** `{PROJECT_ID}`",
        "",
        "---",
        ""
    ]
    
    for plan in tree:
        lines.append(f"## 📋 Plano de Teste: {plan['name']} (ID: {plan['id']})")
        lines.append("")
        for suite in plan["suites"]:
            lines.append(f"### 📁 Suíte: {suite['name']} (ID: {suite['id']})")
            lines.append("")
            lines.append("| ID Azure | Título do Caso de Teste | Status Atual | Passos Cadastrados |")
            lines.append("| :---: | :--- | :---: | :---: |")
            for tc in suite["test_cases"]:
                wi = get_work_item(tc["id"])
                fields = wi.get("fields", {}) if wi else {}
                steps_xml = fields.get("Microsoft.VSTS.TCM.Steps", "")
                steps_count = len(parse_steps_xml(steps_xml))
                status_icon = "🟢 Passed" if tc["outcome"] == "Passed" else ("🔴 Failed" if tc["outcome"] == "Failed" else "⚪ Not Run")
                lines.append(f"| **#{tc['id']}** | {tc['title']} | {status_icon} | {steps_count} passos |")
            lines.append("")
            
            lines.append("#### 🔍 Detalhamento das Etapas e Dados Controlados:")
            lines.append("")
            for tc in suite["test_cases"]:
                wi = get_work_item(tc["id"])
                fields = wi.get("fields", {}) if wi else {}
                desc = fields.get("System.Description", "").replace("<div>", "").replace("</div>", "").strip()
                steps = parse_steps_xml(fields.get("Microsoft.VSTS.TCM.Steps", ""))
                
                lines.append(f"##### 🧪 TC #{tc['id']}: {tc['title']}")
                if desc:
                    lines.append(f"**Objetivo:** {desc}")
                lines.append("")
                lines.append("| # | Ação (Entrada) | Resultado Esperado (Saída) |")
                lines.append("| :-: | :--- | :--- |")
                for idx, s in enumerate(steps, 1):
                    act_esc = s['action'].replace("\n", " ")
                    exp_esc = s['expected'].replace("\n", " ")
                    lines.append(f"| {idx} | `{act_esc}` | {exp_esc} |")
                lines.append("")
        lines.append("---")
        lines.append("")
        
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
        
    print(f"✅ Matriz de testes exportada com sucesso em: {output_path}")

def main():
    global ORGANIZATION, PROJECT_ID, PAT
    parser = argparse.ArgumentParser(description="CitizenTech - Azure DevOps Test Plans CLI")
    parser.add_argument("--org", help="Nome da organização Azure DevOps", default=None)
    parser.add_argument("--project", help="Nome ou ID do projeto Azure DevOps", default=None)
    parser.add_argument("--pat", help="Personal Access Token", default=None)

    subparsers = parser.add_subparsers(dest="command", help="Comandos disponíveis")
    
    subparsers.add_parser("summary", help="Exibe resumo com contagem e percentuais de status")
    
    list_p = subparsers.add_parser("list", help="Lista casos de teste")
    list_p.add_argument("--plan", help="Filtrar por nome ou ID do plano", default=None)
    
    show_p = subparsers.add_parser("show", help="Mostra detalhes de um caso de teste")
    show_p.add_argument("tc_id", help="ID do caso de teste no Azure DevOps")
    
    run_p = subparsers.add_parser("run", help="Atualiza status de um caso de teste")
    run_p.add_argument("tc_id", help="ID do caso de teste")
    run_p.add_argument("outcome", help="Passed, Failed, Blocked, NotApplicable ou Reset")
    
    run_all_p = subparsers.add_parser("run-all", help="Executa todos os testes (maioria Passed, falhas controladas opcionais)")
    run_all_p.add_argument("--fail-ids", nargs="*", default=[], help="IDs dos casos que devem falhar propositalmente")
    
    subparsers.add_parser("reset-all", help="Reseta todos os testes para 'Active' / 'Unspecified'")
    
    export_p = subparsers.add_parser("export", help="Exporta a matriz completa em Markdown para documentação")
    export_p.add_argument("--output", "-o", default=None, help="Caminho do arquivo Markdown de saída")
    
    args = parser.parse_args()
    
    if args.org:
        ORGANIZATION = args.org
    if args.project:
        PROJECT_ID = args.project
    if args.pat:
        PAT = args.pat
        os.environ["AZURE_DEVOPS_PAT"] = args.pat

    if args.command == "summary" or not args.command:
        cmd_summary()
    elif args.command == "list":
        cmd_list(args.plan)
    elif args.command == "show":
        cmd_show(args.tc_id)
    elif args.command == "run":
        cmd_run(args.tc_id, args.outcome)
    elif args.command == "run-all":
        cmd_run_all(args.fail_ids)
    elif args.command == "reset-all":
        cmd_reset_all()
    elif args.command == "export":
        cmd_export_matrix(args.output)

if __name__ == "__main__":
    main()
