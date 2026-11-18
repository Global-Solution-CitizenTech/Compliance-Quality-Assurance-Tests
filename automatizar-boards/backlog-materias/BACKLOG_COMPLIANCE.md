# 📋 Backlog Master Azure Boards — Global Solution 2026/2: Compliance, Quality Assurance & Tests

> **Projeto Integrado:** ZelaFix — Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  
> **Disciplina:** Compliance, Quality Assurance & Tests (FIAP — 2TDSPG)  
> **Repositório GitHub:** [Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests)  
> **Organização / Projeto Azure DevOps:** `ZelaFixGS` / `ZelaFix`  
> **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`  
> **Tag Oficial:** `Compliance`  
> **Responsible Owner:** `RM561432@fiap.com.br` (Enzo Okuizumi Miranda de Souza)  
> **Epic Principal:** `[EPIC] Compliance, Quality Assurance & Tests: Governança Scrum, Rastreabilidade Multi-Repo, Suíte Postman e Azure Test Plans` (**AB#67**)  
> **Start Date:** `2026-11-04`  
> **Target Date:** `2026-11-19`  
> **Padrão:** Azure Boards (Scrum Process: Epic ➔ Feature ➔ PBI)  
> **Diretrizes Estratégicas:** 100% de aderência à rubrica oficial da Global Solution 2 (5 critérios de 20% cada), governança ágil Scrum no Azure Boards para todas as 7 disciplinas (`7` Epics, `30` Features, `89` PBIs, `276` Story Points), validação estrita de contrato via Python (`parser_backlog.py` + `run_sync.py --validate`), iterações padronizadas (`Semana 1` e `Semana 2`), tag única por disciplina (sem tag redundante `ZelaFix`), rastreabilidade contínua de commits e PRs nos 7 repositórios (GitHub + Azure Repos), suíte automatizada Postman (`6` pastas, `57` requests, `57` scripts `pm.test()`, `25` variáveis) e homologação 1:1 em **4 Azure Test Plans / 4 Suites / 25 Casos de Teste (`TC-01`..`TC-25` — 100% `Passed`)** alinhados à arquitetura `DeferredResult` (`90s`), RBAC `GESTOR`/`ADMIN`, recusa de imagem IA sem persistência no Oracle e às `13` tabelas / `5` ENUMs oficiais.

---

## 👥 Integrantes do Grupo (Ordem Alfabética Estrita)

> ⚠️ **Regra da Banca:** Todos os documentos, apresentações e entregáveis mantêm a ordem alfabética estrita dos integrantes.

| Integrante | RM | Turma | Papel no Projeto / Foco na Global Solution 2 |
| :--- | :---: | :---: | :--- |
| **Enzo Okuizumi Miranda de Souza** | **561432** | 2TDSPG | Governança Scrum, Java Advanced, Disruptive AI e Automação QA/Azure DevOps |
| **Gustavo Keiji Okada** | **563428** | 2TDSPG | Arquitetura .NET 10, Testes Unitários xUnit (106 testes) e Observabilidade OpenTelemetry |
| **Lucas Barros Gouveia** | **566422** | 2TDSPG | Database Advanced (Oracle PL/SQL 13 Tabelas 3FN, Auditoria DML e MongoDB) |
| **Luna de Carvalho Guimarães** | **562290** | 2TDSPG | Mobile Development (React Native Expo SDK 58, Rotas Protegidas e EAS Build) |
| **Milton Jakson de Sousa Marcelino** | **564836** | 2TDSPG | DevOps Tools & Cloud Computing (Docker Multi-Stage, IaC Azure CLI e CI/CD) |

---

## 🎯 1. Matriz de Alinhamento com a Rubrica da Global Solution 2 (5 Critérios — 20 pts Cada)

| Item | Critério de Avaliação | Pontos | Escopo e Implementação Prática no Projeto ZelaFix | Evidência de Conformidade |
| :---: | :--- | :---: | :--- | :--- |
| **01** | **Estrutura de Projeto** | **20 pts** | Governança consolidada no Azure Boards (`ZelaFixGS/ZelaFix`) cobrindo 7 Epics, 30 Features e 89 PBIs (`276 SP`), sendo o Epic de Compliance `#67` composto por 3 Features e 7 PBIs (`21 SP`), organizados por iteração (`Semana 1` e `Semana 2`) e responsável por matéria. | Hierarquia pai-filho validada no Azure Boards, tag única por disciplina e `run_sync.py --validate` com `0` erros. |
| **02** | **Critérios de Aceite por Feature** | **20 pts** | Features e PBIs padronizados no formato Scrum (`Como / Eu quero / Para que`) com `System.Description`, `Microsoft.VSTS.Common.AcceptanceCriteria`, datas, `Effort` e `Business Value` impostos pelo contrato `BacklogValidationError` (`parser_backlog.py`). | Campos nativos preenchidos em 100% dos Work Items via `SyncEngine` e validados em modo `strict=True`. |
| **03** | **Lista de Test Cases Positivos e Negativos** | **20 pts** | Matriz oficial ampliada para **25 Casos de Teste** (`TC-01`..`TC-25`) com **15 cenários positivos (60%)** e **10 cenários negativos/borda (40%)**, espelhando **57 requests** Postman com `57` scripts `pm.test()` e **25 variáveis** de ambiente. | Cobertura completa de Auth/RBAC JWT, Usuários/Endereços ViaCEP, Chamados `DeferredResult` (`90s`), recusa IA sem Oracle e ZelaBot RAG. |
| **04** | **Sumário dos Test Cases** | **20 pts** | Sumário estruturado por caso contendo: Azure Test Case ID, Plan/Suite, Prioridade (`P1`/`P2`), Objetivo, Pré-condições (Flyway `V1`–`V3`), Payloads controlados, Enums oficiais (`5` ENUMs) e HTTP Codes esperados. | Documentado em [`docs/MATRIZ_CASOS_DE_TESTE_AZURE.md`](../../docs/MATRIZ_CASOS_DE_TESTE_AZURE.md) e sincronizado 1:1 no Azure Test Plans. |
| **05** | **Passos Detalhados dos Test Cases** | **20 pts** | Passo a passo sequencial relacionando Ação do Testador (Entrada) e Resposta Esperada do Sistema (Saída), distribuído em **4 Test Plans / 4 Test Suites** (`#132`/`#133`, `#143`/`#144`, `#153`/`#154`, `#122`/`#123`) após higienização de `14` duplicados. | XML de passos no campo nativo `Microsoft.VSTS.TCM.Steps` em todos os 25 Test Cases (`Ready`). |
| **TOTAL** | **Pontuação Total da Entrega** | **100 pts** | **Atendimento Rigoroso a 100% dos Requisitos do Edital** | **Boards + Test Plans + Postman + Automação Python** |

