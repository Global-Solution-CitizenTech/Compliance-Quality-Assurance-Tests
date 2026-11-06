# 📋 Backlog Master Azure Boards — Global Solution 2026/2: Disruptive Architectures (IoT & IA)

> **Projeto Integrado:** ZelaFix — Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  
> **Disciplina:** Disruptive Architectures: IoT, IoB & Generative IA (FIAP — 2TDSPG)  
> **Epic Principal:** `[EPIC] GS 2026/2 - Disruptive Architectures: Monitoramento Urbano Inteligente via IoT (ESP32/MQTT) e IA Generativa para Triagem de Ocorrências`  
> **Start Date:** `2026-11-04`  
> **Target Date:** `2026-11-19`  
> **Padrão:** Azure Boards (Scrum Process: Epic ➔ Feature ➔ PBI ➔ Task)  
> **Diretrizes Estratégicas:** Desenvolvimento de hardware inteligente de sensoriamento urbano baseado no microcontrolador ESP32 com comunicação MQTT para prevenção de alagamentos e monitoramento de bueiros, acoplado a um microsserviço em Python (FastAPI) com Inteligência Artificial Generativa e Visão Computacional para análise semântica e triagem preditiva de fotos de ocorrências urbanas submetidas pela população.

---

## 👥 Integrantes do Grupo (Ordem Alfabética Estrita)

| Integrante | RM | Turma |
| :--- | :---: | :---: |
| **Enzo Okuizumi** | **561432** | 2TDSPG |
| **Gustavo Keiji Okada** | **563428** | 2TDSPG |
| **Lucas Barros Gouveia** | **566422** | 2TDSPG |
| **Luna de Carvalho Guimarães** | **562290** | 2TDSPG |
| **Milton Jakson de Sousa Marcelino** | **564836** | 2TDSPG |

---

## 🌳 1. Estrutura Hierárquica no Azure Boards

```text
[EPIC] GS 2026/2 - Disruptive Architectures: Monitoramento Urbano Inteligente via IoT (ESP32/MQTT) e IA Generativa para Triagem de Ocorrências
│
├── 🏆 [FEATURE 01] Sensoriamento Urbano com ESP32 e Protocolo MQTT
│   ├── 📄 [PBI-01] Circuito IoT de Detecção de Nível de Alagamento e Bueiros no Wokwi/ESP32 (3 pts)
│   └── 📄 [PBI-02] Publicação de Telemetria e Ingestão de Dados via Broker MQTT (3 pts)
│
├── 🏆 [FEATURE 02] Microsserviço Python com IA Generativa e Visão Computacional
│   ├── 📄 [PBI-03] API FastAPI para Processamento de Imagens e Classificação de Urgência via LLM (3 pts)
│   └── 📄 [PBI-04] Pipeline de Filtragem de Conteúdo Inapropriado e Validação de Imagens Urbanas (3 pts)
│
└── 🏆 [FEATURE 03] Integração com o Painel de Gestão e Documentação Técnica
    └── 📄 [PBI-05] Integração de Alertas Críticos de Sensores e Dossiê Técnico de IA (3 pts)
```

---

## 📊 2. Tabela Resumo do Backlog

| Feature Pai | ID do PBI | Título do Item de Backlog (PBI) | Story Points | Prioridade | Horas Estimadas |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **[FEATURE 01] Sensoriamento IoT** | **PBI-01** | Circuito IoT de Detecção de Nível de Alagamento e Bueiros no Wokwi/ESP32 | 3 pts | 1 - Critical | 7.5h |
| | **PBI-02** | Publicação de Telemetria e Ingestão de Dados via Broker MQTT | 3 pts | 1 - Critical | 6.5h |
| **[FEATURE 02] IA Generativa** | **PBI-03** | API FastAPI para Processamento de Imagens e Classificação de Urgência via LLM | 3 pts | 1 - Critical | 8.5h |
| | **PBI-04** | Pipeline de Filtragem de Conteúdo Inapropriado e Validação de Imagens Urbanas | 3 pts | 1 - Critical | 6.5h |
| **[FEATURE 03] Integração & Docs** | **PBI-05** | Integração de Alertas Críticos de Sensores e Dossiê Técnico de IA | 3 pts | 2 - High | 6.0h |
| **TOTAL CONSOLIDADO** | **3 Features** | **5 PBIs / 15 Child Tasks Técnicas** | **15 pts** | — | **35.0h** |

