# ☕ Backlog Master Azure Boards — Global Solution 2026/2: Java Advanced

> **Projeto Integrado:** ZelaFix — Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  
> **Disciplina:** Java Advanced (FIAP — 2TDSPG)  
> **Epic Principal:** `[EPIC] Java Advanced: Microsserviços com RabbitMQ, Spring AI e API RESTful Spring Boot Core`  
> **Responsável / Owner:** Enzo Okuizumi Miranda de Souza (`RM561432@fiap.com.br`)  
> **Start Date:** `2026-11-04`  
> **Target Date:** `2026-11-19`  
> **Padrão:** Azure Boards (Scrum Process: Epic ➔ Feature ➔ PBI)  
> **Opção Distribuída Escolhida:** **Opção A — Mensageria Assíncrona com RabbitMQ** (2 microsserviços autônomos: `zelafix-api` e `zelafix-worker`)  
> **Diretrizes Estratégicas:** Arquitetura distribuída de microsserviços em Java 21+ com Spring Boot 3+, persistência relacional no Oracle Database 11g/19c com Spring Data JPA em 3FN (`citizenTech.ddl`), versionamento de schema com Flyway Migrations (V1, V2, V3), segurança stateless com Spring Security e par de chaves RSA Nimbus JWT, controle de acesso baseado em papéis (RBAC: CIDADAO, GESTOR e ADMIN), mensageria assíncrona com RabbitMQ (Direct Exchange `zelafix.direct`), triagem inteligente de ocorrências com Spring AI (OpenAI / Groq LLM com fallback heurístico), agregador de votos com buffer thread-safe (`ConcurrentHashMap` - Padrão Paredão), documentação OpenAPI 3.0 / Swagger UI e suíte de testes unitários com JUnit 5 e Mockito.

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
[EPIC] Java Advanced: Microsserviços com RabbitMQ, Spring AI e API RESTful Spring Boot Core
│
├── 🏆 [FEATURE 01] Modelagem de Domínio JPA 3FN, Migrations Flyway e Otimizações Oracle
│   ├── 📄 [PBI-01] Mapeamento das Entidades Core e Relacionamentos 3FN no Schema Oracle (3 pts)
│   ├── 📄 [PBI-02] Repositórios Spring Data JPA e Consultas Otimizadas com EntityGraph (3 pts)
│   └── 📄 [PBI-03] Versionamento de Banco de Dados com Migrations Flyway (V1, V2, V3) e Carga Inicial (3 pts)
│
├── 🏆 [FEATURE 02] Segurança Stateless com Spring Security RSA Nimbus JWT e RBAC
│   ├── 📄 [PBI-04] Configuração de SecurityFilterChain Stateless com Par de Chaves RSA 2048-bit (3 pts)
│   ├── 📄 [PBI-05] Endpoints de Autenticação (Login, Registro e /auth/me com Hash BCrypt) (3 pts)
│   └── 📄 [PBI-06] Controle de Acesso Baseado em Papéis (RBAC: CIDADAO, GESTOR e ADMIN) (3 pts)
│
├── 🏆 [FEATURE 03] Regras de Negócio de Zeladoria Urbana, DTOs e Endpoints REST
│   ├── 📄 [PBI-07] Camada de DTOs Padronizados com Padrão aplicarEm e Validações Jakarta Bean Validation (3 pts)
│   ├── 📄 [PBI-08] Ciclo de Vida e Gestão de Chamados com Enriquecimento em Lote e Histórico de Transições (3 pts)
│   ├── 📄 [PBI-09] Sistema de Apoio Comunitário (/chamados/{id}/apoiar) e Registro em HistChamado (3 pts)
│   └── 📄 [PBI-10] Endpoints REST Diretos, Paginação (Pageable), Integração ViaCEP e ProblemDetail RFC 7807 (3 pts)
│
└── 🏆 [FEATURE 04] Arquitetura Distribuída com RabbitMQ, Triagem com Spring AI e Testes Unitários
    ├── 📄 [PBI-11] Mensageria Assíncrona com RabbitMQ (Direct Exchange, Filas e Produtores de Eventos na API) (3 pts)
    ├── 📄 [PBI-12] Microsserviço Worker com Triagem Inteligente via Spring AI / LLM (Urgência e Parecer) (3 pts)
    ├── 📄 [PBI-13] Agregador de Votos em Memória com ConcurrentHashMap (Padrão Paredão) e Flush Periódico (3 pts)
    └── 📄 [PBI-14] Suíte de Testes Unitários Automatizados com JUnit 5/Mockito e Documentação Swagger OpenAPI 3.0 (3 pts)
