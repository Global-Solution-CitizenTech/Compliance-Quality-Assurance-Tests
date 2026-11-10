# 📋 Backlog Master Azure Boards — Global Solution 2026/2: Compliance, Quality Assurance & Tests

> **Projeto Integrado:** ZelaFix — Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  
> **Disciplina:** Compliance, Quality Assurance & Tests (FIAP — 2TDSPG)  
> **Epic Principal:** `[EPIC] Compliance, Quality Assurance & Tests: Governança Scrum, Rastreabilidade de Commits e Plano de Testes Manuais Caixa-Preta`  
> **Start Date:** `2026-11-04`  
> **Target Date:** `2026-11-19`  
> **Padrão:** Azure Boards (Scrum Process: Epic ➔ Feature ➔ PBI ➔ Task)  
> **Diretrizes Estratégicas:** 100% de aderência à rubrica oficial da Global Solution 2 (5 critérios de 20% cada), gestão ágil e governança de backlog no padrão Scrum do Azure Boards, alinhamento estrito com os objetivos de produto da plataforma ZelaFix (ODS 11), padronização de Histórias de Usuário com critérios de aceitação e Definition of Done (DoD), balanceamento temporal de entregas (Sprint 1 vs Sprint 2), rastreabilidade de commits dos 7 repositórios e homologação via Azure Test Plans com dados controlados (casos positivos e negativos).

---

## 👥 Integrantes do Grupo (Ordem Alfabética Estrita)

> ⚠️ **Regra da Banca:** Todos os documentos, apresentações e entregáveis mantêm a ordem alfabética estrita dos integrantes.

| Integrante | RM | Turma | Papel no Projeto / Foco na Global Solution 2 |
| :--- | :---: | :---: | :--- |
| **Enzo Okuizumi** | **561432** | 2TDSPG | Governança Scrum, Gestão Azure DevOps e Automação de Testes |
| **Gustavo Keiji Okada** | **563428** | 2TDSPG | Arquitetura .NET, Testes Unitários AAA e Observabilidade |
| **Lucas Barros Gouveia** | **566422** | 2TDSPG | Database Advanced (Oracle PL/SQL, Triggers DML e MongoDB) |
| **Luna de Carvalho Guimarães** | **562290** | 2TDSPG | Mobile Development (React Native, Rotas Protegidas e Cache) |
| **Milton Jakson de Sousa Marcelino** | **564836** | 2TDSPG | DevOps & Cloud (Docker/Azure) e Disruptive IoT/GenAI |

---

## 🎯 1. Matriz de Alinhamento com a Rubrica da Global Solution 2 (5 Critérios — 20 pts Cada)

| Item | Critério de Avaliação | Pontos | Escopo e Implementação Prática no Projeto ZelaFix | Evidência de Conformidade |
| :---: | :--- | :---: | :--- | :--- |
| **01** | **Estrutura de Projeto** | **20 pts** | Backlog 100% estruturado na hierarquia oficial Scrum do Azure Boards: 1 Épico integrador, 3 Features de governança, 7 PBIs e 17 Tasks técnicas de execução. | Hierarquia rastreável no Azure Boards com vínculos pai-filho e tags padronizadas. |
| **02** | **Critérios de Aceite por Feature** | **20 pts** | Todas as Features e PBIs documentados com descrições objetivas no padrão Scrum e critérios de aceite explícitos nos campos nativos do Azure DevOps. | Campos `System.Description` e `Microsoft.VSTS.Common.AcceptanceCriteria` preenchidos. |
| **03** | **Lista de Test Cases Positivos e Negativos** | **20 pts** | Cobertura caixa-preta contendo 20 casos de testes manuais distribuídos estrategicamente entre fluxos positivos (65%) e negativos/limites (35%). | Suíte completa com cenários de caminho feliz, validação de erros e restrições. |
| **04** | **Sumário dos Test Cases** | **20 pts** | Sumário detalhado para cada caso contendo: Objetivo do Teste, Preparação (Pré-condições), Dados de Entrada Controlados (Inputs) e Outputs Esperados. | Documentação formal em Markdown e cadastrada em campos ricos do Azure Boards. |
| **05** | **Passos Detalhados dos Test Cases** | **20 pts** | Sequenciamento minucioso passo a passo relacionando a Ação do Testador (Entrada) com a Resposta Esperada do Sistema (Saída). | XML de passos no campo nativo `Microsoft.VSTS.TCM.Steps` do Azure Test Plans. |
| **TOTAL** | **Pontuação Total da Entrega** | **100 pts** | **Atendimento Rigoroso a 100% dos Requisitos do Edital** | **Dossiê Unificado com Prints e Link de Admin** |