---

## 🌳 2. Estrutura Hierárquica no Azure Boards

```text
📌 [EPIC] Compliance, Quality Assurance & Tests: Governança Scrum, Rastreabilidade Multi-Repo, Suíte Postman e Azure Test Plans [AB#67]
│
├── 🏆 [FEATURE 01] Governança Scrum, Validação Estrita de Contrato e Estruturação do Backlog Geral [AB#68]
│   ├── 🔹 [PBI-01] Planejamento e Estruturação Hierárquica dos Épicos e Backlogs das 7 Disciplinas [AB#69] (3 pts)
│   ├── 🔹 [PBI-02] Padronização de User Stories, Critérios de Aceite e Validação Estrita de Contrato (parser_backlog.py) [AB#70] (3 pts)
│   └── 🔹 [PBI-03] Mapeamento de Dependências, Iteration Paths (Semana 1 e Semana 2) e Governança de Tags/Responsáveis [AB#71] (3 pts)
│
├── 🏆 [FEATURE 02] Matriz de 25 Casos de Teste Caixa-Preta e Suíte Automatizada Postman (57 Requests) [AB#72]
│   ├── 🔹 [PBI-04] Especificação de Casos de Teste Positivos (15 TCs) e Suíte Postman E2E (6 Pastas / 57 Requests / 25 Variáveis) [AB#73] (3 pts)
│   └── 🔹 [PBI-05] Especificação de Casos de Teste Negativos, RBAC, Guardrails IA e Recusa sem Persistência Oracle (10 TCs) [AB#74] (3 pts)
│
└── 🏆 [FEATURE 03] Operação dos 4 Azure Test Plans (25 TCs) e Rastreabilidade Multi-Repo de Commits/PRs [AB#75]
    ├── 🔹 [PBI-06] Configuração e Sincronização 1:1 dos 4 Azure Test Plans (25 Test Cases), Higienização e Métricas QA [AB#76] (3 pts)
    └── 🔹 [PBI-07] Rastreabilidade Contínua de Commits/PRs dos 7 Repositórios (GitHub + Azure Repos) via SyncEngine [AB#77] (3 pts)
```

---

## 📊 3. Tabela Resumo do Backlog & Rastreabilidade

| Feature Pai | ID do PBI | Título do Item de Backlog (PBI) | ID Azure Boards | Story Points | Prioridade | Business Value | Commits | Status |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Feature 01** `[AB#68]` | **PBI-01** | Planejamento e Estruturação Hierárquica dos Épicos e Backlogs das 7 Disciplinas | **#69** | 3 pts | 1 - Critical | 100 | 3 | Committed |
| | **PBI-02** | Padronização de User Stories, Critérios de Aceite e Validação Estrita de Contrato (`parser_backlog.py`) | **#70** | 3 pts | 1 - Critical | 100 | 4 | Committed |
| | **PBI-03** | Mapeamento de Dependências, Iteration Paths (`Semana 1` e `Semana 2`) e Governança de Tags/Responsáveis | **#71** | 3 pts | 1 - Critical | 100 | 5 | Committed |
| **Feature 02** `[AB#72]` | **PBI-04** | Especificação de Casos de Teste Positivos (`15` TCs) e Suíte Postman E2E (`6` Pastas / `57` Requests / `25` Variáveis) | **#73** | 3 pts | 1 - Critical | 100 | 2 | Committed |
| | **PBI-05** | Especificação de Casos de Teste Negativos, RBAC, Guardrails IA e Recusa sem Persistência Oracle (`10` TCs) | **#74** | 3 pts | 1 - Critical | 100 | 1 | Committed |
| **Feature 03** `[AB#75]` | **PBI-06** | Configuração e Sincronização 1:1 dos `4` Azure Test Plans (`25` Test Cases), Higienização e Métricas QA | **#76** | 3 pts | 1 - Critical | 100 | 3 | Committed |
| | **PBI-07** | Rastreabilidade Contínua de Commits/PRs dos `7` Repositórios (GitHub + Azure Repos) via `SyncEngine` | **#77** | 3 pts | 2 - High | 80 | 5 | Committed |
| **TOTAL CONSOLIDADO** | **3 Features** | **7 PBIs (11 Work Items de Backlog + 4 Test Plans / 4 Suites / 25 Test Cases)** | **`#67`..`#77`** | **21 pts** | — | — | **22/22 únicos** | **100% Sincronizado** |