```

---

## 📊 2. Tabela Resumo do Backlog

| Feature Pai | ID do PBI | Título do Item de Backlog (PBI) | Story Points | Prioridade | Horas Estimadas |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **[FEATURE 01] Domínio & Oracle** | **PBI-01** | Mapeamento das Entidades Core e Relacionamentos 3FN no Schema Oracle | 3 pts | 1 - Critical | 7.0h |
| | **PBI-02** | Repositórios Spring Data JPA e Consultas Otimizadas com EntityGraph | 3 pts | 1 - Critical | 6.5h |
| | **PBI-03** | Versionamento de Banco de Dados com Migrations Flyway (V1, V2, V3) e Carga Inicial | 3 pts | 1 - Critical | 5.5h |
| **[FEATURE 02] Security & JWT** | **PBI-04** | Configuração de SecurityFilterChain Stateless com Par de Chaves RSA 2048-bit | 3 pts | 1 - Critical | 7.5h |
| | **PBI-05** | Endpoints de Autenticação (Login, Registro e /auth/me com Hash BCrypt) | 3 pts | 1 - Critical | 6.5h |
| | **PBI-06** | Controle de Acesso Baseado em Papéis (RBAC: CIDADAO, GESTOR e ADMIN) | 3 pts | 1 - Critical | 6.0h |
| **[FEATURE 03] Regras & REST** | **PBI-07** | Camada de DTOs Padronizados com Padrão aplicarEm e Validações Jakarta Bean Validation | 3 pts | 1 - Critical | 6.5h |
| | **PBI-08** | Ciclo de Vida e Gestão de Chamados com Enriquecimento em Lote e Histórico de Transições | 3 pts | 1 - Critical | 8.0h |
| | **PBI-09** | Sistema de Apoio Comunitário (/chamados/{id}/apoiar) e Registro em HistChamado | 3 pts | 1 - Critical | 6.5h |
| | **PBI-10** | Endpoints REST Diretos, Paginação (Pageable), Integração ViaCEP e ProblemDetail RFC 7807 | 3 pts | 1 - Critical | 7.0h |
| **[FEATURE 04] Distribuído & AI** | **PBI-11** | Mensageria Assíncrona com RabbitMQ (Direct Exchange, Filas e Produtores de Eventos na API) | 3 pts | 1 - Critical | 8.0h |
| | **PBI-12** | Microsserviço Worker com Triagem Inteligente via Spring AI / LLM (Urgência e Parecer) | 3 pts | 1 - Critical | 8.5h |
| | **PBI-13** | Agregador de Votos em Memória com ConcurrentHashMap (Padrão Paredão) e Flush Periódico | 3 pts | 1 - Critical | 7.0h |
| | **PBI-14** | Suíte de Testes Unitários Automatizados com JUnit 5/Mockito e Documentação Swagger OpenAPI 3.0 | 3 pts | 1 - Critical | 7.5h |
| **TOTAL CONSOLIDADO** | **4 Features** | **14 Product Backlog Items (PBIs)** | **42 pts** | — | **98.0h** |

---

## 📦 3. Detalhamento dos Itens de Trabalho

---

### 🏛️ ÉPICO
* **Work Item Type:** `Epic`
* **Title:** `[EPIC] Java Advanced: Microsserviços com RabbitMQ, Spring AI e API RESTful Spring Boot Core`
* **Tags:** `JavaAdvanced, ZelaFix, GlobalSolution2, SpringBoot, RabbitMQ, SpringAI, Oracle, JWT`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `42`
* **Business Value:** `100`
* **Description:** Arquitetura distribuída de microsserviços em Java 21+ com Spring Boot 3+ (Opção A da Global Solution), composta pela API REST Gateway (`zelafix-api`) e pelo Worker de processamento assíncrono (`zelafix-worker`). Contempla banco de dados relacional Oracle em Terceira Forma Normal (3FN), versionamento com Flyway, autenticação via tokens JWT assinados por chaves RSA assimétricas, controle de acesso RBAC, mensageria com RabbitMQ (Direct Exchange e filas duráveis), triagem inteligente de urgência com Spring AI (OpenAI / Groq LLM com fallback heurístico), agregador de votos comunitários em buffer de memória com flush em lote (Padrão Paredão), documentação OpenAPI 3.0 e suíte completa de testes unitários com JUnit 5 e Mockito.

---

### 🏆 [FEATURE 01] Modelagem de Domínio JPA 3FN, Migrations Flyway e Otimizações Oracle
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Java Advanced: Microsserviços com RabbitMQ, Spring AI e API RESTful Spring Boot Core`
* **Title:** `[FEATURE 01] Modelagem de Domínio JPA 3FN, Migrations Flyway e Otimizações Oracle`
* **Tags:** `JavaAdvanced, JPA, Oracle, Flyway, Database`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-09`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Description:** Configuração do pool HikariCP com o Oracle Database, mapeamento objeto-relacional estrito em 3FN, versionamento de banco com Flyway e otimização de consultas JPA para evitar queries N+1.
* **Acceptance Criteria:**
  - [x] Mapeamento JPA completo das 10 entidades: `Usuario`, `CargoUsuario`, `Chamado`, `HistChamado`, `Status`, `Categoria`, `VotoChamado`, `Endereco`, `Bairro`, `Cidade`, `Estado`, `Telefone`.
  - [x] Migrations versionadas Flyway (V1, V2, V3) com criação de sequences, tabelas e carga inicial com IDs explícitos.
  - [x] Consultas com `@EntityGraph` eliminando problema de N+1 queries.

#### 🔹 [PBI-01] Mapeamento das Entidades Core e Relacionamentos 3FN no Schema Oracle
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Modelagem de Domínio JPA 3FN, Migrations Flyway e Otimizações Oracle`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, Entities, JPA, Oracle3FN`

##### Descrição (História de Usuário)
> **Como** arquiteto de software backend Java,  
> **Eu quero** mapear as entidades relacionais com JPA/Hibernate espelhando fielmente o script corporativo Oracle (`citizenTech.ddl`),  
> **Para que** todas as chaves primárias, estrangeiras e restrições de integridade sejam respeitadas em 3FN sem redundância.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Entidades `Chamado`, `Categoria`, `Status`, `Usuario`, `CargoUsuario`, `VotoChamado`, `HistChamado`, `Endereco`, `Bairro`, `Cidade`, `Estado`, `Telefone` mapeadas no pacote de domínio.
- [ ] Mapeamento de chaves primárias via sequences nativas do Oracle com `@GeneratedValue(strategy = GenerationType.SEQUENCE)`.
- [ ] Remoção de entidades ou relacionamentos legados não mapeados (ex: remoção da entidade `Comentario`).

---

#### 🔹 [PBI-02] Repositórios Spring Data JPA e Consultas Otimizadas com EntityGraph
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Modelagem de Domínio JPA 3FN, Migrations Flyway e Otimizações Oracle`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, Repositories, EntityGraph, Performance`

##### Descrição (História de Usuário)
> **Como** desenvolvedor backend,  
> **Eu quero** criar interfaces `JpaRepository` com consultas otimizadas utilizando `@EntityGraph` e projeções em lote,  
> **Para que** as listagens paginadas de chamados não disparem consultas N+1 desnecessárias sobre relacionamentos de categoria, usuário e status.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] `@EntityGraph(attributePaths = {"usuario", "categoria", "status", "endereco"})` configurado nas consultas de `ChamadoRepository`.
- [ ] Consultas agregadas em lote para contagem de votos e verificação de apoio comunitário.
- [ ] Repositórios desacoplados e expurgo de consultas lentas ou buscas iterativas em loop.

---

#### 🔹 [PBI-03] Versionamento de Banco de Dados com Migrations Flyway (V1, V2, V3) e Carga Inicial
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Modelagem de Domínio JPA 3FN, Migrations Flyway e Otimizações Oracle`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, Flyway, Migrations, DatabaseSeed`

##### Descrição (História de Usuário)
> **Como** engenheiro de dados e DevOps,  
> **Eu quero** gerenciar as mudanças no banco de dados através de migrations versionadas do Flyway,  
> **Para que** o schema corporativo e os dados essenciais (categorias, status, administrador inicial) sejam criados deterministicamente em qualquer ambiente.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Migration `V1__criar_tabelas_zelafix.sql` com DDL completo de tabelas e sequences.
- [ ] Migration `V2__dados_iniciais_zelafix.sql` pré-carregando categorias, status e cargos com IDs explícitos.
- [ ] Migration `V3__admin_inicial.sql` criando o usuário gestor/administrador inicial com senha criptografada via BCrypt.
- [ ] Expurgo de `DatabaseSeeder` procedural em favor de migrations declarativas.

---

### 🏆 [FEATURE 02] Segurança Stateless com Spring Security RSA Nimbus JWT e RBAC
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Java Advanced: Microsserviços com RabbitMQ, Spring AI e API RESTful Spring Boot Core`
* **Title:** `[FEATURE 02] Segurança Stateless com Spring Security RSA Nimbus JWT e RBAC`
* **Tags:** `JavaAdvanced, SpringSecurity, RSA, JWT, RBAC`
* **Start Date:** `2026-11-07`
* **Target Date:** `2026-11-12`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Description:** Sistema de autenticação e autorização stateless via Spring Security 6 / OAuth2 Resource Server, com tokens JWT assinados via par de chaves RSA assimétricas e controle de acesso baseado em papéis (RBAC).
* **Acceptance Criteria:**
  - [x] SecurityFilterChain configurado como STATELESS.
  - [x] Par de chaves RSA 2048-bit (pública e privada) para assinatura e validação JWT.
  - [x] Senhas salvas com hash BCrypt.
  - [x] Controle RBAC com `@PreAuthorize` para `ROLE_CIDADAO`, `ROLE_GESTOR` e `ROLE_ADMIN`.