---

## 🌳 2. Estrutura Hierárquica no Azure Boards

```text
[EPIC] Compliance, Quality Assurance & Tests: Governança Scrum, Rastreabilidade de Commits e Plano de Testes Manuais Caixa-Preta
│
├── 🏆 [FEATURE 01] Governança Scrum e Estruturação do Backlog Geral no Azure Boards
│   ├── 📄 [PBI-01] Planejamento e Estruturação Hierárquica dos Épicos de Todas as Disciplinas (3 pts)
│   ├── 📄 [PBI-02] Elaboração e Padronização de User Stories e Critérios de Aceite por Feature (3 pts)
│   └── 📄 [PBI-03] Mapeamento de Dependências Técnicas e Release Plan das Sprints 1 e 2 (3 pts)
│
├── 🏆 [FEATURE 02] Matriz de Casos de Testes Manuais Caixa-Preta com Dados Controlados
│   ├── 📄 [PBI-04] Especificação de Casos de Testes Funcionais Positivos (Caminho Feliz) (3 pts)
│   └── 📄 [PBI-05] Especificação de Casos de Testes Funcionais Negativos e Cenários de Borda (3 pts)
│
└── 🏆 [FEATURE 03] Gestão de Execução no Azure Test Plans e Rastreabilidade de Commits Git
    ├── 📄 [PBI-06] Configuração de Test Plans, Execução Manual e Emissão de Métricas Analíticas (3 pts)
    └── 📄 [PBI-07] Rastreabilidade Contínua de Commits Git dos 7 Repositórios Vinculados aos Work Items (3 pts)
```

---

## 📊 3. Tabela Resumo do Backlog

| Feature Pai | ID do PBI | Título do Item de Backlog (PBI) | Story Points | Prioridade | Horas Estimadas |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **[FEATURE 01] Governança Scrum** | **PBI-01** | Planejamento e Estruturação Hierárquica dos Épicos de Todas as Disciplinas | 3 pts | 1 - Critical | 5.0h |
| | **PBI-02** | Elaboração e Padronização de User Stories e Critérios de Aceite por Feature | 3 pts | 1 - Critical | 5.0h |
| | **PBI-03** | Mapeamento de Dependências Técnicas e Release Plan das Sprints 1 e 2 | 3 pts | 1 - Critical | 4.0h |
| **[FEATURE 02] Casos de Testes** | **PBI-04** | Especificação de Casos de Testes Funcionais Positivos (Caminho Feliz) | 3 pts | 1 - Critical | 7.0h |
| | **PBI-05** | Especificação de Casos de Testes Funcionais Negativos e Cenários de Borda | 3 pts | 1 - Critical | 7.0h |
| **[FEATURE 03] Test Plans & Commits** | **PBI-06** | Configuração de Test Plans, Execução Manual e Emissão de Métricas Analíticas | 3 pts | 1 - Critical | 6.0h |
| | **PBI-07** | Rastreabilidade Contínua de Commits Git dos 7 Repositórios Vinculados aos Work Items | 3 pts | 2 - High | 6.0h |
| **TOTAL CONSOLIDADO** | **3 Features** | **7 PBIs / 17 Child Tasks Técnicas** | **21 pts** | — | **40.0h** |

---

## 📦 4. Detalhamento dos Itens de Trabalho (Épico, Features, PBIs e Tasks)

---

### 🏛️ ÉPICO
* **Work Item Type:** `Epic`
* **Title:** `[EPIC] Compliance, Quality Assurance & Tests: Governança Scrum, Rastreabilidade de Commits e Plano de Testes Manuais Caixa-Preta`
* **Tags:** `Compliance, GlobalSolution2, QA, Scrum, AzureBoards`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `21`
* **Business Value:** `100`
* **Description:** Governança ágil de todo o ciclo de vida do projeto ZelaFix na plataforma Microsoft Azure DevOps, englobando a criação da estrutura completa de Backlog Scrum (Epics, Features, PBIs e Tasks) para as 7 disciplinas da Global Solution 2, redação de Histórias de Usuário e Critérios de Aceitação rigorosos, modelagem de 20 Casos de Teste Funcionais Caixa-Preta com dados controlados (positivos e negativos), execução e emissão de métricas analíticas no Azure Test Plans e garantia de rastreabilidade de commits git entre os 7 repositórios oficiais.

