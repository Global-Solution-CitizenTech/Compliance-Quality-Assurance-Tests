# 📋 Backlog Master Azure Boards — Global Solution 2026/2: DevOps Tools & Cloud Computing

> **Projeto Integrado:** ZelaFix — Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  
> **Disciplina:** DevOps Tools & Cloud Computing (FIAP — 2TDSPG)  
> **Epic Principal:** `[EPIC] GS 2026/2 - DevOps Tools & Cloud Computing: Infraestrutura em Nuvem Azure, Containerização Docker e Esteira de CI/CD`  
> **Start Date:** `2026-11-04`  
> **Target Date:** `2026-11-19`  
> **Padrão:** Azure Boards (Scrum Process: Epic ➔ Feature ➔ PBI ➔ Task)  
> **Diretrizes Estratégicas:** Containerização profissional dos microsserviços do ZelaFix utilizando Dockerfiles multi-stage otimizados com usuário sem privilégios (non-root), orquestração local via Docker Compose, provisionamento automatizado de infraestrutura em nuvem na Microsoft Azure (ACR e App Services / ACI) via scripts IaC/CLI e automação completa de esteira de integração e entrega contínua (CI/CD) via GitHub Actions.

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
[EPIC] GS 2026/2 - DevOps Tools & Cloud Computing: Infraestrutura em Nuvem Azure, Containerização Docker e Esteira de CI/CD
│
├── 🏆 [FEATURE 01] Containerização Multi-Container com Docker e Docker Compose
│   ├── 📄 [PBI-01] Criação de Dockerfiles Multi-Stage Seguros e Otimizados (3 pts)
│   └── 📄 [PBI-02] Orquestração do Ecossistema Integrado via Docker Compose (3 pts)
│
├── 🏆 [FEATURE 02] Infraestrutura como Código (IaC) e Provisionamento na Nuvem Azure
│   ├── 📄 [PBI-03] Provisionamento do Azure Container Registry (ACR) e App Services (3 pts)
│   └── 📄 [PBI-04] Configuração de Variáveis de Ambiente Seguras e Network Security (2 pts)
│
└── 🏆 [FEATURE 03] Automação de Pipelines CI/CD via GitHub Actions e Monitoramento
    ├── 📄 [PBI-05] Esteira de CI/CD com Build, Testes Automatizados e Deploy no Azure (3 pts)
    └── 📄 [PBI-06] Documentação Operacional de Deploy e Métricas de Disponibilidade (2 pts)