#### 🔹 [PBI-04] Configuração de SecurityFilterChain Stateless com Par de Chaves RSA 2048-bit
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Segurança Stateless com Spring Security RSA Nimbus JWT e RBAC`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, SecurityConfig, RSA, NimbusJWT`

##### Descrição (História de Usuário)
> **Como** especialista em segurança cibernética,  
> **Eu quero** configurar o Spring Security com OAuth2 Resource Server e tokens JWT assinados com par de chaves RSA de 2048 bits,  
> **Para que** a autenticação seja assimétrica, de alto padrão de mercado e sem acoplamento de segredos simétricos em código-fonte.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] `SecurityConfig.java` configurado com `sessionManagement(STATELESS)`.
- [ ] Geração de par de chaves RSA pública e privada com beans `RSAPublicKey` e `RSAPrivateKey`.
- [ ] Configuração de encoder `JwtEncoder` e decoder `JwtDecoder` utilizando a biblioteca Nimbus JOSE+JWT.
- [ ] Configuração de CORS permissivo em `CorsConfig.java` para consumo pelo app Expo e navegadores web.

---

#### 🔹 [PBI-05] Endpoints de Autenticação (Login, Registro e /auth/me com Hash BCrypt)
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Segurança Stateless com Spring Security RSA Nimbus JWT e RBAC`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, AuthController, BCrypt, TokenService`

