# 📋 Backlog Master Azure Boards — Global Solution 2026/2: Java Advanced

> **Projeto Integrado:** ZelaFix — Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  
> **Disciplina:** Java Advanced (FIAP — 2TDSPG)  
> **Epic Principal:** `[EPIC] GS 2026/2 - Java Advanced: API RESTful Spring Boot Core, Segurança JWT e Regras de Negócio de Zeladoria Urbana`  
> **Start Date:** `2026-11-04`  
> **Target Date:** `2026-11-19`  
> **Padrão:** Azure Boards (Scrum Process: Epic ➔ Feature ➔ PBI ➔ Task)  
> **Diretrizes Estratégicas:** API RESTful robusta desenvolvida em Java 17+ com Spring Boot 3+, persistência relacional no Oracle Database via Spring Data JPA e Hibernate, segurança stateless com Spring Security e autenticação JWT, controle de acesso baseado em papéis (RBAC: CIDADAO vs GESTOR), validação de payloads com Bean Validation, paginação, documentação interativa OpenAPI 3 / Swagger UI e tratamento global de erros conforme RFC 7807.

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
[EPIC] GS 2026/2 - Java Advanced: API RESTful Spring Boot Core, Segurança JWT e Regras de Negócio de Zeladoria Urbana
│
├── 🏆 [FEATURE 01] Modelagem de Domínio JPA, Entidades Relacionais e Conexão Oracle
│   ├── 📄 [PBI-01] Mapeamento das Entidades Core (Chamado, Categoria, Usuario, HistStatus, VotoChamado) (3 pts)
│   └── 📄 [PBI-02] Camada de Repositórios Spring Data JPA e Queries Especializadas (3 pts)
│
├── 🏆 [FEATURE 02] Segurança Stateless com Spring Security, Autenticação JWT e RBAC
│   ├── 📄 [PBI-03] Configuração de SecurityFilterChain, TokenService e Interceptor JWT (3 pts)
│   └── 📄 [PBI-04] Endpoints de Autenticação (Login e Cadastro com Hash BCrypt) (3 pts)
│
├── 🏆 [FEATURE 03] Regras de Negócio, Serviços Core e Ciclo de Vida de Ocorrências
│   ├── 📄 [PBI-05] Serviços de Gestão de Chamados e Cálculo de Prazos SLA por Categoria (3 pts)
│   ├── 📄 [PBI-06] Mecanismo de Votação Comunitária e Auditoria de Transição em HistStatus (3 pts)
│   └── 📄 [PBI-07] Paginação, Filtros Dinâmicos por Bairro/Categoria e Tratamento Global RFC 7807 (3 pts)
│
└── 🏆 [FEATURE 04] Documentação OpenAPI / Swagger UI e Qualidade de Código
    └── 📄 [PBI-08] Documentação Interativa OpenAPI 3.0 e Cobertura de Testes Unitários JUnit 5 (2 pts)