---

## 📦 4. Detalhamento dos Itens de Trabalho (Épico, Features e PBIs)

---

### 🏛️ ÉPICO

* **Work Item Type:** `Epic`
* **Azure Boards ID:** `#67`
* **Title:** `[EPIC] Compliance, Quality Assurance & Tests: Governança Scrum, Rastreabilidade Multi-Repo, Suíte Postman e Azure Test Plans`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `Compliance`
* **Assigned To:** `RM561432@fiap.com.br`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `21`
* **Business Value:** `100`
* **Description:** Governança ágil Scrum de ponta a ponta para o ecossistema ZelaFix no Microsoft Azure DevOps (`ZelaFixGS/ZelaFix`), contemplando a centralização e validação estrita dos backlogs das 7 disciplinas (`7` Epics, `30` Features, `89` PBIs e `276` Story Points) via `parser_backlog.py` (`BacklogValidationError` e `run_sync.py --validate`), organização em duas iterações (`Release 1 - Global Solution\Semana 1` e `Semana 2`), governança de tag única por disciplina e responsáveis, rastreabilidade automatizada de commits e Pull Requests (GitHub e Azure Repos ArtifactLinks), suíte Postman automatizada (`6` pastas, `57` requests, `57` scripts `pm.test()`, `25` variáveis) e homologação 1:1 em 4 Azure Test Plans / 4 Test Suites / 25 Casos de Teste (`TC-01`..`TC-25`) cobrindo API Java (`DeferredResult` `90s`, RBAC `GESTOR`/`ADMIN`, recusa IA sem Oracle, 13 tabelas 3FN / 5 ENUMs) e ZelaBot AI.
* **Acceptance Criteria:**
  - [x] Todos os 7 arquivos de backlog aprovados por `run_sync.py --validate` (`strict=True`) sem perda de datas, tags, esforço, valor de negócio, histórias ou critérios de aceite.
  - [x] Work Items padronizados com `IterationPath` (`Semana 1` e `Semana 2`), `AssignedTo` correto e tag exclusiva da disciplina (sem tag `ZelaFix`).
  - [x] Coleção Postman v2.0 validada com `6` pastas, `57` requests, `57` scripts `pm.test()` e `25` variáveis de ambiente Local/Cloud.
  - [x] Matriz `docs/MATRIZ_CASOS_DE_TESTE_AZURE.md` com `25` Casos de Teste (`15` Positivos / `10` Negativos) sincronizados 1:1 nos `4` Azure Test Plans (`#132`, `#143`, `#153`, `#122`).
  - [x] Todos os `22` commits de `Compliance-Quality-Assurance-Tests` vinculados aos respectivos PBIs no Azure Boards, além da rastreabilidade dos demais repositórios.

---

### 🏆 [FEATURE 01] Governança Scrum, Validação Estrita de Contrato e Estruturação do Backlog Geral

* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#68`
* **Parent:** `[EPIC] Compliance, Quality Assurance & Tests: Governança Scrum, Rastreabilidade Multi-Repo, Suíte Postman e Azure Test Plans` (`#67`)
* **Title:** `[FEATURE 01] Governança Scrum, Validação Estrita de Contrato e Estruturação do Backlog Geral`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `Compliance`
* **Assigned To:** `RM561432@fiap.com.br`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-11`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Description:** Estruturação arquitetural e governança de todos os Work Items da plataforma ZelaFix no Azure Boards segundo o processo Scrum (`Epic -> Feature -> PBI`), com contrato mínimo obrigatório validado automaticamente por `parser_backlog.py` (`validate_backlog_document` e `BacklogValidationError`), balanceamento entre `Semana 1` e `Semana 2`, responsáveis por disciplina e higienização estrita de tags.
* **Acceptance Criteria:**
  - [x] Todos os 7 épicos das matérias cadastrados com títulos formais limpos (`clean_title`) e sem emojis decorativos no Azure Boards.
  - [x] Contrato obrigatório (`Start Date`, `Target Date`, `Tags`, `Effort`, `Priority`, `Business Value`, `Description` e `Acceptance Criteria`) validado via `run_sync.py --validate`.
  - [x] Iterações distribuídas entre `Release 1 - Global Solution\Semana 1` (Mobile, Java, Database) e `Semana 2` (.NET, DevOps, IoT, Compliance).
  - [x] Remoção completa da tag redundante `ZelaFix` em todos os backlogs e Work Items.

---

#### 🔹 [PBI-01] Planejamento e Estruturação Hierárquica dos Épicos e Backlogs das 7 Disciplinas

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#69`
* **Parent Feature:** `[FEATURE 01] Governança Scrum, Validação Estrita de Contrato e Estruturação do Backlog Geral` (`#68`)
* **Title:** `[PBI-01] Planejamento e Estruturação Hierárquica dos Épicos e Backlogs das 7 Disciplinas`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `Compliance`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** QA Lead da equipe ZelaFix,  
> **Eu quero** planejar, centralizar e estruturar os Épicos, Features e PBIs de todas as 7 disciplinas em `automatizar-boards/backlog-materias/`,  
> **Para que** o time tenha visibilidade consolidada do escopo integrado (`7` Epics, `30` Features, `89` PBIs, `276 SP`) no Azure Boards.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Levantamento de escopo realizado junto a todos os 7 repositórios técnicos da Global Solution 2.
- [x] Backlogs Markdown centralizados em `automatizar-boards/backlog-materias/` com hierarquia estrita Epic ➔ Feature ➔ PBI.
- [x] Épicos (`#1`, `#14`, `#27`, `#36`, `#48`, `#58`, `#67`) sincronizados no Azure Boards sem títulos duplicados ou itens órfãos.