---

### 🏆 [FEATURE 01] Governança Scrum e Estruturação do Backlog Geral no Azure Boards
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Compliance, Quality Assurance & Tests: Governança Scrum, Rastreabilidade de Commits e Plano de Testes Manuais Caixa-Preta`
* **Title:** `[FEATURE 01] Governança Scrum e Estruturação do Backlog Geral no Azure Boards`
* **Tags:** `Compliance, Scrum, ProductBacklog`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-11`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Description:** Estruturação arquitetural de todos os itens de trabalho da solução ZelaFix no Azure Boards segundo os preceitos do Scrum Guide e requisitos institucionais FIAP.
* **Acceptance Criteria:**
  - [x] Todos os 7 épicos das matérias cadastrados com títulos formais e sem emojis decorativos.
  - [x] Features divididas respeitando o prazo das Sprints 1 e 2.
  - [x] PBIs devidamente vinculados às suas Features com pontuação em Story Points e prioridades atribuídas.
  - [x] Todas as User Stories escritas no formato 'Como / Quero / Para que'.

#### 🔹 [PBI-01] Planejamento e Estruturação Hierárquica dos Épicos de Todas as Disciplinas
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Governança Scrum e Estruturação do Backlog Geral no Azure Boards`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Compliance, Scrum, Backlog`

##### Descrição (História de Usuário)
> **Como** QA Lead da equipe ZelaFix,  
> **Eu quero** planejar e estruturar os Épicos e Features de todas as 7 disciplinas no Azure Boards,  
> **Para que** o time tenha visibilidade consolidada do escopo integrado da Global Solution 2.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Levantamento de escopo realizado junto a todos os repositórios técnicos.
- [ ] Épicos e Features criados no Azure Boards com hierarquia estrita.
- [ ] Tags de cada disciplina configuradas corretamente.
---

#### 🔹 [PBI-02] Elaboração e Padronização de User Stories e Critérios de Aceite por Feature
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Governança Scrum e Estruturação do Backlog Geral no Azure Boards`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Compliance, UserStories, AcceptanceCriteria`

##### Descrição (História de Usuário)
> **Como** Product Owner e Analista de QA,  
> **Eu quero** padronizar as Histórias de Usuário e os Critérios de Aceitação de todas as Features,  
> **Para que** os desenvolvedores tenham critérios claros e testáveis de Definition of Done (DoD).

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Histórias formuladas segundo o padrão ágil canônico.
- [ ] Critérios de aceitação objetivos cadastrados no campo nativo do Azure DevOps.
- [ ] Eliminação de ambiguidades e requisitos não verificáveis.
---

#### 🔹 [PBI-03] Mapeamento de Dependências Técnicas e Release Plan das Sprints 1 e 2
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Governança Scrum e Estruturação do Backlog Geral no Azure Boards`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Compliance, Dependencies, ReleasePlan`

##### Descrição (História de Usuário)
> **Como** Scrum Master,  
> **Eu quero** mapear as dependências técnicas cruzadas entre Banco de Dados, APIs e Frontend,  
> **Para que** o cronograma de entrega da Global Solution seja balanceado sem gargalos de integração.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Matriz de dependências documentada entre as 7 disciplinas.
- [ ] Divisão balanceada entre Sprint 1 (modelagem e base) e Sprint 2 (integrações, cloud e testes).
---

