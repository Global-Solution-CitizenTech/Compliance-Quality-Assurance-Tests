#!/usr/bin/env python3
"""
ZelaFix - Script de Atualização e Governança de Work Items no Azure Boards
1. Remove o prefixo 'GS 2026/2 - ' dos títulos de todos os Épicos.
2. Remove blocos HTML redundantes (header_desc) das descrições dos Épicos.
3. Atribui formalmente os responsáveis por disciplina:
   - Mobile: Luna de Carvalho Guimarães (RM562290@fiap.com.br)
   - .NET: Gustavo Okada / MR563428 (MR563428@fiap.com.br)
   - DevOps: Milton Jakson de Sousa Marcelino (RM564836@fiap.com.br)
   - Database: Lucas Barros Gouveia (RM566422@fiap.com.br)
   - Disruptive Architectures (IoT & IA): Enzo Okuizumi (RM561432@fiap.com.br)
   - Compliance, QA & Tests: Enzo Okuizumi (RM561432@fiap.com.br)
   - Java Advanced: Enzo Okuizumi (RM561432@fiap.com.br)
4. Atualiza o State de todos os itens:
   - Epics: 'In Progress'
   - Features: 'In Progress'
   - PBIs: 'Committed' (In Progress no modelo Scrum)
   - Test Cases: 'Ready'
"""

import sys
import os
import json
import base64
import requests
from dotenv import load_dotenv

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ASSIGNMENT_MAP = {
    "Mobile": "RM562290@fiap.com.br",
    "DotNet": "MR563428@fiap.com.br",
    "DevOps": "RM564836@fiap.com.br",
    "Database": "RM566422@fiap.com.br",
    "DisruptiveArchitectures": "RM561432@fiap.com.br",
    "Compliance": "RM561432@fiap.com.br",
    "JavaAdvanced": "RM561432@fiap.com.br"
}

CLEAN_EPIC_DESCRIPTIONS = {
    "Mobile": "<p>Desenvolvimento do aplicativo móvel ZelaFix em React Native com Expo e TypeScript para viabilizar o relato e acompanhamento transparente de problemas urbanos, integrando autenticação segura JWT, geolocalização por GPS, envio de fotos de evidência, engajamento por votação coletiva em melhorias do bairro e suporte a cache offline resiliente.</p>",
    "JavaAdvanced": "<p>Desenvolvimento da API RESTful Spring Boot central da plataforma ZelaFix, integrando persistência relacional no Oracle Cloud, segurança stateless com Spring Security e JWT, regras de negócio robustas para abertura e ciclo de vida de chamados municipais e documentação viva via OpenAPI 3 / Swagger.</p>",
    "DotNet": "<p>Desenvolvimento do microsserviço de mensageria, notificações push/e-mail e alertas urbanos do ZelaFix em ASP.NET Core (.NET 8), implementando Arquitetura Limpa, observabilidade avançada (OpenTelemetry, Prometheus, HealthChecks) e suite rigorosa de testes unitários xUnit com Moq.</p>",
    "Database": "<p>Modelagem relacional completa do ecossistema ZelaFix no Oracle Database 11g, automação de regras críticas via PL/SQL (Packages, Stored Procedures, Functions e Triggers de auditoria DML) e persistência de documentos semiestruturados de telemetria no MongoDB.</p>",
    "DevOps": "<p>Estruturação da infraestrutura como código (IaC) e esteira de entrega contínua para o ZelaFix na Microsoft Azure, containerização multi-serviço com Docker e Docker Compose, e pipeline robusto de CI/CD com GitHub Actions e monitoramento.</p>",
    "DisruptiveArchitectures": "<p>Implementação do sistema inteligente de sensoriamento urbano (ESP32/MQTT) para monitoramento em tempo real de alagamentos e bueiros, aliado a um microsserviço Python com IA Generativa e visão computacional para triagem e classificação automática de ocorrências.</p>",
    "Compliance": "<p>Planejamento ágil Scrum no Azure Boards, governança de backlog multidisciplinar, garantia de rastreabilidade de commits dos 7 repositórios e formalização de plano de testes manuais caixa-preta para homologação do ecossistema ZelaFix.</p>"
}

