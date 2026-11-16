# 📋 Backlog Master Azure Boards — Global Solution 2026/2: DevOps Tools & Cloud Computing

> **Projeto Integrado:** ZelaFix — Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  
> **Disciplina:** DevOps Tools & Cloud Computing (FIAP — 2TDSPG)  
> **Repositório GitHub:** [Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing)  
> **API em Produção (Azure Web App):** [https://app-zelafix.azurewebsites.net](https://app-zelafix.azurewebsites.net)  
> **Worker em Produção (Azure Web App):** [https://app-zelafix-worker.azurewebsites.net](https://app-zelafix-worker.azurewebsites.net)  
> **Organização / Projeto Azure DevOps:** `ZelaFixGS` / `ZelaFix`  
> **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`  
> **Tag Oficial:** `DevOps`  
> **Responsible Owner:** `RM564836@fiap.com.br` (Milton Jakson de Sousa Marcelino)  
> **Epic Principal:** `[EPIC] DevOps Tools & Cloud Computing: Infraestrutura em Nuvem Azure, Containerização Docker e Esteira de CI/CD` (**AB#48**)  
> **Start Date:** `2026-11-04`  
> **Target Date:** `2026-11-19`  
> **Padrão:** Azure Boards (Scrum Process: Epic ➔ Feature ➔ PBI)  
> **Diretrizes Estratégicas:** Infraestrutura em nuvem **Microsoft Azure** provisionada de forma declarativa e idempotente via **Azure CLI** (`scripts/script-provisionamento.sh`) utilizando App Service Plan Linux `F1` Free Tier compartilhado para API REST (`app-zelafix`, porta `8080`) e Worker Assíncrono (`app-zelafix-worker`, porta `8081`), **Provedor de LLM Multimodal** (via `AI_MODEL`), mensageria TLS via **CloudAMQP** (`RABBITMQ_URI`), banco **Oracle 19c** (`scripts/script-bd.sql` com 13 tabelas 3FN + `auditoria_dml_chamado`), **Dockerfiles multi-stage** non-root e esteira CI/CD multi-service no **Azure Pipelines** (`azure-pipelines.yml`) executando **211 testes automatizados JUnit 5**.

---

## 👥 Integrantes do Grupo (Ordem Alfabética Estrita)

| Integrante | RM | Turma |
| :--- | :---: | :---: |
| **Enzo Okuizumi Miranda de Souza** | **561432** | 2TDSPG |
| **Gustavo Keiji Okada** | **563428** | 2TDSPG |
| **Lucas Barros Gouveia** | **566422** | 2TDSPG |
| **Luna de Carvalho Guimarães** | **562290** | 2TDSPG |
| **Milton Jakson de Sousa Marcelino** | **564836** | 2TDSPG |

---

## 🌳 1. Estrutura Hierárquica no Azure Boards

```text
📌 [EPIC] DevOps Tools & Cloud Computing: Infraestrutura em Nuvem Azure, Containerização Docker e Esteira de CI/CD [AB#48]
│
├── 🏆 [FEATURE 01] Empacotamento Java 21, Dockerfiles Multi-Stage e Mensageria Gerenciada (CloudAMQP) [AB#49]
│   ├── 🔹 [PBI-01] Criação de Dockerfiles Multi-Stage Seguros e Otimizados (API e Worker) [AB#50] (3 pts)
│   └── 🔹 [PBI-02] Integração da Mensageria RabbitMQ Online via CloudAMQP (TLS AMQPS) [AB#51] (3 pts)
│
├── 🏆 [FEATURE 02] Infraestrutura como Código (IaC), Serviços de IA Multimodal, Banco Oracle 19c e DevSecOps [AB#52]
│   ├── 🔹 [PBI-03] Provisionamento IaC via Azure CLI (App Service Plan F1, Web Apps e Serviços de IA Multimodal) [AB#53] (5 pts)
│   ├── 🔹 [PBI-04] DevSecOps: Isolamento de Variáveis Sensíveis (.env/AppSettings) e Limpeza de Hardcodes [AB#54] (3 pts)
│   └── 🔹 [PBI-05] Script DDL Oracle 19c em Nuvem (13 Tabelas 3FN, Auditoria DML e Alinhamento Flyway) [AB#191] (3 pts)
│
└── 🏆 [FEATURE 03] Automação de Pipelines CI/CD (Azure Pipelines), Diagrama Draw.io e Documentação [AB#55]
    ├── 🔹 [PBI-06] Esteira CI/CD Multi-Service no Azure Pipelines (Build Gradle, 211 Testes JUnit e Deploy API + Worker) [AB#56] (5 pts)
    └── 🔹 [PBI-07] Diagrama Arquitetural Draw.io, Documentação Operacional (README.md) e Contratos de Entrega [AB#57] (3 pts)
```

---

## 📊 2. Tabela Resumo do Backlog & Rastreabilidade

| Feature Pai | ID do PBI | Título do Item de Backlog (PBI) | ID Azure Boards | Story Points | Prioridade | Business Value | Commits | Status |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Feature 01** `[AB#49]` | **PBI-01** | Criação de Dockerfiles Multi-Stage Seguros e Otimizados (API e Worker) | **#50** | 3 pts | 1 - Critical | 100 | 2 | Done |
| | **PBI-02** | Integração da Mensageria RabbitMQ Online via CloudAMQP (TLS AMQPS) | **#51** | 3 pts | 1 - Critical | 100 | 3 | Done |
| **Feature 02** `[AB#52]` | **PBI-03** | Provisionamento IaC via Azure CLI (App Service Plan F1, Web Apps e Serviços de IA Multimodal) | **#53** | 5 pts | 1 - Critical | 100 | 4 | Done |
| | **PBI-04** | DevSecOps: Isolamento de Variáveis Sensíveis (`.env`/AppSettings) e Limpeza de Hardcodes | **#54** | 3 pts | 1 - Critical | 100 | 3 | Done |
| | **PBI-05** | Script DDL Oracle 19c em Nuvem (13 Tabelas 3FN, Auditoria DML e Alinhamento Flyway) | **#191** | 3 pts | 1 - Critical | 100 | 1 | Done |
| **Feature 03** `[AB#55]` | **PBI-06** | Esteira CI/CD Multi-Service no Azure Pipelines (Build Gradle, 211 Testes JUnit e Deploy API + Worker) | **#56** | 5 pts | 1 - Critical | 100 | 2 | Done |
| | **PBI-07** | Diagrama Arquitetural Draw.io, Documentação Operacional (`README.md`) e Contratos de Entrega | **#57** | 3 pts | 2 - High | 80 | 6 | Done |
| **TOTAL CONSOLIDADO** | **3 Features** | **7 PBIs (11 Work Items no Azure Boards)** | **`#48`..`#57`, `#191`** | **25 pts** | — | — | **22 commits** | **100% Sincronizado** |

---

## 📦 3. Detalhamento dos Itens de Trabalho (Épico, Features e PBIs)

---

### 🏛️ ÉPICO

* **Work Item Type:** `Epic`
* **Azure Boards ID:** `#48`
* **Title:** `[EPIC] DevOps Tools & Cloud Computing: Infraestrutura em Nuvem Azure, Containerização Docker e Esteira de CI/CD`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DevOps`
* **Assigned To:** `RM564836@fiap.com.br`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `25`
* **Business Value:** `100`
* **Description:** Implementação completa da cultura DevOps, Infraestrutura como Código (IaC) e arquitetura em nuvem Microsoft Azure para o ecossistema ZelaFix, contemplando Dockerfiles multi-stage non-root para Java 21 (`dockerfiles/Dockerfile.api` e `dockerfiles/Dockerfile.worker`), mensageria TLS gerenciada via CloudAMQP (`RABBITMQ_URI`), provisionamento idempotente via Azure CLI (`scripts/script-provisionamento.sh`) incluindo App Service Plan Linux F1, Web Apps (API + Worker) e Serviços de IA Multimodal, DDL Oracle 19c em 3FN (`scripts/script-bd.sql`), isolamento DevSecOps de credenciais e esteira CI/CD multi-service no Azure Pipelines (`azure-pipelines.yml`) com 211 testes JUnit 5.
* **Acceptance Criteria:**
  - [x] Dockerfiles multi-stage (`Dockerfile.api` e `Dockerfile.worker`) utilizando `gradle:8.10-jdk21-alpine` + `eclipse-temurin:21-jre-alpine`, usuário não-root (`appuser`) e geração de chaves RSA 2048-bit.
  - [x] Mensageria CloudAMQP (`amqps://`) configurada via `SPRING_RABBITMQ_ADDRESSES` com desacoplamento total entre Worker e Oracle DB.
  - [x] Script IaC `scripts/script-provisionamento.sh` idempotente provisionando `rg-zelafix`, `asp-zelafix` (F1 Linux), Web Apps `app-zelafix` e `app-zelafix-worker` e Serviços de IA Multimodal (deployment multimodal).
  - [x] Script DDL `scripts/script-bd.sql` alinhado às 13 tabelas 3FN + `auditoria_dml_chamado` no Oracle 19c e migrations Flyway (`V1`, `V2`, `V3`).
  - [x] Esteira CI/CD `azure-pipelines.yml` executando build Gradle multi-project, 211 testes JUnit 5 (`181` API + `30` Worker) e deploy contínuo nos dois Azure Web Apps, documentada com diagrama Draw.io.

---

### 🏆 [FEATURE 01] Empacotamento Java 21, Dockerfiles Multi-Stage e Mensageria Gerenciada (CloudAMQP)

* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#49`
* **Parent:** `[EPIC] DevOps Tools & Cloud Computing: Infraestrutura em Nuvem Azure, Containerização Docker e Esteira de CI/CD` (`#48`)
* **Title:** `[FEATURE 01] Empacotamento Java 21, Dockerfiles Multi-Stage e Mensageria Gerenciada (CloudAMQP)`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DevOps`
* **Assigned To:** `RM564836@fiap.com.br`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-12`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** Padronização do empacotamento em containers Docker multi-stage com Java 21 LTS para os microsserviços ZelaFix (API REST e Worker Assíncrono) e adoção de mensageria gerenciada CloudAMQP sobre TLS (`amqps://`), garantindo portabilidade, segurança non-root e desacoplamento entre a API e o processamento assíncrono de IA.
* **Acceptance Criteria:**
  - [x] Pastas oficiais `/dockerfiles` e `/scripts` estruturadas conforme rubrica de entrega.
  - [x] Dockerfiles multi-stage determinísticos com `gradle:8.10-jdk21-alpine` no build e `eclipse-temurin:21-jre-alpine` no runtime com `appuser`.
  - [x] Mensageria RabbitMQ operada em nuvem via CloudAMQP (`RABBITMQ_URI` / `SPRING_RABBITMQ_ADDRESSES`) sem dependência de container ACI local.

---

#### 🔹 [PBI-01] Criação de Dockerfiles Multi-Stage Seguros e Otimizados (API e Worker)

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#50`
* **Parent Feature:** `[FEATURE 01] Empacotamento Java 21, Dockerfiles Multi-Stage e Mensageria Gerenciada (CloudAMQP)` (`#49`)
* **Title:** `[PBI-01] Criação de Dockerfiles Multi-Stage Seguros e Otimizados (API e Worker)`
* **State:** `Done`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DevOps`
* **Assigned To:** `RM564836@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`
* **Commits Vinculados:** `ecf0dd5`, `7bc8cbd`

##### Descrição (História de Usuário)
> **Como** engenheiro DevOps,  
> **Eu quero** criar Dockerfiles multi-stage determinísticos na pasta `dockerfiles/` para a API REST (`Dockerfile.api`) e para o Worker Assíncrono (`Dockerfile.worker`),  
> **Para que** as imagens Java 21 sejam enxutas, seguras com usuário não-root (`appuser`), timezone `America/Sao_Paulo` e chaves RSA geradas em tempo de build.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Stage 1 (`gradle:8.10-jdk21-alpine`) com cache de dependências multi-project, geração de chaves RSA 2048-bit via `openssl` em `zelafix-api/src/main/resources/keys/` e geração de `bootJar`.
- [x] Stage 2 (`eclipse-temurin:21-jre-alpine`) com instalação de `tzdata` (`America/Sao_Paulo`) e criação de `appgroup` / `appuser` sem privilégios de root.
- [x] Exposição correta das portas `8080` (`Dockerfile.api`) e `8081` (`Dockerfile.worker`) com `ENTRYPOINT` configurado para JVM Java 21.
- [x] Padronização da estrutura de pastas `/dockerfiles` e `/scripts` idêntica ao repositório `Java-Advanced`.

---

#### 🔹 [PBI-02] Integração da Mensageria RabbitMQ Online via CloudAMQP (TLS AMQPS)

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#51`
* **Parent Feature:** `[FEATURE 01] Empacotamento Java 21, Dockerfiles Multi-Stage e Mensageria Gerenciada (CloudAMQP)` (`#49`)
* **Title:** `[PBI-02] Integração da Mensageria RabbitMQ Online via CloudAMQP (TLS AMQPS)`
* **State:** `Done`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DevOps`
* **Assigned To:** `RM564836@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`
* **Commits Vinculados:** `4ea9b75`, `7a7355f`, `83c015e`

##### Descrição (História de Usuário)
> **Como** arquiteto de sistemas distribuídos,  
> **Eu quero** conectar a API e o Worker ao broker RabbitMQ gerenciado no CloudAMQP (plano gratuito Little Lemur) utilizando TLS (`amqps://`) e remover o provisionamento local/ACI de RabbitMQ,  
> **Para que** os eventos de triagem e votos comunitários trafeguem com criptografia e alta disponibilidade sem custos ou falhas de container em nuvem.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Variável `RABBITMQ_URI` (`amqps://USER:SENHA@HOST/VHOST`) injetada como `SPRING_RABBITMQ_ADDRESSES` nos App Settings da API e do Worker e na esteira CI.
- [x] Remoção do provisionamento legado de Azure Container Instances (ACI) no script IaC e alinhamento de health check resiliente do RabbitMQ no Worker.
- [x] Garantia arquitetural de que o Worker permanece 100% desacoplado do banco Oracle, comunicando-se apenas via CloudAMQP e Provedor de LLM Multimodal.

---

### 🏆 [FEATURE 02] Infraestrutura como Código (IaC), Serviços de IA Multimodal, Banco Oracle 19c e DevSecOps

* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#52`
* **Parent:** `[EPIC] DevOps Tools & Cloud Computing: Infraestrutura em Nuvem Azure, Containerização Docker e Esteira de CI/CD` (`#48`)
* **Title:** `[FEATURE 02] Infraestrutura como Código (IaC), Serviços de IA Multimodal, Banco Oracle 19c e DevSecOps`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DevOps`
* **Assigned To:** `RM564836@fiap.com.br`
* **Start Date:** `2026-11-09`
* **Target Date:** `2026-11-14`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `11`
* **Business Value:** `100`
* **Description:** Provisionamento declarativo e idempotente da infraestrutura em nuvem no Microsoft Azure via Azure CLI (`scripts/script-provisionamento.sh`), incluindo Resource Group `rg-zelafix`, App Service Plan Linux `F1`, Web Apps Java 21 (API e Worker), serviço cognitivo de IA Multimodal, governança DevSecOps de segredos e script DDL oficial Oracle 19c (`scripts/script-bd.sql`).
* **Acceptance Criteria:**
  - [x] Script `scripts/script-provisionamento.sh` idempotente (com suporte a `--clean`) criando Resource Group, Plan `F1`, Serviço cognitivo (AIServices S0 com deployment multimodal) e dois Web Apps Linux Java 21.
  - [x] Segredos isolados em `.env` (protegido via `.gitignore`), `.env.example` documentado e App Settings injetados sem credenciais ou URLs hardcoded no repositório.
  - [x] Script `scripts/script-bd.sql` contendo DDL completo Oracle 19c com 13 tabelas em 3FN + `auditoria_dml_chamado` alinhado ao Flyway.

---

#### 🔹 [PBI-03] Provisionamento IaC via Azure CLI (App Service Plan F1, Web Apps e Serviços de IA Multimodal)

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#53`
* **Parent Feature:** `[FEATURE 02] Infraestrutura como Código (IaC), Serviços de IA Multimodal, Banco Oracle 19c e DevSecOps` (`#52`)
* **Title:** `[PBI-03] Provisionamento IaC via Azure CLI (App Service Plan F1, Web Apps e Serviços de IA Multimodal)`
* **State:** `Done`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DevOps`
* **Assigned To:** `RM564836@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `5`
* **Business Value:** `100`
* **Commits Vinculados:** `0e19e6a`, `4385ad2`, `4f8f830`, `ee58679`, `d802cfb`, `7c11343`, `23a134d`

##### Descrição (História de Usuário)
> **Como** arquiteto de nuvem,  
> **Eu quero** automatizar o provisionamento do Resource Group, App Service Plan Linux F1, Azure Web Apps (API e Worker) e serviço de IA multimodal (deployment do modelo multimodal via variáveis de ambiente) via Azure CLI em `scripts/script-provisionamento.sh`,  
> **Para que** toda a infraestrutura da solução seja reproduzível, idempotente, otimizada em memória e a custo zero no Free Tier.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Criação idempotente de `rg-zelafix` (`eastus`), plano Linux `asp-zelafix` (`SKU F1`) e flag opcional `--clean` para reconstrução limpa.
- [x] Provisionamento dos Web Apps `app-zelafix` (API porta `8080`) e `app-zelafix-worker` (Worker porta `8081`) com runtime `JAVA|21-java21`, startup commands customizados e `JAVA_OPTS="-Xms256m -Xmx512m -XX:+UseG1GC -Djava.security.egd=file:/dev/./urandom"`.
- [x] Provisionamento do serviço de IA (kind `AIServices`, SKU `S0`) e deployment do modelo multimodal configurados via Azure CLI idempotente, obtendo `AI_API_KEY` dinamicamente.

---

#### 🔹 [PBI-04] DevSecOps: Isolamento de Variáveis Sensíveis (.env/AppSettings) e Limpeza de Hardcodes

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#54`
* **Parent Feature:** `[FEATURE 02] Infraestrutura como Código (IaC), Serviços de IA Multimodal, Banco Oracle 19c e DevSecOps` (`#52`)
* **Title:** `[PBI-04] DevSecOps: Isolamento de Variáveis Sensíveis (.env/AppSettings) e Limpeza de Hardcodes`
* **State:** `Done`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DevOps`
* **Assigned To:** `RM564836@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`
* **Commits Vinculados:** `a28f045`, `046ff1c`, `e0ff9ac`

##### Descrição (História de Usuário)
> **Como** especialista em DevSecOps,  
> **Eu quero** isolar todas as credenciais (Oracle FIAP, CloudAMQP e Provedor de IA) em arquivos `.env` ignorados pelo Git, documentar o contrato em `.env.example` e limpar variáveis obsoletas ou URLs hardcoded,  
> **Para que** nenhum segredo ou parâmetro redundante seja exposto no repositório público e os Application Settings dos Web Apps reflitam apenas a configuração ativa.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `.gitignore` bloqueando `.env` e `.env.example` fornecendo template completo para Azure, Oracle (`ORACLE_URL`, `ORACLE_USER`, `ORACLE_PASSWORD`), `RABBITMQ_URI` e Provedor de IA (`AI_ACCOUNT_NAME`, `AI_BASE_URL`, `AI_API_KEY`, `AI_MODEL`).
- [x] Injeção automatizada das configurações seguras via `az webapp config appsettings set` na API e no Worker, validando presença obrigatória de `RABBITMQ_URI`.
- [x] Limpeza de variáveis obsoletas (`FLYWAY_ENABLED`, `JPA_DDL_AUTO`, `PORT`, `WORKER_PORT`, `WORKER_URL`, `RABBITMQ_CONCURRENCY`) e remoção de URL hardcoded da API de IA em `.env.example`, `azure-pipelines.yml` e `scripts/script-provisionamento.sh`.

---

#### 🔹 [PBI-05] Script DDL Oracle 19c em Nuvem (13 Tabelas 3FN, Auditoria DML e Alinhamento Flyway)

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#191`
* **Parent Feature:** `[FEATURE 02] Infraestrutura como Código (IaC), Serviços de IA Multimodal, Banco Oracle 19c e DevSecOps` (`#52`)
* **Title:** `[PBI-05] Script DDL Oracle 19c em Nuvem (13 Tabelas 3FN, Auditoria DML e Alinhamento Flyway)`
* **State:** `Done`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DevOps`
* **Assigned To:** `RM564836@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`
* **Commits Vinculados:** `d9c87a6`, `15c98e5`

##### Descrição (História de Usuário)
> **Como** engenheiro de banco de dados e infraestrutura,  
> **Eu quero** disponibilizar o script DDL oficial `scripts/script-bd.sql` idempotente para o Oracle Database 19c da FIAP com as 13 tabelas normalizadas em 3FN e tabela de auditoria DML,  
> **Para que** o esquema em nuvem possa ser provisionado de forma consistente e 100% compatível com as migrations Flyway (`V1`, `V2`, `V3`) executadas pela API Spring Boot.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Bloco de limpeza segura e idempotente (`DROP TABLE ... CASCADE CONSTRAINTS PURGE` e remoção de packages PL/SQL preexistentes).
- [x] Criação das 13 tabelas 3FN fiéis a `citizenTech.ddl` (`estado`, `cidade`, `bairro`, `endereco`, `usuario`, `telefone`, `categoria`, `status`, `prioridade`, `orgao_governo`, `chamado`, `hist_chamado`, `voto_chamado`) mais tabela `auditoria_dml_chamado`.
- [x] Constraints, chaves primárias/estrangeiras e alinhamento integral com `jdbc:oracle:thin:@//oracle.fiap.com.br:1521/orcl` e migrations Flyway da API.

---

### 🏆 [FEATURE 03] Automação de Pipelines CI/CD (Azure Pipelines), Diagrama Draw.io e Documentação

* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#55`
* **Parent:** `[EPIC] DevOps Tools & Cloud Computing: Infraestrutura em Nuvem Azure, Containerização Docker e Esteira de CI/CD` (`#48`)
* **Title:** `[FEATURE 03] Automação de Pipelines CI/CD (Azure Pipelines), Diagrama Draw.io e Documentação`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DevOps`
* **Assigned To:** `RM564836@fiap.com.br`
* **Start Date:** `2026-11-10`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `8`
* **Business Value:** `100`
* **Description:** Automação de integração e entrega contínua multi-service via Azure Pipelines (`azure-pipelines.yml`) com compilação Gradle, validação de 211 testes JUnit 5, publicação de artefatos e deploy nos Web Apps da API e do Worker, acompanhada de diagrama arquitetural em Draw.io e documentação operacional completa no `README.md`.
* **Acceptance Criteria:**
  - [x] Pipeline `azure-pipelines.yml` ativa com estágios `Build` (CI) e `Deploy` (CD) para `main` e `develop`.
  - [x] Relatório JUnit publicado com `failTaskOnFailedTests: true` validando os 211 testes (`181` API + `30` Worker) antes do deploy.
  - [x] Diagrama `docs/gs2-zelafix-diagrama.drawio` / `.png` e `README.md` atualizados com arquitetura Azure, 13 tabelas, 211 testes, URLs ativas e payloads CRUD.

---

#### 🔹 [PBI-06] Esteira CI/CD Multi-Service no Azure Pipelines (Build Gradle, 211 Testes JUnit e Deploy API + Worker)

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#56`
* **Parent Feature:** `[FEATURE 03] Automação de Pipelines CI/CD (Azure Pipelines), Diagrama Draw.io e Documentação` (`#55`)
* **Title:** `[PBI-06] Esteira CI/CD Multi-Service no Azure Pipelines (Build Gradle, 211 Testes JUnit e Deploy API + Worker)`
* **State:** `Done`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DevOps`
* **Assigned To:** `RM564836@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `5`
* **Business Value:** `100`
* **Commits Vinculados:** `52c0476`, `f6dfa88`, `990f81a`

##### Descrição (História de Usuário)
> **Como** equipe de engenharia ZelaFix,  
> **Eu quero** automatizar o build Gradle multi-project, a execução dos 211 testes JUnit e o deploy simultâneo da API e do Worker no Azure App Service via `azure-pipelines.yml`,  
> **Para que** cada alteração integrada nas branches `main` e `develop` seja validada e publicada automaticamente em produção sem intervenção manual.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Estágio `Build` executando `gradlew.bat clean test bootJar --no-daemon` com JDK 21 e variáveis mascaradas (`ORACLE_*`, `RABBITMQ_URI`, `AI_MODEL`).
- [x] Publicação dos relatórios XML de testes JUnit via `PublishTestResults@2` (`failTaskOnFailedTests: true`) e empacotamento de `zelafix-api.jar`, `app.jar` e `zelafix-worker.jar` no artefato `drop`.
- [x] Estágio `Deploy` utilizando Service Connection `ZelaFix-Connection` e tarefas `AzureWebApp@1` para publicar `app-zelafix` (porta `8080`) e `app-zelafix-worker` (porta `8081`).

---

#### 🔹 [PBI-07] Diagrama Arquitetural Draw.io, Documentação Operacional (README.md) e Contratos de Entrega

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#57`
* **Parent Feature:** `[FEATURE 03] Automação de Pipelines CI/CD (Azure Pipelines), Diagrama Draw.io e Documentação` (`#55`)
* **Title:** `[PBI-07] Diagrama Arquitetural Draw.io, Documentação Operacional (README.md) e Contratos de Entrega`
* **State:** `Done`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`
* **Tags:** `DevOps`
* **Assigned To:** `RM564836@fiap.com.br`
* **Priority:** `2 - High`
* **Effort (Story Points):** `3`
* **Business Value:** `80`
* **Commits Vinculados:** `3924462`, `e45cb07`, `cc4081b`, `5c22825`, `d70063b`, `0c7ff10`, `0bb681e`, `1da20c0`, `094f8ce`, `2d9193a`

##### Descrição (História de Usuário)
> **Como** avaliador da FIAP e mantenedor do projeto,  
> **Eu quero** um `README.md` corporativo acompanhado do diagrama arquitetural em Draw.io (`docs/gs2-zelafix-diagrama.drawio` e `.png`), links de produção e payloads JSON de teste,  
> **Para que** toda a arquitetura em nuvem Azure, as 10 etapas da esteira CI/CD, o modelo de dados e os endpoints possam ser auditados e homologados com clareza.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Diagrama `docs/gs2-zelafix-diagrama.drawio` e imagem renderizada `docs/gs2-zelafix-diagrama.png` incorporada no `README.md` retratando GitHub Actions, Azure Repos, Azure Pipelines, CloudAMQP TLS, Oracle 19c e Provedor de LLM Multimodal (`AI_MODEL`).
- [x] `README.md` atualizado com links ativos (`app-zelafix`, `app-zelafix-worker`, Swagger UI, Actuator Health, OpenAPI), justificativa do plano F1, 13 tabelas 3FN, 211 testes e governança do Azure DevOps.
- [x] Payloads JSON de exemplo atualizados para `POST /login`, `POST/GET/PUT/DELETE /usuarios` e `POST/GET/PUT/DELETE /chamados` (`multipart/form-data` com `DeferredResult` e `/apoiar`).

---

## 🔗 4. Matriz de Rastreabilidade de Commits (GitHub ↔ Azure Boards)

| Commit | Data | Mensagem | Work Item (PBI) |
| :--- | :---: | :--- | :---: |
| [`3924462`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/3924462) | 2026-11-04 | `Initial commit` | **PBI-07** (`#57`) |
| [`0e19e6a`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/0e19e6a) | 2026-11-10 | `feat(devops): adicionar esteira ci/cd multi-service, script de provisionamento azure cli e documentacao` | **PBI-03** (`#53`) |
| [`a28f045`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/a28f045) | 2026-11-11 | `feat(devops): atualizar credenciais oracle fiap rm566422 e incluir branch develop na esteira` | **PBI-04** (`#54`) |
| [`046ff1c`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/046ff1c) | 2026-11-11 | `feat(devops): isolar variaveis sensiveis em .env, atualizar docs e script de provisionamento idempotente` | **PBI-04** (`#54`) |
| [`4ea9b75`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/4ea9b75) | 2026-11-11 | `fix(iac): adicionar flag de saude resiliente do rabbitmq no worker` | **PBI-02** (`#51`) |
| [`ecf0dd5`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/ecf0dd5) | 2026-11-11 | `feat(devops): provisionamento ACI RabbitMQ, conformidade de rubrica com pastas /scripts e /dockerfiles e variáveis seguras` | **PBI-01** (`#50`) |
| [`4385ad2`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/4385ad2) | 2026-11-11 | `chore(devops): script de provisionamento apenas em /scripts, Flyway habilitado e ACI opcional` | **PBI-03** (`#53`) |
| [`7a7355f`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/7a7355f) | 2026-11-11 | `chore(devops): CloudAMQP via RABBITMQ_URI, remove ACI do provisionamento` | **PBI-02** (`#51`) |
| [`83c015e`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/83c015e) | 2026-11-11 | `chore(devops): alinhar JPA_DDL_AUTO=none e remover restos locais` | **PBI-02** (`#51`) |
| [`52c0476`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/52c0476) | 2026-11-11 | `fix(ci): passar AI_BASE_URL com /v1 na esteira de build` | **PBI-06** (`#56`) |
| [`f6dfa88`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/f6dfa88) | 2026-11-11 | `fix(ci): evitar rate limit 429 de IA nos testes unitários da esteira` | **PBI-06** (`#56`) |
| [`e45cb07`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/e45cb07) | 2026-11-12 | `docs: atualizar README com arquitetura multi-service, CloudAMQP, Dockerfiles e CI/CD` | **PBI-07** (`#57`) |
| [`cc4081b`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/cc4081b) | 2026-11-12 | `docs: padronizar status de chamados e modelo LLM Multimodal Vision no README e diagramas` | **PBI-07** (`#57`) |
| [`5c22825`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/5c22825) | 2026-11-12 | `docs: substituir diagrama ascii pela imagem renderizada do Draw.io no README` | **PBI-07** (`#57`) |
| [`7bc8cbd`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/7bc8cbd) | 2026-11-12 | `refactor(docker): atualizar Dockerfile.api e Dockerfile.worker para multi-stage build profissional idêntico ao repositório Java` | **PBI-01** (`#50`) |
| [`4f8f830`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/4f8f830) | 2026-11-12 | `feat: atualizando script provisionamento` | **PBI-03** (`#53`) |
| [`ee58679`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/ee58679) | 2026-11-13 | `chore(devops): atualizar scripts, diagrama e README para servicos de IA multimodal` | **PBI-03** (`#53`) |
| [`e0ff9ac`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/e0ff9ac) | 2026-11-14 | `chore(devops): limpar variaveis obsoletas e remover URL hardcoded da API de IA` | **PBI-04** (`#54`) |
| [`d70063b`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/d70063b) | 2026-11-14 | `docs(devops): atualizar README com 13 tabelas, 211 testes e contratos atuais` | **PBI-07** (`#57`) |
| [`d9c87a6`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/d9c87a6) | 2026-11-14 | `feat: atualizando script banco` | **PBI-05** (`#191`) |
| [`0c7ff10`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/0c7ff10) | 2026-11-15 | `docs: generalizar especificacoes e variaveis do modelo de IA no README e env.example` | **PBI-07** (`#57`) |
| [`0bb681e`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/0bb681e) | 2026-11-15 | `docs(devops): generalizar servicos de IA e desvincular modelos especificos de IaC e diagramas` | **PBI-07** (`#57`) |
| [`d802cfb`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/d802cfb) | 2026-11-15 | `refactor(diagram,script): atualizar box de IA no diagrama e desacoplar script de provisionamento de servico de IA especifico` | **PBI-03** (`#53`) |
| [`7c11343`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/7c11343) | 2026-11-15 | `refactor(infra): remover sufixo RM dos Web Apps app-zelafix e app-zelafix-worker` | **PBI-03** (`#53`) |
| [`15c98e5`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/15c98e5) | 2026-11-15 | `feat: atualizando script bd` | **PBI-05** (`#191`) |
| [`990f81a`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/990f81a) | 2026-11-15 | `ci: adiciona AI_BASE_URL e AI_API_KEY no job de build da pipeline` | **PBI-06** (`#56`) |
| [`1da20c0`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/1da20c0) | 2026-11-15 | `feat: atualizando imagens drawio` | **PBI-07** (`#57`) |
| [`094f8ce`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/094f8ce) | 2026-11-15 | `docs(devops): adicionar link para a documentacao oficial em PDF` | **PBI-07** (`#57`) |
| [`2d9193a`](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing/commit/2d9193a) | 2026-11-15 | `docs: atualizar diagrama arquitetural com as 4 filas RabbitMQ e documentacao PDF` | **PBI-07** (`#57`) |