```

---

## 📊 2. Tabela Resumo do Backlog

| Feature Pai | ID do PBI | Título do Item de Backlog (PBI) | Story Points | Prioridade | Horas Estimadas |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **[FEATURE 01] Domínio & Oracle** | **PBI-01** | Mapeamento das Entidades Core (Chamado, Categoria, Usuario, HistStatus, Voto) | 3 pts | 1 - Critical | 7.0h |
| | **PBI-02** | Camada de Repositórios Spring Data JPA e Queries Especializadas | 3 pts | 1 - Critical | 6.0h |
| **[FEATURE 02] Security & JWT** | **PBI-03** | Configuração de SecurityFilterChain, TokenService e Interceptor JWT | 3 pts | 1 - Critical | 7.5h |
| | **PBI-04** | Endpoints de Autenticação (Login e Cadastro com Hash BCrypt) | 3 pts | 1 - Critical | 6.5h |
| **[FEATURE 03] Serviços & SLA** | **PBI-05** | Serviços de Gestão de Chamados e Cálculo de Prazos SLA por Categoria | 3 pts | 1 - Critical | 8.0h |
| | **PBI-06** | Mecanismo de Votação Comunitária e Auditoria de Transição em HistStatus | 3 pts | 1 - Critical | 7.5h |
| | **PBI-07** | Paginação, Filtros Dinâmicos por Bairro/Categoria e Tratamento Global RFC 7807 | 3 pts | 1 - Critical | 6.5h |
| **[FEATURE 04] Swagger & JUnit** | **PBI-08** | Documentação Interativa OpenAPI 3.0 e Cobertura de Testes Unitários JUnit 5 | 2 pts | 2 - High | 5.0h |
| **TOTAL CONSOLIDADO** | **4 Features** | **8 PBIs / 23 Child Tasks Técnicas** | **23 pts** | — | **54.0h** |

---

## 📦 3. Detalhamento dos Itens de Trabalho (Épico, Features, PBIs e Tasks)

---

### 🏛️ ÉPICO
* **Work Item Type:** `Epic`
* **Title:** `[EPIC] GS 2026/2 - Java Advanced: API RESTful Spring Boot Core, Segurança JWT e Regras de Negócio de Zeladoria Urbana`
* **Tags:** `JavaAdvanced, ZelaFix, GlobalSolution2, SpringBoot, Oracle, JWT, REST`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `23`
* **Business Value:** `100`
* **Description:** Desenvolvimento da API RESTful central da plataforma ZelaFix em Spring Boot 3+, integrando banco Oracle relacional, arquitetura em camadas (Controller, Service, Repository, DTO), Spring Security com emissão e validação de tokens JWT, regras de negócio de zeladoria pública municipal e homologação de endpoints com OpenAPI 3.0.

---

### 🏆 [FEATURE 01] Modelagem de Domínio JPA, Entidades Relacionais e Conexão Oracle
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] GS 2026/2 - Java Advanced: API RESTful Spring Boot Core, Segurança JWT e Regras de Negócio de Zeladoria Urbana`
* **Title:** `[FEATURE 01] Modelagem de Domínio JPA, Entidades Relacionais e Conexão Oracle`
* **Tags:** `JavaAdvanced, JPA, Oracle, Database`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-09`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** Configuração do pool de conexões com o Oracle Database 11g e mapeamento objeto-relacional completo das tabelas da solução.
* **Acceptance Criteria:**
  - [x] Conexão ativa com o Oracle Database via HikariCP.
  - [x] Mapeamento JPA estrito das tabelas CHAMADO, CATEGORIA, USUARIO, HIST_STATUS, VOTO_CHAMADO, BAIRRO e ENDERECO.
  - [x] Relacionamentos bidirecionais (@ManyToOne, @OneToMany) sem recursão infinita na serialização JSON (@JsonIgnore / DTOs).

#### 🔹 [PBI-01] Mapeamento das Entidades Core (Chamado, Categoria, Usuario, HistStatus, Voto)
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Modelagem de Domínio JPA, Entidades Relacionais e Conexão Oracle`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, Entities, JPA`

##### Descrição (História de Usuário)
> **Como** desenvolvedor backend Java,  
> **Eu quero** criar as entidades JPA anotadas refletindo com precisão o modelo relacional do Oracle,  
> **Para que** as operações de persistência mantenham integridade referencial e validações automáticas.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Entidades `Chamado`, `Categoria`, `Usuario`, `HistStatus`, `VotoChamado` criadas no pacote `domain.entity`.
- [ ] Enums para Status do Chamado (`ABERTO`, `EM_ANALISE`, `EM_EXECUCAO`, `CONCLUIDO`, `REJEITADO`) e Cargo (`CIDADAO`, `GESTOR`).
- [ ] Chaves primárias com `@GeneratedValue` adequadas ao Oracle (Sequence).
---

#### 🔹 [PBI-02] Camada de Repositórios Spring Data JPA e Queries Especializadas
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Modelagem de Domínio JPA, Entidades Relacionais e Conexão Oracle`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, Repositories, SpringData`

##### Descrição (História de Usuário)
> **Como** desenvolvedor backend,  
> **Eu quero** interfaces `JpaRepository` com métodos de consulta customizados por bairro, categoria e status,  
> **Para que** a camada de serviço realize buscas filtradas com alta performance no Oracle.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Repositórios criados no pacote `domain.repository`.
- [ ] Métodos como `findByStatusAndCategoriaId`, `findByUsuarioId` e `countVotosByChamadoId`.
- [ ] Queries `@Query` otimizadas para carregamento eagerly quando necessário.
---

### 🏆 [FEATURE 02] Segurança Stateless com Spring Security, Autenticação JWT e RBAC
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] GS 2026/2 - Java Advanced: API RESTful Spring Boot Core, Segurança JWT e Regras de Negócio de Zeladoria Urbana`
* **Title:** `[FEATURE 02] Segurança Stateless com Spring Security, Autenticação JWT e RBAC`
* **Tags:** `JavaAdvanced, SpringSecurity, JWT, RBAC`
* **Start Date:** `2026-11-07`
* **Target Date:** `2026-11-12`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** Mecanismo de autenticação e autorização por tokens JWT com controle de perfis Cidadão e Gestor.
* **Acceptance Criteria:**
  - [x] SecurityFilterChain configurado como STATELESS (sem sessões HTTP no servidor).
  - [x] Senhas criptografadas com BCryptPasswordEncoder.
  - [x] Endpoints públicos limitados a `/api/auth/**` e documentação Swagger.
  - [x] Endpoints administrativos protegidos por `@PreAuthorize("hasRole('GESTOR')")`.

