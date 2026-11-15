#!/usr/bin/env python3
"""
Sincroniza os Work Items de Disruptive Architectures diretamente no Azure Boards (Azure DevOps)
com base no BACKLOG_DISRUPTIVE_ARCHITECTURES.md.
"""
import sys
import os
import re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from config import AZURE_ORG, AZURE_PROJECT, AZURE_PAT, GITHUB_ORG
from azure_client import AzureClient

def sync_iot_to_azure_boards():
    client = AzureClient(AZURE_ORG, AZURE_PROJECT, AZURE_PAT)
    ok, msg = client.check_connection()
    if not ok:
        print(f"❌ Erro de conexão com Azure DevOps: {msg}")
        return False
    print(f"✅ Conectado ao Azure DevOps ({AZURE_ORG}/{AZURE_PROJECT}): {msg}")

    # Atualizações de Título, Descrição e Critérios
    updates = [
        {
            "id": 58,
            "type": "Epic",
            "title": "[EPIC] Disruptive Architectures: Microsserviço ZelaFix AI (Azure AI Foundry, RAG Semântico, Tool Calling Oracle & Visão Computacional)",
            "description": "Desenvolvimento e refatoração do microsserviço inteligente ZelaFix AI (Python + FastAPI) integrado ao ecossistema CitizenTech, combinando Azure AI Foundry (LLM multimodal compatível OpenAI v1 via AI_MODEL e embeddings semânticos 1536D via AI_EMBEDDING_MODEL), banco vetorial ChromaDB com 31 chunks normativos municipais PMSP em 8 módulos, histórico multi-turno em SQLite WAL, consulta somente leitura ao Oracle FIAP via Tool Calling ReAct nativo e engajamento comunitário IoB (+1), publicado em produção no Render Cloud.",
            "acceptance_criteria": "<ul><li>Microsserviço FastAPI modular em deploy_zelafixai_render/ com entrypoint main.py e deploy em produção ativo no Render.</li><li>Base normativa municipal PMSP indexada no ChromaDB (HNSW cosseno 1536D) com AI_EMBEDDING_MODEL e reranking híbrido lexical.</li><li>Motor cognitivo único em Azure AI Foundry via AI_MODEL sem modelos fallback legados, cobrindo /ai/chat, /ai/triagem (com visão Base64) e /ai/insights.</li><li>Cliente Oracle FIAP em modo Thin (somente SELECT) com Tool Calling nativo ReAct e sanitização LGPD.</li><li>Suíte automatizada de 49 verificações funcionais (RAG normativo e cenários E2E) aprovada com 100% de cobertura e proteção contra esgotamento de quota.</li></ul>"
        },
        {
            "id": 62,
            "type": "Feature",
            "title": "[FEATURE 02] Motor Cognitivo Azure AI Foundry Multimodal, ZelaBot e Visão Computacional Urbana",
            "description": "Orquestração de IA generativa exclusivamente no Azure AI Foundry utilizando modelo multimodal compatível OpenAI v1 via AI_MODEL para chat cidadão estruturado (/ai/chat), laudo técnico de triagem com visão computacional Base64 (/ai/triagem), diagnósticos preventivos por bairro (/ai/insights), sinais IoB (+1) e guardrails LGPD.",
            "acceptance_criteria": "<ul><li>Integração direta ao Azure AI Foundry (FoundryService) utilizando modelo único multimodal via AI_MODEL e embeddings 1536D via AI_EMBEDDING_MODEL, sem fallback de provedores legados.</li><li>Chat ZelaBot em JSON estruturado com resposta, categoria, urgencia e acoes_recomendadas contextuais.</li><li>Triagem multimodal de ocorrências com enquadramento legal PMSP, SLA, checklist operacional e validação visual de evidências em Base64.</li></ul>"
        },
        {
            "id": 63,
            "type": "Product Backlog Item",
            "title": "[PBI-04] Pipeline Generativo Dinâmico em Azure AI Foundry Único e sem Fallbacks",
            "description": "<div><b>Como</b> engenheiro de IA,<br/><b>Eu quero</b> centralizar toda inferência generativa e geração de embeddings exclusivamente no Azure AI Foundry via FoundryService usando modelo multimodal dinâmico via AI_MODEL e embeddings via AI_EMBEDDING_MODEL,<br/><b>Para que</b> a plataforma opere com modelo único multimodal econômico, previsível e livre de complexidade de fallbacks legados.</div>",
            "acceptance_criteria": "<ul><li>Cliente unificado FoundryService via OpenAI(base_url=AI_BASE_URL, api_key=AI_API_KEY) suportando texto, visão Base64 e Tool Calling.</li><li>Embeddings vetoriais de 1536 dimensões gerados via AI_EMBEDDING_MODEL via endpoint REST Foundry.</li><li>Eliminação completa de provedores e modelos de fallback (Gemini, Groq, Qwen, Kimi e hash local 512D).</li></ul>"
        },
        {
            "id": 185,
            "type": "Feature",
            "title": "[FEATURE 04] Garantia de Qualidade (49 Testes Automatizados), Homologação E2E e Documentação Técnica",
            "description": "Garantia de confiabilidade, segurança contra prompt injection, alinhamento normativo e rastreabilidade documental do microsserviço ZelaFix AI por meio de suítes automatizadas funcionais (49 testes), script de homologação E2E com Azure Foundry + Oracle e documentação arquitetural completa (README.md, AGENT.md e ENTREGA_GS_2026_2.txt).",
            "acceptance_criteria": "<ul><li>49 testes automatizados aprovados cobrindo RAG (37) e cenários E2E (12) com eliminação de testes de sobrecarga destrutiva para preservação de cota de tokens (TPM/RPM).</li><li>Roteiro de homologação run_qa_demo.py validando Oracle FIAP, Visão Computacional e ZelaBot em 10 cenários.</li><li>Documentação técnica atualizada com arquitetura Foundry, links de produção no Render e manifesto de entrega.</li></ul>"
        },
        {
            "id": 189,
            "type": "Product Backlog Item",
            "title": "[PBI-09] Suítes Automatizadas (test_knowledge_coverage e test_zelafix_scenarios) e Homologação E2E",
            "description": "<div><b>Como</b> engenheiro de QA,<br/><b>Eu quero</b> manter suítes automatizadas determinísticas e end-to-end cobrindo RAG, triagem, ZelaBot, Oracle Tool Calling e resistência adversarial,<br/><b>Para que</b> cada refatoração mantenha 100% de confiabilidade clínica/normativa sem regressões em produção.</div>",
            "acceptance_criteria": "<ul><li>test_knowledge_coverage.py (37/37 asserções) cobrindo os 8 módulos normativos PMSP e 31 chunks.</li><li>test_zelafix_scenarios.py (12/12 cenários) testando visão multimodal, triagem, chat, Oracle e persistência SQLite.</li><li>Eliminação de testes de sobrecarga destrutiva (stress_test_zelafix.py) para proteção de cota de tokens (TPM/RPM) e blindagem contra erro HTTP 429.</li><li>Script run_qa_demo.py para homologação integrada de 10 cenários em terminal.</li></ul>"
        },
        {
            "id": 190,
            "type": "Product Backlog Item",
            "title": "[PBI-10] Especificação AGENT.md, Documentação README.md com Diagramas ASCII, URLs de Produção e Manifesto",
            "description": "<div><b>Como</b> mantenedor do repositório e avaliador técnico,<br/><b>Eu quero</b> dispor de documentação padronizada (README.md, AGENT.md e ENTREGA_GS_2026_2.txt) com diagramas ASCII, contratos de API e links ativos do Render,<br/><b>Para que</b> qualquer desenvolvedor ou avaliador compreenda e teste imediatamente a arquitetura Foundry + RAG + Oracle do projeto.</div>",
            "acceptance_criteria": "<ul><li>README.md padronizado no padrão CitizenTech com URL de produção no Render, Swagger /docs e links de saúde/telemetria.</li><li>AGENT.md especificando arquitetura Foundry agnóstica a modelo (via AI_MODEL e AI_EMBEDDING_MODEL), regras operacionais e estrutura de diretórios.</li><li>Manifesto formal ENTREGA_GS_2026_2.txt atualizado em sincronia com a entrega final da Global Solution.</li></ul>"
        }
    ]

    print("\n🔄 Atualizando Work Items no Azure Boards...")
    for up in updates:
        wid = up["id"]
        patch = [
            {"op": "add", "path": "/fields/System.Title", "value": up["title"]},
            {"op": "add", "path": "/fields/System.Description", "value": up["description"]},
            {"op": "add", "path": "/fields/Microsoft.VSTS.Common.AcceptanceCriteria", "value": up["acceptance_criteria"]}
        ]
        ok = client.update_work_item(wid, patch)
        status = "✅ OK" if ok else "❌ FALHA"
        print(f"  {status} | #{wid} [{up['type']}] -> {up['title']}")

    # Vínculo dos novos commits nos PBIs correspondentes
    commits_to_link = [
        # PBI-04 (#63)
        (63, "e754b84", "refactor(ai): atualizar modelo padrao para gpt-5-nano e aprimorar contingencia normativa"),
        (63, "162c4a5", "refactor(foundry): replace Groq and local hash embeddings with Azure AI Foundry"),
        # PBI-09 (#189)
        (189, "5b6a8a4", "refactor(qa,docs): generalizar especificacao de modelo de IA e remover testes de estresse de alto consumo"),
        (189, "fb21647", "test(qa): align RAG, scenario, and stress suites with phi-4-multimodal and embed-v-4-0"),
        # PBI-10 (#190)
        (190, "7f6c1f8", "docs: alinhar AGENT e README com modelo gpt-5-nano e especificacao de deploy"),
        (190, "f3f9526", "docs: update README and AGENT specs for Azure AI Foundry"),
    ]

    print("\n🔗 Vinculando commits Git aos Work Items no Azure Boards...")
    repo_name = "Disruptive-Architectures-IoT-IoB-IA"
    for wid, sha, msg in commits_to_link:
        url = f"https://github.com/{GITHUB_ORG}/{repo_name}/commit/{sha}"
        comment = f"Commit {sha}: {msg} ({repo_name})"
        
        # Verifica se já está vinculado
        item = client.get_work_item(wid)
        existing_urls = [r["url"] for r in item.get("relations", []) if r.get("rel") == "Hyperlink"]
        if url in existing_urls:
            print(f"  ℹ️ Já vinculado | #{wid} <- {sha}")
            continue

        ok = client.link_commit(wid, url, comment)
        status = "✅ Vinculado" if ok else "❌ Falha"
        print(f"  {status} | #{wid} <- {sha}: {msg}")

    print("\n🎉 Sincronização direta com o Azure Boards concluída com sucesso!")
    return True

if __name__ == "__main__":
    sync_iot_to_azure_boards()
