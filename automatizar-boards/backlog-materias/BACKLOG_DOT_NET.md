# 📋 Backlog Master Azure Boards — Global Solution 2026/2: Advanced Business Development with .NET

> **Projeto Integrado:** ZelaFix — Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  
> **Disciplina:** Advanced Business Development with .NET (FIAP — 2TDSPG)  
> **Epic Principal:** `[EPIC] GS 2026/2 - Advanced Business Development with .NET: Microsserviço de Notificações Urbanas, Observabilidade e Qualidade de Software`  
> **Start Date:** `2026-11-04`  
> **Target Date:** `2026-11-19`  
> **Padrão:** Azure Boards (Scrum Process: Epic ➔ Feature ➔ PBI ➔ Task)  
> **Diretrizes Estratégicas:** Desenvolvimento de Web API em C# e .NET 8 com Clean Architecture, microsserviço de notificações e alertas municipais, observabilidade completa com OpenTelemetry, métricas exportadas para Prometheus/Grafana, Health Checks nativos com checagem de integridade, logs estruturados via Serilog e suíte de testes unitários xUnit com padrão AAA (Arrange, Act, Assert).

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
[EPIC] GS 2026/2 - Advanced Business Development with .NET: Microsserviço de Notificações Urbanas, Observabilidade e Qualidade de Software
│
├── 🏆 [FEATURE 01] Arquitetura Limpa e API de Alertas e Notificações Municipais
│   ├── 📄 [PBI-01] Estruturação da Clean Architecture e Endpoints de Notificação (3 pts)
│   └── 📄 [PBI-02] Regras de Negócio de Despacho de Alertas por Região e Categoria (3 pts)
│
├── 🏆 [FEATURE 02] Observabilidade Completa (OpenTelemetry, Prometheus e HealthChecks)
│   ├── 📄 [PBI-03] Instrumentação com OpenTelemetry e Exportação de Métricas Prometheus (3 pts)
│   └── 📄 [PBI-04] Health Checks Customizados e Logs Estruturados com Serilog (3 pts)
│
└── 🏆 [FEATURE 03] Qualidade de Software e Cobertura de Testes Automatizados xUnit
    └── 📄 [PBI-05] Suíte de Testes Unitários com xUnit no Padrão AAA e FluentAssertions (3 pts)
```

---

## 📊 2. Tabela Resumo do Backlog

| Feature Pai | ID do PBI | Título do Item de Backlog (PBI) | Story Points | Prioridade | Horas Estimadas |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **[FEATURE 01] API & Alertas** | **PBI-01** | Estruturação da Clean Architecture e Endpoints de Notificação | 3 pts | 1 - Critical | 7.0h |
| | **PBI-02** | Regras de Negócio de Despacho de Alertas por Região e Categoria | 3 pts | 1 - Critical | 6.5h |
| **[FEATURE 02] Observabilidade**| **PBI-03** | Instrumentação com OpenTelemetry e Exportação de Métricas Prometheus | 3 pts | 1 - Critical | 7.5h |
| | **PBI-04** | Health Checks Customizados e Logs Estruturados com Serilog | 3 pts | 1 - Critical | 6.0h |
| **[FEATURE 03] Testes xUnit** | **PBI-05** | Suíte de Testes Unitários com xUnit no Padrão AAA e FluentAssertions | 3 pts | 1 - Critical | 8.0h |
| **TOTAL CONSOLIDADO** | **3 Features** | **5 PBIs / 15 Child Tasks Técnicas** | **15 pts** | — | **35.0h** |

---

## 📦 3. Detalhamento dos Itens de Trabalho (Épico, Features, PBIs e Tasks)

---

### 🏛️ ÉPICO
* **Work Item Type:** `Epic`
* **Title:** `[EPIC] GS 2026/2 - Advanced Business Development with .NET: Microsserviço de Notificações Urbanas, Observabilidade e Qualidade de Software`
* **Tags:** `DotNet, ZelaFix, GlobalSolution2, CSharp, OpenTelemetry, Serilog, xUnit`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `15`
* **Business Value:** `100`
* **Description:** Construção do microsserviço .NET 8 em Clean Architecture responsável pelo processamento e despacho de notificações de emergência urbana (alertas climáticos e avisos de zeladoria), integrando telemetria avançada OpenTelemetry, logs estruturados Serilog, endpoints de health check para auditoria e testes unitários com xUnit no padrão AAA.

---

### 🏆 [FEATURE 01] Arquitetura Limpa e API de Alertas e Notificações Municipais
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] GS 2026/2 - Advanced Business Development with .NET: Microsserviço de Notificações Urbanas, Observabilidade e Qualidade de Software`
* **Title:** `[FEATURE 01] Arquitetura Limpa e API de Alertas e Notificações Municipais`
* **Tags:** `DotNet, CleanArchitecture, WebAPI`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-10`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** Estruturação da solução em camadas desacopladas (Domain, Application, Infrastructure, API) com controladores RESTful para despacho de comunicados aos cidadãos.
* **Acceptance Criteria:**
  - [x] Solução .NET 8 com separação estrita de projetos (Domain, Application, Infrastructure e API).
  - [x] Endpoints RESTful documentados no Swagger UI com DTOs e validações FluentValidation.

#### 🔹 [PBI-01] Estruturação da Clean Architecture e Endpoints de Notificação
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Arquitetura Limpa e API de Alertas e Notificações Municipais`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DotNet, CleanArch, Setup`

##### Descrição (História de Usuário)
> **Como** arquiteto de software .NET,  
> **Eu quero** criar a estrutura de projetos seguindo a Clean Architecture,  
> **Para que** a lógica de negócio de notificações fique isolada de detalhes de infraestrutura e frameworks.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Solução `ZelaFix.Notifications.sln` com 4 projetos desacoplados.
- [ ] Injeção de dependência configurada no `Program.cs`.
- [ ] Swagger interativo ativo em ambiente de desenvolvimento.
---

#### 🔹 [PBI-02] Regras de Negócio de Despacho de Alertas por Região e Categoria
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Arquitetura Limpa e API de Alertas e Notificações Municipais`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DotNet, BusinessRules, Notifications`

##### Descrição (História de Usuário)
> **Como** operador da Defesa Civil,  
> **Eu quero** emitir comunicados segmentados por bairro e nível de severidade (Informativo, Alerta, Emergência),  
> **Para que** os munícipes afetados recebam avisos imediatos sobre interdições e alagamentos.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Entidade `AlertaUrbano` com validações de domínio.
- [ ] Serviço `NotificationService` processando regras de triagem de destinatários.
- [ ] Retorno HTTP 201 Created com identificador único de despacho.
---

### 🏆 [FEATURE 02] Observabilidade Completa (OpenTelemetry, Prometheus e HealthChecks)
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] GS 2026/2 - Advanced Business Development with .NET: Microsserviço de Notificações Urbanas, Observabilidade e Qualidade de Software`
* **Title:** `[FEATURE 02] Observabilidade Completa (OpenTelemetry, Prometheus e HealthChecks)`
* **Tags:** `DotNet, Observability, OpenTelemetry, Serilog, HealthChecks`
* **Start Date:** `2026-11-09`
* **Target Date:** `2026-11-15`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** Implementação de monitoramento contínuo da aplicação com traces, métricas e logs estruturados.
* **Acceptance Criteria:**
  - [x] OpenTelemetry instrumentado coletando métricas de requisições HTTP e latência.
  - [x] Endpoint `/metrics` expondo métricas no formato Prometheus.
  - [x] Health checks ativos em `/health` e `/health/ready`.
  - [x] Logs estruturados com Serilog gravados em formato JSON.