### 🏆 [FEATURE 02] Matriz de Casos de Testes Manuais Caixa-Preta com Dados Controlados
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Compliance, Quality Assurance & Tests: Governança Scrum, Rastreabilidade de Commits e Plano de Testes Manuais Caixa-Preta`
* **Title:** `[FEATURE 02] Matriz de Casos de Testes Manuais Caixa-Preta com Dados Controlados`
* **Tags:** `Compliance, Testing, QA, BlackBox`
* **Start Date:** `2026-11-08`
* **Target Date:** `2026-11-15`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** Construção minuciosa da suíte de 20 casos de testes manuais caixa-preta, com separação obrigatória entre cenários positivos (caminho feliz) e negativos (erros, validações, exceções e borda), com técnica de dados controlados predefinidos.
* **Acceptance Criteria:**
  - [x] Mínimo de 15 a 20 casos de testes cobrindo todas as áreas da solução ZelaFix.
  - [x] Presença de cenários positivos e negativos em proporção equilibrada.
  - [x] Todos os casos contendo Objetivo, Preparação, Inputs e Outputs esperados.
  - [x] Passos de teste detalhando sequencialmente a Ação do Testador e a Resposta do Sistema.

#### 🔹 [PBI-04] Especificação de Casos de Testes Funcionais Positivos (Caminho Feliz)
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Matriz de Casos de Testes Manuais Caixa-Preta com Dados Controlados`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Compliance, Testing, PositiveTests`

##### Descrição (História de Usuário)
> **Como** Testador de Software QA,  
> **Eu quero** especificar casos de teste positivos para todas as funcionalidades principais do ZelaFix,  
> **Para que** possamos homologar que a solução cumpre com êxito os requisitos funcionais solicitados.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Casos de teste cobrindo cadastro, login JWT, abertura de chamado, filtros, radar e voto.
- [ ] Parâmetros de entrada controlados com valores realistas predefinidos.
- [ ] Resultados esperados claros com verificação de status code HTTP e elementos de UI.
---

#### 🔹 [PBI-05] Especificação de Casos de Testes Funcionais Negativos e Cenários de Borda
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Matriz de Casos de Testes Manuais Caixa-Preta com Dados Controlados`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Compliance, Testing, NegativeTests`

##### Descrição (História de Usuário)
> **Como** Especialista em Qualidade e Segurança,  
> **Eu quero** projetar casos de testes negativos e exceções de regras de negócio,  
> **Para que** possamos auditar a robustez e resiliência da aplicação frente a falhas, dados incorretos e acessos não autorizados.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Casos negativos para duplicidade de e-mail, senha incorreta e campos em branco.
- [ ] Testes de permissão RBAC (tentativa de cidadão alterar status de chamado).
- [ ] Verificação de restrições geográficas fora dos limites da cidade.
---

### 🏆 [FEATURE 03] Gestão de Execução no Azure Test Plans e Rastreabilidade de Commits Git
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Compliance, Quality Assurance & Tests: Governança Scrum, Rastreabilidade de Commits e Plano de Testes Manuais Caixa-Preta`
* **Title:** `[FEATURE 03] Gestão de Execução no Azure Test Plans e Rastreabilidade de Commits Git`
* **Tags:** `Compliance, TestPlans, Commits, Traceability`
* **Start Date:** `2026-11-12`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** Operação formal do Azure Test Plans com execução dos testes manuais planejados, geração de evidências analíticas e vinculação de commits dos 7 repositórios do ZelaFix aos Work Items.
* **Acceptance Criteria:**
  - [x] Todos os casos de teste importados para o Azure Boards e Test Plans via automação.
  - [x] Execução simulada com maioria Passed e falhas controladas para evidência de Bug Tracking.
  - [x] Commits git dos 7 repositórios vinculados por hyperlinks rastreáveis nos itens de trabalho.
  - [x] Dossiê com prints obrigatórios e identificacao.txt pronto para submissão no portal.

#### 🔹 [PBI-06] Configuração de Test Plans, Execução Manual e Emissão de Métricas Analíticas
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] Gestão de Execução no Azure Test Plans e Rastreabilidade de Commits Git`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Compliance, TestPlans, Metrics`

##### Descrição (História de Usuário)
> **Como** QA Lead,  
> **Eu quero** operar os Planos de Testes no Azure Test Plans e registrar os resultados de execução,  
> **Para que** possamos gerar relatórios e gráficos analíticos de qualidade para a banca examinadora.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Suíte de testes ativa no Azure Test Plans.
- [ ] Test points executados com status Passed e Failed documentados.
- [ ] Gráficos de pizza e relatórios gerados pela plataforma Azure DevOps.
---

#### 🔹 [PBI-07] Rastreabilidade Contínua de Commits Git dos 7 Repositórios Vinculados aos Work Items
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] Gestão de Execução no Azure Test Plans e Rastreabilidade de Commits Git`
* **Priority:** `2 - High`
* **Effort (Story Points):** `3`
* **Tags:** `Compliance, Git, Traceability`

##### Descrição (História de Usuário)
> **Como** Engenheiro de Qualidade e Governança,  
> **Eu quero** vincular os commits dos 7 repositórios aos seus respectivos Work Items,  
> **Para que** possamos comprovar a conformidade com o edital que exige commits rastreáveis ao backlog.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Commits identificados via git log em cada um dos 7 repositórios.
- [ ] Hyperlinks dos commits adicionados aos Work Items via API REST do Azure Boards.
- [ ] Dossiê de evidências e identificacao.txt consolidados conforme rubrica.