```

---

## 📊 2. Tabela Resumo do Backlog

| Feature Pai | ID do PBI | Título do Item de Backlog (PBI) | Story Points | Prioridade | Horas Estimadas |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **[FEATURE 01] Docker & Compose** | **PBI-01** | Criação de Dockerfiles Multi-Stage Seguros e Otimizados | 3 pts | 1 - Critical | 7.0h |
| | **PBI-02** | Orquestração do Ecossistema Integrado via Docker Compose | 3 pts | 1 - Critical | 6.5h |
| **[FEATURE 02] Cloud Azure** | **PBI-03** | Provisionamento do Azure Container Registry (ACR) e App Services | 3 pts | 1 - Critical | 8.0h |
| | **PBI-04** | Configuração de Variáveis de Ambiente Seguras e Network Security | 2 pts | 1 - Critical | 5.0h |
| **[FEATURE 03] CI/CD & Deploy** | **PBI-05** | Esteira de CI/CD com Build, Testes Automatizados e Deploy no Azure | 3 pts | 1 - Critical | 8.5h |
| | **PBI-06** | Documentação Operacional de Deploy e Métricas de Disponibilidade | 2 pts | 2 - High | 4.0h |
| **TOTAL CONSOLIDADO** | **3 Features** | **6 PBIs / 18 Child Tasks Técnicas** | **16 pts** | — | **39.0h** |

---

## 📦 3. Detalhamento dos Itens de Trabalho (Épico, Features, PBIs e Tasks)

---

### 🏛️ ÉPICO
* **Work Item Type:** `Epic`
* **Title:** `[EPIC] GS 2026/2 - DevOps Tools & Cloud Computing: Infraestrutura em Nuvem Azure, Containerização Docker e Esteira de CI/CD`
* **Tags:** `DevOps, ZelaFix, GlobalSolution2, Docker, Azure, CICD, GitHubActions`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `16`
* **Business Value:** `100`
* **Description:** Implementação da cultura DevOps e infraestrutura em nuvem para a plataforma ZelaFix, contemplando empacotamento em containers Docker, orquestração local de desenvolvimento, provisionamento na nuvem Microsoft Azure (ACR e Web Apps) e automação de entrega contínua com GitHub Actions.

---

### 🏆 [FEATURE 01] Containerização Multi-Container com Docker e Docker Compose
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] GS 2026/2 - DevOps Tools & Cloud Computing: Infraestrutura em Nuvem Azure, Containerização Docker e Esteira de CI/CD`
* **Title:** `[FEATURE 01] Containerização Multi-Container com Docker e Docker Compose`
* **Tags:** `DevOps, Docker, DockerCompose, Containers`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-10`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** Padronização dos ambientes de execução dos serviços através de containers Docker seguros e eficientes.
* **Acceptance Criteria:**
  - [x] Dockerfiles multi-stage construídos com imagem base slim/alpine.
  - [x] Configuração de usuário sem privilégios de root (`USER appuser`).
  - [x] Arquivo docker-compose.yml orquestrando API Java, Banco de Dados e serviços de IA.

#### 🔹 [PBI-01] Criação de Dockerfiles Multi-Stage Seguros e Otimizados
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Containerização Multi-Container com Docker e Docker Compose`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DevOps, Dockerfile, Security`

##### Descrição (História de Usuário)
> **Como** engenheiro DevOps,  
> **Eu quero** criar Dockerfiles multi-stage para os serviços Java, .NET e Python,  
> **Para que** as imagens finais de produção sejam leves e livres de vulnerabilidades com execução non-root.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Separação explícita entre estágios de build e runtime.
- [ ] Criação de grupo e usuário de sistema dedicado para execução.
- [ ] Geração de imagens com tamanho inferior a 250MB.
---

#### 🔹 [PBI-02] Orquestração do Ecossistema Integrado via Docker Compose
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Containerização Multi-Container com Docker e Docker Compose`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DevOps, DockerCompose, LocalEnv`

##### Descrição (História de Usuário)
> **Como** desenvolvedor do time ZelaFix,  
> **Eu quero** subir todo o ambiente de desenvolvimento (bancos, APIs e mensageria) com um único comando `docker compose up`,  
> **Para que** os testes de integração locais sejam ágeis e reprodutíveis.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Arquivo `docker-compose.yml` na raiz com redes e volumes nomeados.
- [ ] Health checks configurados para garantir dependências prontas antes do início dos serviços.
---

### 🏆 [FEATURE 02] Infraestrutura como Código (IaC) e Provisionamento na Nuvem Azure
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] GS 2026/2 - DevOps Tools & Cloud Computing: Infraestrutura em Nuvem Azure, Containerização Docker e Esteira de CI/CD`
* **Title:** `[FEATURE 02] Infraestrutura como Código (IaC) e Provisionamento na Nuvem Azure`
* **Tags:** `DevOps, Azure, Cloud, IaC, ACR`
* **Start Date:** `2026-11-09`
* **Target Date:** `2026-11-14`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `5`
* **Business Value:** `100`
* **Description:** Provisionamento da infraestrutura cloud no Microsoft Azure por meio de scripts IaC/CLI automatizados.
* **Acceptance Criteria:**
  - [x] Azure Container Registry (ACR) provisionado para armazenar as imagens oficiais.
  - [x] Azure App Service (Web App for Containers) ou ACI configurado para hospedagem pública.
  - [x] Credenciais sensíveis protegidas via GitHub Secrets e Azure Key Vault/AppSettings.