##### Descrição (História de Usuário)
> **Como** usuário munícipe ou agente público,  
> **Eu quero** realizar cadastro pelo endpoint `/auth/register` e login pelo `/auth/login`, bem como consultar meu perfil ativo via `/auth/me`,  
> **Para que** eu possa me autenticar e obter meu Bearer Token JWT para consumir os serviços da plataforma.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] `AuthController.java` expondo `POST /auth/register`, `POST /auth/login` e `GET /auth/me`.
- [ ] Senhas criptografadas com `BCryptPasswordEncoder` antes da gravação no Oracle.
- [ ] Retorno de payload padronizado `LoginResponse` contendo o token JWT, tempo de expiração e dados básicos do usuário.
- [ ] Tratamento de credenciais inválidas retornando HTTP 401 Unauthorized.

---

#### 🔹 [PBI-06] Controle de Acesso Baseado em Papéis (RBAC: CIDADAO, GESTOR e ADMIN)
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Segurança Stateless com Spring Security RSA Nimbus JWT e RBAC`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, RBAC, Roles, PreAuthorize`

##### Descrição (História de Usuário)
> **Como** administrador do sistema de zeladoria,  
> **Eu quero** controlar o acesso a endpoints críticos através de anotações `@PreAuthorize` e claims de papéis no JWT,  
> **Para que** apenas agentes da prefeitura atualizem o status das obras e apenas administradores gerenciem cargos e usuários.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Enum e entidade `CargoUsuario` mapeando `ROLE_CIDADAO`, `ROLE_GESTOR` e `ROLE_ADMIN`.
- [ ] Claims `scope` ou `roles` inseridas no payload do token JWT pelo `TokenService`.
- [ ] Endpoints de abertura e apoio a chamados restritos a munícipes e gestores (`hasAnyRole('CIDADAO', 'GESTOR', 'ADMIN')`).
- [ ] Endpoints de alteração de cargo e gestão global de categorias/status restritos a `ROLE_ADMIN`.