##### Commits vinculados (GitHub Repository):
- [`2628131`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/2628131) — `Initial commit` *(vinculado em AB#69)*
- [`189b5e0`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/189b5e0) — `feat(compliance): centraliza backlogs das 7 disciplinas, sincroniza Azure Boards ZelaFix e estrutura 20 casos de testes` *(vinculado em AB#69)*
- [`439d072`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/439d072) — `feat(compliance): expandir backlog de mobile para 15 PBIs com granularidade refinada` *(vinculado em AB#69)*

---

#### 🔹 [PBI-02] Padronização de User Stories, Critérios de Aceite e Validação Estrita de Contrato (parser_backlog.py)

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#70`
* **Parent Feature:** `[FEATURE 01] Governança Scrum, Validação Estrita de Contrato e Estruturação do Backlog Geral` (`#68`)
* **Title:** `[PBI-02] Padronização de User Stories, Critérios de Aceite e Validação Estrita de Contrato (parser_backlog.py)`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `Compliance`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** Product Owner e Analista de QA,  
> **Eu quero** padronizar todas as Histórias de Usuário e Critérios de Aceitação e impor validação automática via `parser_backlog.py` (`strict=True` e `run_sync.py --validate`),  
> **Para que** nenhuma atualização de backlog remova datas, tags, story points, prioridades ou critérios de aceite de forma acidental.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Histórias formuladas no padrão ágil canônico (`Como / Eu quero / Para que`) com separação estrita entre `System.Description` e `Microsoft.VSTS.Common.AcceptanceCriteria`.
- [x] Função `validate_backlog_document()` e exceção `BacklogValidationError` integradas em `parser_backlog.py` e `SyncEngine.sync_discipline()`.
- [x] CLI `run_sync.py --validate` validando os 7 backlogs com `0` erros e exibindo resumo de datas, Features, PBIs e Story Points.

##### Commits vinculados (GitHub Repository):
- [`48bfacf`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/48bfacf) — `feat(compliance): refatorar backlog de java advanced com microsservicos, rabbitmq e spring ai` *(vinculado em AB#70)*
- [`e219b90`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/e219b90) — `feat(compliance): alinhar backlogs de java e database com commits e entregas reais da GS` *(vinculado em AB#70)*
- [`c620a5a`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/c620a5a) — `fix(docs): restaurar integralmente metadados, historias de usuario e criterios de aceite dos PBIs 01-14 e expandir Feature 05 (PBIs 15-18)` *(vinculado em AB#70)*
- [`e3260a0`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/e3260a0) — `feat(boards): exigir campos obrigatorios no parser e restaurar datas e tags em BACKLOG_DISRUPTIVE_ARCHITECTURES` *(vinculado em AB#70)*

---

#### 🔹 [PBI-03] Mapeamento de Dependências, Iteration Paths (Semana 1 e Semana 2) e Governança de Tags/Responsáveis

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#71`
* **Parent Feature:** `[FEATURE 01] Governança Scrum, Validação Estrita de Contrato e Estruturação do Backlog Geral` (`#68`)
* **Title:** `[PBI-03] Mapeamento de Dependências, Iteration Paths (Semana 1 e Semana 2) e Governança de Tags/Responsáveis`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `Compliance`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** Scrum Master do time ZelaFix,  
> **Eu quero** configurar os Iteration Paths oficiais (`Semana 1` e `Semana 2`), atribuir os responsáveis corretos por disciplina em `config.py` e garantir governança estrita de tag única e estados (`In Progress` / `Committed`),  
> **Para que** o cronograma da Global Solution 2 reflita com exatidão as dependências técnicas entre modelagem/APIs e cloud/IA/QA.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `Semana 1` configurada para `Mobile` (Luna), `JavaAdvanced` (Enzo) e `Database` (Lucas); `Semana 2` configurada para `DotNet` (Gustavo), `DevOps` (Milton), `DisruptiveArchitectures` (Enzo) e `Compliance` (Enzo).
- [x] Remoção integral da tag redundante `ZelaFix` nos 7 backlogs e no motor `SyncEngine`, mantendo exatamente a tag oficial de cada disciplina.
- [x] Governança aplicada via `run_sync.py --govern` (`In Progress` para Epics/Features e `Committed` para PBIs) e remoção de artefatos/scripts temporários.

##### Commits vinculados (GitHub Repository):
- [`b9402cf`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/b9402cf) — `refactor(compliance): remove header_desc redundante e prefixo GS, atribui responsaveis por materia e atualiza status para In Progress` *(vinculado em AB#71)*
- [`068b6f2`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/068b6f2) — `refactor(compliance): remover tag redundante ZelaFix de todos os backlogs e sync engine` *(vinculado em AB#71)*
- [`cde44f4`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/cde44f4) — `feat(boards): configurar iteration paths Release 1 - Global Solution (Semana 1 e Semana 2) e sincronizar 93 work items` *(vinculado em AB#71)*
- [`8d04c01`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/8d04c01) — `chore(boards): remover scripts temporarios de ajuste de iteracoes` *(vinculado em AB#71)*
- [`390eede`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/390eede) — `feat: removendo arquivo inútil` *(vinculado em AB#71)*

---

### 🏆 [FEATURE 02] Matriz de 25 Casos de Teste Caixa-Preta e Suíte Automatizada Postman (57 Requests)

* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#72`
* **Parent:** `[EPIC] Compliance, Quality Assurance & Tests: Governança Scrum, Rastreabilidade Multi-Repo, Suíte Postman e Azure Test Plans` (`#67`)
* **Title:** `[FEATURE 02] Matriz de 25 Casos de Teste Caixa-Preta e Suíte Automatizada Postman (57 Requests)`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `Compliance`
* **Assigned To:** `RM561432@fiap.com.br`
* **Start Date:** `2026-11-08`
* **Target Date:** `2026-11-15`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** Especificação completa da matriz `docs/MATRIZ_CASOS_DE_TESTE_AZURE.md` com 25 casos de teste caixa-preta (`15` positivos e `10` negativos), alinhados aos 5 ENUMs oficiais, 13 tabelas Oracle/MongoDB, seeds Flyway (`V2`/`V3`) e à suíte Postman `CitizenTech_QA_Automation.postman_collection.json` (`6` pastas, `57` requests, `57` scripts `pm.test()`, `25` variáveis em `CitizenTech_QA_Environment.postman_environment.json`).
* **Acceptance Criteria:**
  - [x] `25` casos de teste (`TC-01`..`TC-25`) documentados com Objetivo, Pré-condições, Dados de Entrada, HTTP Codes esperados e passos estruturados.
  - [x] Proporção equilibrada entre fluxos positivos (`15` TCs — `60%`) e negativos/segurança/borda (`10` TCs — `40%`).
  - [x] Coleção Postman v2.0 com `6` pastas, `57` requests e `57` asserções `pm.test()` alinhadas 1:1 aos endpoints `DeferredResult` (`90s`), `multipart/form-data` e teardown.
  - [x] Cobertura explícita de recusa de imagem fora de escopo (`ocorrenciaValida=false`) sem persistência no Oracle e guardrails do ZelaBot AI.

---

#### 🔹 [PBI-04] Especificação de Casos de Teste Positivos (15 TCs) e Suíte Postman E2E (6 Pastas / 57 Requests / 25 Variáveis)

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#73`
* **Parent Feature:** `[FEATURE 02] Matriz de 25 Casos de Teste Caixa-Preta e Suíte Automatizada Postman (57 Requests)` (`#72`)
* **Title:** `[PBI-04] Especificação de Casos de Teste Positivos (15 TCs) e Suíte Postman E2E (6 Pastas / 57 Requests / 25 Variáveis)`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `Compliance`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** Testador de Software QA,  
> **Eu quero** especificar `15` casos de teste positivos com dados controlados e manter a coleção Postman automatizada (`6` pastas, `57` requests, `57` scripts `pm.test()`, `25` variáveis),  
> **Para que** possamos homologar de ponta a ponta os fluxos de autenticação JWT, usuários, endereços ViaCEP, chamados `DeferredResult` (`90s`), BLOB de fotos, apoio comunitário (`+1`), RabbitMQ/Worker AI e ZelaBot RAG.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `15` casos positivos especificados cobrindo `TC-01`, `TC-07`, `TC-09`, `TC-10`, `TC-12`, `TC-13`, `TC-14`, `TC-16`, `TC-17`, `TC-18`, `TC-19`, `TC-21`, `TC-22`, `TC-24` e `TC-25`.
- [x] Suíte Postman organizada em `6` pastas (`01. Observabilidade`, `02. Autenticação & RBAC`, `03. Usuários`, `04. Endereços`, `05. Chamados, Triagem IA (DeferredResult) & Apoio`, `06. Teardown & Limpeza`) com `57` requests e `57` `pm.test()`.
- [x] Ambiente `CitizenTech_QA_Environment.postman_environment.json` configurado com `25` variáveis compatíveis com Local (`8080`/`8081`) e Cloud Azure (`app-zelafix.azurewebsites.net`).

##### Commits vinculados (GitHub Repository):
- [`6766e2e`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/6766e2e) — `feat: Adicionando mudanças no readme e criando matriz de casos de teste.` *(vinculado em AB#73)*
- [`d756cb2`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/d756cb2) — `feat(postman): atualizar colecao QA (57 requests) e environment alinhados a API Java e 13 tabelas` *(vinculado em AB#73)*

---

#### 🔹 [PBI-05] Especificação de Casos de Teste Negativos, RBAC, Guardrails IA e Recusa sem Persistência Oracle (10 TCs)

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#74`
* **Parent Feature:** `[FEATURE 02] Matriz de 25 Casos de Teste Caixa-Preta e Suíte Automatizada Postman (57 Requests)` (`#72`)
* **Title:** `[PBI-05] Especificação de Casos de Teste Negativos, RBAC, Guardrails IA e Recusa sem Persistência Oracle (10 TCs)`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `Compliance`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** Especialista em Qualidade e Segurança de Aplicações,  
> **Eu quero** projetar `10` casos de teste negativos cobrindo falhas de autenticação/JWT, bloqueios RBAC, validações de payload, recusa de imagem pela IA sem persistência no Oracle e desvios de escopo no ZelaBot,  
> **Para que** possamos comprovar a resiliência, integridade transacional e conformidade de segurança da plataforma CitizenTech.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Casos negativos `TC-02`, `TC-03`, `TC-04`, `TC-05` e `TC-06` validando HTTP `401`/`403`/`400` para login inválido, ausência de Bearer, token adulterado e restrições RBAC (`CIDADAO` vs `GESTOR` vs `ADMIN`).
- [x] Casos `TC-08`, `TC-11` e `TC-15` validando HTTP `409 Conflict` (e-mail duplicado), Bean Validation (`@DddValidation`, CEP inválido) e rejeição de `POST /chamados` sem part `foto` ou magic bytes inválidos.
- [x] Casos `TC-20` e `TC-23` validando recusa de imagem fora de escopo (`ocorrenciaValida=false` via `TriagemPendenteStore` sem persistência na tabela `CHAMADOS`) e recusa de solicitações off-topic no ZelaBot AI.

##### Commits vinculados (GitHub Repository):
- [`9ccf50c`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/9ccf50c) — `docs(qa): atualizar README e matriz de casos de teste com o Azure Test Plans` *(vinculado em AB#74)*

---

### 🏆 [FEATURE 03] Operação dos 4 Azure Test Plans (25 TCs) e Rastreabilidade Multi-Repo de Commits/PRs

* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#75`
* **Parent:** `[EPIC] Compliance, Quality Assurance & Tests: Governança Scrum, Rastreabilidade Multi-Repo, Suíte Postman e Azure Test Plans` (`#67`)
* **Title:** `[FEATURE 03] Operação dos 4 Azure Test Plans (25 TCs) e Rastreabilidade Multi-Repo de Commits/PRs`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `Compliance`
* **Assigned To:** `RM561432@fiap.com.br`
* **Start Date:** `2026-11-12`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** Operação e sincronização 1:1 dos 4 Azure Test Plans (`api-auth-rbac` `#132`, `api-usuarios-enderecos` `#143`, `api-chamados` `#153`, `ai-service` `#122`) com 25 Test Cases em estado `Ready` após higienização de duplicados, aliada à rastreabilidade automatizada de commits GitHub e Pull Requests / ArtifactLinks do Azure Repos para todos os 7 repositórios do ecossistema ZelaFix.
* **Acceptance Criteria:**
  - [x] `4` Test Plans (`#132`, `#143`, `#153`, `#122`) e `4` Test Suites (`#133`, `#144`, `#154`, `#123`) operacionais no Azure DevOps com `25` Test Cases (`TC-01`..`TC-25`) em paridade 1:1 com a matriz Markdown.
  - [x] Remoção de `14` casos de teste duplicados/obsoletos (`#125`, `#130`, `#135`, `#136`, `#138`, `#146`, `#150`, `#157`, `#159`, `#160`, `#162`, `#164`, `#165`, `#167`).
  - [x] Commits GitHub e ArtifactLinks do Azure Repos vinculados aos PBIs das disciplinas por meio da automação Python (`SyncEngine` / `AzureClient`).
  - [x] Dossiê visual (`docs/*.png`), `README.md` consolidado e `identificacao.txt` atualizados para submissão.

---

#### 🔹 [PBI-06] Configuração e Sincronização 1:1 dos 4 Azure Test Plans (25 Test Cases), Higienização e Métricas QA

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#76`
* **Parent Feature:** `[FEATURE 03] Operação dos 4 Azure Test Plans (25 TCs) e Rastreabilidade Multi-Repo de Commits/PRs` (`#75`)
* **Title:** `[PBI-06] Configuração e Sincronização 1:1 dos 4 Azure Test Plans (25 Test Cases), Higienização e Métricas QA`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `Compliance`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** QA Lead no Azure DevOps,  
> **Eu quero** estruturar, higienizar e sincronizar os `4` Test Plans (`api-auth-rbac`, `api-usuarios-enderecos`, `api-chamados` e `ai-service`) e seus `25` Test Cases com passos XML nativos (`Microsoft.VSTS.TCM.Steps`),  
> **Para que** a matriz `docs/MATRIZ_CASOS_DE_TESTE_AZURE.md` e o Azure Test Plans estejam em paridade 1:1 sem duplicidades para execução e emissão de métricas.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `4` Test Plans e `4` Test Suites ativos no Azure Test Plans (`#132`/`#133` com `6` TCs, `#143`/`#144` com `6` TCs, `#153`/`#154` com `6` TCs e `#122`/`#123` com `7` TCs), com `#142`, `#155`, `#163` e `#166` sincronizados para RBAC `GESTOR`/`ADMIN` e timeout `90s`.
- [x] `14` Test Cases duplicados/obsoletos removidos do Azure DevOps garantindo exatamente `25` Test Cases ativos em estado `Ready`.
- [x] Todos os Test Cases atribuídos a `RM561432@fiap.com.br` na iteração `ZelaFix\Release 1 - Global Solution\Semana 2` com tags sem `ZelaFix` e passos XML completos.

##### Commits vinculados (GitHub Repository):
- [`b1b105c`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/b1b105c) — `refactor(compliance): remove test plan e casos de teste do codigo e do Azure Boards conforme alinhamento` *(vinculado em AB#76)*
- [`9ccf50c`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/9ccf50c) — `docs(qa): atualizar README e matriz de casos de teste com o Azure Test Plans` *(vinculado em AB#76)*
- [`6ad2806`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/6ad2806) — `docs(qa): atualizar matriz de 25 casos de teste Azure Test Plans e README consolidado` *(vinculado em AB#76)*
- [`5f5aefe`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/5f5aefe) — `docs(qa): alinhar matriz de casos de teste com enums canonicos e endpoints de producao` *(vinculado em AB#76)*
- [`1315724`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/1315724) — `docs(compliance): adiciona PDF oficial de entrega e vincula no README` *(vinculado em AB#76)*
- [`e4a0e5f`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/e4a0e5f) — `docs(compliance): atualizar PDF final, totais consolidados (30 Features, 89 PBIs, 276 SP) e identificacao.txt` *(vinculado em AB#76)*
- [`1504468`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/1504468) — `docs(boards,qa): sincronizar todos os commits recentes das 7 disciplinas, RBAC GESTOR/ADMIN no Postman/Matriz e APK versionCode 13` *(vinculado em AB#76)*
- [`31468e6`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/31468e6) — `docs(compliance): atualizar versao final do PDF de documentacao da GS 2` *(vinculado em AB#76)*

---

#### 🔹 [PBI-07] Rastreabilidade Contínua de Commits/PRs dos 7 Repositórios (GitHub + Azure Repos) via SyncEngine

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#77`
* **Parent Feature:** `[FEATURE 03] Operação dos 4 Azure Test Plans (25 TCs) e Rastreabilidade Multi-Repo de Commits/PRs` (`#75`)
* **Title:** `[PBI-07] Rastreabilidade Contínua de Commits/PRs dos 7 Repositórios (GitHub + Azure Repos) via SyncEngine`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `Compliance`
* **Assigned To:** `RM561432@fiap.com.br`
* **Priority:** `2 - High`
* **Effort (Story Points):** `3`
* **Business Value:** `80`

##### Descrição (História de Usuário)
> **Como** Engenheiro de Qualidade e Governança DevOps,  
> **Eu quero** operar a suíte Python (`SyncEngine`, `AzureClient`, `link_commits.py` e `install_git_hooks.py`) para vincular commits GitHub (`Hyperlink`) e commits/PRs Azure Repos (`ArtifactLink`) aos PBIs de cada disciplina,  
> **Para que** todos os repositórios da Global Solution 2 possuam rastreabilidade verificável entre código-fonte e Azure Boards.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Arquitetura Python unificada em `automatizar-boards/` (`run_sync.py`, `sync_engine.py`, `azure_client.py`, `parser_backlog.py`, `config.py`, `install_git_hooks.py`) e documentação atualizada para `ZelaFixGS/ZelaFix`.
- [x] Rastreabilidade aplicada aos repositórios integrados (Mobile `48` commits, Java `120+` commits Azure Repos + PRs, Database `25` commits, DevOps `35` commits, Disruptive AI `45` commits e Compliance `24+` commits).
- [x] Documentação consolidada em `README.md` (com Declaração de Uso de IA), `identificacao.txt` e capturas de evidência preservadas em `docs/*.png`.

##### Commits vinculados (GitHub Repository):
- [`015c6dd`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/015c6dd) — `refactor(compliance): unifica arquitetura de automacao no AzureClient, SyncEngine e config centralizada, eliminando codigo legado e redundante` *(vinculado em AB#77)*
- [`c17a4a9`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/c17a4a9) — `docs(java): atualizar BACKLOG_JAVA_ADVANCED.md com Feature 05, 18 PBIs, 54 story points e vinculos Azure Repos` *(vinculado em AB#77)*
- [`df43043`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/df43043) — `docs(boards): sincronizar BACKLOG_MOBILE com Azure Boards` *(vinculado em AB#77)*
- [`471c6be`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/471c6be) — `docs(boards): sincronizar BACKLOG_DISRUPTIVE_ARCHITECTURES e vincular commits ao Azure Boards` *(vinculado em AB#77)*
- [`12ae289`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/12ae289) — `docs(boards): atualizar backlogs de Mobile, Java, Database e DevOps e sincronizar Azure Boards` *(vinculado em AB#77)*
- [`72db657`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/72db657) — `chore: remover script temporario de sincronizacao sync_azure_boards_iot` *(vinculado em AB#77)*
- [`8f4ec6a`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/8f4ec6a) — `feat(boards): implementar Smart Upsert (--update), eliminar scripts redundantes e unificar CLI` *(vinculado em AB#77)*
- [`f9164b9`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/f9164b9) — `docs(dotnet): mapear Azure Boards IDs #27..#35 no BACKLOG_DOT_NET.md e sincronizar nuvem` *(vinculado em AB#77)*
- [`e89c5c8`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/e89c5c8) — `docs(compliance): generalizar mencoes de modelos de IA em todos os backlogs e README` *(vinculado em AB#77)*
- [`a4b343d`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/a4b343d) — `docs(compliance): eliminar mencoes a provedores e modelos especificos nos backlogs, matriz e colecao` *(vinculado em AB#77)*
- [`318e741`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/318e741) — `docs(java): atualizar backlog com fail-fast na IA e historico duplo do chamado` *(vinculado em AB#77)*
- [`d4a7e25`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/d4a7e25) — `docs(backlog): alinhar PBI-13 com escalonamento comunitario de votos via rabbitmq` *(vinculado em AB#77)*
- [`576000e`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/576000e) — `refactor: atualizar endpoints dos Web Apps para app-zelafix e app-zelafix-worker` *(vinculado em AB#77)*
- [`4ade001`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/4ade001) — `docs(backlogs): sincronizar commits recentes de Java, IoT e DevOps no Azure Boards` *(vinculado em AB#77)*
- [`28b5ecd`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/28b5ecd) — `docs(mobile,java): sincronizar 8 commits de mobile, versionCode 8, 66 testes e PRs de java` *(vinculado em AB#77)*
- [`1549492`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/1549492) — `docs(boards): atualizar backlog de Java Advanced com PRs #33, #34, #35 e commit afe5b7e` *(vinculado em AB#77)*
- [`e04e576`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/e04e576) — `feat(boards): sincronizar backlog completo de Dot Net com 5 Features, 15 PBIs e commits vinculados no Azure Boards` *(vinculado em AB#77)*
- [`0d2cd49`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/0d2cd49) — `docs(boards): atualizar BACKLOG_DOT_NET.md com 105 testes (>91% cobertura), Swagger 23 paths e commits f5a8305/6979213` *(vinculado em AB#77)*
- [`5e37abc`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/5e37abc) — `docs(boards): sincronizar ultimos commits de Java, Mobile, Database, DevOps e DotNet` *(vinculado em AB#77)*
- [`d962aa3`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/d962aa3) — `feat: add identificação.txt` *(vinculado em AB#77)*
- [`3a0870c`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/3a0870c) — `feat: Só um pequeno ajuste no identificação.txt` *(vinculado em AB#77)*
- [`dd3efd0`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/dd3efd0) — `docs(boards): atualizar Database (d3ea34e) e Java (631a585, c3109df) e sincronizar Azure Boards` *(vinculado em AB#77)*
- [`c358710`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/c358710) — `feat: add imagens no readme de compliance!` *(vinculado em AB#77)*
- [`b808f8c`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/b808f8c) — `feat: só um pequeno ajuste em identificação.txt` *(vinculado em AB#77)*
- [`e16a3cc`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/e16a3cc) — `refactor(boards): impor tag unica por disciplina em Java, Database e no SyncEngine` *(vinculado em AB#77)*
- [`48476a7`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/48476a7) — `feat(boards): definir estado Done para todas as Features e PBIs mantendo Epics In Progress` *(vinculado em AB#77)*
- [`f9e4b47`](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests/commit/f9e4b47) — `feat: só um pequeno ajuste backlog devops` *(vinculado em AB#77)*