---

## 📦 3. Detalhamento dos Itens de Trabalho (Épico, Features, PBIs e Tasks)

---

### 🏛️ ÉPICO
* **Work Item Type:** `Epic`
* **Title:** `[EPIC] GS 2026/2 - Disruptive Architectures: Monitoramento Urbano Inteligente via IoT (ESP32/MQTT) e IA Generativa para Triagem de Ocorrências`
* **Tags:** `DisruptiveArchitectures, ZelaFix, GlobalSolution2, IoT, ESP32, MQTT, IA, GenAI, FastAPI`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `15`
* **Business Value:** `100`
* **Description:** Implementação das tecnologias disruptivas do projeto ZelaFix, combinando sensoriamento físico com microcontrolador ESP32 para monitoramento de drenagem pluvial e bueiros inteligentes via telemetria MQTT, somado a um microsserviço de Inteligência Artificial Generativa para análise visual automática de chamados, detecção de urgência e validação de autenticidade de evidências.

---

### 🏆 [FEATURE 01] Sensoriamento Urbano com ESP32 e Protocolo MQTT
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] GS 2026/2 - Disruptive Architectures: Monitoramento Urbano Inteligente via IoT (ESP32/MQTT) e IA Generativa para Triagem de Ocorrências`
* **Title:** `[FEATURE 01] Sensoriamento Urbano com ESP32 e Protocolo MQTT`
* **Tags:** `DisruptiveArchitectures, IoT, ESP32, MQTT, Sensors`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-11`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** Desenvolvimento do circuito eletrônico simulado no Wokwi com ESP32, sensores de nível/ultrassônico e envio de telemetria MQTT.
* **Acceptance Criteria:**
  - [x] Código C++ / Arduino para ESP32 compilado sem erros.
  - [x] Publicação periódica de dados JSON em tópico MQTT (`citizentech/sensores/bueiro`).
  - [x] Emissão de alerta quando a lâmina d'água atinge o patamar crítico de transbordamento.

#### 🔹 [PBI-01] Circuito IoT de Detecção de Nível de Alagamento e Bueiros no Wokwi/ESP32
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Sensoriamento Urbano com ESP32 e Protocolo MQTT`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DisruptiveArchitectures, ESP32, Wokwi, Hardware`

##### Descrição (História de Usuário)
> **Como** engenheiro de IoT municipal,  
> **Eu quero** um circuito com sensor ultrassônico instalado na tampa do bueiro para medir o nível de acúmulo de água,  
> **Para que** a Defesa Civil identifique pontos iminentes de enchente antes que a via seja interditada.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Diagrama no Wokwi com ESP32, sensor HC-SR04 e LEDs de status (Verde, Amarelo, Vermelho).
- [ ] Leitura contínua com filtragem de ruídos no sinal.
---

#### 🔹 [PBI-02] Publicação de Telemetria e Ingestão de Dados via Broker MQTT
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Sensoriamento Urbano com ESP32 e Protocolo MQTT`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DisruptiveArchitectures, MQTT, Telemetry`

##### Descrição (História de Usuário)
> **Como** arquiteto de sistemas,  
> **Eu quero** que o microcontrolador publique mensagens JSON em um broker MQTT público (HiveMQ/Mosquitto),  
> **Para que** os sistemas backend consumam a telemetria em tempo real e disparem chamados automáticos.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Conexão Wi-Fi simulada e autenticação com broker MQTT.
- [ ] Payload JSON contendo `deviceId`, `distancia_cm`, `nivel_critico` e `timestamp`.
---