#### 🔹 [PBI-03] Instrumentação com OpenTelemetry e Exportação de Métricas Prometheus
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Observabilidade Completa (OpenTelemetry, Prometheus e HealthChecks)`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DotNet, OpenTelemetry, Prometheus`

##### Descrição (História de Usuário)
> **Como** engenheiro de SRE e operações,  
> **Eu quero** rastrear o tempo de resposta e taxa de erros dos despachos de alertas via OpenTelemetry,  
> **Para que** possamos monitorar a saúde do serviço em dashboards do Grafana.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Pacotes `OpenTelemetry.Extensions.Hosting` e `OpenTelemetry.Exporter.Prometheus.AspNetCore` configurados.
- [ ] Métricas customizadas (contador de alertas emitidos e gauge de fila).
---

#### 🔹 [PBI-04] Health Checks Customizados e Logs Estruturados com Serilog
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Observabilidade Completa (OpenTelemetry, Prometheus e HealthChecks)`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DotNet, HealthChecks, Serilog`

##### Descrição (História de Usuário)
> **Como** equipe de infraestrutura,  
> **Eu quero** endpoints de liveness/readiness e logs estruturados em JSON no console,  
> **Para que** orquestradores como Docker e Kubernetes identifiquem a integridade da aplicação.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Endpoint `/health` retornando status Healthy/Unhealthy com detalhes de memória e dependências.
- [ ] Serilog configurado com enrichers de correlationId e timestamps UTC.
---

### 🏆 [FEATURE 03] Qualidade de Software e Cobertura de Testes Automatizados xUnit
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] GS 2026/2 - Advanced Business Development with .NET: Microsserviço de Notificações Urbanas, Observabilidade e Qualidade de Software`
* **Title:** `[FEATURE 03] Qualidade de Software e Cobertura de Testes Automatizados xUnit`
* **Tags:** `DotNet, Testing, xUnit, AAA, Quality`
* **Start Date:** `2026-11-12`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`
* **Description:** Projeto de testes unitários automatizados cobrindo regras de negócio críticas e validações.
* **Acceptance Criteria:**
  - [x] Testes unitários utilizando xUnit, Moq e FluentAssertions.
  - [x] Aplicação estrita do padrão AAA (Arrange, Act, Assert).
  - [x] 100% dos testes executados com sucesso no `dotnet test`.

#### 🔹 [PBI-05] Suíte de Testes Unitários com xUnit no Padrão AAA e FluentAssertions
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] Qualidade de Software e Cobertura de Testes Automatizados xUnit`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DotNet, xUnit, FluentAssertions`

##### Descrição (História de Usuário)
> **Como** desenvolvedor responsável pela qualidade,  
> **Eu quero** testes unitários para a camada de serviços e validações de domínio no padrão AAA,  
> **Para que** alterações no código não causem regressão nas regras de negócio de zeladoria.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Projeto `ZelaFix.Tests` referenciando xUnit e Moq.
- [ ] Testes cobrindo casos positivos (alerta emitido com sucesso) e negativos (dados inválidos).
- [ ] Bloco de testes com comentários explícitos `// Arrange`, `// Act` e `// Assert`.