---

### 🏆 [FEATURE 03] Regras de Negócio de Zeladoria Urbana, DTOs e Endpoints REST
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Java Advanced: Microsserviços com RabbitMQ, Spring AI e API RESTful Spring Boot Core`
* **Title:** `[FEATURE 03] Regras de Negócio de Zeladoria Urbana, DTOs e Endpoints REST`
* **Tags:** `JavaAdvanced, Services, DTO, RestAPI, RFC7807`
* **Start Date:** `2026-11-10`
* **Target Date:** `2026-11-16`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `12`
* **Business Value:** `100`
* **Description:** Camada de serviços de negócio, padronização de contratos DTOs com validações Bean Validation, gestão de chamados com cálculo de SLA e API RESTful com rotas diretas.
* **Acceptance Criteria:**
  - [x] Contratos DTO padronizados com validação estrita (`@Valid`).
  - [x] CRUD completo de chamados com cálculo de prazo de previsão conforme categoria.
  - [x] Sistema de apoio comunitário com rota unificada `/chamados/{id}/apoiar`.
  - [x] Endpoints diretos sem prefixo `/api` e respostas de erro estruturadas em RFC 7807 (ProblemDetail).

#### 🔹 [PBI-07] Camada de DTOs Padronizados com Padrão aplicarEm e Validações Jakarta Bean Validation
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] Regras de Negócio de Zeladoria Urbana, DTOs e Endpoints REST`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, DTO, BeanValidation, CleanCode`

##### Descrição (História de Usuário)
> **Como** desenvolvedor backend,  
> **Eu quero** criar classes de transferência de dados (DTOs) com validações Jakarta Bean Validation e método `aplicarEm()`,  
> **Para que** a camada de entidades permaneça encapsulada e as alterações de estado ocorram de forma padronizada e imutável.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] DTOs de request e response: `ChamadoRequest`, `ChamadoResponse`, `UsuarioRequest`, `UsuarioResponse`, `CategoriaRequest`, `CategoriaResponse`, etc.
- [ ] Anotações de validação: `@NotBlank`, `@Email`, `@Size`, `@NotNull` e validador customizado `@EnumValidation`.
- [ ] Padrão de conversão `toEntity()` e método de atualização `aplicarEm(Entity target)` eliminando boilerplate nos controllers.

---

#### 🔹 [PBI-08] Ciclo de Vida e Gestão de Chamados com Enriquecimento em Lote e Histórico de Transições
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] Regras de Negócio de Zeladoria Urbana, DTOs e Endpoints REST`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, ChamadoService, SLA, HistChamado`

##### Descrição (História de Usuário)
> **Como** munícipe e gestor público,  
> **Eu quero** que cada novo chamado seja registrado com prazo de atendimento calculado pelo SLA da categoria e cada transição de status seja auditada em `HIST_CHAMADO`,  
> **Para que** haja transparência completa sobre os prazos e responsáveis por cada etapa da obra urbana.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] `ChamadoService.java` registrando chamado com data de abertura, prazo de previsão e status inicial `PENDENTE`.
- [ ] Enriquecimento de chamados em lote com dados de categoria, status e contagem de votos.
- [ ] Registro atômico em `HistChamado` a cada mudança de status do chamado (`PENDENTE`, `EM_ANALISE`, `EM_EXECUCAO`, `CONCLUIDO`, `REJEITADO`).

---

#### 🔹 [PBI-09] Sistema de Apoio Comunitário (/chamados/{id}/apoiar) e Registro em HistChamado
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] Regras de Negócio de Zeladoria Urbana, DTOs e Endpoints REST`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, ApoioComunitario, Votos, Chamados`

##### Descrição (História de Usuário)
> **Como** cidadão afetado por um problema no meu bairro,  
> **Eu quero** acessar a rota unificada `POST /chamados/{id}/apoiar` para manifestar meu apoio àquela ocorrência,  
> **Para que** a solicitação ganhe prioridade coletiva diante da administração pública.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Rota unificada `POST /chamados/{id}/apoiar` validando a existência do chamado e usuário autenticado.
- [ ] Bloqueio de votos repetidos pelo mesmo cidadão na mesma ocorrência.
- [ ] Publicação do evento de voto na fila do RabbitMQ para processamento otimizado.

---

#### 🔹 [PBI-10] Endpoints REST Diretos, Paginação (Pageable), Integração ViaCEP e ProblemDetail RFC 7807
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] Regras de Negócio de Zeladoria Urbana, DTOs e Endpoints REST`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, REST, Pageable, ViaCEP, ProblemDetail`

##### Descrição (História de Usuário)
> **Como** desenvolvedor frontend e mobile,  
> **Eu quero** rotas REST diretas e semânticas com suporte a paginação `Pageable`, busca de endereço por CEP e tratamento de erro RFC 7807,  
> **Para que** o aplicativo consuma dados leves e receba respostas de erro compreensíveis em falhas de validação ou regras de negócio.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Rotas diretas: `/chamados`, `/usuarios`, `/categorias`, `/status`, `/enderecos` (sem prefixo `/api` redundante).
- [ ] Paginação com `Pageable` e ordenação dinâmica nas listagens de chamados.
- [ ] Serviço `ViaCepService` consultando a API pública ViaCEP para autocompletar endereços no cadastro.
- [ ] `@RestControllerAdvice` padronizando respostas de erro com `ProblemDetail` (RFC 7807).

---

### 🏆 [FEATURE 04] Arquitetura Distribuída com RabbitMQ, Triagem com Spring AI e Testes Unitários
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Java Advanced: Microsserviços com RabbitMQ, Spring AI e API RESTful Spring Boot Core`
* **Title:** `[FEATURE 04] Arquitetura Distribuída com RabbitMQ, Triagem com Spring AI e Testes Unitários`
* **Tags:** `JavaAdvanced, RabbitMQ, SpringAI, Worker, JUnit5, Docker`
* **Start Date:** `2026-11-12`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `12`
* **Business Value:** `100`
* **Description:** Implementação da arquitetura distribuída com 2 microsserviços autônomos, mensageria RabbitMQ, triagem inteligente com Spring AI / Groq LLM, buffer de votos em memória, documentação Swagger e suíte de testes unitários.
* **Acceptance Criteria:**
  - [x] Microsserviço `zelafix-worker` processando filas do RabbitMQ de forma desacoplada da API.
  - [x] Triagem automatizada de criticidade e parecer com Spring AI (OpenAI / Groq LLM) com fallback heurístico.
  - [x] Agregador de votos em memória com `ConcurrentHashMap` e flush periódico em lote via `@Scheduled`.
  - [x] Documentação interativa Swagger UI e suíte de testes unitários com JUnit 5 e Mockito.