def update_all():
    load_dotenv()
    org = os.getenv("AZURE_DEVOPS_ORG", "ZelaFixGS")
    project = os.getenv("AZURE_DEVOPS_PROJECT", "ZelaFix")
    pat = os.getenv("AZURE_DEVOPS_PAT", "")

    if not pat:
        print("❌ PAT não encontrado no .env")
        return

    auth = base64.b64encode(f":{pat}".encode()).decode()
    headers_patch = {"Authorization": f"Basic {auth}", "Content-Type": "application/json-patch+json"}
    headers_get = {"Authorization": f"Basic {auth}", "Content-Type": "application/json"}

    print("================================================================================")
    print("🚀 INICIANDO ATUALIZAÇÃO E GOVERNANÇA GERAL NO AZURE BOARDS")
    print(f"🏛️ Organização: {org} | Projeto: {project}")
    print("================================================================================")

    # 1. Busca todos os IDs
    wiql = {"query": "Select [System.Id] From WorkItems Where [System.TeamProject] = @project"}
    res = requests.post(f"https://dev.azure.com/{org}/{project}/_apis/wit/wiql?api-version=7.0", json=wiql, headers=headers_get)
    if res.status_code != 200:
        print(f"❌ Erro ao buscar work items: {res.text}")
        return

    ids = [it["id"] for it in res.json().get("workItems", [])]
    print(f"📦 Total de itens encontrados: {len(ids)}")

    # 2. Busca detalhes em lote
    b_res = requests.post(
        f"https://dev.azure.com/{org}/{project}/_apis/wit/workitemsbatch?api-version=7.0",
        json={"ids": ids, "fields": ["System.Id", "System.Title", "System.WorkItemType", "System.Tags", "System.State", "System.AssignedTo", "System.Description"]},
        headers=headers_get
    )
    items_data = b_res.json().get("value", [])

    updated_count = 0

    for item in items_data:
        item_id = item["id"]
        fields = item.get("fields", {})
        wtype = fields.get("System.WorkItemType")
        title = fields.get("System.Title", "")
        tags = fields.get("System.Tags", "")
        curr_state = fields.get("System.State", "")

        patch_doc = []

        # Identifica a matéria pela tag
        matched_discipline = None
        for disc in ASSIGNMENT_MAP.keys():
            if disc in tags:
                matched_discipline = disc
                break

        # Responsável
        if matched_discipline:
            target_user = ASSIGNMENT_MAP[matched_discipline]
            patch_doc.append({"op": "add", "path": "/fields/System.AssignedTo", "value": target_user})
        elif wtype == "Test Case":
            patch_doc.append({"op": "add", "path": "/fields/System.AssignedTo", "value": "RM561432@fiap.com.br"})

        # State
        if wtype in ["Epic", "Feature"]:
            if curr_state != "In Progress":
                patch_doc.append({"op": "add", "path": "/fields/System.State", "value": "In Progress"})
        elif wtype == "Product Backlog Item":
            if curr_state != "Committed":
                patch_doc.append({"op": "add", "path": "/fields/System.State", "value": "Committed"})
        elif wtype == "Test Case":
            if curr_state != "Ready":
                patch_doc.append({"op": "add", "path": "/fields/System.State", "value": "Ready"})

        # Limpeza de Título e Descrição nos Épicos
        if wtype == "Epic":
            new_title = title.replace("GS 2026/2 - ", "").replace("GS 2026/2 -", "").strip()
            if new_title != title:
                patch_doc.append({"op": "add", "path": "/fields/System.Title", "value": new_title})
            
            # Limpa descrição se contiver header redundante
            if matched_discipline and matched_discipline in CLEAN_EPIC_DESCRIPTIONS:
                clean_desc = CLEAN_EPIC_DESCRIPTIONS[matched_discipline]
                patch_doc.append({"op": "add", "path": "/fields/System.Description", "value": clean_desc})

        if patch_doc:
            p_res = requests.patch(
                f"https://dev.azure.com/{org}/_apis/wit/workitems/{item_id}?api-version=7.0",
                json=patch_doc,
                headers=headers_patch
            )
            if p_res.status_code == 200:
                updated_count += 1
                assigned_name = p_res.json().get("fields", {}).get("System.AssignedTo", {}).get("displayName", "N/A")
                res_state = p_res.json().get("fields", {}).get("System.State", "")
                print(f"  ✅ #{item_id} [{wtype}] atualizado: Responsável={assigned_name} | State={res_state}")
            else:
                print(f"  ❌ Erro ao atualizar #{item_id}: {p_res.text[:150]}")

    print("================================================================================")
    print(f"✨ Concluído! {updated_count}/{len(ids)} Work Items atualizados com sucesso.")
    print("================================================================================")

if __name__ == "__main__":
    update_all()