### 🏆 [FEATURE 02] Microsserviço Python com IA Generativa e Visão Computacional
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] GS 2026/2 - Disruptive Architectures: Monitoramento Urbano Inteligente via IoT (ESP32/MQTT) e IA Generativa para Triagem de Ocorrências`
* **Title:** `[FEATURE 02] Microsserviço Python com IA Generativa e Visão Computacional`
* **Tags:** `DisruptiveArchitectures, Python, FastAPI, GenAI, Vision`
* **Start Date:** `2026-11-08`
* **Target Date:** `2026-11-15`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** API REST em FastAPI integrada a modelos multimodais de IA para classificação de fotos e análise de gravidade.
* **Acceptance Criteria:**
  - [x] Microsserviço FastAPI estruturado com endpoint `/api/v1/analyze-image`.
  - [x] Integração com API de LLM multimodal (Gemini / OpenAI Vision) para classificação de imagens.
  - [x] Retorno estruturado contendo categoria sugerida, nível de severidade e justificativa.

#### 🔹 [PBI-03] API FastAPI para Processamento de Imagens e Classificação de Urgência via LLM
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Microsserviço Python com IA Generativa e Visão Computacional`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DisruptiveArchitectures, FastAPI, LLM, Vision`

##### Descrição (História de Usuário)
> **Como** atendente de triagem pública,  
> **Eu quero** que a imagem anexada ao chamado seja interpretada por IA com sugestão de categoria e prioridade,  
> **Para que** ocorrências de alto risco (ex: crateras abertas, fios rompidos) sejam priorizadas automaticamente.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Endpoint aceitando multipart/form-data ou URL de imagem.
- [ ] Prompt engineering especializado instruindo o modelo a avaliar infraestrutura urbana.
- [ ] Resposta em JSON com campos `categoria_sugerida`, `gravidade` (`BAIXA`, `MEDIA`, `ALTA`, `CRITICA`) e `resumo`.
---

#### 🔹 [PBI-04] Pipeline de Filtragem de Conteúdo Inapropriado e Validação de Imagens Urbanas
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Microsserviço Python com IA Generativa e Visão Computacional`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DisruptiveArchitectures, Guardrails, Safety, AI`

##### Descrição (História de Usuário)
> **Como** gestor do sistema municipal,  
> **Eu quero** que fotos irrelevantes (memes, selfies, fotos internas de casas) sejam sinalizadas como inválidas,  
> **Para que** a equipe de campo não perca tempo com chamados fraudulentos ou inconsistentes.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Detecção de imagens sem relação com zeladoria urbana.
- [ ] Flag `is_valid_incident: false` com recomendação de nova foto pelo cidadão.
---

### 🏆 [FEATURE 03] Integração com o Painel de Gestão e Documentação Técnica
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] GS 2026/2 - Disruptive Architectures: Monitoramento Urbano Inteligente via IoT (ESP32/MQTT) e IA Generativa para Triagem de Ocorrências`
* **Title:** `[FEATURE 03] Integração com o Painel de Gestão e Documentação Técnica`
* **Tags:** `DisruptiveArchitectures, Integration, Documentation, Video`
* **Start Date:** `2026-11-13`
* **Target Date:** `2026-11-19`
* **Priority:** `2 - High`
* **Effort (Story Points):** `3`
* **Business Value:** `80`
* **Description:** Conexão dos alertas do sensor IoT e relatórios de IA ao ecossistema do ZelaFix e elaboração da documentação técnica e vídeo.
* **Acceptance Criteria:**
  - [x] Webhook ou endpoint de integração conectando alertas de sensores ao backend Java.
  - [x] README.md com diagrama de blocos, esquemático do Wokwi e instruções de execução da API FastAPI.

#### 🔹 [PBI-05] Integração de Alertas Críticos de Sensores e Dossiê Técnico de IA
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] Integração com o Painel de Gestão e Documentação Técnica`
* **Priority:** `2 - High`
* **Effort (Story Points):** `3`
* **Tags:** `DisruptiveArchitectures, Documentation, Webhook`

##### Descrição (História de Usuário)
> **Como** avaliador técnico da disciplina,  
> **Eu quero** um README.md completo com link navegável do circuito no Wokwi, código-fonte documentado e roteiro de testes da IA,  
> **Para que** a avaliação comprove o cumprimento de 100% dos requisitos de IoT e IA.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Link do projeto Wokwi compartilhado e funcionando.
- [ ] Documentação de endpoints e exemplos de requisição curl no README.md.