#### 🔹 [PBI-11] Mensageria Assíncrona com RabbitMQ (Direct Exchange, Filas e Produtores de Eventos na API)
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 04] Arquitetura Distribuída com RabbitMQ, Triagem com Spring AI e Testes Unitários`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, RabbitMQ, DirectExchange, Producers`

##### Descrição (História de Usuário)
> **Como** arquiteto de microsserviços,  
> **Eu quero** configurar o RabbitMQ na `zelafix-api` com Direct Exchange e produtores de mensagens assíncronas,  
> **Para que** requisições pesadas (triagem por IA e agregação de votos) sejam despachadas para filas sem prender a thread HTTP do usuário.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] `RabbitConfig.java` configurando Direct Exchange `zelafix.direct` e filas `chamado.triagem.queue` e `chamado.voto.queue`.
- [ ] Produtor `ChamadoEventProducer.java` despachando evento com routing key `chamado.triagem.key`.
- [ ] Produtor `VotoEventProducer.java` despachando evento com routing key `chamado.voto.key`.
- [ ] Configuração do broker RabbitMQ no `docker-compose.yml`.

---

#### 🔹 [PBI-12] Microsserviço Worker com Triagem Inteligente via Spring AI / LLM (Urgência e Parecer)
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 04] Arquitetura Distribuída com RabbitMQ, Triagem com Spring AI e Testes Unitários`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, Worker, SpringAI, LLM, Triagem`

