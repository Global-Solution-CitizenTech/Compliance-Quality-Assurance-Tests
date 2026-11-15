# Matriz de Casos de Teste — Azure Test Plans (ZelaFix / CitizenTech)

Matriz oficial de QA sincronizada 1:1 com o **Azure Test Plans** do projeto [`ZelaFixGS/ZelaFix`](https://dev.azure.com/ZelaFixGS/ZelaFix), com a arquitetura real da API/Worker (`Java-Advanced`), com o microserviço **ZelaBot AI** (`Disruptive-Architectures-IoT-IoB-IA`), com a modelagem Oracle/MongoDB (`Database-Advanced` — **13 tabelas** e **5 enums**) e com a suíte automatizada Postman (`57` requisições em `6` pastas).

---

## 1. Governança e Rastreabilidade no Azure DevOps

| Campo | Valor Oficial |
| :--- | :--- |
| **Organização / Projeto** | `ZelaFixGS` / `ZelaFix` |
| **Iteration Path** | `ZelaFix\Release 1 - Global Solution\Semana 2` |
| **Responsável / Owner (QA)** | Enzo Okuizumi Miranda de Souza (`RM561432@fiap.com.br`) |
| **Estado dos Test Cases** | `Ready` |
| **Test Plans / Test Suites** | **4 Test Plans** (`#132`, `#143`, `#153`, `#122`) e **4 Test Suites** (`#133`, `#144`, `#154`, `#123`) |
| **Total de Casos de Teste Ativos** | **25 Casos de Teste** (`15` Positivos / `10` Negativos) |
| **Higienização / Duplicados Removidos** | `14` casos duplicados/obsoletos removidos (`#125, #130, #135, #136, #138, #146, #150, #157, #159, #160, #162, #164, #165, #167`) |
| **Paridade Postman Automation** | [`CitizenTech_QA_Automation.postman_collection.json`](../postman/CitizenTech_QA_Automation.postman_collection.json) (`6` pastas, `57` requests com `pm.test()`) e [`CitizenTech_QA_Environment.postman_environment.json`](../postman/CitizenTech_QA_Environment.postman_environment.json) (`25` variáveis) |

---

## 2. Ambientes, Perfis Seeded e Enums Oficiais

### 2.1 Endpoints de Referência
- **API Java (`zelafix-api`):** Local `http://localhost:8080` | Cloud (Render) `https://zelafix-api.onrender.com`
- **ZelaBot AI (`deploy_zelafixai_render`):** Local `http://localhost:8000` | Cloud (Render) `https://zelafix-ai.onrender.com`
- **Worker Spring AI (`zelafix-worker`):** Assíncrono via RabbitMQ (`zelafix.chamados.triagem.queue` -> `zelafix.chamados.feedback.queue`), utilizando `ZelaFixAiService` + `TriagemNormativaTools`

### 2.2 Contas Semeadas para QA (Flyway `V2__admin_inicial.sql` e `V3__dados_iniciais_zelafix.sql`)
- **ADMIN:** `admin@zelafix.com.br` (perfil administrativo global)
- **GESTOR:** `roberto.gestor@subprefeitura.sp.gov.br` (gestor de subprefeitura habilitado para triagem/status)
- **CIDADAO:** `enzo.okuizumi@gmail.com` (bem como `ana.silva@gmail.com` e `lucas.gouveia@gmail.com`)

### 2.3 Contrato de Enums (Oracle DDL / Flyway / Java / MongoDB)
- **`CargoUsuario`:** `CIDADAO`, `GESTOR`, `ADMIN`
- **`CategoriaEnum`:** `BURACO`, `ILUMINACAO`, `LIXO`, `ALAGAMENTO`, `SEMAFORO`, `CALCADA`, `ARVORE`, `OUTROS`
- **`StatusChamadoEnum`:** `EM_ANALISE`, `EM_EXECUCAO`, `RESOLVIDO`, `REJEITADO`, `PENDENTE` *(sem estado `ABERTO`)*
- **`PrioridadeEnum`:** `BAIXA`, `MEDIA`, `ALTA`, `URGENTE`
- **`OrgaoGovernoEnum`:** `CET`, `SABESP`, `ENEL`, `SPTRANS`, `SUBPREFEITURA`, `BOMBEIROS`, `DEFESA_CIVIL`, `VERDE_MEIO_AMBIENTE`, `ILUME`, `LIMPEZA_URBANA`

---

## 3. Estrutura de Test Plans e Test Suites no Azure DevOps

| Plan ID | Suite ID | Test Plan / Suite | Escopo Arquitetural | Pastas Postman / Origem | Qtd. TCs |
| :--- | :--- | :--- | :--- | :--- | :---: |
| `#132` | `#133` | **`api-auth-rbac`** | Autenticação Stateless (JWT RSA Nimbus), Validação de Tokens e Controle de Acesso (RBAC) | 02, 03, 04, 05, 06 | **6** |
| `#143` | `#144` | **`api-usuarios-enderecos`** | Gestão de Usuários, Endereços (ViaCEP), Observabilidade e Respostas 404 | 01, 03, 04, 05, 06 | **6** |
| `#153` | `#154` | **`api-chamados`** | Ciclo de Vida de Chamados Multipart/BLOB, DeferredResult, Apoio Comunitário e Histórico | 05, 06 | **6** |
| `#122` | `#123` | **`ai-service`** | Worker Spring AI (RabbitMQ + Tools Normativas) e Microserviço ZelaBot AI (FastAPI + RAG ChromaDB + SQLite/Oracle) | 01, 05 + ZelaBot AI FastAPI | **7** |
| — | — | **TOTAL** | **4 Test Plans / 4 Test Suites** | **6 Pastas (`57` requests) + ZelaBot AI** | **25** |

---

## 4. Matriz Resumo de Cobertura (`TC-01` a `TC-25`)

| Código | Azure ID | Test Suite | Prioridade | Tipo | Endpoints / Componentes | Cobertura / Pasta Postman |
| :--- | :--- | :--- | :---: | :--- | :--- | :--- |
| **TC-01** | `#134` | `api-auth-rbac` | P1 | Positivo | `POST /login, GET /usuarios/me` | 02. Autenticação & RBAC / 03. Usuários (/usuarios) (02.1–02.3, 03.5) |
| **TC-02** | `#137` | `api-auth-rbac` | P1 | Negativo | `POST /login` | 02. Autenticação & RBAC (02.4–02.5) |
| **TC-03** | `#139` | `api-auth-rbac` | P1 | Negativo | `GET /usuarios, POST /enderecos, POST /chamados, PATCH /chamados/{id}/status` | 02. Autenticação & RBAC (02.6) |
| **TC-04** | `#140` | `api-auth-rbac` | P1 | Negativo | `GET /usuarios/me, GET /chamados` | 02. Autenticação & RBAC (02.7) |
| **TC-05** | `#141` | `api-auth-rbac` | P1 | Negativo | `GET /actuator/metrics, GET /usuarios, PATCH /usuarios/{id}/cargo, POST /enderecos, POST /chamados/ia/feedback` | 02. Autenticação & RBAC / 03. Usuários / 04. Endereços (02.8, 03.7, 03.12, 04.1) |
| **TC-06** | `#142` | `api-auth-rbac` | P1 | Negativo | `PATCH /chamados/{id}/status, DELETE /chamados/{id}` | 05. Chamados / 06. Teardown & Limpeza (05.11, 06.1) |
| **TC-07** | `#145` | `api-usuarios-enderecos` | P1 | Positivo | `POST /usuarios, POST /login, PUT /usuarios/me` | 03. Usuários (/usuarios) (03.1, 03.4–03.6) |
| **TC-08** | `#147` | `api-usuarios-enderecos` | P1 | Negativo | `POST /usuarios` | 03. Usuários (/usuarios) (03.2–03.3) |
| **TC-09** | `#148` | `api-usuarios-enderecos` | P2 | Positivo | `GET /usuarios, GET /usuarios/by-email, PUT /usuarios/{id}, PATCH /usuarios/{id}/cargo, DELETE /usuarios/{id}` | 03. Usuários / 06. Teardown & Limpeza (03.8–03.14, 06.5–06.6) |
| **TC-10** | `#149` | `api-usuarios-enderecos` | P1 | Positivo | `POST /enderecos, GET /enderecos, GET /enderecos/{id}, PUT /enderecos/{id}, DELETE /enderecos/{id}` | 04. Endereços (/enderecos — ADMIN only) (04.2, 04.4–04.8) |
| **TC-11** | `#151` | `api-usuarios-enderecos` | P2 | Negativo | `POST /enderecos` | 04. Endereços (/enderecos — ADMIN only) (04.3) |
| **TC-12** | `#152` | `api-usuarios-enderecos` | P2 | Positivo | `GET /actuator/health, GET /actuator/info, GET /v3/api-docs, GET /enderecos/{id}, GET /chamados/{id}` | 01. Observabilidade, Actuator & OpenAPI / 04. Endereços / 05. Chamados (01.1–01.4, 04.8, 05.9) |
| **TC-13** | `#155` | `api-chamados` | P1 | Positivo | `POST /chamados (multipart/form-data, DeferredResult)` | 05. Chamados, Triagem IA (DeferredResult) & Apoio (05.1) |
| **TC-14** | `#156` | `api-chamados` | P1 | Positivo | `GET /chamados/{id}/foto` | 05. Chamados, Triagem IA (DeferredResult) & Apoio (05.8) |
| **TC-15** | `#158` | `api-chamados` | P1 | Negativo | `POST /chamados` | 05. Chamados, Triagem IA (DeferredResult) & Apoio (05.2–05.3) |
| **TC-16** | `#161` | `api-chamados` | P1 | Positivo | `GET /chamados, GET /chamados/{id}, GET /chamados/estatisticas` | 05. Chamados, Triagem IA (DeferredResult) & Apoio (05.5–05.7, 05.16) |
| **TC-17** | `#163` | `api-chamados` | P1 | Positivo | `PUT /chamados/{id}, POST /chamados/{id}/apoiar, PATCH /chamados/{id}/status` | 05. Chamados, Triagem IA (DeferredResult) & Apoio (05.10, 05.12–05.15) |
| **TC-18** | `#166` | `api-chamados` | P1 | Positivo | `DELETE /chamados/{id}, GET /chamados/{id}, DELETE /usuarios/me` | 06. Teardown & Limpeza (06.2–06.4) |
| **TC-19** | `#124` | `ai-service` | P1 | Positivo | `POST /chamados, RabbitMQ zelafix.chamados.triagem.queue -> zelafix.chamados.feedback.queue` | 01. Observabilidade / 05. Chamados, Triagem IA (01.2, 05.1) |
| **TC-20** | `#126` | `ai-service` | P1 | Negativo | `POST /chamados, TriagemPendenteStore, GET /chamados/estatisticas` | 05. Chamados, Triagem IA (DeferredResult) & Apoio (05.4) |
| **TC-21** | `#127` | `ai-service` | P1 | Positivo | `POST /ai/chat, POST /ai/chat/public` | ZelaBot AI FastAPI (test_zelafix_scenarios.py) |
| **TC-22** | `#128` | `ai-service` | P1 | Positivo | `POST /ai/chat` | ZelaBot AI FastAPI (test_zelafix_scenarios.py) |
| **TC-23** | `#129` | `ai-service` | P2 | Negativo | `POST /ai/chat` | ZelaBot AI FastAPI (test_zelafix_scenarios.py) |
| **TC-24** | `#131` | `ai-service` | P1 | Positivo | `POST /ai/triagem, POST /ai/insights` | ZelaBot AI FastAPI (test_zelafix_scenarios.py) |
| **TC-25** | `#197` | `ai-service` | P2 | Positivo | `GET /, GET /health, GET /health/ready, GET /ai/vector-store/status, GET /ai/oracle/status, GET /ai/history, GET /ai/audit, GET /ai/sessions, GET /ai/chamados/{id}, DELETE /ai/sessions/{session_id}` | ZelaBot AI FastAPI (health.py / ai.py) |

---

## 5. Especificação Detalhada dos Casos de Teste

### Plan `#132` / Suite `#133` — `api-auth-rbac` (6 Casos de Teste)

> Autenticação Stateless (JWT RSA Nimbus), Validação de Tokens e Controle de Acesso (RBAC)

#### [TC-01] Autenticar contas de QA (ADMIN, GESTOR e CIDADAO) e validar GET /usuarios/me

- **Azure Test Case ID:** `#134` | **Plan/Suite:** `#132` / `#133` (`api-auth-rbac`) | **Tipo:** `Positivo` | **Prioridade:** `P1` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `Auth`, `RBAC`
- **Cobertura / Endpoints:** 02. Autenticação & RBAC / 03. Usuários (/usuarios) (02.1–02.3, 03.5) (`POST /login, GET /usuarios/me`)
- **Objetivo:** Validar autenticação stateless via JWT RSA (Nimbus) para os três perfis semeados via Flyway (ADMIN, GESTOR e CIDADAO) e conferência do perfil autenticado.
- **Pré-condições:** API Java (zelafix-api) e banco Oracle ativos com migrations Flyway V1/V2/V3 executadas (admin@zelafix.com.br, roberto.gestor@subprefeitura.sp.gov.br, enzo.okuizumi@gmail.com).
- **Dados de Entrada / Payload:** POST /login com JSON { "email": "<email_seed>", "senha": "<senha_seed>" } para ADMIN, GESTOR e CIDADAO; em seguida GET /usuarios/me com Authorization: Bearer <token>.
- **Resultado Esperado & HTTP Codes:** HTTP 200 OK em POST /login com { token, user: { id, nome, email, cargo, ddd, numeroTelefone, endereco } } e HTTP 200 OK em GET /usuarios/me com cargo correspondente.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Enviar POST /login com as credenciais do perfil ADMIN (admin@zelafix.com.br). | API retorna HTTP 200 OK com token JWT RSA e user.cargo igual a 'ADMIN'. |
| 2 | Enviar GET /usuarios/me utilizando o header Authorization: Bearer <adminToken>. | API retorna HTTP 200 OK com os dados completos do Administrador Geral. |
| 3 | Repetir POST /login e GET /usuarios/me para o perfil GESTOR (roberto.gestor@subprefeitura.sp.gov.br). | API retorna HTTP 200 OK com token válido e user.cargo igual a 'GESTOR'. |
| 4 | Repetir POST /login e GET /usuarios/me para o perfil CIDADAO (enzo.okuizumi@gmail.com). | API retorna HTTP 200 OK com token válido e user.cargo igual a 'CIDADAO'. |

#### [TC-02] Rejeitar login com credenciais invalidas ou payload malformado

- **Azure Test Case ID:** `#137` | **Plan/Suite:** `#132` / `#133` (`api-auth-rbac`) | **Tipo:** `Negativo` | **Prioridade:** `P1` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `Auth`, `Negative`
- **Cobertura / Endpoints:** 02. Autenticação & RBAC (02.4–02.5) (`POST /login`)
- **Objetivo:** Confirmar que senhas incorretas, e-mails inexistentes e payloads inválidos em POST /login são rejeitados sem emissão de token.
- **Pré-condições:** API Java disponível; conta de QA existente na base.
- **Dados de Entrada / Payload:** Subcaso A: senha incorreta; Subcaso B: e-mail inexistente; Subcaso C: e-mail fora do padrão ou campos em branco.
- **Resultado Esperado & HTTP Codes:** HTTP 401 Unauthorized (ApiErrorResponse) para credenciais inválidas; HTTP 400 Bad Request ({ erros: [{ campo, mensagem }] }) para falha de Bean Validation.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Enviar POST /login com e-mail válido e senha incorreta. | API retorna HTTP 401 Unauthorized com ApiErrorResponse e mensagem de credenciais inválidas, sem emitir token. |
| 2 | Enviar POST /login com e-mail não cadastrado na base. | API retorna HTTP 401 Unauthorized com ApiErrorResponse. |
| 3 | Enviar POST /login com formato de e-mail inválido e senha em branco. | API retorna HTTP 400 Bad Request com lista 'erros' detalhando os campos 'email' e 'senha'. |

#### [TC-03] Bloquear endpoints protegidos sem token Bearer

- **Azure Test Case ID:** `#139` | **Plan/Suite:** `#132` / `#133` (`api-auth-rbac`) | **Tipo:** `Negativo` | **Prioridade:** `P1` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `Security`, `Negative`
- **Cobertura / Endpoints:** 02. Autenticação & RBAC (02.6) (`GET /usuarios, POST /enderecos, POST /chamados, PATCH /chamados/{id}/status`)
- **Objetivo:** Garantir que todas as rotas protegidas pelo SecurityFilterChain rejeitem requisições anônimas sem header Authorization.
- **Pré-condições:** API Java disponível.
- **Dados de Entrada / Payload:** Requisições GET /usuarios/me, GET /chamados e POST /chamados sem header Authorization.
- **Resultado Esperado & HTTP Codes:** HTTP 401 Unauthorized em todas as tentativas sem credencial Bearer.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Enviar GET /usuarios/me sem header Authorization. | API bloqueia a requisição retornando HTTP 401 Unauthorized. |
| 2 | Enviar GET /chamados sem header Authorization. | API bloqueia a requisição retornando HTTP 401 Unauthorized. |
| 3 | Enviar POST /chamados multipart sem header Authorization. | API bloqueia a requisição retornando HTTP 401 Unauthorized antes de processar upload. |

#### [TC-04] Rejeitar token JWT invalido ou assinatura adulterada

- **Azure Test Case ID:** `#140` | **Plan/Suite:** `#132` / `#133` (`api-auth-rbac`) | **Tipo:** `Negativo` | **Prioridade:** `P1` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `Security`, `Negative`
- **Cobertura / Endpoints:** 02. Autenticação & RBAC (02.7) (`GET /usuarios/me, GET /chamados`)
- **Objetivo:** Confirmar que o NimbusJwtDecoder rejeita tokens malformados, expirados ou com assinatura RSA inválida.
- **Pré-condições:** API Java disponível.
- **Dados de Entrada / Payload:** Header Authorization: Bearer token.invalido.assinatura em GET /usuarios/me e GET /chamados.
- **Resultado Esperado & HTTP Codes:** HTTP 401 Unauthorized sem acesso aos dados protegidos.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Enviar GET /usuarios/me com Authorization: Bearer token.invalido.assinatura. | Spring Security OAuth2 Resource Server rejeita a assinatura e retorna HTTP 401 Unauthorized. |
| 2 | Enviar GET /chamados com token JWT truncado/adulterado. | API retorna HTTP 401 Unauthorized. |

#### [TC-05] Bloquear acesso de CIDADAO a endpoints administrativos (RBAC)

- **Azure Test Case ID:** `#141` | **Plan/Suite:** `#132` / `#133` (`api-auth-rbac`) | **Tipo:** `Negativo` | **Prioridade:** `P1` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `RBAC`, `Negative`
- **Cobertura / Endpoints:** 02. Autenticação & RBAC / 03. Usuários / 04. Endereços (02.8, 03.7, 03.12, 04.1) (`GET /actuator/metrics, GET /usuarios, PATCH /usuarios/{id}/cargo, POST /enderecos, POST /chamados/ia/feedback`)
- **Objetivo:** Validar restrições @PreAuthorize('hasRole("ADMIN")') e SecurityConfig para rotas administrativas.
- **Pré-condições:** Token JWT válido do perfil CIDADAO.
- **Dados de Entrada / Payload:** Requisições autenticadas como CIDADAO para GET /enderecos, GET /usuarios, PATCH /usuarios/2/cargo e GET /actuator/metrics.
- **Resultado Esperado & HTTP Codes:** HTTP 403 Forbidden (ApiErrorResponse) em todas as rotas exclusivas de ADMIN.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Autenticado como CIDADAO, enviar GET /enderecos. | API retorna HTTP 403 Forbidden (ApiErrorResponse). |
| 2 | Autenticado como CIDADAO, enviar GET /usuarios e PATCH /usuarios/2/cargo com { "cargo": "ADMIN" }. | API retorna HTTP 403 Forbidden em ambas as tentativas. |
| 3 | Autenticado como CIDADAO, enviar GET /actuator/metrics. | API retorna HTTP 403 Forbidden conforme regra do SecurityFilterChain. |

#### [TC-06] Impedir CIDADAO de alterar status e GESTOR nao-autor de excluir chamado

- **Azure Test Case ID:** `#142` | **Plan/Suite:** `#132` / `#133` (`api-auth-rbac`) | **Tipo:** `Negativo` | **Prioridade:** `P1` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `RBAC`, `Negative`
- **Cobertura / Endpoints:** 05. Chamados / 06. Teardown & Limpeza (05.11, 06.1) (`PATCH /chamados/{id}/status, DELETE /chamados/{id}`)
- **Objetivo:** Validar isolamento RBAC nas operações de ciclo de vida de chamados (PATCH /status restrito a GESTOR/ADMIN e DELETE restrito ao Autor ou ADMIN).
- **Pré-condições:** Tokens JWT válidos de CIDADAO e GESTOR; chamado existente criado por outro usuário (ex.: seed ID 1).
- **Dados de Entrada / Payload:** PATCH /chamados/{id}/status como CIDADAO ({ "status": "EM_EXECUCAO", "observacao": "Teste" }); DELETE /chamados/{id} como GESTOR não autor.
- **Resultado Esperado & HTTP Codes:** HTTP 403 Forbidden (ApiErrorResponse) em ambas as operações não autorizadas.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Autenticado como CIDADAO, enviar PATCH /chamados/1/status com { "status": "EM_EXECUCAO", "observacao": "Tentativa indevida" }. | API bloqueia via @PreAuthorize('hasAnyRole(GESTOR, ADMIN)') e retorna HTTP 403 Forbidden. |
| 2 | Autenticado como GESTOR (não autor do chamado 1), enviar DELETE /chamados/1. | ChamadoService.validarPermissaoExclusao lança AccessDeniedException e API retorna HTTP 403 Forbidden. |

### Plan `#143` / Suite `#144` — `api-usuarios-enderecos` (6 Casos de Teste)

> Gestão de Usuários, Endereços (ViaCEP), Observabilidade e Respostas 404

#### [TC-07] Cadastrar novo cidadao (POST /usuarios) e atualizar perfil (/usuarios/me)

- **Azure Test Case ID:** `#145` | **Plan/Suite:** `#143` / `#144` (`api-usuarios-enderecos`) | **Tipo:** `Positivo` | **Prioridade:** `P1` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `Usuarios`
- **Cobertura / Endpoints:** 03. Usuários (/usuarios) (03.1, 03.4–03.6) (`POST /usuarios, POST /login, PUT /usuarios/me`)
- **Objetivo:** Validar o fluxo completo de autocadastro público do cidadão, login imediato e atualização de perfil com renovação de JWT via header X-Novo-Token.
- **Pré-condições:** API Java e integração ViaCEP operacionais; e-mail inédito para QA.
- **Dados de Entrada / Payload:** POST /usuarios com UsuarioRequest { nome, email, senha, ddd, numeroTelefone, endereco: { cep, numero, referencia, rua } }; PUT /usuarios/me com dados atualizados.
- **Resultado Esperado & HTTP Codes:** HTTP 201 Created em POST /usuarios com cargo='CIDADAO' forçado; HTTP 200 OK em PUT /usuarios/me com header X-Novo-Token válido.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Enviar POST /usuarios sem token com payload UsuarioRequest válido (CEP '01310-100', DDD '11', telefone 9 dígitos). | API cria o usuário com cargo 'CIDADAO' (ignorando qualquer tentativa de elevação) e retorna HTTP 201 Created. |
| 2 | Autenticar o usuário recém-criado via POST /login. | API retorna HTTP 200 OK com token Bearer válido. |
| 3 | Enviar PUT /usuarios/me com novo nome/telefone autenticado pelo token do cidadão. | API retorna HTTP 200 OK com os dados atualizados e devolve o novo token no header 'X-Novo-Token'. |
| 4 | Consultar GET /usuarios/me usando o novo token recebido. | API retorna HTTP 200 OK refletindo o perfil atualizado. |

#### [TC-08] Rejeitar cadastro com e-mail duplicado (409) ou dados invalidos (400)

- **Azure Test Case ID:** `#147` | **Plan/Suite:** `#143` / `#144` (`api-usuarios-enderecos`) | **Tipo:** `Negativo` | **Prioridade:** `P1` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `Usuarios`, `Negative`
- **Cobertura / Endpoints:** 03. Usuários (/usuarios) (03.2–03.3) (`POST /usuarios`)
- **Objetivo:** Validar tratamento de violação de chave única no Oracle (ORA-00001 -> 409 Conflict) e regras de Bean Validation / @DddValidation no UsuarioRequest.
- **Pré-condições:** API Java disponível; conta 'enzo.okuizumi@gmail.com' já cadastrada.
- **Dados de Entrada / Payload:** Subcaso A: POST /usuarios com e-mail existente; Subcaso B: DDD inválido ('00'), senha curta (<6 chars) e CEP fora do padrão.
- **Resultado Esperado & HTTP Codes:** HTTP 409 Conflict (ApiErrorResponse) para e-mail duplicado; HTTP 400 Bad Request ({ erros: [...] }) para dados inválidos.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Enviar POST /usuarios com e-mail já existente na base. | GlobalExceptionHandler mapeia ORA-00001 e retorna HTTP 409 Conflict. |
| 2 | Enviar POST /usuarios com DDD inválido ('00'), senha com 3 caracteres e CEP inválido. | API rejeita via Bean Validation retornando HTTP 400 Bad Request com array 'erros'. |

#### [TC-09] Gerenciar usuarios como ADMIN (listar, by-email, PATCH cargo e DELETE)

- **Azure Test Case ID:** `#148` | **Plan/Suite:** `#143` / `#144` (`api-usuarios-enderecos`) | **Tipo:** `Positivo` | **Prioridade:** `P2` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `Usuarios`, `Admin`
- **Cobertura / Endpoints:** 03. Usuários / 06. Teardown & Limpeza (03.8–03.14, 06.5–06.6) (`GET /usuarios, GET /usuarios/by-email, PUT /usuarios/{id}, PATCH /usuarios/{id}/cargo, DELETE /usuarios/{id}`)
- **Objetivo:** Validar as operações administrativas de gestão de contas (listagem paginada, busca por ID/e-mail, alteração de cargo e exclusão de usuário descartável).
- **Pré-condições:** Token JWT ADMIN; usuário descartável sem chamados vinculados criado para teste.
- **Dados de Entrada / Payload:** GET /usuarios?page=0&size=10; GET /usuarios/by-email?email=...; GET /usuarios/{id}; PATCH /usuarios/{id}/cargo ({ "cargo": "GESTOR" }); DELETE /usuarios/{id}.
- **Resultado Esperado & HTTP Codes:** HTTP 200 OK nas consultas e alteração de cargo; HTTP 204 No Content na exclusão e HTTP 404 Not Found em consulta posterior.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Como ADMIN, enviar GET /usuarios?page=0&size=10. | API retorna HTTP 200 OK com Page<UsuarioResponse>. |
| 2 | Como ADMIN, enviar GET /usuarios/by-email?email=<qaEmail> e GET /usuarios/{id}. | API retorna HTTP 200 OK com o usuário localizado. |
| 3 | Como ADMIN, enviar PATCH /usuarios/{id}/cargo com { "cargo": "GESTOR" } (e validar 400 ao enviar cargo inválido). | API atualiza cargo para 'GESTOR' com HTTP 200 OK. |
| 4 | Como ADMIN, enviar DELETE /usuarios/{id} no usuário descartável e confirmar GET /usuarios/{id}. | Exclusão retorna HTTP 204 No Content e consulta posterior retorna HTTP 404 Not Found. |

#### [TC-10] Criar, listar, atualizar e excluir endereco como ADMIN com ViaCEP

- **Azure Test Case ID:** `#149` | **Plan/Suite:** `#143` / `#144` (`api-usuarios-enderecos`) | **Tipo:** `Positivo` | **Prioridade:** `P1` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `Enderecos`, `ViaCEP`
- **Cobertura / Endpoints:** 04. Endereços (/enderecos — ADMIN only) (04.2, 04.4–04.8) (`POST /enderecos, GET /enderecos, GET /enderecos/{id}, PUT /enderecos/{id}, DELETE /enderecos/{id}`)
- **Objetivo:** Validar o ciclo CRUD completo de endereços exclusivos do perfil ADMIN com normalização de CEP (8 dígitos) e resolução automática de logradouro/bairro/cidade/estado via ViaCEP.
- **Pré-condições:** API Java e integração ViaCEP disponíveis; token ADMIN.
- **Dados de Entrada / Payload:** POST /enderecos { "cep": "01310-100", "numero": "1578", "referencia": "Em frente ao MASP" }; GET /enderecos/{id}; PUT /enderecos/{id}; DELETE /enderecos/{id}.
- **Resultado Esperado & HTTP Codes:** HTTP 201 Created na criação (CEP normalizado para '01310100' e bairro/cidade/estado resolvidos), HTTP 200 OK nas consultas/edição e HTTP 204 No Content na remoção.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Como ADMIN, enviar POST /enderecos omitindo 'rua' para acionar resolução automática ViaCEP. | API retorna HTTP 201 Created com 'cep' normalizado sem hífen, 'rua', 'bairro', 'cidade' e 'estado' preenchidos. |
| 2 | Enviar GET /enderecos/{id} e GET /enderecos?page=0&size=10. | API retorna HTTP 200 OK com os dados persistidos. |
| 3 | Enviar PUT /enderecos/{id} alterando 'numero' e 'referencia'. | API retorna HTTP 200 OK com o endereço atualizado. |
| 4 | Enviar DELETE /enderecos/{id} e confirmar GET /enderecos/{id}. | API retorna HTTP 204 No Content na exclusão e HTTP 404 Not Found após remoção. |

#### [TC-11] Rejeitar criacao de endereco com CEP ou campos obrigatorios invalidos

- **Azure Test Case ID:** `#151` | **Plan/Suite:** `#143` / `#144` (`api-usuarios-enderecos`) | **Tipo:** `Negativo` | **Prioridade:** `P2` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `Enderecos`, `Negative`
- **Cobertura / Endpoints:** 04. Endereços (/enderecos — ADMIN only) (04.3) (`POST /enderecos`)
- **Objetivo:** Confirmar validação do padrão regex do CEP (^\d{5}-?\d{3}$), obrigatoriedade de numero/referencia e erro quando o CEP não existe no ViaCEP.
- **Pré-condições:** Token JWT ADMIN.
- **Dados de Entrada / Payload:** Subcaso A: cep='ABC-XYZ', numero='', referencia=''; Subcaso B: cep='00000000' inexistente.
- **Resultado Esperado & HTTP Codes:** HTTP 400 Bad Request ({ erros: [...] }) para formato inválido/campos vazios; HTTP 400 Bad Request (ApiErrorResponse) para CEP não encontrado.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Como ADMIN, enviar POST /enderecos com cep='ABC-XYZ', numero='' e referencia=''. | API retorna HTTP 400 Bad Request com array 'erros' listando 'cep', 'numero' e 'referencia'. |
| 2 | Como ADMIN, enviar POST /enderecos com CEP sintaticamente válido porém inexistente ('00000-000'). | ViaCEP/EnderecoService rejeita e API retorna HTTP 400 Bad Request. |

#### [TC-12] Validar observabilidade (/actuator/health, /v3/api-docs) e 404 para IDs inexistentes

- **Azure Test Case ID:** `#152` | **Plan/Suite:** `#143` / `#144` (`api-usuarios-enderecos`) | **Tipo:** `Positivo` | **Prioridade:** `P2` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `Observabilidade`
- **Cobertura / Endpoints:** 01. Observabilidade, Actuator & OpenAPI / 04. Endereços / 05. Chamados (01.1–01.4, 04.8, 05.9) (`GET /actuator/health, GET /actuator/info, GET /v3/api-docs, GET /enderecos/{id}, GET /chamados/{id}`)
- **Objetivo:** Verificar endpoints públicos de healthcheck e OpenAPI da API/Worker, acesso restrito a /actuator/metrics para ADMIN e padronização de resposta HTTP 404.
- **Pré-condições:** API Java e Worker Spring AI em execução.
- **Dados de Entrada / Payload:** GET /actuator/health (API e Worker), GET /actuator/info, GET /v3/api-docs, GET /actuator/metrics (ADMIN), GET /enderecos/999999 e GET /usuarios/999999.
- **Resultado Esperado & HTTP Codes:** HTTP 200 OK para health/info/api-docs/metrics (ADMIN) e HTTP 404 Not Found (ApiErrorResponse) para IDs inexistentes.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Enviar GET /actuator/health na API Java e no Worker Spring AI. | Ambos retornam HTTP 200 OK com status 'UP'. |
| 2 | Enviar GET /v3/api-docs e GET /actuator/info na API Java. | API retorna HTTP 200 OK com especificação OpenAPI 3.0 e metadados da aplicação. |
| 3 | Autenticado como ADMIN, enviar GET /actuator/metrics. | API retorna HTTP 200 OK com lista de métricas disponíveis. |
| 4 | Autenticado como ADMIN, enviar GET /enderecos/999999 e GET /usuarios/999999. | API retorna HTTP 404 Not Found com payload ApiErrorResponse padronizado. |

### Plan `#153` / Suite `#154` — `api-chamados` (6 Casos de Teste)

> Ciclo de Vida de Chamados Multipart/BLOB, DeferredResult, Apoio Comunitário e Histórico

#### [TC-13] Abrir chamado multipart/form-data via DeferredResult e triagem IA (POST /chamados)

- **Azure Test Case ID:** `#155` | **Plan/Suite:** `#153` / `#154` (`api-chamados`) | **Tipo:** `Positivo` | **Prioridade:** `P1` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `Chamados`, `DeferredResult`
- **Cobertura / Endpoints:** 05. Chamados, Triagem IA (DeferredResult) & Apoio (05.1) (`POST /chamados (multipart/form-data, DeferredResult)`)
- **Objetivo:** Validar a criação de ocorrência urbana exclusivamente via multipart/form-data com DeferredResult (timeout 60s), publicação no RabbitMQ e persistência pós-triagem IA no Oracle.
- **Pré-condições:** API Java, RabbitMQ, Worker Spring AI e Oracle ativos; token CIDADAO válido; imagem real de ocorrência urbana (ex.: Java-Advanced/docs/rua-esburacada.png).
- **Dados de Entrada / Payload:** POST /chamados (multipart/form-data) com campos cep='01310-100', numero='1000', referencia='Proximo ao MASP', rua='Avenida Paulista' e part 'foto' (image/png ou image/jpeg).
- **Resultado Esperado & HTTP Codes:** HTTP 201 Created com ChamadoResponse contendo idChamado, titulo, descricao, categoriaNome (6 enums), prioridadeNome (4 enums), orgaoNome (6 enums), status='EM_ANALISE' (ou 'PENDENTE' em contingência), totalVotos=1, apoiadoPorMim=true e historico[].

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Autenticado como CIDADAO, enviar POST /chamados em multipart/form-data com cep, numero, referencia, rua e part 'foto' contendo foto real de problema urbano. | API valida magic bytes da imagem, resolve endereço e mantém conexão assíncrona via DeferredResult aguardando retorno do Worker. |
| 2 | Aguardar conclusão da triagem assíncrona via RabbitMQ. | API retorna HTTP 201 Created com ChamadoResponse completo (idChamado gerado, titulo/descricao gerados pela IA, enums válidos, totalVotos=1, apoiadoPorMim=true). |
| 3 | Verificar o array 'historico' e o campo 'foto' no JSON retornado. | historico contém registro inicial ('EM_ANALISE' ou 'PENDENTE') e foto aponta para '/chamados/{idChamado}/foto'. |

#### [TC-14] Recuperar foto BLOB do chamado com MIME dinamico (GET /chamados/{id}/foto)

- **Azure Test Case ID:** `#156` | **Plan/Suite:** `#153` / `#154` (`api-chamados`) | **Tipo:** `Positivo` | **Prioridade:** `P1` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `Chamados`, `BLOB`
- **Cobertura / Endpoints:** 05. Chamados, Triagem IA (DeferredResult) & Apoio (05.8) (`GET /chamados/{id}/foto`)
- **Objetivo:** Validar o endpoint público de download da evidência fotográfica armazenada em BLOB no Oracle com detecção dinâmica de Content-Type (ImageMimeTypeDetector).
- **Pré-condições:** Chamado existente com foto BLOB persistida (ex.: chamado criado no TC-13 ou seed ID 1).
- **Dados de Entrada / Payload:** GET /chamados/{id}/foto sem header Authorization; GET /chamados/999999/foto.
- **Resultado Esperado & HTTP Codes:** HTTP 200 OK com bytes binários da imagem, header Content-Type image/jpeg|png|webp|gif e Content-Disposition: inline; HTTP 404 Not Found para ID inexistente.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Enviar GET /chamados/{id}/foto sem enviar token Bearer. | API responde HTTP 200 OK (rota pública conforme SecurityConfig) com Content-Type compatível (image/*) e Content-Disposition: inline. |
| 2 | Confirmar que o corpo binário possui assinatura válida de imagem (tamanho > 0). | Bytes correspondem integralmente à imagem armazenada em BLOB no Oracle. |
| 3 | Enviar GET /chamados/999999/foto para ID inexistente. | API retorna HTTP 404 Not Found com ApiErrorResponse. |

#### [TC-15] Rejeitar abertura de chamado com part foto ausente, arquivo invalido ou endereco invalido

- **Azure Test Case ID:** `#158` | **Plan/Suite:** `#153` / `#154` (`api-chamados`) | **Tipo:** `Negativo` | **Prioridade:** `P1` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `Chamados`, `Negative`
- **Cobertura / Endpoints:** 05. Chamados, Triagem IA (DeferredResult) & Apoio (05.2–05.3) (`POST /chamados`)
- **Objetivo:** Verificar validações de entrada síncronas em POST /chamados antes de publicar na fila RabbitMQ.
- **Pré-condições:** Token JWT CIDADAO válido.
- **Dados de Entrada / Payload:** Subcaso A: multipart sem part 'foto'; Subcaso B: part 'foto' com arquivo texto/PDF não-imagem; Subcaso C: EnderecoRequest com cep='invalido', numero='' e referencia=''.
- **Resultado Esperado & HTTP Codes:** HTTP 400 Bad Request em todos os subcasos (ApiErrorResponse para foto ausente/inválida; { erros: [...] } para EnderecoRequest inválido).

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Enviar POST /chamados multipart sem incluir a part 'foto'. | GlobalExceptionHandler (MissingServletRequestPartException) retorna HTTP 400 Bad Request. |
| 2 | Enviar POST /chamados com part 'foto' contendo bytes de texto plano (.txt) em vez de imagem. | ImageMimeTypeDetector rejeita os magic bytes e API retorna HTTP 400 Bad Request. |
| 3 | Enviar POST /chamados com cep='invalido', numero='' e referencia=''. | Bean Validation retorna HTTP 400 Bad Request com array 'erros'. |

#### [TC-16] Consultar chamados paginados com filtros dinamicos e painel de estatisticas

- **Azure Test Case ID:** `#161` | **Plan/Suite:** `#153` / `#154` (`api-chamados`) | **Tipo:** `Positivo` | **Prioridade:** `P1` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `Chamados`
- **Cobertura / Endpoints:** 05. Chamados, Triagem IA (DeferredResult) & Apoio (05.5–05.7, 05.16) (`GET /chamados, GET /chamados/{id}, GET /chamados/estatisticas`)
- **Objetivo:** Validar paginação Spring Data, combinação de filtros dinâmicos (status, categoria, busca, apenasMeus, cidade, bairro, estado) e indicadores do dashboard.
- **Pré-condições:** Token JWT CIDADAO; pelo menos um chamado existente na base.
- **Dados de Entrada / Payload:** GET /chamados?page=0&size=10; GET /chamados?apenasMeus=true; GET /chamados?status=EM_ANALISE&categoria=VIAS_E_PAVIMENTACAO&bairro=Pinheiros; GET /chamados/estatisticas.
- **Resultado Esperado & HTTP Codes:** HTTP 200 OK com estrutura Page<ChamadoResponse> e EstatisticasResponse { total, abertos, emAndamento, resolvidos, rejeitados, totalApoios }.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Enviar GET /chamados?page=0&size=10 autenticado. | API retorna HTTP 200 OK com Page<ChamadoResponse> paginada. |
| 2 | Enviar GET /chamados?apenasMeus=true. | API retorna apenas chamados onde usuarioId corresponde ao usuário autenticado. |
| 3 | Enviar GET /chamados com filtros combinados (status, categoria, bairro, busca). | API aplica os filtros corretamente sem erros de query JPA. |
| 4 | Enviar GET /chamados/estatisticas. | API retorna HTTP 200 OK com os 6 contadores numéricos consolidados. |

#### [TC-17] Atualizar chamado, alternar apoio comunitario e evoluir status com historico

- **Azure Test Case ID:** `#163` | **Plan/Suite:** `#153` / `#154` (`api-chamados`) | **Tipo:** `Positivo` | **Prioridade:** `P1` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `Chamados`, `RabbitMQ`
- **Cobertura / Endpoints:** 05. Chamados, Triagem IA (DeferredResult) & Apoio (05.10, 05.12–05.15) (`PUT /chamados/{id}, POST /chamados/{id}/apoiar, PATCH /chamados/{id}/status`)
- **Objetivo:** Validar edição de dados (PUT), alternância de voto comunitário (POST /apoiar + RabbitMQ), transições FSM de status (PATCH /status como GESTOR/ADMIN) e rastreabilidade do histórico.
- **Pré-condições:** Chamado descartável criado; tokens CIDADAO (autor) e GESTOR/ADMIN.
- **Dados de Entrada / Payload:** PUT /chamados/{id} (ChamadoRequest); POST /chamados/{id}/apoiar (2x para toggle OFF/ON); PATCH /chamados/{id}/status ({ "status": "EM_EXECUCAO" | "CONCLUIDO", "observacao": "..." }).
- **Resultado Esperado & HTTP Codes:** HTTP 200 OK em todas as etapas; totalVotos e apoiadoPorMim alternam corretamente; GET /chamados/{id} exibe historico[] ordenado do mais recente ao mais antigo.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Como autor (ou GESTOR/ADMIN), enviar PUT /chamados/{id} com novo título, descrição, CategoriaEnum e EnderecoRequest. | API retorna HTTP 200 OK com os dados atualizados. |
| 2 | Enviar POST /chamados/{id}/apoiar (toggle OFF) e repetir POST /chamados/{id}/apoiar (toggle ON). | A cada chamada HTTP 200 OK, totalVotos e apoiadoPorMim alternam e VotoEventProducer publica evento em chamado.voto.queue. |
| 3 | Como GESTOR ou ADMIN, enviar PATCH /chamados/{id}/status para EM_EXECUCAO e depois CONCLUIDO com 'observacao' preenchida. | API retorna HTTP 200 OK e grava cada transição em HIST_CHAMADO. |
| 4 | Enviar PATCH /chamados/{id}/status com status inexistente ou observacao em branco. | API rejeita via @EnumValidation / @NotBlank retornando HTTP 400 Bad Request. |
| 5 | Consultar GET /chamados/{id}. | API retorna HTTP 200 OK com historico[] completo em ordem cronológica decrescente. |

#### [TC-18] Excluir chamado como Autor ou ADMIN e confirmar remocao em cascata (404)

- **Azure Test Case ID:** `#166` | **Plan/Suite:** `#153` / `#154` (`api-chamados`) | **Tipo:** `Positivo` | **Prioridade:** `P1` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `Chamados`
- **Cobertura / Endpoints:** 06. Teardown & Limpeza (06.2–06.4) (`DELETE /chamados/{id}, GET /chamados/{id}, DELETE /usuarios/me`)
- **Objetivo:** Validar exclusão de chamado com remoção em cascata de votos (VOTO_CHAMADO) e históricos (HIST_CHAMADO), confirmando ausência posterior do recurso.
- **Pré-condições:** Chamado descartável existente; token do Autor ou ADMIN.
- **Dados de Entrada / Payload:** DELETE /chamados/{id} seguido de GET /chamados/{id} e GET /chamados/{id}/foto.
- **Resultado Esperado & HTTP Codes:** HTTP 204 No Content na exclusão e HTTP 404 Not Found nas consultas subsequentes.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Autenticado como Autor ou ADMIN, enviar DELETE /chamados/{id}. | API remove votos, histórico e chamado e retorna HTTP 204 No Content. |
| 2 | Enviar GET /chamados/{id} e GET /chamados/{id}/foto após a exclusão. | Ambas as consultas retornam HTTP 404 Not Found confirmando remoção definitiva. |

### Plan `#122` / Suite `#123` — `ai-service` (7 Casos de Teste)

> Worker Spring AI (RabbitMQ + Tools Normativas) e Microserviço ZelaBot AI (FastAPI + RAG ChromaDB + SQLite/Oracle)

#### [TC-19] Confirmar triagem assincrona do Worker Spring AI com Tools normativas e SLA

- **Azure Test Case ID:** `#124` | **Plan/Suite:** `#122` / `#123` (`ai-service`) | **Tipo:** `Positivo` | **Prioridade:** `P1` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `WorkerAI`, `RabbitMQ`
- **Cobertura / Endpoints:** 01. Observabilidade / 05. Chamados, Triagem IA (01.2, 05.1) (`POST /chamados, RabbitMQ zelafix.chamados.triagem.queue -> zelafix.chamados.feedback.queue`)
- **Objetivo:** Validar o pipeline reativo zelafix-api -> RabbitMQ (chamado.triagem.queue) -> zelafix-worker (ZelaFixAiService + TriagemNormativaTools @Tool + @Retryable) -> chamado.triagem-concluida.queue com classificação nos enums oficiais e proteção de limites UTF-8 do Oracle.
- **Pré-condições:** zelafix-api, RabbitMQ e zelafix-worker conectados com Provedor de LLM Multimodal ativo; foto válida de ocorrência urbana.
- **Dados de Entrada / Payload:** POST /chamados multipart com foto real de buraco/lixo/poste/alagamento em via pública.
- **Resultado Esperado & HTTP Codes:** Worker executa consultarNormaMunicipal e calcularPrazoSla, gera TriagemIaResult válido (título <= 100 bytes UTF-8, descrição <= 1000 bytes UTF-8, sem CAPS LOCK/inglês), API persiste chamado com status EM_ANALISE e enums coerentes.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Enviar POST /chamados multipart com fotografia nítida de problema urbano (ex.: buraco no asfalto). | zelafix-api publica ChamadoTriagemMessage com correlationId na fila chamado.triagem.queue. |
| 2 | Acompanhar retorno do DeferredResult / logs do zelafix-worker. | ZelaFixAiService detecta MIME type via magic bytes, aciona @Tool consultarNormaMunicipal e calcularPrazoSla e publica TriagemFeedbackMessage em chamado.triagem-concluida.queue. |
| 3 | Inspecionar o ChamadoResponse retornado (HTTP 201). | categoriaNome, prioridadeNome e orgaoNome correspondem aos enums oficiais (Oracle + Java), título/descrição em pt-BR dentro dos limites UTF-8 e status inicial='EM_ANALISE'. |

#### [TC-20] Recusar imagem fora de escopo na triagem IA sem persistir chamado no Oracle

- **Azure Test Case ID:** `#126` | **Plan/Suite:** `#122` / `#123` (`ai-service`) | **Tipo:** `Negativo` | **Prioridade:** `P1` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `WorkerAI`, `Guardrail`, `Negative`
- **Cobertura / Endpoints:** 05. Chamados, Triagem IA (DeferredResult) & Apoio (05.4) (`POST /chamados, TriagemPendenteStore, GET /chamados/estatisticas`)
- **Objetivo:** Validar que imagens fora do escopo de zeladoria urbana (ex.: captura de tela, meme, selfie, objeto pessoal ou ambiente interno) são recusadas pelo ZelaFixAiService (ocorrenciaValida=false) e devolvidas com HTTP 400 Bad Request sem gravar registros nas tabelas CHAMADO, HIST_CHAMADO ou VOTO_CHAMADO.
- **Pré-condições:** zelafix-api, RabbitMQ, zelafix-worker e Oracle ativos; token CIDADAO; imagem válida JPEG/PNG porém sem ocorrência urbana (ex.: selfie ou print de tela).
- **Dados de Entrada / Payload:** POST /chamados multipart com endereço válido e part 'foto' contendo imagem PNG/JPEG fora do escopo urbano.
- **Resultado Esperado & HTTP Codes:** HTTP 400 Bad Request com ApiErrorResponse descrevendo o motivo da recusa pela IA e contagem inalterada em GET /chamados/estatisticas (zero persistência no Oracle).

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Registrar a contagem atual 'total' via GET /chamados/estatisticas. | Contagem base obtida com sucesso (HTTP 200). |
| 2 | Enviar POST /chamados multipart com endereço válido e imagem fora de escopo (ex.: print de tela ou ambiente interno). | Worker define ocorrenciaValida=false sem chamar Tools e devolve TriagemFeedbackMessage.recusa (recusado=true). |
| 3 | Verificar resposta HTTP do DeferredResult. | TriagemPendenteStore.rejeitar retorna HTTP 400 Bad Request (ApiErrorResponse) com a justificativa da recusa. |
| 4 | Consultar novamente GET /chamados/estatisticas. | O campo 'total' permanece idêntico ao inicial, comprovando que nenhum chamado, histórico ou voto foi persistido no Oracle. |

#### [TC-21] Responder consulta ZelaBot com RAG normativo (ChromaDB) e higienizacao mobile

- **Azure Test Case ID:** `#127` | **Plan/Suite:** `#122` / `#123` (`ai-service`) | **Tipo:** `Positivo` | **Prioridade:** `P1` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `ZelaBot`, `RAG`
- **Cobertura / Endpoints:** ZelaBot AI FastAPI (test_zelafix_scenarios.py) (`POST /ai/chat, POST /ai/chat/public`)
- **Objetivo:** Validar resposta conversacional do ZelaBot AI fundamentada nos decretos municipais PMSP indexados no ChromaDB e formatada sem tabelas pipes ou markdown bruto para exibição mobile.
- **Pré-condições:** Microsserviço ZelaBot AI (FastAPI) online com índice ChromaDB carregado.
- **Dados de Entrada / Payload:** POST /ai/chat com { "pergunta": "Onde posso descartar entulho de obra residencial e quanto custa no ecoponto?", "sessionId": "qa_rag_01" }.
- **Resultado Esperado & HTTP Codes:** HTTP 200 OK com rag_grounded=true, sources_used não vazio referenciando Lei 13.478/2002 / ecopontos e resposta limpa sem '|' ou '**'.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Enviar POST /ai/chat com pergunta sobre descarte de entulho/ecopontos e sessionId controlado. | API retorna HTTP 200 OK com ChatResponse estruturado. |
| 2 | Validar os campos 'rag_grounded' e 'sources_used'. | rag_grounded é true e sources_used lista chunks normativos recuperados do ChromaDB. |
| 3 | Validar higienização Mobile Clean no campo 'resposta'. | Texto responde corretamente em pt-BR sem conter caracteres '\|' ou '**'. |

#### [TC-22] Acionar guardrail de risco vital no ZelaBot (Defesa Civil / Bombeiros / ENEL)

- **Azure Test Case ID:** `#128` | **Plan/Suite:** `#122` / `#123` (`ai-service`) | **Tipo:** `Positivo` | **Prioridade:** `P1` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `ZelaBot`, `Guardrail`
- **Cobertura / Endpoints:** ZelaBot AI FastAPI (test_zelafix_scenarios.py) (`POST /ai/chat`)
- **Objetivo:** Confirmar que relatos envolvendo risco vital imediato (fio energizado caído / galhos na rede elétrica) acionam orientação prioritária de segurança e emergência.
- **Pré-condições:** Microsserviço ZelaBot AI disponível.
- **Dados de Entrada / Payload:** POST /ai/chat com relato sintético de fio energizado caído / galhos encostando na fiação elétrica do poste.
- **Resultado Esperado & HTTP Codes:** HTTP 200 OK com urgencia elevada ('alta' ou 'URGENTE') e orientação imediata de afastamento e contato de emergência (Defesa Civil 199 / Bombeiros 193 / ENEL).

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Enviar POST /ai/chat relatando fio energizado caído em via pública. | API retorna HTTP 200 OK. |
| 2 | Inspecionar campos 'urgencia', 'acoes_recomendadas' e 'resposta'. | Resposta orienta manter distância e acionar órgãos de emergência (ENEL / Bombeiros 193 / Defesa Civil 199). |

#### [TC-23] Manter escopo civico do ZelaBot diante de solicitacao fora de dominio

- **Azure Test Case ID:** `#129` | **Plan/Suite:** `#122` / `#123` (`ai-service`) | **Tipo:** `Negativo` | **Prioridade:** `P2` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `ZelaBot`, `Guardrail`, `Negative`
- **Cobertura / Endpoints:** ZelaBot AI FastAPI (test_zelafix_scenarios.py) (`POST /ai/chat`)
- **Objetivo:** Verificar que o ZelaBot recusa solicitações fora do domínio de zeladoria urbana (ex.: geração de código de programação), mantendo o escopo cívico.
- **Pré-condições:** Microsserviço ZelaBot AI disponível.
- **Dados de Entrada / Payload:** POST /ai/chat com { "pergunta": "Escreva um script em Python para fazer web scraping de um site.", "sessionId": "qa_scope_01" }.
- **Resultado Esperado & HTTP Codes:** HTTP 200 OK com recusa educada, sem entregar código de programação, redirecionando o usuário para dúvidas de zeladoria urbana.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Enviar POST /ai/chat solicitando criação de código Python fora do domínio urbano. | API retorna HTTP 200 OK. |
| 2 | Inspecionar o texto de 'resposta'. | Assistente recusa educadamente gerar código e reafirma seu escopo exclusivo em zeladoria urbana. |

#### [TC-24] Gerar laudo tecnico estruturado (POST /ai/triagem) e insights preventivos (/ai/insights)

- **Azure Test Case ID:** `#131` | **Plan/Suite:** `#122` / `#123` (`ai-service`) | **Tipo:** `Positivo` | **Prioridade:** `P1` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `ZelaBot`, `IoT`
- **Cobertura / Endpoints:** ZelaBot AI FastAPI (test_zelafix_scenarios.py) (`POST /ai/triagem, POST /ai/insights`)
- **Objetivo:** Validar geração de laudo técnico com engajamento comunitário (+1 IoB) e telemetria IoT via POST /ai/triagem e alertas preventivos por bairro via POST /ai/insights.
- **Pré-condições:** Microsserviço ZelaBot AI e índice RAG ativos.
- **Dados de Entrada / Payload:** POST /ai/triagem com ChamadoContextPayload (cratera na Av. Paulista, apoios_comunitarios=32 + cenário drenagem com telemetria_iot); POST /ai/insights?bairro=Pinheiros.
- **Resultado Esperado & HTTP Codes:** HTTP 200 OK em /ai/triagem com prioridade ALTA/URGENTE, sla_sugerido_horas <= 24, parecer_ia <= 150 chars e checklist_vistoria >= 3 itens; HTTP 200 OK em /ai/insights com total_alertas >= 3.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Enviar POST /ai/triagem com ChamadoContextPayload de pavimentação e apoios_comunitarios=32. | API retorna HTTP 200 OK com prioridade ALTA ou URGENTE, enquadramento_legal, checklist_vistoria (>= 3 itens) e parecer_ia (<= 150 caracteres). |
| 2 | Enviar POST /ai/triagem para categoria 'Drenagem e Esgoto' com telemetria_iot (anomalia_detectada=true). | API retorna HTTP 200 OK roteando para órgão de drenagem/SIURB/Subprefeitura com prioridade elevada. |
| 3 | Enviar POST /ai/insights?bairro=Pinheiros. | API retorna HTTP 200 OK com InsightsResponse contendo bairro, total_alertas e lista estruturada de insights. |

#### [TC-25] Validar observabilidade, sessoes SQLite e leitura Oracle no ZelaBot AI

- **Azure Test Case ID:** `#197` | **Plan/Suite:** `#122` / `#123` (`ai-service`) | **Tipo:** `Positivo` | **Prioridade:** `P2` | **Estado:** `Ready`
- **Tags Azure:** `Compliance`, `QA`, `ZelaBot`, `Oracle`, `SQLite`
- **Cobertura / Endpoints:** ZelaBot AI FastAPI (health.py / ai.py) (`GET /, GET /health, GET /health/ready, GET /ai/vector-store/status, GET /ai/oracle/status, GET /ai/history, GET /ai/audit, GET /ai/sessions, GET /ai/chamados/{id}, DELETE /ai/sessions/{session_id}`)
- **Objetivo:** Validar healthchecks, status do ChromaDB vetorial, telemetria Oracle Thin Client, persistência de histórico/auditoria em SQLite, gestão de sessões e consulta direta de chamado Oracle.
- **Pré-condições:** Microsserviço ZelaBot AI disponível; sessão prévia executada no TC-21.
- **Dados de Entrada / Payload:** GET /health, GET /health/ready, GET /ai/vector-store/status, GET /ai/oracle/status, GET /ai/history?session_id=qa_rag_01, GET /ai/audit, GET /ai/sessions, GET /ai/chamados/1, DELETE /ai/sessions/qa_rag_01.
- **Resultado Esperado & HTTP Codes:** HTTP 200 OK nos endpoints de status, histórico SQLite e sessões; GET /ai/chamados/1 retorna 200 OK (ou 503 controlado se Oracle inacessível / 404 para ID 999999); DELETE /ai/sessions/{id} remove sessão.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Enviar GET /health, GET /health/ready e GET /ai/vector-store/status. | Retornam HTTP 200 OK com status='healthy'/'ready' e indexed_chunks >= 20. |
| 2 | Enviar GET /ai/oracle/status e GET /ai/chamados?limit=5. | Retornam HTTP 200 OK informando status da conexão Oracle Thin Client. |
| 3 | Enviar GET /ai/history?session_id=qa_rag_01, GET /ai/audit e GET /ai/sessions. | Retornam HTTP 200 OK comprovando persistência multi-turno e trilha de auditoria no SQLite. |
| 4 | Enviar GET /ai/chamados/999999 e depois DELETE /ai/sessions/qa_rag_01. | GET retorna 404 (ou 503 se Oracle offline) e DELETE retorna HTTP 200 OK com status='ok'. |
