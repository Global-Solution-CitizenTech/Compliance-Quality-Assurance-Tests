# ☕ Backlog Master Azure Boards — Global Solution 2026/2: Java Advanced

> **Projeto Integrado:** ZelaFix — Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  
> **Disciplina:** Java Advanced (FIAP — 2TDSPG)  
> **Epic Principal:** `[EPIC] Java Advanced: Microsserviços com RabbitMQ, Spring AI e API RESTful Spring Boot Core` (AB#14)  
> **Responsável / Owner:** Enzo Okuizumi Miranda de Souza (`RM561432@fiap.com.br`)  
> **Start Date:** `2026-11-04`  
> **Target Date:** `2026-11-19`  
> **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`  
> **Padrão:** Azure Boards (Scrum Process: Epic ➔ Feature ➔ PBI)  
> **Opção Distribuída Escolhida:** **Opção A — Mensageria Assíncrona com RabbitMQ** (2 microsserviços autônomos: `zelafix-api` e `zelafix-worker`)  
> **Diretrizes Estratégicas:** Arquitetura distribuída de microsserviços em Java 21+ com Spring Boot 3+, estruturada em **Gradle Multi-Project** (`rootProject.name = 'zelafix-backend'`, `zelafix-api` e `zelafix-worker`), persistência relacional no Oracle Database 11g/19c com Spring Data JPA em 3FN (`citizenTech.ddl`), versionamento de schema com Flyway Migrations (V1, V2, V3), segurança stateless com Spring Security e par de chaves RSA Nimbus JWT, controle de acesso baseado em papéis (RBAC: CIDADAO, GESTOR e ADMIN), mensageria assíncrona gerenciada com RabbitMQ / CloudAMQP (Direct Exchange `zelafix.direct`), triagem inteligente de ocorrências multimodal com Spring AI (Groq Qwen 3.8 27B Vision com fallback heurístico), agregador de votos com buffer thread-safe (`ConcurrentHashMap` - Padrão Paredão), containerização otimizada com Docker multi-stage build (Temurin 21 alpine com usuário não-root `appuser:appgroup`), esteira de CI/CD automatizada no Azure DevOps (`azure-pipelines.yml`) com espelhamento contínuo GitHub Actions e proteção estrita de branch na main (`TF402455`) com Pull Requests de homologação.

---

## 👥 Integrantes do Grupo (Ordem Alfabética Estrita)

| Integrante | RM | Turma | Papel / Responsabilidade |
| :--- | :---: | :---: | :--- |
| **Enzo Okuizumi Miranda de Souza** | **561432** | 2TDSPG | **Java Advanced (Microsserviços, RabbitMQ, Spring AI) & Compliance** |
| **Gustavo Keiji Okada** | **563428** | 2TDSPG | Back-end .NET Enterprise & Minimal APIs |
| **Lucas Barros Gouveia** | **566422** | 2TDSPG | Database Modeling & Engenharia de Dados Oracle |
| **Luna de Carvalho Guimarães** | **562290** | 2TDSPG | Mobile Application Development (React Native / Expo) |
| **Milton Jakson de Sousa Marcelino** | **564836** | 2TDSPG | DevOps Tools, Cloud Computing & CI/CD Pipelines |

---

## 🏛️ 1. Estrutura Hierárquica no Azure Boards

```text
[EPIC] Java Advanced: Microsserviços com RabbitMQ, Spring AI e API RESTful Spring Boot Core [AB#14]
│
├── 🏆 [FEATURE 01] Modelagem de Domínio JPA 3FN, Migrations Flyway e Otimizações Oracle [AB#15]
│   ├── 📄 [PBI-01] Mapeamento das Entidades Core e Relacionamentos 3FN no Schema Oracle (3 pts) [AB#16]
│   ├── 📄 [PBI-02] Repositórios Spring Data JPA e Consultas Otimizadas com EntityGraph (3 pts) [AB#17]
│   └── 📄 [PBI-03] Versionamento de Banco de Dados com Migrations Flyway (V1, V2, V3) e Carga Inicial (3 pts) [AB#113]
│
├── 🏆 [FEATURE 02] Segurança Stateless com Spring Security RSA Nimbus JWT e RBAC [AB#18]
│   ├── 📄 [PBI-04] Configuração de SecurityFilterChain Stateless com Par de Chaves RSA 2048-bit (3 pts) [AB#19]
│   ├── 📄 [PBI-05] Endpoints de Autenticação (Login, Registro e /auth/me com Hash BCrypt) (3 pts) [AB#20]
│   └── 📄 [PBI-06] Controle de Acesso Baseado em Papéis (RBAC: CIDADAO, GESTOR e ADMIN) (3 pts) [AB#114]
│
├── 🏆 [FEATURE 03] Regras de Negócio de Zeladoria Urbana, DTOs e Endpoints REST [AB#21]
│   ├── 📄 [PBI-07] Camada de DTOs Padronizados com Padrão aplicarEm e Validações Jakarta Bean Validation (3 pts) [AB#115]
│   ├── 📄 [PBI-08] Ciclo de Vida e Gestão de Chamados com Enriquecimento em Lote e Histórico de Transições (3 pts) [AB#22]
│   ├── 📄 [PBI-09] Sistema de Apoio Comunitário (/chamados/{id}/apoiar) e Registro em HistChamado (3 pts) [AB#23]
│   └── 📄 [PBI-10] Endpoints REST Diretos, Paginação (Pageable), Integração ViaCEP e ProblemDetail RFC 7807 (3 pts) [AB#24]
│
├── 🏆 [FEATURE 04] Arquitetura Distribuída com RabbitMQ, Triagem com Spring AI e Testes Unitários [AB#25]
│   ├── 📄 [PBI-11] Mensageria Assíncrona com RabbitMQ (Direct Exchange, Filas e Produtores de Eventos na API) (3 pts) [AB#116]
│   ├── 📄 [PBI-12] Microsserviço Worker com Triagem Inteligente via Spring AI / LLM (Urgência e Parecer) (3 pts) [AB#117]
│   ├── 📄 [PBI-13] Agregador de Votos em Memória com ConcurrentHashMap (Padrão Paredão) e Flush Periódico (3 pts) [AB#118]
│   └── 📄 [PBI-14] Suíte de Testes Unitários Automatizados com JUnit 5/Mockito e Documentação Swagger OpenAPI 3.0 (3 pts) [AB#26]
│
└── 🏆 [FEATURE 05] Arquitetura Gradle Multi-Project, Containerização Docker e Esteira CI/CD em Nuvem [AB#170]
    ├── 📄 [PBI-15] Modularização em Gradle Multi-Project e Alinhamento Java 21 LTS (3 pts) [AB#171]
    ├── 📄 [PBI-16] Containerização Multi-Stage com Docker, Imagem Alpine e Usuário Não-Root (3 pts) [AB#172]
    ├── 📄 [PBI-17] Esteira de CI/CD no Azure DevOps e Espelhamento com Políticas de Branch (3 pts) [AB#173]
    └── 📄 [PBI-18] Governança Técnica, Padrão de Engenharia (AGENT.md) e Documentação Corporativa (3 pts) [AB#174]
```

---

## 📊 2. Tabela Resumo do Backlog

| Feature Pai | ID do PBI | Título do Item de Backlog (PBI) | Story Points | Prioridade | Horas Estimadas | ID Azure Boards |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **[FEATURE 01] Domínio & Oracle** | **PBI-01** | Mapeamento das Entidades Core e Relacionamentos 3FN no Schema Oracle | 3 pts | 1 - Critical | 7.0h | **#16** |
| | **PBI-02** | Repositórios Spring Data JPA e Consultas Otimizadas com EntityGraph | 3 pts | 1 - Critical | 6.5h | **#17** |
| | **PBI-03** | Versionamento de Banco de Dados com Migrations Flyway (V1, V2, V3) e Carga Inicial | 3 pts | 1 - Critical | 5.5h | **#113** |
| **[FEATURE 02] Security & JWT** | **PBI-04** | Configuração de SecurityFilterChain Stateless com Par de Chaves RSA 2048-bit | 3 pts | 1 - Critical | 7.5h | **#19** |
| | **PBI-05** | Endpoints de Autenticação (Login, Registro e /auth/me com Hash BCrypt) | 3 pts | 1 - Critical | 6.5h | **#20** |
| | **PBI-06** | Controle de Acesso Baseado em Papéis (RBAC: CIDADAO, GESTOR e ADMIN) | 3 pts | 1 - Critical | 6.0h | **#114** |
| **[FEATURE 03] Regras & REST** | **PBI-07** | Camada de DTOs Padronizados com Padrão aplicarEm e Validações Jakarta Bean Validation | 3 pts | 1 - Critical | 6.5h | **#115** |
| | **PBI-08** | Ciclo de Vida e Gestão de Chamados com Enriquecimento em Lote e Histórico de Transições | 3 pts | 1 - Critical | 8.0h | **#22** |
| | **PBI-09** | Sistema de Apoio Comunitário (/chamados/{id}/apoiar) e Registro em HistChamado | 3 pts | 1 - Critical | 6.5h | **#23** |
| | **PBI-10** | Endpoints REST Diretos, Paginação (Pageable), Integração ViaCEP e ProblemDetail RFC 7807 | 3 pts | 1 - Critical | 7.0h | **#24** |
| **[FEATURE 04] Distribuído & AI** | **PBI-11** | Mensageria Assíncrona com RabbitMQ (Direct Exchange, Filas e Produtores de Eventos na API) | 3 pts | 1 - Critical | 8.0h | **#116** |
| | **PBI-12** | Microsserviço Worker com Triagem Inteligente via Spring AI / LLM (Urgência e Parecer) | 3 pts | 1 - Critical | 8.5h | **#117** |
| | **PBI-13** | Agregador de Votos em Memória com ConcurrentHashMap (Padrão Paredão) e Flush Periódico | 3 pts | 1 - Critical | 7.0h | **#118** |
| | **PBI-14** | Suíte de Testes Unitários Automatizados com JUnit 5/Mockito e Documentação Swagger OpenAPI 3.0 | 3 pts | 1 - Critical | 7.5h | **#26** |
| **[FEATURE 05] Gradle, Docker & CI/CD** | **PBI-15** | Modularização em Gradle Multi-Project e Alinhamento Java 21 LTS | 3 pts | 1 - Critical | 6.5h | **#171** |
| | **PBI-16** | Containerização Multi-Stage com Docker, Imagem Alpine e Usuário Não-Root | 3 pts | 1 - Critical | 7.0h | **#172** |
| | **PBI-17** | Esteira de CI/CD no Azure DevOps e Espelhamento com Políticas de Branch | 3 pts | 1 - Critical | 8.5h | **#173** |
| | **PBI-18** | Governança Técnica, Padrão de Engenharia (AGENT.md) e Documentação Corporativa | 3 pts | 1 - Critical | 6.0h | **#174** |
| **TOTAL CONSOLIDADO** | **5 Features** | **18 Product Backlog Items (PBIs)** | **54 pts** | — | **126.0h** | — |

---

## 📦 3. Detalhamento dos Itens de Trabalho

---

### 🏛️ ÉPICO
* **Work Item Type:** `Epic`
* **Azure Boards ID:** `#14`
* **Title:** `[EPIC] Java Advanced: Microsserviços com RabbitMQ, Spring AI e API RESTful Spring Boot Core`
* **Tags:** `JavaAdvanced, GlobalSolution2, SpringBoot, RabbitMQ, SpringAI, Oracle, JWT, Gradle, Docker, AzurePipelines`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `54`
* **Business Value:** `100`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Description:** Arquitetura distribuída de microsserviços em Java 21+ com Spring Boot 3+ (Opção A da Global Solution), composta pela API REST Gateway (`zelafix-api`) e pelo Worker de processamento assíncrono (`zelafix-worker`) estruturados em arquitetura Gradle Multi-Project. Contempla banco relacional Oracle 11g/19c em Terceira Forma Normal (3FN), versionamento Flyway (V1, V2, V3), autenticação via JWT RSA Nimbus assimétrico, RBAC (CIDADAO, GESTOR e ADMIN), mensageria com RabbitMQ / CloudAMQP (Exchange `zelafix.direct` e filas duráveis), triagem inteligente com Spring AI (Groq Qwen 3.8 27B Vision com fallback heurístico), agregador de votos com buffer thread-safe em memória (Padrão Paredão), containerização com Docker multi-stage build (Temurin 21 alpine com usuário não-root) e esteira de CI/CD completa no Azure DevOps (`azure-pipelines.yml`) com espelhamento GitHub Actions e proteção de branch na main (`TF402455`).

---

### 🏆 [FEATURE 01] Modelagem de Domínio JPA 3FN, Migrations Flyway e Otimizações Oracle
* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#15`
* **Parent:** `[EPIC] Java Advanced: Microsserviços com RabbitMQ, Spring AI e API RESTful Spring Boot Core` (#14)
* **Title:** `[FEATURE 01] Modelagem de Domínio JPA 3FN, Migrations Flyway e Otimizações Oracle`
* **Tags:** `JavaAdvanced, JPA, Oracle, Flyway, Database`
* **Effort (Story Points):** `9`
* **Acceptance Criteria:**
  - [x] Mapeamento JPA completo das 10 entidades em 3FN: `Usuario`, `CargoUsuario`, `Chamado`, `HistChamado`, `Status`, `Categoria`, `VotoChamado`, `Endereco`, `Bairro`, `Cidade`, `Estado`, `Telefone`.
  - [x] Migrations versionadas Flyway (V1, V2, V3) com criação de sequences, tabelas e carga inicial com IDs explícitos.
  - [x] Consultas com `@EntityGraph` eliminando problema de N+1 queries.

#### 🔹 [PBI-01] Mapeamento das Entidades Core e Relacionamentos 3FN no Schema Oracle
* **Azure Boards ID:** `#16` | **Effort:** `3 pts`
* **Commits vinculados (Development):**
  - `5a00d4c` Initial commit
  - `2666742` feat: Subindo o esqueleto base do projeto.
  - `61397f2` refactor(domain): remove unused comentario entity, endpoints and seeder references
  - `e9bc384` feat(backend): refatorar entidades, DTOs e worker para alinhamento 100% com modelo 3FN Oracle
  - `f58f087` refactor(api): alinhar entidades com Oracle 3FN, unificar DTOs e simplificar arquitetura
  - `eb4756a` refactor(model): alinhar entidades com DDL estrito 1:1 em telefone e limpar DTOs response

#### 🔹 [PBI-02] Repositórios Spring Data JPA e Consultas Otimizadas com EntityGraph
* **Azure Boards ID:** `#17` | **Effort:** `3 pts`
* **Commits vinculados (Development):**
  - `6d0d05b` refactor(data): otimizar repositorios e expurgar enums legados nao mapeados
  - `9237241` refactor(core): otimizar consultas com entitygraph, remover cascade indevido e configurar cors
  - `ceb5f50` perf(persistence): adicionar entity graphs e consultas agregadas em lote para eliminar N+1

#### 🔹 [PBI-03] Versionamento de Banco de Dados com Migrations Flyway (V1, V2, V3) e Carga Inicial
* **Azure Boards ID:** `#113` | **Effort:** `3 pts`
* **Pull Request:** PR #1 (`fix(devops,flyway): CloudAMQP, migrations V2/V3 e CI/CD unificado`)
* **Commits vinculados (Development):**
  - `8d7bbfd` feat(database): adicionar migration V3 para admin inicial e remover DatabaseSeeder
  - `cc2ae95` fix(db): garantir insercao com IDs explicitos para status pendente e admin inicial no Oracle
  - `1da8029` fix(db,config): corrigir IDENTITY nas migrations V2/V3, validar Flyway e migrar properties para CloudAMQP

---

### 🏆 [FEATURE 02] Segurança Stateless com Spring Security RSA Nimbus JWT e RBAC
* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#18`
* **Parent:** `[EPIC] Java Advanced: Microsserviços com RabbitMQ, Spring AI e API RESTful Spring Boot Core` (#14)
* **Title:** `[FEATURE 02] Segurança Stateless com Spring Security RSA Nimbus JWT e RBAC`
* **Tags:** `JavaAdvanced, SpringSecurity, RSA, JWT, RBAC`
* **Effort (Story Points):** `9`
* **Acceptance Criteria:**
  - [x] SecurityFilterChain configurado como STATELESS.
  - [x] Par de chaves RSA 2048-bit (pública e privada) para assinatura e validação JWT via Nimbus JOSE+JWT.
  - [x] Senhas salvas com hash BCrypt.
  - [x] Controle RBAC com `@PreAuthorize` para `ROLE_CIDADAO`, `ROLE_GESTOR` e `ROLE_ADMIN`.

#### 🔹 [PBI-04] Configuração de SecurityFilterChain Stateless com Par de Chaves RSA 2048-bit
* **Azure Boards ID:** `#19` | **Effort:** `3 pts`
* **Commits vinculados (Development):**
  - `a338026` feat(architecture): refactor monolithic api and worker with rabbitmq, spring ai, jwt and clean dtos
  - `9803e6c` refactor(service): desacoplar regras de negocio, aplicar padrão aplicarEm e eliminar código redundante

#### 🔹 [PBI-05] Endpoints de Autenticação (Login, Registro e /auth/me com Hash BCrypt)
* **Azure Boards ID:** `#20` | **Effort:** `3 pts`
* **Commits vinculados (Development):**
  - `8036680` refactor(controller): consolidar endpoints rest, controle de acesso rbac e swagger openapi
  - `892c011` test(auth): adicionar testes unitarios de AuthService e tratar exceptions no GlobalExceptionHandler

#### 🔹 [PBI-06] Controle de Acesso Baseado em Papéis (RBAC: CIDADAO, GESTOR e ADMIN)
* **Azure Boards ID:** `#114` | **Effort:** `3 pts`
* **Commits vinculados (Development):**
  - `eb5f627` refactor(api): standardize direct endpoints without /api prefix and restrict roles to CIDADAO and GESTOR
  - `e481a4b` refactor(usuario): padronizar validacao de cargo com EnumValidation e mapear conflitos de concorrencia

---

### 🏆 [FEATURE 03] Regras de Negócio de Zeladoria Urbana, DTOs e Endpoints REST
* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#21`
* **Parent:** `[EPIC] Java Advanced: Microsserviços com RabbitMQ, Spring AI e API RESTful Spring Boot Core` (#14)
* **Title:** `[FEATURE 03] Regras de Negócio de Zeladoria Urbana, DTOs e Endpoints REST`
* **Tags:** `JavaAdvanced, Services, DTO, RestAPI, RFC7807`
* **Effort (Story Points):** `12`
* **Acceptance Criteria:**
  - [x] Contratos DTO padronizados com validação estrita (`@Valid`, `@DddValidation`, `@EnumValidation`).
  - [x] CRUD completo de chamados com cálculo de prazo de previsão conforme categoria e `@TransactionalEventListener`.
  - [x] Sistema de apoio comunitário com rota unificada `/chamados/{id}/apoiar`.
  - [x] Endpoints diretos sem prefixo `/api` e respostas de erro estruturadas em RFC 7807 (ProblemDetail).

#### 🔹 [PBI-07] Camada de DTOs Padronizados com Padrão aplicarEm e Validações Jakarta Bean Validation
* **Azure Boards ID:** `#115` | **Effort:** `3 pts`
* **Pull Request:** PR #2 (`refactor(usuario,chamado): padrão Clyvo 4 em UsuarioService, @TransactionalEventListener e ViaCepServiceTest`)
* **Commits vinculados (Development):**
  - `361cd51` refactor(dto): padronizar contratos com toEntity, validacoes customizadas e expurgo de respostas legadas
  - `895fbd8` feat(validation): implementar validador customizado de DDD e aplicar em UsuarioRequest
  - `96b32ad` refactor(chamado): renomear StatusRequest para ChamadoStatusRequest e padronizar responses de chamado e historico
  - `c641cf9` refactor(usuario): enxugar aplicarEm no UsuarioService alinhado ao padrao Clyvo 4
  - `bd759cb` refactor(usuario,chamado): padronizar UsuarioService (Clyvo 4), mover Telefone, usar @TransactionalEventListener e criar ViaCepServiceTest

#### 🔹 [PBI-08] Ciclo de Vida e Gestão de Chamados com Enriquecimento em Lote e Histórico de Transições
* **Azure Boards ID:** `#22` | **Effort:** `3 pts`
* **Pull Request:** PR #2
* **Commits vinculados (Development):**
  - `8dbf652` refactor(service): refatorar ChamadoService com enriquecimento em lote e validacoes isoladas (padrao Clyvo 4)
  - `0151504` refactor(chamado): otimizar ChamadoService com ifPresentOrElse, toEntity e enriquecimento inline
  - `7e3ca5e` refactor(chamado): eliminar sobrecargas em ChamadoService, unificar create e permitir edicao por Gestor

#### 🔹 [PBI-09] Sistema de Apoio Comunitário (/chamados/{id}/apoiar) e Registro em HistChamado
* **Azure Boards ID:** `#23` | **Effort:** `3 pts`
* **Commits vinculados (Development):**
  - `01cb1cd` refactor(chamado): unificar rota de apoio comunitario para /chamados/{id}/apoiar
  - `78b36f9` test(chamado): atualizar testes unitarios para o metodo apoiar

#### 🔹 [PBI-10] Endpoints REST Diretos, Paginação (Pageable), Integração ViaCEP e ProblemDetail RFC 7807
* **Azure Boards ID:** `#24` | **Effort:** `3 pts`
* **Commits vinculados (Development):**
  - `b257117` test(chamado): adicionar teste unitario de busca paginada com hidratacao em lote
  - `cb9d7bd` perf(core): aplicar cache declarativo em catalogo e configurar timeouts HTTP para ViaCEP

---

### 🏆 [FEATURE 04] Arquitetura Distribuída com RabbitMQ, Triagem com Spring AI e Testes Unitários
* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#25`
* **Parent:** `[EPIC] Java Advanced: Microsserviços com RabbitMQ, Spring AI e API RESTful Spring Boot Core` (#14)
* **Title:** `[FEATURE 04] Arquitetura Distribuída com RabbitMQ, Triagem com Spring AI e Testes Unitários`
* **Tags:** `JavaAdvanced, RabbitMQ, SpringAI, Worker, JUnit5`
* **Effort (Story Points):** `12`
* **Acceptance Criteria:**
  - [x] Microsserviço `zelafix-worker` 100% Stateless (zero conexões JDBC/JPA com banco) processando RabbitMQ / CloudAMQP.
  - [x] Triagem automatizada multimodal com Spring AI (Groq Qwen 3.8 27B Vision) com detecção dinâmica de MIME type e fallback.
  - [x] Fila de feedback bidirecional (`chamado.triagem-concluida.queue`) para persistência ACID pela API.
  - [x] Agregador de votos em memória com `ConcurrentHashMap` e flush periódico em lote via `@Scheduled`.
  - [x] Suíte de testes unitários com JUnit 5, Mockito e documentação Swagger OpenAPI 3.0.

#### 🔹 [PBI-11] Mensageria Assíncrona com RabbitMQ (Direct Exchange, Filas e Produtores de Eventos na API)
* **Azure Boards ID:** `#116` | **Effort:** `3 pts`
* **Pull Request:** PR #1
* **Commits vinculados (Development):**
  - `d13aa34` feat(rabbitmq): estruturar produtores e consumidores assincronos com tipagem AMQP e buffer concorrente
  - `862b01c` refactor(worker): simplificar mensageria rabbitmq, expurgar entidade redundante e atualizar consumidor ai
  - `3595457` refactor(queue): remover Serializable redundante de DTOs e ajustar feedback de IA
  - `905961a` chore: migrar mensageria para CloudAMQP e remover docker-compose

#### 🔹 [PBI-12] Microsserviço Worker com Triagem Multimodal via Spring AI / LLM (Urgência e Parecer)
* **Azure Boards ID:** `#117` | **Effort:** `3 pts`
* **Commits vinculados (Development):**
  - `18caf51` feat(ai): implementar triagem multimodal com Qwen 3.8 27B e suporte a imagens mobile
  - `1b8382c` chore(config): configurar integracao com Groq LLM no worker e remover configuracoes redundantes da api
  - `c7117fa` refactor(worker): desacoplar totalmente do banco e publicar parecer de IA na fila de retorno
  - `c8bba67` feat(api): configurar fila de retorno e consumer para persistir parecer da triagem por IA
  - `ce55cca` refactor(chamado): aplicar parecer de IA no historico e tratar exclusao cascata via repositorio
  - `21d09e5` feat(worker): consolidar triagem multimodal obrigatoria com foto e consumidor de votos enxuto

#### 🔹 [PBI-13] Agregador de Votos em Memória com ConcurrentHashMap (Padrão Paredão) e Flush Periódico
* **Azure Boards ID:** `#118` | **Effort:** `3 pts`
* **Commits vinculados (Development):**
  - `d13aa34` feat(rabbitmq): estruturar produtores e consumidores assincronos com tipagem AMQP e buffer concorrente
  - `21d09e5` feat(worker): consolidar triagem multimodal obrigatoria com foto e consumidor de votos enxuto

#### 🔹 [PBI-14] Suíte de Testes Unitários Automatizados com JUnit 5/Mockito e Documentação Swagger OpenAPI 3.0
* **Azure Boards ID:** `#26` | **Effort:** `3 pts`
* **Commits vinculados (Development):**
  - `4f499bf` test(suite): atualizar testes unitarios e documentacao de compliance de arquitetura
  - `749078f` test(suite): adicionar testes unitarios para usuarioservice e zelafixaiservice
  - `877e260` test(api): implementar suite de testes pesados para servicos, controllers, seguranca e excecoes da api
  - `5995252` test(worker): implementar suite de testes para consumidor rabbitmq, concorrencia e integracao real com groq
  - `3184b84` test(e2e): adicionar suite completa de testes de integracao, concorrencia e stress maximo
  - `b6193e3` test(chamado): expandir testes extremos de controller, blindar cache e unificar exceptions
  - `c7031b5` fix(test,ci): ajustar GROQ_BASE_URL=/v1 no ZelaFixAiLiveIntegrationTest e pipeline
  - `49f16e6` fix(ci): isolar chave Groq da etapa unitária para evitar 429 na pipeline

---

### 🏆 [FEATURE 05] Arquitetura Gradle Multi-Project, Containerização Docker e Esteira CI/CD em Nuvem
* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#170`
* **Parent:** `[EPIC] Java Advanced: Microsserviços com RabbitMQ, Spring AI e API RESTful Spring Boot Core` (#14)
* **Title:** `[FEATURE 05] Arquitetura Gradle Multi-Project, Containerização Docker e Esteira CI/CD em Nuvem`
* **Tags:** `JavaAdvanced, Gradle, Docker, AzurePipelines, CICD, DevOps`
* **Effort (Story Points):** `12`
* **Acceptance Criteria:**
  - [x] Estrutura Gradle Multi-Project (`rootProject.name = 'zelafix-backend'`, `zelafix-api`, `zelafix-worker`) compilando e testando atomicamente via `gradlew test bootJar`.
  - [x] Dockerfiles multi-stage build (`gradle:8.10-jdk21-alpine` para `eclipse-temurin:21-jre-alpine`) com usuário `appuser:appgroup`, timezone `America/Sao_Paulo` e geração dinâmica de chaves RSA via openssl.
  - [x] Pipeline Azure DevOps funcional (`azure-pipelines.yml`) realizando build, validação e deploy em Azure App Services (`app-zelafix-561432` e `app-zelafix-worker-561432`).
  - [x] Proteção de branch na branch `main` do Azure Repos (`TF402455`) exigindo Pull Requests de homologação e governança técnica documentada no `AGENT.md`.

#### 🔹 [PBI-15] Modularização em Gradle Multi-Project e Alinhamento Java 21 LTS
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#171`
* **Parent Feature:** `[FEATURE 05] Arquitetura Gradle Multi-Project, Containerização Docker e Esteira CI/CD em Nuvem` (#170)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, Gradle, MultiProject, Java21, Build`

##### Descrição (História de Usuário)
> **Como** arquiteto e desenvolvedor backend,  
> **Eu quero** modularizar o repositório em arquitetura Gradle Multi-Project com `rootProject.name = 'zelafix-backend'` e submódulos autônomos `zelafix-api` e `zelafix-worker`,  
> **Para que** o ciclo de build e testes unitários seja centralizado enquanto os artefatos de deploy permanecem completamente desacoplados.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `settings.gradle` declarando `zelafix-api` e `zelafix-worker`.
- [x] `build.gradle` raiz centralizando plugins Spring Boot e Java toolchain 21.
- [x] `zelafix-worker` sem dependências transacionais ou drivers de banco de dados.
- [x] Flag `-parameters` habilitada no compilador Java para reflection precisa nos endpoints.

##### Commits vinculados (Development):
- `a3f41e7` build(gradle): alinhar toolchain para Java 21 LTS e habilitar flag -parameters
- `7fc4003` chore(scripts): remover scripts temporarios de manutencao do flyway
- `4d5d970` feat: removendo comentários inúteis

---

#### 🔹 [PBI-16] Containerização Multi-Stage com Docker, Imagem Alpine e Usuário Não-Root
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#172`
* **Parent Feature:** `[FEATURE 05] Arquitetura Gradle Multi-Project, Containerização Docker e Esteira CI/CD em Nuvem` (#170)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, Docker, MultiStage, Security, Alpine`

##### Descrição (História de Usuário)
> **Como** engenheiro de DevSecOps,  
> **Eu quero** containerizar os microsserviços via Dockerfiles com multi-stage build (`gradle:8.10-jdk21-alpine` para `eclipse-temurin:21-jre-alpine`) executando com usuário não-root (`appuser:appgroup`),  
> **Para que** os contêineres sejam leves, seguros, com timezone `America/Sao_Paulo` e geração dinâmica de par de chaves RSA.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Dockerfiles da API e Worker com multi-stage build a partir da raiz do projeto.
- [x] Usuário e grupo não-root (`appuser:appgroup`) configurados no contêiner.
- [x] Fuso horário configurado como `America/Sao_Paulo`.
- [x] Script dinâmico de geração de par de chaves RSA via openssl no build da API.

##### Pull Request:
- PR #3 (`refactor(docker,agent): multi-stage build Temurin 21, documentacao e limpeza`)

##### Commits vinculados (Development):
- `ec9928b` chore(infra): padronizar Dockerfiles para runtime alpine e remover artefatos orfaos de build
- `70f9c43` chore(infra): injetar env em tasks do gradle e configurar docker compose e propriedades
- `b7e1297` refactor(docker): migrar dockerfiles para multi-stage build com temurin 21 e usuario nao-root

---

#### 🔹 [PBI-17] Esteira de CI/CD no Azure DevOps e Espelhamento com Políticas de Branch
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#173`
* **Parent Feature:** `[FEATURE 05] Arquitetura Gradle Multi-Project, Containerização Docker e Esteira CI/CD em Nuvem` (#170)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, AzurePipelines, CICD, GitHubActions, BranchProtection`

##### Descrição (História de Usuário)
> **Como** líder técnico e engenheiro DevOps,  
> **Eu quero** estruturar a pipeline `azure-pipelines.yml` no Azure DevOps e o workflow GitHub Actions com política de branch protegida na `main` (TF402455),  
> **Para que** deploys nos Azure App Services ocorram de forma automática e auditada exclusivamente via Pull Requests de homologação.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `azure-pipelines.yml` executando build do Gradle e deploy nos Azure App Services.
- [x] Workflow `.github/workflows/mirror-to-azure.yml` espelhando branches `main` e `develop`.
- [x] Política de proteção de branch na `main` bloqueando pushes diretos e exigindo PRs com revisão.
- [x] Tratamento de isolamento de variáveis e chaves da Groq para evitar erros 429 na esteira de CI.

##### Pull Requests:
- PR #1 (`fix(devops,flyway): CloudAMQP, migrations V2/V3 e CI/CD unificado`)
- PR #5 (`ci: ajustar script do mirror para protecao de branch do Azure Repos`)

##### Commits vinculados (Development):
- `6981364` ci: adicionar esteira azure-pipelines para build e deploy dos microsservicos api e worker
- `c704048` ci: habilitar triggers e release automáticos para branches main e develop
- `7a9e1fa` ci(devops): alinhar mapeamento de variáveis de pipeline e documentar docker-compose para dev local
- `a5847ec` ci: remover FLYWAY_ENABLED=false da pipeline
- `2546b3d` ci(github-actions): espelhar automaticamente github -> azure repos ao push em main/develop
- `082d516` ci(github-actions): tratar protecao de branch TF402455 do Azure Repos no espelhamento da main

---

#### 🔹 [PBI-18] Governança Técnica, Padrão de Engenharia (AGENT.md) e Documentação Corporativa
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#174`
* **Parent Feature:** `[FEATURE 05] Arquitetura Gradle Multi-Project, Containerização Docker e Esteira CI/CD em Nuvem` (#170)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, Documentation, AGENT, Architecture, README`

##### Descrição (História de Usuário)
> **Como** arquiteto do projeto ZelaFix,  
> **Eu quero** documentar as decisões arquiteturais no `AGENT.md` e `README.md` com diretrizes de Clean Code e padrão Ponytail,  
> **Para que** a equipe e os agentes autônomos sigam as mesmas convenções de código, DTOs e testes, garantindo 100% de conformidade com os critérios da FIAP.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Guia `AGENT.md` detalhando arquitetura reativa, separação de responsabilidades e regras Ponytail.
- [x] `README.md` atualizado com justificativa corporativa do Gradle Multi-Project e arquitetura de nuvem.
- [x] Lista oficial dos 5 integrantes em ordem alfabética estrita com RMs e atribuições.

##### Pull Requests:
- PR #4 (`docs: atualizar README com justificativa Gradle multi-project e arquitetura de nuvem`)
- PR #6 (`docs: atualizar AGENT.md com arquitetura Gradle multi-project e CI/CD`)

##### Commits vinculados (Development):
- `7582fbd` docs(readme): atualizar lista oficial de integrantes do grupo para entrega da GS AB#26
- `f7b15fa` docs(agent): adicionar AGENT.md com diretrizes arquiteturais e padrao de desenvolvimento
- `c8b15c2` docs(agent): atualizar AGENT.md com regras de DTOs enxutos, cache e visao multimodal obrigatoria
- `88bd467` docs(agent): remover referencias a projetos externos e atualizar com arquitetura atual e comandos docker
- `c030583` docs: atualizar README com justificativa Gradle multi-project, arquitetura CI/CD Azure, Docker e Cloud deploy
- `8e7328c` docs(agent): atualizar AGENT.md com arquitetura Gradle multi-project, Flyway, CI/CD e politicas de branch