##### Descrição (História de Usuário)
> **Como** equipe de triagem municipal,  
> **Eu quero** um microsserviço worker que consuma chamados recém-criados e consulte uma LLM para classificar a criticidade e emitir parecer técnico,  
> **Para que** chamados perigosos (ex: fios elétricos expostos ou crateras) sejam priorizados imediatamente de forma automatizada.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Microsserviço autônomo `zelafix-worker` com consumidor `ChamadoAiConsumer.java` anotado com `@RabbitListener`.
- [ ] Serviço `ZelaFixAiService.java` integrado com `ChatClient` do Spring AI (OpenAI / Groq LLM).
- [ ] Algoritmo de fallback heurístico em caso de indisponibilidade da API da LLM ou ausência de chave de API.
- [ ] Atualização do chamado no banco de dados com órgão competente, urgência e parecer técnico.

---

#### 🔹 [PBI-13] Agregador de Votos em Memória com ConcurrentHashMap (Padrão Paredão) e Flush Periódico
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 04] Arquitetura Distribuída com RabbitMQ, Triagem com Spring AI e Testes Unitários`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, Worker, VotoConsumer, Buffer, Paredao`

##### Descrição (História de Usuário)
> **Como** arquiteto de alta disponibilidade,  
> **Eu quero** um buffer thread-safe em memória que acumule os votos comunitários e descarregue os totais no Oracle a cada 3 segundos,  
> **Para que** o sistema suporte milhares de munícipes votando simultaneamente sem gerar contenção de locks ou gargalo no banco.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Consumidor `VotoConsumer.java` escutando a fila `chamado.voto.queue`.
- [ ] Buffer de votos implementado com `ConcurrentHashMap<Long, LongAdder>` para garantir concorrência thread-safe.
- [ ] Método de descarga periódico anotado com `@Scheduled(fixedDelay = 3000)` executando updates em lote no Oracle.
- [ ] Tratamento gracioso de shutdown para gravação residual de votos pendentes.

---

#### 🔹 [PBI-14] Suíte de Testes Unitários Automatizados com JUnit 5/Mockito e Documentação Swagger OpenAPI 3.0
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 04] Arquitetura Distribuída com RabbitMQ, Triagem com Spring AI e Testes Unitários`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, JUnit5, Mockito, Swagger, OpenAPI`

##### Descrição (História de Usuário)
> **Como** professor avaliador da FIAP e engenheiro de software,  
> **Eu quero** testar os endpoints interativamente via Swagger UI e executar a suíte de testes unitários automatizados com JUnit 5 e Mockito,  
> **Para que** seja comprovada a cobertura de código, conformidade dos contratos REST e robustez das regras de negócio.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Swagger UI interativo disponível em `http://localhost:8080/swagger-ui.html` com suporte a autenticação Bearer JWT.
- [ ] Testes unitários para `ChamadoService` cobrindo criação, apoio comunitário e busca paginada com hidratação em lote.
- [ ] Testes unitários para `UsuarioService`, `AuthController` e `ZelaFixAiService`.
- [ ] Todos os testes passando com sucesso via `.\gradlew test`.