#### 🔹 [PBI-03] Provisionamento do Azure Container Registry (ACR) e App Services
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Infraestrutura como Código (IaC) e Provisionamento na Nuvem Azure`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DevOps, AzureCLI, ACR, WebApp`

##### Descrição (História de Usuário)
> **Como** arquiteto de nuvem,  
> **Eu quero** scripts automatizados do Azure CLI para criar o Resource Group, ACR e Web App,  
> **Para que** o provisionamento de recursos em nuvem seja auditável e reproduzível.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Script `deploy-azure.sh` executável criando os recursos na região East US / Brazil South.
- [ ] Atribuição de permissão AcrPull para o Web App autenticar no registro de containers.
---

#### 🔹 [PBI-04] Configuração de Variáveis de Ambiente Seguras e Network Security
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Infraestrutura como Código (IaC) e Provisionamento na Nuvem Azure`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `2`
* **Tags:** `DevOps, Security, Secrets`

##### Descrição (História de Usuário)
> **Como** oficial de segurança cibernética,  
> **Eu quero** que connection strings e senhas de banco sejam injetadas via Application Settings seguras no Azure,  
> **Para que** nenhuma credencial seja exposta no repositório de código aberto.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Variáveis `SPRING_DATASOURCE_URL`, `AZURE_DEVOPS_PAT` isoladas nos AppSettings.
- [ ] Proteção HTTPS forçada com redirecionamento de tráfego HTTP.
---

### 🏆 [FEATURE 03] Automação de Pipelines CI/CD via GitHub Actions e Monitoramento
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] GS 2026/2 - DevOps Tools & Cloud Computing: Infraestrutura em Nuvem Azure, Containerização Docker e Esteira de CI/CD`
* **Title:** `[FEATURE 03] Automação de Pipelines CI/CD via GitHub Actions e Monitoramento`
* **Tags:** `DevOps, GitHubActions, Pipeline, CICD`
* **Start Date:** `2026-11-12`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `5`
* **Business Value:** `100`
* **Description:** Pipeline de automação contínua disparada a cada push/PR na branch develop/main com testes, build e deploy.
* **Acceptance Criteria:**
  - [x] Pipeline `.github/workflows/deploy.yml` ativa no repositório.
  - [x] Execução de testes automatizados como gate obrigatório antes do deploy.
  - [x] Deploy contínuo da imagem docker no Azure Container Registry e restart do Web App.

#### 🔹 [PBI-05] Esteira de CI/CD com Build, Testes Automatizados e Deploy no Azure
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] Automação de Pipelines CI/CD via GitHub Actions e Monitoramento`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DevOps, GitHubActions, Workflow`

##### Descrição (História de Usuário)
> **Como** equipe de desenvolvimento ágil,  
> **Eu quero** que qualquer código mergeado passe automaticamente por testes de unidade e deploy no ambiente de produção,  
> **Para que** tenhamos entregas contínuas e seguras sem intervenção manual.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Workflow GitHub Actions com jobs de lint, test, build-and-push e deploy.
- [ ] Utilização de Secrets (`AZURE_CREDENTIALS`, `REGISTRY_USERNAME`, `REGISTRY_PASSWORD`).
- [ ] Notificação de status de pipeline no GitHub.
---

#### 🔹 [PBI-06] Documentação Operacional de Deploy e Métricas de Disponibilidade
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] Automação de Pipelines CI/CD via GitHub Actions e Monitoramento`
* **Priority:** `2 - High`
* **Effort (Story Points):** `2`
* **Tags:** `DevOps, Documentation, Metrics`

##### Descrição (História de Usuário)
> **Como** avaliador da FIAP,  
> **Eu quero** um README.md com o diagrama da arquitetura de nuvem, comandos de deploy e URLs ativas dos serviços,  
> **Para que** a infraestrutura possa ser homologada com facilidade.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] README.md contendo arquitetura em nuvem, passos de IaC e links de produção.
- [ ] Evidências de liveness e readiness comprovadas por curl e Swagger.