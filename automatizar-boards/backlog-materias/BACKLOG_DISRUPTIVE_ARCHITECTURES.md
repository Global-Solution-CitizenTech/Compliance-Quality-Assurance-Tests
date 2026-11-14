# 🤖 ZelaFix — Backlog: Disruptive Architectures (IoT, IoB & IA)

> **Disciplina:** Disruptive Architectures: IoT, IoB & Generative IA (FIAP 2TDSPG — Global Solution 2026/2)  
> **Projeto:** ZelaFix — Plataforma Colaborativa de Zeladoria Urbana com IA Generativa, RAG Semântico e IoB  
> **Repositório GitHub:** [Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA)  
> **URL de Produção (Render Cloud):** [https://disruptive-architectures-iot-iob-ia-mpl5.onrender.com/](https://disruptive-architectures-iot-iob-ia-mpl5.onrender.com/)  
> **Organização / Projeto Azure DevOps:** `ZelaFixGS` / `ZelaFix`  
> **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`  
> **Tag Base:** `DisruptiveArchitectures`  
> **Responsible Owner:** `RM561432@fiap.com.br` (Enzo Okuizumi)  
> **Epic Principal:** `[EPIC] Disruptive Architectures: Microsserviço ZelaFix AI (Azure AI Foundry, RAG Semântico, Tool Calling Oracle & Visão Computacional)` (**AB#58**)  
> **Integrantes (2TDSPG):** Enzo Okuizumi (`561432`), Gustavo Okada (`563428`), Lucas Barros Gouveia (`566422`), Luna de Carvalho Guimarães (`562290`), Milton Marcelino (`564836`)

---

## 🗂️ Estrutura Hierárquica do Backlog (Azure Boards)

```text
📌 [EPIC] Disruptive Architectures: Microsserviço ZelaFix AI (Azure AI Foundry, RAG Semântico, Tool Calling Oracle & Visão Computacional) [AB#58]
│
├── 🏆 [FEATURE 01] Arquitetura FastAPI, Base Normativa PMSP e Persistência Vetorial/SQLite [AB#59]
│   ├── 🔹 [PBI-01] Estrutura Modular FastAPI, Schemas Pydantic v2, Health Checks e Deploy em Nuvem Render [AB#60] (3 pts)
│   ├── 🔹 [PBI-02] Base Normativa PMSP (31 Chunks em 8 Módulos), ChromaDB HNSW e Persistência Multi-turno SQLite WAL [AB#61] (5 pts)
│   └── 🔹 [PBI-03] Recuperação Híbrida (Embeddings embed-v-4-0 1536D + Reranking Lexical) e Endpoints RAG/Histórico/Sessões [AB#186] (3 pts)
│
├── 🏆 [FEATURE 02] Motor Cognitivo Azure AI Foundry (phi-4-multimodal), ZelaBot e Visão Computacional Urbana [AB#62]
│   ├── 🔹 [PBI-04] Pipeline Generativo em Azure AI Foundry Único (phi-4-multimodal e embed-v-4-0) sem Fallbacks [AB#63] (5 pts)
│   ├── 🔹 [PBI-05] Chat Cidadão ZelaBot (POST /ai/chat) com JSON Estruturado, IoB e Guardrails LGPD [AB#64] (5 pts)
│   └── 🔹 [PBI-06] Laudo Técnico de Triagem (POST /ai/triagem), Visão Computacional Multimodal e Insights por Bairro [AB#187] (3 pts)
│
├── 🏆 [FEATURE 03] Integração Oracle FIAP Thin Client (Somente Leitura) e Tool Calling Nativo ReAct [AB#65]
│   ├── 🔹 [PBI-07] Cliente Oracle oracledb Modo Thin (SELECT em CHAMADOS/CATEGORIAS/APOIADORES), BLOB e Segurança de Credenciais [AB#66] (5 pts)
│   └── 🔹 [PBI-08] Tool Calling Nativo ReAct (consultar_chamados_oracle e calcular_prazo_sla) e Endpoints /ai/chamados [AB#188] (3 pts)
│
└── 🏆 [FEATURE 04] Garantia de Qualidade (82 Testes Automatizados), Homologação E2E e Documentação Técnica [AB#185]
    ├── 🔹 [PBI-09] Suítes Automatizadas (test_knowledge_coverage, test_zelafix_scenarios, stress_test_zelafix) e Demo run_qa_demo.py [AB#189] (5 pts)
    └── 🔹 [PBI-10] Especificação AGENT.md, Documentação README.md com Diagramas ASCII, URLs de Produção e Manifesto [AB#190] (3 pts)
```

---

## 📊 Resumo de Esforço, Story Points & Rastreabilidade

| Feature | PBI | Título do Item | ID Azure Boards | Story Points | Prioridade | Commits | Status |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Feature 01** `[AB#59]` | **PBI-01** | Estrutura Modular FastAPI, Schemas Pydantic v2, Health Checks e Deploy em Nuvem Render | **#60** | 3 pts | 1 - Critical | 5 | Committed |
| | **PBI-02** | Base Normativa PMSP (31 Chunks em 8 Módulos), ChromaDB HNSW e Persistência Multi-turno SQLite WAL | **#61** | 5 pts | 1 - Critical | 3 | Committed |
| | **PBI-03** | Recuperação Híbrida (Embeddings `embed-v-4-0` 1536D + Reranking Lexical) e Endpoints RAG/Histórico/Sessões | **#186** | 3 pts | 1 - Critical | 1 | Committed |
| **Feature 02** `[AB#62]` | **PBI-04** | Pipeline Generativo em Azure AI Foundry Único (`phi-4-multimodal` e `embed-v-4-0`) sem Fallbacks | **#63** | 5 pts | 1 - Critical | 4 | Committed |
| | **PBI-05** | Chat Cidadão ZelaBot (`POST /ai/chat`) com JSON Estruturado, IoB e Guardrails LGPD | **#64** | 5 pts | 1 - Critical | 3 | Committed |
| | **PBI-06** | Laudo Técnico de Triagem (`POST /ai/triagem`), Visão Computacional Multimodal e Insights por Bairro | **#187** | 3 pts | 1 - Critical | 1 | Committed |
| **Feature 03** `[AB#65]` | **PBI-07** | Cliente Oracle `oracledb` Modo Thin (`SELECT` em `CHAMADOS`/`CATEGORIAS`/`APOIADORES`), BLOB e Segurança de Credenciais | **#66** | 5 pts | 1 - Critical | 3 | Committed |
| | **PBI-08** | Tool Calling Nativo ReAct (`consultar_chamados_oracle` e `calcular_prazo_sla`) e Endpoints `/ai/chamados` | **#188** | 3 pts | 1 - Critical | 2 | Committed |
| **Feature 04** `[AB#185]` | **PBI-09** | Suítes Automatizadas (`test_knowledge_coverage`, `test_zelafix_scenarios`, `stress_test_zelafix`) e Demo `run_qa_demo.py` | **#189** | 5 pts | 2 - High | 5 | Committed |
| | **PBI-10** | Especificação `AGENT.md`, Documentação `README.md` com Diagramas ASCII, URLs de Produção e Manifesto | **#190** | 3 pts | 2 - High | 5 | Committed |
| **TOTAL** | **10 PBIs** | **4 Features / 1 Epic (`#58`)** | **15 Work Items** | **40 pts** | — | **32 commits** | **100% Sincronizado** |

---

## 🏆 EPIC PRINCIPAL

* **Azure Boards ID:** `#58`
* **Type:** `Epic`
* **Title:** `[EPIC] Disruptive Architectures: Microsserviço ZelaFix AI (Azure AI Foundry, RAG Semântico, Tool Calling Oracle & Visão Computacional)`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DisruptiveArchitectures`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort:** `40`
* **Description:** Desenvolvimento e refatoração do microsserviço inteligente **ZelaFix AI** (Python + FastAPI) integrado ao ecossistema CitizenTech, combinando **Azure AI Foundry** (`phi-4-multimodal` para chat estruturado/visão computacional e `embed-v-4-0` para embeddings semânticos 1536D), banco vetorial **ChromaDB** com 31 chunks normativos municipais PMSP em 8 módulos, histórico multi-turno em **SQLite WAL**, consulta somente leitura ao **Oracle FIAP** via Tool Calling ReAct nativo e engajamento comunitário **IoB (+1)**, publicado em produção no Render Cloud.
* **Acceptance Criteria:**
  - [x] Microsserviço FastAPI modular em `deploy_zelafixai_render/` com entrypoint `main.py` e deploy em produção ativo no Render.
  - [x] Base normativa municipal PMSP indexada no ChromaDB (HNSW cosseno 1536D) com `embed-v-4-0` e reranking híbrido lexical.
  - [x] Motor cognitivo único em Azure AI Foundry (`phi-4-multimodal`) sem modelos fallback legados, cobrindo `/ai/chat`, `/ai/triagem` (com visão Base64) e `/ai/insights`.
  - [x] Cliente Oracle FIAP em modo Thin (somente `SELECT`) com Tool Calling nativo ReAct e sanitização LGPD.
  - [x] Suíte automatizada de 82 verificações (RAG, cenários E2E e stress adversarial) aprovada com 100% de cobertura.

---

### 🏆 [FEATURE 01] Arquitetura FastAPI, Base Normativa PMSP e Persistência Vetorial/SQLite

* **Azure Boards ID:** `#59`
* **Type:** `Feature`
* **Parent:** `[EPIC] Disruptive Architectures: Microsserviço ZelaFix AI (Azure AI Foundry, RAG Semântico, Tool Calling Oracle & Visão Computacional)` (`#58`)
* **Title:** `[FEATURE 01] Arquitetura FastAPI, Base Normativa PMSP e Persistência Vetorial/SQLite`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DisruptiveArchitectures`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort:** `11` Story Points
* **Description:** Estruturação modular do microsserviço FastAPI com entrypoint `main.py`, contratos Pydantic v2, health checks, banco relacional SQLite WAL para conversas/auditorias, base normativa municipal PMSP em 8 módulos (31 chunks) e motor vetorial ChromaDB com busca híbrida.

---

#### 🔹 [PBI-01] Estrutura Modular FastAPI, Schemas Pydantic v2, Health Checks e Deploy em Nuvem Render

* **Azure Boards ID:** `#60`
* **Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Arquitetura FastAPI, Base Normativa PMSP e Persistência Vetorial/SQLite` (`#59`)
* **Title:** `[PBI-01] Estrutura Modular FastAPI, Schemas Pydantic v2, Health Checks e Deploy em Nuvem Render`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DisruptiveArchitectures`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort:** `3` Story Points

##### Descrição (User Story):
> **Como** engenheiro backend e DevOps,
> **Eu quero** estruturar o microsserviço FastAPI de forma modular com entrypoint `main.py`, contratos Pydantic v2, health checks e configuração para deploy no Render Cloud,
> **Para que** o aplicativo mobile, API Java e painéis possam consumir a camada de IA com estabilidade, CORS configurado e observabilidade de startup.

##### Critérios de Aceite (Acceptance Criteria):
- [x] Entrypoint dual (`deploy_zelafixai_render/main.py` e `api.py`) compatível com `uvicorn main:app` no Render Cloud.
- [x] Routers desacoplados em `src/routers/health.py` e `src/routers/ai.py` com schemas validados em `src/schemas/`.
- [x] Endpoints `/`, `/health` e `/health/ready` informando modelo ativo (`phi-4-multimodal`), embeddings (`embed-v-4-0`) e status do ChromaDB.
- [x] Remoção de estruturas legadas de hardware Wokwi/MQTT e endurecimento de `.gitignore` para conformidade.

##### Commits vinculados (GitHub Repository):
- [`6c83591`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/6c83591) — `Initial commit` *(vinculado em AB#60)*
- [`564a9b1`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/564a9b1) — `feat(infra): setup de dependencias, dockerfile, config e schemas pydantic` *(vinculado em AB#60)*
- [`c16280c`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/c16280c) — `feat(iot-firmware): firmware ESP32 de borda, diagrama Wokwi, simulador de streaming e documentação completa` *(registro histórico substituído pelo microsserviço de IA no commit `c4a155d` — vinculado em AB#60)*
- [`c4a155d`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/c4a155d) — `refactor(arch): remove legacy structure and harden .gitignore for compliance` *(vinculado em AB#60)*
- [`846f9ed`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/846f9ed) — `fix(deploy,docs): add main.py entrypoint for Render and align README without Render YAML section` *(vinculado em AB#60)*

---

#### 🔹 [PBI-02] Base Normativa PMSP (31 Chunks em 8 Módulos), ChromaDB HNSW e Persistência Multi-turno SQLite WAL

* **Azure Boards ID:** `#61`
* **Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Arquitetura FastAPI, Base Normativa PMSP e Persistência Vetorial/SQLite` (`#59`)
* **Title:** `[PBI-02] Base Normativa PMSP (31 Chunks em 8 Módulos), ChromaDB HNSW e Persistência Multi-turno SQLite WAL`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DisruptiveArchitectures`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort:** `5` Story Points

##### Descrição (User Story):
> **Como** arquiteto de dados e conhecimento cívico,
> **Eu quero** consolidar a legislação municipal paulistana em 8 módulos temáticos indexados no ChromaDB com persistência multi-turno em SQLite WAL,
> **Para que** toda resposta do ZelaBot e cada laudo técnico tenha lastro jurídico real e histórico auditável por sessão e chamado.

##### Critérios de Aceite (Acceptance Criteria):
- [x] 31 chunks normativos distribuídos em 8 módulos em `src/knowledge/` (drenagem, pavimentação, iluminação, arborização, resíduos/Ecopontos, saneamento, trânsito/CET e direitos do cidadão).
- [x] Banco vetorial persistente `VectorStore` em ChromaDB com métrica cosseno (HNSW 1536D) e fallback automático seguro.
- [x] Camada `ChatRepository` + `connection.py` em SQLite com modo WAL gravando mensagens de sessão e auditorias técnicas de triagem.

##### Commits vinculados (GitHub Repository):
- [`8c69823`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/8c69823) — `feat(rag): add municipal knowledge base modules (PMSP) and pydantic schemas` *(vinculado em AB#61)*
- [`ace3b7a`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/ace3b7a) — `feat(core): implement 512D local embedder, vital risk guardrails, SQLite WAL and ChromaDB store` *(vinculado em AB#61)*
- [`5c076cd`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/5c076cd) — `feat(knowledge): reestruturacao e enriquecimento da base RAG municipal PMSP com 31 chunks normativos` *(vinculado em AB#61)*

---

#### 🔹 [PBI-03] Recuperação Híbrida (Embeddings embed-v-4-0 1536D + Reranking Lexical) e Endpoints RAG/Histórico/Sessões

* **Azure Boards ID:** `#186`
* **Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Arquitetura FastAPI, Base Normativa PMSP e Persistência Vetorial/SQLite` (`#59`)
* **Title:** `[PBI-03] Recuperação Híbrida (Embeddings embed-v-4-0 1536D + Reranking Lexical) e Endpoints RAG/Histórico/Sessões`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DisruptiveArchitectures`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort:** `3` Story Points

##### Descrição (User Story):
> **Como** engenheiro de busca e IA aplicada,
> **Eu quero** combinar similaridade vetorial no ChromaDB com reranking lexical no `KnowledgeService` e expor endpoints de status vetorial, histórico, auditorias e sessões,
> **Para que** consultas jurídicas e cidadãs recuperem exatamente o decreto e prazo SLA corretos mesmo diante de jargão informal.

##### Critérios de Aceite (Acceptance Criteria):
- [x] `KnowledgeService` preservando metadados de urgência e categoria estrita com boost lexical sobre hits vetoriais do ChromaDB.
- [x] Endpoints operacionais `GET /ai/vector-store/status`, `GET /ai/history`, `GET /ai/audit`, `GET /ai/sessions` e `DELETE /ai/sessions/{session_id}`.
- [x] Degradação elegante para busca normativa local quando o índice vetorial estiver em inicialização.

##### Commits vinculados (GitHub Repository):
- [`1960ca3`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/1960ca3) — `fix(rag): preserve urgency metadata, strict category filtering and hybrid lexical reranking` *(vinculado em AB#186)*

---

### 🏆 [FEATURE 02] Motor Cognitivo Azure AI Foundry (phi-4-multimodal), ZelaBot e Visão Computacional Urbana

* **Azure Boards ID:** `#62`
* **Type:** `Feature`
* **Parent:** `[EPIC] Disruptive Architectures: Microsserviço ZelaFix AI (Azure AI Foundry, RAG Semântico, Tool Calling Oracle & Visão Computacional)` (`#58`)
* **Title:** `[FEATURE 02] Motor Cognitivo Azure AI Foundry (phi-4-multimodal), ZelaBot e Visão Computacional Urbana`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DisruptiveArchitectures`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort:** `13` Story Points
* **Description:** Orquestração de IA generativa exclusivamente no Azure AI Foundry utilizando `phi-4-multimodal` para chat cidadão estruturado (`/ai/chat`), laudo técnico de triagem com visão computacional Base64 (`/ai/triagem`), diagnósticos preventivos por bairro (`/ai/insights`), sinais IoB (+1) e guardrails LGPD.

---

#### 🔹 [PBI-04] Pipeline Generativo em Azure AI Foundry Único (phi-4-multimodal e embed-v-4-0) sem Fallbacks

* **Azure Boards ID:** `#63`
* **Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Motor Cognitivo Azure AI Foundry (phi-4-multimodal), ZelaBot e Visão Computacional Urbana` (`#62`)
* **Title:** `[PBI-04] Pipeline Generativo em Azure AI Foundry Único (phi-4-multimodal e embed-v-4-0) sem Fallbacks`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DisruptiveArchitectures`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort:** `5` Story Points

##### Descrição (User Story):
> **Como** engenheiro de IA,
> **Eu quero** centralizar toda inferência generativa e geração de embeddings exclusivamente no Azure AI Foundry via `FoundryService` usando apenas `phi-4-multimodal` e `embed-v-4-0`,
> **Para que** a plataforma opere com modelo único multimodal econômico, previsível e livre de complexidade de fallbacks legados.

##### Critérios de Aceite (Acceptance Criteria):
- [x] Cliente unificado `FoundryService` via `OpenAI(base_url=AI_BASE_URL, api_key=AI_API_KEY)` suportando texto, visão Base64 e Tool Calling.
- [x] Embeddings vetoriais de 1536 dimensões gerados pelo deployment `embed-v-4-0` via endpoint REST Foundry.
- [x] Eliminação completa de provedores e modelos de fallback (Gemini, Groq, Qwen, Kimi e hash local 512D).

##### Commits vinculados (GitHub Repository):
- [`6f3e57b`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/6f3e57b) — `feat(ai-core): implementacao de visao computacional, rag normativo, gemini genai, iot e iob` *(vinculado em AB#63)*
- [`1c23ffd`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/1c23ffd) — `feat(api): implement multiprovider generative AI services (Groq/Gemini-3.5) and REST endpoints` *(vinculado em AB#63)*
- [`ba95048`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/ba95048) — `feat(ai): migracao para Groq Multimodal Qwen 3.8 27B com visao computacional e remocao do Gemini` *(vinculado em AB#63)*
- [`162c4a5`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/162c4a5) — `refactor(foundry): replace Groq and local hash embeddings with Azure AI Foundry` *(vinculado em AB#63)*

---

#### 🔹 [PBI-05] Chat Cidadão ZelaBot (POST /ai/chat) com JSON Estruturado, IoB e Guardrails LGPD

* **Azure Boards ID:** `#64`
* **Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Motor Cognitivo Azure AI Foundry (phi-4-multimodal), ZelaBot e Visão Computacional Urbana` (`#62`)
* **Title:** `[PBI-05] Chat Cidadão ZelaBot (POST /ai/chat) com JSON Estruturado, IoB e Guardrails LGPD`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DisruptiveArchitectures`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort:** `5` Story Points

##### Descrição (User Story):
> **Como** munícipe utilizando o aplicativo ZelaFix,
> **Eu quero** conversar com o assistente cívico ZelaBot enviando dúvidas urbanas ou contexto de ocorrência e recebendo orientação estruturada em português,
> **Para que** eu saiba meus direitos, o órgão competente, ações recomendadas e o peso do engajamento comunitário (+1) sem exposição de dados pessoais.

##### Critérios de Aceite (Acceptance Criteria):
- [x] Endpoint `POST /ai/chat` retornando JSON estruturado (`resposta`, `categoria`, `urgencia`, `acoes_recomendadas`, `fontes`).
- [x] Suporte a contexto IoB (quantidade de apoios comunitários `+1`) elevando severidade de triagem quando crítico.
- [x] Guardrails determinísticos LGPD (`sanitizar_lgpd` em `src/utils/guardrails.py`) mascarando CPF, RG e e-mail antes da persistência ou exibição.
- [x] Histórico multi-turno restaurado por `session_id` no SQLite WAL.

##### Commits vinculados (GitHub Repository):
- [`15d5124`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/15d5124) — `feat(chat): endpoint /api/v1/chat-cidadao com zelabot rag e suporte mobile` *(vinculado em AB#64)*
- [`fd35eaf`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/fd35eaf) — `feat(api): rotas restful fastapi, endpoint mobile /triagem-ia/analisar e dashboard web interativo` *(vinculado em AB#64)*
- [`885c284`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/885c284) — `refactor(ai): remocao de guardrails artificiais de emergencia e sanitizacao desnecessaria de codigo` *(vinculado em AB#64)*

---

#### 🔹 [PBI-06] Laudo Técnico de Triagem (POST /ai/triagem), Visão Computacional Multimodal e Insights por Bairro

* **Azure Boards ID:** `#187`
* **Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Motor Cognitivo Azure AI Foundry (phi-4-multimodal), ZelaBot e Visão Computacional Urbana` (`#62`)
* **Title:** `[PBI-06] Laudo Técnico de Triagem (POST /ai/triagem), Visão Computacional Multimodal e Insights por Bairro`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DisruptiveArchitectures`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort:** `3` Story Points

##### Descrição (User Story):
> **Como** gestor público municipal e sistema backend Java,
> **Eu quero** submeter uma ocorrência (texto e foto Base64 opcional) para emissão automática de laudo técnico com SLA, órgão competente e insights preventivos por bairro,
> **Para que** subprefeituras e concessionárias recebam despacho preciso alinhado ao ODS 11 e à legislação paulistana.

##### Critérios de Aceite (Acceptance Criteria):
- [x] `POST /ai/triagem` retornando categoria, urgência, órgão responsável, SLA normativo, checklist técnico de vistoria e parecer técnico sintético (`<= 150` caracteres).
- [x] Análise visual multimodal nativa em `phi-4-multimodal` identificando coerência da foto Base64 com o relato urbano sem rebaixamentos artificiais.
- [x] `POST /ai/insights` consolidando diagnósticos e alertas preventivos comunitários por bairro via ODS 11.

##### Commits vinculados (GitHub Repository):
- [`4102d6b`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/4102d6b) — `feat(ai,oracle): integrate Qwen JSON triage, IoT telemetry, read-only Oracle queries and session memory` *(vinculado em AB#187)*

---

### 🏆 [FEATURE 03] Integração Oracle FIAP Thin Client (Somente Leitura) e Tool Calling Nativo ReAct

* **Azure Boards ID:** `#65`
* **Type:** `Feature`
* **Parent:** `[EPIC] Disruptive Architectures: Microsserviço ZelaFix AI (Azure AI Foundry, RAG Semântico, Tool Calling Oracle & Visão Computacional)` (`#58`)
* **Title:** `[FEATURE 03] Integração Oracle FIAP Thin Client (Somente Leitura) e Tool Calling Nativo ReAct`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DisruptiveArchitectures`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort:** `8` Story Points
* **Description:** Conexão segura em modo Thin (`oracledb`) com o banco Oracle acadêmico da FIAP para leitura em tempo real de chamados reais, categorias, endereços, votos IoB (`+1`) e fotos BLOB, exposta via endpoints REST e acionada dinamicamente pelo modelo via Tool Calling nativo.

---

#### 🔹 [PBI-07] Cliente Oracle oracledb Modo Thin (SELECT em CHAMADOS/CATEGORIAS/APOIADORES), BLOB e Segurança de Credenciais

* **Azure Boards ID:** `#66`
* **Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] Integração Oracle FIAP Thin Client (Somente Leitura) e Tool Calling Nativo ReAct` (`#65`)
* **Title:** `[PBI-07] Cliente Oracle oracledb Modo Thin (SELECT em CHAMADOS/CATEGORIAS/APOIADORES), BLOB e Segurança de Credenciais`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DisruptiveArchitectures`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort:** `5` Story Points

##### Descrição (User Story):
> **Como** engenheiro de integração de dados,
> **Eu quero** conectar o microsserviço Python diretamente ao banco Oracle FIAP em modo Thin somente leitura sem credenciais hardcoded,
> **Para que** a IA consulte ocorrências reais cadastradas pelo backend Java/Mobile, seus votos comunitários (+1) e fotos em Base64 com segurança.

##### Critérios de Aceite (Acceptance Criteria):
- [x] Classe `OracleClient` usando driver `oracledb` modo Thin executando exclusivamente comandos `SELECT` com parâmetros bind.
- [x] Consultas a chamados individuais (com leitura opcional de BLOB fotográfico em Base64), listagem recente por bairro e contagem de apoios IoB.
- [x] Configuração 100% externalizada via `ORACLE_DSN`, `ORACLE_USER` e `ORACLE_PASSWORD` sem segredos em código-fonte.

##### Commits vinculados (GitHub Repository):
- [`05df0a4`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/05df0a4) — `feat(database): integracao com Oracle FIAP em modo Thin para consulta de chamados, historico e votos IoB` *(vinculado em AB#66)*
- [`cc2378d`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/cc2378d) — `fix(security,config): remove hardcoded Oracle credentials, trim prompts and sync render blueprint` *(vinculado em AB#66)*
- [`4493013`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/4493013) — `feat(viacep,oracle,triagem): replace hardcoded neighborhoods with ViaCEP + dynamic Oracle catalog and fix heuristic edge cases` *(vinculado em AB#66)*

---

#### 🔹 [PBI-08] Tool Calling Nativo ReAct (consultar_chamados_oracle e calcular_prazo_sla) e Endpoints /ai/chamados

* **Azure Boards ID:** `#188`
* **Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] Integração Oracle FIAP Thin Client (Somente Leitura) e Tool Calling Nativo ReAct` (`#65`)
* **Title:** `[PBI-08] Tool Calling Nativo ReAct (consultar_chamados_oracle e calcular_prazo_sla) e Endpoints /ai/chamados`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DisruptiveArchitectures`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort:** `3` Story Points

##### Descrição (User Story):
> **Como** engenheiro de agentes conversacionais,
> **Eu quero** equipar o ZelaBot com Tool Calling nativo ReAct no Foundry e expor endpoints REST de consulta e triagem direta de chamados do Oracle,
> **Para que** o modelo busque protocolos reais ou panoramas de bairro sob demanda e calcule prazos exatos de SLA no fuso de São Paulo.

##### Critérios de Aceite (Acceptance Criteria):
- [x] Definição OpenAI Tools em `TOOLS_ZELAFIX` (`consultar_chamados_oracle` e `calcular_prazo_sla`) com fast-path determinístico por `#ID`.
- [x] Suporte ao código especial `CET_SEMAFORO` (4h) e prioridades `URGENTE` (12h), `ALTA` (24h), `MEDIA` (48h) e `BAIXA` (72h).
- [x] Endpoints `GET /ai/chamados` e `GET /ai/chamados/{id_chamado}` retornando chamado Oracle enriquecido com parecer técnico.

##### Commits vinculados (GitHub Repository):
- [`aeceaf5`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/aeceaf5) — `fix(oracle,qa): parse 'chamado numero X' in regex and validate real vision output in QA` *(vinculado em AB#188)*
- [`7f651f4`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/7f651f4) — `refactor(oracle,chat): remove ViaCEP/regex bloat and use native Groq tool calling for Oracle queries` *(vinculado em AB#188)*

---

### 🏆 [FEATURE 04] Garantia de Qualidade (82 Testes Automatizados), Homologação E2E e Documentação Técnica

* **Azure Boards ID:** `#185`
* **Type:** `Feature`
* **Parent:** `[EPIC] Disruptive Architectures: Microsserviço ZelaFix AI (Azure AI Foundry, RAG Semântico, Tool Calling Oracle & Visão Computacional)` (`#58`)
* **Title:** `[FEATURE 04] Garantia de Qualidade (82 Testes Automatizados), Homologação E2E e Documentação Técnica`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DisruptiveArchitectures`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `2 - High`
* **Effort:** `8` Story Points
* **Description:** Garantia de confiabilidade, segurança contra prompt injection, alinhamento normativo e rastreabilidade documental do microsserviço ZelaFix AI por meio de três suítes automatizadas (82 testes), script de homologação E2E com Azure Foundry + Oracle e documentação arquitetural completa (`README.md`, `AGENT.md` e `ENTREGA_GS_2026_2.txt`).

---

#### 🔹 [PBI-09] Suítes Automatizadas (test_knowledge_coverage, test_zelafix_scenarios, stress_test_zelafix) e Demo run_qa_demo.py

* **Azure Boards ID:** `#189`
* **Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 04] Garantia de Qualidade (82 Testes Automatizados), Homologação E2E e Documentação Técnica` (`#185`)
* **Title:** `[PBI-09] Suítes Automatizadas (test_knowledge_coverage, test_zelafix_scenarios, stress_test_zelafix) e Demo run_qa_demo.py`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DisruptiveArchitectures`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `2 - High`
* **Effort:** `5` Story Points

##### Descrição (User Story):
> **Como** engenheiro de QA,
> **Eu quero** manter suítes automatizadas determinísticas e end-to-end cobrindo RAG, triagem, ZelaBot, Oracle Tool Calling e resistência adversarial,
> **Para que** cada refatoração mantenha 100% de confiabilidade clínica/normativa sem regressões em produção.

##### Critérios de Aceite (Acceptance Criteria):
- [x] `test_knowledge_coverage.py` (37/37 asserções) cobrindo os 8 módulos normativos PMSP e 31 chunks.
- [x] `test_zelafix_scenarios.py` (12/12 cenários) testando visão multimodal, triagem, chat, Oracle e persistência SQLite.
- [x] `stress_test_zelafix.py` (33/33 verificações) validando LGPD, prompt injection, off-topic, IoB e Tool Calling ReAct (Total: 82/82 aprovados).
- [x] Script `run_qa_demo.py` para homologação integrada de 10 cenários em terminal.

##### Commits vinculados (GitHub Repository):
- [`35d9539`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/35d9539) — `feat(test-docs): suite de 29 testes unitarios, benchmark quantitativo, matriz de confusao e readme final` *(vinculado em AB#189)*
- [`c3d1489`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/c3d1489) — `test(qa): add comprehensive test suites for RAG coverage, scenarios and adversarial stress` *(vinculado em AB#189)*
- [`d6022e5`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/d6022e5) — `test(qa): implementacao do run_qa_demo com 10 cenarios de homologacao, delay e integracao Oracle/Visao` *(vinculado em AB#189)*
- [`b54102e`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/b54102e) — `test,docs(qa): expand automated QA suites to 82 tests and sync README and AGENT docs` *(vinculado em AB#189)*
- [`fb21647`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/fb21647) — `test(qa): align RAG, scenario, and stress suites with phi-4-multimodal and embed-v-4-0` *(vinculado em AB#189)*

---

#### 🔹 [PBI-10] Especificação AGENT.md, Documentação README.md com Diagramas ASCII, URLs de Produção e Manifesto

* **Azure Boards ID:** `#190`
* **Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 04] Garantia de Qualidade (82 Testes Automatizados), Homologação E2E e Documentação Técnica` (`#185`)
* **Title:** `[PBI-10] Especificação AGENT.md, Documentação README.md com Diagramas ASCII, URLs de Produção e Manifesto`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DisruptiveArchitectures`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `2 - High`
* **Effort:** `3` Story Points

##### Descrição (User Story):
> **Como** mantenedor do repositório e avaliador técnico,
> **Eu quero** dispor de documentação padronizada (`README.md`, `AGENT.md` e `ENTREGA_GS_2026_2.txt`) com diagramas ASCII, contratos de API e links ativos do Render,
> **Para que** qualquer desenvolvedor ou avaliador compreenda e teste imediatamente a arquitetura Foundry + RAG + Oracle do projeto.

##### Critérios de Aceite (Acceptance Criteria):
- [x] `README.md` padronizado no padrão CitizenTech com URL de produção no Render, Swagger `/docs` e links de saúde/telemetria.
- [x] `AGENT.md` especificando arquitetura Foundry, modelos ativos (`phi-4-multimodal`, `embed-v-4-0`), regras operacionais e estrutura de diretórios.
- [x] Manifesto formal `ENTREGA_GS_2026_2.txt` atualizado em sincronia com a entrega final da Global Solution.

##### Commits vinculados (GitHub Repository):
- [`5b6bdb6`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/5b6bdb6) — `docs(compliance): update technical documentation, ASCII architecture diagrams and delivery manifest` *(vinculado em AB#190)*
- [`196ee22`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/196ee22) — `docs(architecture): adicao do AGENT.md e atualizacao do README.md com diagramas ASCII e especificacoes` *(vinculado em AB#190)*
- [`c1735b5`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/c1735b5) — `docs(readme): add live Render production URL, Swagger and telemetry links` *(vinculado em AB#190)*
- [`efc0648`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/efc0648) — `docs(ai): padronizar README e remover secoes de edital` *(vinculado em AB#190)*
- [`f3f9526`](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA/commit/f3f9526) — `docs: update README and AGENT specs for Azure AI Foundry` *(vinculado em AB#190)*