#### 🔹 [PBI-03] Configuração de SecurityFilterChain, TokenService e Interceptor JWT
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Segurança Stateless com Spring Security, Autenticação JWT e RBAC`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, Security, JWTFilter`

##### Descrição (História de Usuário)
> **Como** analista de segurança,  
> **Eu quero** um filtro interceptador OncePerRequestFilter que valide o token Bearer JWT em cada requisição,  
> **Para que** apenas usuários autenticados e autorizados acessem os recursos da API.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Classe `TokenService` gerando tokens assinados com claims de sujeito e perfis.
- [ ] Classe `SecurityFilter` interceptando header `Authorization`.
- [ ] Contexto de segurança injetado corretamente no `SecurityContextHolder`.
---

#### 🔹 [PBI-04] Endpoints de Autenticação (Login e Cadastro com Hash BCrypt)
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Segurança Stateless com Spring Security, Autenticação JWT e RBAC`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, AuthController, BCrypt`

##### Descrição (História de Usuário)
> **Como** munícipe ou gestor público,  
> **Eu quero** endpoints `POST /api/auth/register` e `POST /api/auth/login`,  
> **Para que** eu possa ingressar no sistema e obter meu token JWT de autenticação.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Cadastro com validação de e-mail único e hash BCrypt na senha.
- [ ] Retorno de token JWT e dados do usuário logado no endpoint de login.
- [ ] Tratamento de credenciais incorretas com status 401 Unauthorized.
---

