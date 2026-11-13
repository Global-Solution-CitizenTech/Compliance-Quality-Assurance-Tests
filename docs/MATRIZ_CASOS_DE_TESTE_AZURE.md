# ZelaFix (CitizenTech) — Matriz de Casos de Teste Funcionais (Azure Test Plans)

**Disciplina:** Compliance, Quality Assurance & Tests  
**Tipo:** Caixa-preta (testes positivos e negativos)  
**Organização / Projeto Azure DevOps:** `https://dev.azure.com/ZelaFixGS/ZelaFix`  
**Escopo Real:** API REST Java (`zelafix-api`), Worker Spring AI (`zelafix-worker`) e Microsserviço ZelaBot IA (`deploy_zelafixai_render`).

---

## 1. Sumário dos 24 Casos de Teste (Azure DevOps)

| ID | Caso de Teste | Suíte | Tipo | Work Item ID(s) |
| :---: | :--- | :--- | :---: | :--- |
| **TC-01** | Autenticar contas de QA dos perfis ADMIN, GESTOR e CIDADAO | `api-auth-rbac` | Positivo | 134–136 |
| **TC-02** | Rejeitar login com credenciais inválidas | `api-auth-rbac` | Negativo | 137–138 |
| **TC-03** | Bloquear endpoint protegido sem token | `api-auth-rbac` | Negativo | 139 |
| **TC-04** | Rejeitar token JWT inválido | `api-auth-rbac` | Negativo | 140 |
| **TC-05** | Impedir CIDADAO de criar categoria | `api-auth-rbac` | Negativo | 141 |
| **TC-06** | Impedir CIDADAO de alterar status de chamado | `api-auth-rbac` | Negativo | 142 |
| **TC-07** | Consultar categorias e status disponíveis | `api-catalog-adress` | Positivo | 145–146 |
| **TC-08** | Criar categoria como ADMIN | `api-catalog-adress` | Positivo | 147 |
| **TC-09** | Rejeitar categoria com nome vazio | `api-catalog-adress` | Negativo | 148 |
| **TC-10** | Criar e consultar endereço por ID | `api-catalog-adress` | Positivo | 149–150 |
| **TC-11** | Rejeitar CEP em formato inválido | `api-catalog-adress` | Negativo | 151 |
| **TC-12** | Impedir CIDADAO de listar endereços administrativos | `api-catalog-adress` | Negativo | 152 |
| **TC-13** | Criar chamado com foto Base64 | `api-chamados` | Positivo | 155 |
| **TC-14** | Criar chamado multipart e recuperar foto | `api-chamados` | Positivo | 156–157 |
| **TC-15** | Rejeitar chamado com dados inválidos | `api-chamados` | Negativo | 158–160 |
| **TC-16** | Consultar chamados com paginação e filtro do próprio usuário | `api-chamados` | Positivo | 161–162 |
| **TC-17** | Atualizar ciclo de status e consultar histórico | `api-chamados` | Positivo | 163–165 |
| **TC-18** | Excluir chamado como ADMIN e confirmar remoção | `api-chamados` | Positivo | 166–167 |
| **TC-19** | Confirmar triagem assíncrona do Worker no histórico do chamado | `worker-ai` | Positivo | 124–125 |
| **TC-20** | Responder consulta ZelaBot com contexto normativo | `zelabot-ai` | Positivo | 126 |
| **TC-21** | Acionar guardrail para risco vital | `zelabot-ai` | Positivo | 127 |
| **TC-22** | Manter escopo cívico diante de solicitação de código | `zelabot-ai` | Negativo | 128 |
| **TC-23** | Gerar triagem técnica para cratera com engajamento | `zelabot-ai` | Positivo | 129–130 |
| **TC-24** | Gerar insights preventivos para bairro | `zelabot-ai` | Positivo | 131 |

---

## 2. Preparação Geral e Ambiente

- **API Java (Produção):** `https://app-zelafix-561432.azurewebsites.net` (ou `http://localhost:8080` local)
- **Worker Spring AI (Produção):** `https://app-zelafix-worker-561432.azurewebsites.net` (ou `http://localhost:8081` local)
- **ZelaBot IA (Produção):** `https://disruptive-architectures-iot-iob-ia-mpl5.onrender.com`
- **Perfis de QA:** `CIDADAO`, `GESTOR` e `ADMIN` (semeados via Flyway na API Java).

---

## 3. Especificação por Suíte