### 🏆 [FEATURE 03] Regras de Negócio, Serviços Core e Ciclo de Vida de Ocorrências
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] GS 2026/2 - Java Advanced: API RESTful Spring Boot Core, Segurança JWT e Regras de Negócio de Zeladoria Urbana`
* **Title:** `[FEATURE 03] Regras de Negócio, Serviços Core e Ciclo de Vida de Ocorrências`
* **Tags:** `JavaAdvanced, Services, Chamados, SLA, RFC7807`
* **Start Date:** `2026-11-10`
* **Target Date:** `2026-11-16`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Description:** Camada de regras de negócio para abertura de ocorrências, cálculo de previsão SLA, votação e máquina de estados de status.
* **Acceptance Criteria:**
  - [x] CRUD completo de chamados com cálculo de previsão conforme prazo da categoria.
  - [x] Sistema de votação com bloqueio de voto duplicado (1 voto por usuário/chamado).
  - [x] Histórico de status gravado a cada alteração com autor e observações em HIST_STATUS.
  - [x] Paginação e ordenação nativas do Spring Data.

#### 🔹 [PBI-05] Serviços de Gestão de Chamados e Cálculo de Prazos SLA por Categoria
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] Regras de Negócio, Serviços Core e Ciclo de Vida de Ocorrências`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, ChamadoService, SLA`

##### Descrição (História de Usuário)
> **Como** munícipe que cadastra uma solicitação de reparo,  
> **Eu quero** que o sistema calcule automaticamente a data limite de atendimento com base no prazo da categoria,  
> **Para que** haja transparência no atendimento das demandas públicas.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Criação de chamado gravando `dt_abertura = now()` e `dt_previsao = now() + categoria.prazo`.
- [ ] Associação obrigatória com categoria e usuário autenticado.
- [ ] Status inicial gravado como `ABERTO`.
---

#### 🔹 [PBI-06] Mecanismo de Votação Comunitária e Auditoria de Transição em HistStatus
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] Regras de Negócio, Serviços Core e Ciclo de Vida de Ocorrências`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, Voto, HistStatus, Audit`

##### Descrição (História de Usuário)
> **Como** cidadão e gestor público,  
> **Eu quero** poder apoiar chamados abertos e visualizar todo o histórico de mudanças de status com justificativas,  
> **Para que** a priorização seja democrática e o processo seja 100% auditável.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Endpoint `POST /api/chamados/{id}/votos` com verificação de unicidade.
- [ ] Endpoint `PATCH /api/chamados/{id}/status` restrito a gestores públicos.
- [ ] Inserção atômica em `HIST_STATUS` registrando status anterior, novo status e autor.
---

#### 🔹 [PBI-07] Paginação, Filtros Dinâmicos por Bairro/Categoria e Tratamento Global RFC 7807
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] Regras de Negócio, Serviços Core e Ciclo de Vida de Ocorrências`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `JavaAdvanced, Pagination, RFC7807, ExceptionHandler`

##### Descrição (História de Usuário)
> **Como** cliente consumidor da API (Mobile/Frontend),  
> **Eu quero** endpoints paginados com filtros flexíveis e mensagens de erro estruturadas em Problem Details,  
> **Para que** a interface apresente feedback claro sem quebrar por erros inesperados.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Retorno paginado via `Pageable` e `Page<T>` nos endpoints de listagem.
- [ ] Classe `@RestControllerAdvice` tratando `MethodArgumentNotValidException`, `ResourceNotFoundException` e `AccessDeniedException`.
- [ ] Respostas de erro no padrão `application/problem+json` (RFC 7807).
---

### 🏆 [FEATURE 04] Documentação OpenAPI / Swagger UI e Qualidade de Código
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] GS 2026/2 - Java Advanced: API RESTful Spring Boot Core, Segurança JWT e Regras de Negócio de Zeladoria Urbana`
* **Title:** `[FEATURE 04] Documentação OpenAPI / Swagger UI e Qualidade de Código`
* **Tags:** `JavaAdvanced, Swagger, OpenAPI, JUnit5`
* **Start Date:** `2026-11-14`
* **Target Date:** `2026-11-19`
* **Priority:** `2 - High`
* **Effort (Story Points):** `2`
* **Business Value:** `80`
* **Description:** Documentação interativa completa dos endpoints e suíte de testes automatizados com JUnit 5 e Mockito.
* **Acceptance Criteria:**
  - [x] Swagger UI acessível em `/swagger-ui/index.html` com suporte a autenticação Bearer JWT.
  - [x] Todos os endpoints documentados com descrições e schemas de request/response.
  - [x] Cobertura de testes unitários para Services e Controllers com Mockito.

#### 🔹 [PBI-08] Documentação Interativa OpenAPI 3.0 e Cobertura de Testes Unitários JUnit 5
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 04] Documentação OpenAPI / Swagger UI e Qualidade de Código`
* **Priority:** `2 - High`
* **Effort (Story Points):** `2`
* **Tags:** `JavaAdvanced, OpenAPI, Testing`

##### Descrição (História de Usuário)
> **Como** avaliador e desenvolvedor frontend,  
> **Eu quero** testar todos os endpoints REST interativamente pela interface do Swagger UI com documentação de esquemas,  
> **Para que** a integração seja rápida e os contratos de API sejam transparentes.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Dependência `springdoc-openapi-starter-webmvc-ui` configurada.
- [ ] Anotações `@SecurityRequirement` e `@Operation` em todos os endpoints.
- [ ] Testes unitários com JUnit 5 cobrindo cenários positivos e negativos.