### Suíte 1 — `api-auth-rbac` (TC-01 a TC-06)
- **TC-01 (Positivo):** Enviar `POST /login` com credenciais válidas de `ADMIN`, `GESTOR` e `CIDADAO` -> `HTTP 200` com `token` JWT RSA válido e perfil correspondente em `GET /usuarios/me`.
- **TC-02 (Negativo):** Enviar `POST /login` com senha incorreta ou e-mail inexistente -> `HTTP 401 Unauthorized`.
- **TC-03 (Negativo):** Acessar `GET /usuarios/me` ou `POST /chamados` sem header `Authorization` -> `HTTP 401 Unauthorized`.
- **TC-04 (Negativo):** Enviar header `Authorization: Bearer token.invalido.assinatura` -> `HTTP 401 Unauthorized`.
- **TC-05 (Negativo):** Autenticado como `CIDADAO`, enviar `POST /categorias` -> `HTTP 403 Forbidden`.
- **TC-06 (Negativo):** Autenticado como `CIDADAO`, enviar `PATCH /chamados/{id}/status` -> `HTTP 403 Forbidden`.

### Suíte 2 — `api-catalog-adress` (TC-07 a TC-12)
- **TC-07 (Positivo):** Enviar `GET /categorias` e `GET /status` -> `HTTP 200` com o catálogo completo.
- **TC-08 (Positivo):** Autenticado como `ADMIN`, criar categoria via `POST /categorias` -> `HTTP 201 Created` com ID persistido.
- **TC-09 (Negativo):** Autenticado como `ADMIN`, enviar `POST /categorias` com `nome` em branco -> `HTTP 400 Bad Request` (Bean Validation).
- **TC-10 (Positivo):** Criar endereço válido via `POST /enderecos` (com resolução ViaCEP) e consultar em `GET /enderecos/{id}` -> `HTTP 201` / `HTTP 200`.
- **TC-11 (Negativo):** Enviar `POST /enderecos` com `cep` fora do padrão de 8 dígitos -> `HTTP 400 Bad Request`.
- **TC-12 (Negativo):** Autenticado como `CIDADAO`, enviar `GET /enderecos` (listagem administrativa) -> `HTTP 403 Forbidden`.

### Suíte 3 — `api-chamados` (TC-13 a TC-18)
- **TC-13 (Positivo):** Autenticado como `CIDADAO`, enviar `POST /chamados` com payload JSON e `fotoBase64` válida -> `HTTP 201 Created` com ID gerado.
- **TC-14 (Positivo):** Enviar `POST /chamados` multipart com imagem e recuperar os bytes via `GET /chamados/{id}/foto` -> `HTTP 201` e `HTTP 200` (`image/*`).
- **TC-15 (Negativo):** Enviar `POST /chamados` com título/descrição vazios ou sem foto obrigatória -> `HTTP 400 Bad Request`.
- **TC-16 (Positivo):** Consultar `GET /chamados?page=0&size=10` e filtro do próprio usuário -> `HTTP 200` com estrutura paginada `Page<ChamadoResponse>`.
- **TC-17 (Positivo):** Autenticado como `GESTOR`/`ADMIN`, atualizar status via `PATCH /chamados/{id}/status` e verificar o registro cronológico em `GET /chamados/{id}` -> `HTTP 200` com histórico atualizado.
- **TC-18 (Positivo):** Autenticado como `ADMIN`, excluir chamado via `DELETE /chamados/{id}` e confirmar `HTTP 404` em `GET /chamados/{id}`.

### Suíte 4 — `worker-ai` & `zelabot-ai` (TC-19 a TC-24)
- **TC-19 (Positivo):** Após criação de chamado com foto na `zelafix-api`, confirmar que o `zelafix-worker` processou a fila `chamado.triagem.queue` (via Azure AI Foundry / `phi-4-multimodal`) e gravou prioridade, órgão responsável e parecer técnico no histórico do chamado.
- **TC-20 (Positivo):** Enviar pergunta normativa urbana para `POST /ai/chat` no ZelaBot -> `HTTP 200` com resposta fundamentada no RAG normativo PMSP.
- **TC-21 (Positivo):** Enviar relato com risco vital imediato (ex.: fio energizado caído) para o ZelaBot -> acionamento de guardrail com orientação imediata de emergência (Defesa Civil 199 / Bombeiros 193 / ENEL).
- **TC-22 (Negativo):** Solicitar geração de código de programação ou assunto fora de zeladoria urbana ao ZelaBot -> recusa educada mantendo o escopo cívico.
- **TC-23 (Positivo):** Enviar relato de cratera com engajamento comunitário -> geração de triagem técnica com prioridade elevada e órgão competente.
- **TC-24 (Positivo):** Consultar endpoint de insights preventivos por bairro -> retorno estruturado com recomendações de zeladoria preventiva.
