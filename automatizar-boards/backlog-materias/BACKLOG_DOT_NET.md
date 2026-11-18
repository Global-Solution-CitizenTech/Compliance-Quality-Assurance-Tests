# 📋 Backlog Master Azure Boards — Global Solution 2026/2: Advanced Business Development with .NET

> **Projeto Integrado:** ZelaFix — Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  
> **Disciplina:** Advanced Business Development with .NET (FIAP — 2TDSPG)  
> **Repositório GitHub:** [Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net)  
> **Organização / Projeto Azure DevOps:** `ZelaFixGS` / `ZelaFix`  
> **Epic Principal:** `[EPIC] Advanced Business Development with .NET: API RESTful ZelaFix em .NET 10, EF Core Oracle, Resiliência e Integração Mobile` (**AB#27**)  
> **Responsável / Owner:** Gustavo Keiji Okada (`MR563428@fiap.com.br`)  
> **Start Date:** `2026-11-04`  
> **Target Date:** `2026-11-19`  
> **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`  
> **Padrão:** Azure Boards (Scrum Process: Epic ➔ Feature ➔ PBI)  
> **Tags:** `DotNet`  
> **Diretrizes Estratégicas:** Desenvolvimento de Web API RESTful corporativa de alta performance em C# e .NET 10 (Minimal APIs) estruturada segundo a Clean Architecture e DDD, publicada em nuvem no Render (`https://advanced-business-development-with-dot.onrender.com/`), persistência relacional estrita com Entity Framework Core 10 sobre Oracle Database 19c (`DatabaseVersion19`, 14 tabelas relacionais em 3FN e `DbInitializer` para migração e seed automáticos de domínio e usuários RBAC `gestor@zelafix.com.br` / `cidadao@zelafix.com.br`), resolução resiliente de endereços com ViaCEP, gestão transacional de evidências fotográficas em Base64/BLOB, mecanismo cívico de apoio popular (`VOTO_CHAMADO`) com escalonamento dinâmico de prioridade, trilha de auditoria imutável (`HIST_CHAMADO`), autenticação segura JWT Bearer HS256 com senhas protegidas por BCrypt e RBAC granular (`CIDADAO` / `GESTOR`), garantia de idempotência via cabeçalho `Idempotency-Key`, rate limiting nativo Fixed Window, observabilidade com Health Checks customizados e logs estruturados via Serilog (`X-Correlation-ID`), Swagger OpenAPI 3.0 completo com 23 paths e respostas HTTP (`400`/`401`/`403`/`404`/`429`/`500`), integração total com o aplicativo mobile React Native (Expo) com suporte a miniaturas (`incluirFoto`) e suíte de **106 testes automatizados** (53 unitários + 53 de integração com WebApplicationFactory, >91% de cobertura em todas as camadas) no padrão AAA.

---

## 👥 Integrantes do Grupo (Ordem Alfabética Estrita)

| Integrante | RM | Turma | Papel / Responsabilidade |
| :--- | :---: | :---: | :--- |
| **Enzo Okuizumi Miranda de Souza** | **561432** | 2TDSPG | IoT, Compliance, Java & Arquitetura Geral |
| **Gustavo Keiji Okada** | **563428** | 2TDSPG | **Back-end .NET Enterprise & Minimal APIs (Owner da Disciplina)** |
| **Lucas Barros Gouveia** | **566422** | 2TDSPG | Database Modeling & Engenharia de Dados Oracle |
| **Luna de Carvalho Guimarães** | **562290** | 2TDSPG | Mobile Application Development (React Native / Expo) |
| **Milton Jakson de Sousa Marcelino** | **564836** | 2TDSPG | DevOps Tools, Cloud Computing & CI/CD Pipelines |

---

## 🌳 1. Estrutura Hierárquica no Azure Boards

```text
[EPIC] Advanced Business Development with .NET: API RESTful ZelaFix em .NET 10, EF Core Oracle, Resiliência e Integração Mobile [AB#27]
│
├── 🏆 [FEATURE 01] Arquitetura Limpa, Domínio Relacional e Persistência Oracle com EF Core [AB#28]
│   ├── 📄 [PBI-01] Setup da Solução .NET 10, Clean Architecture e Injeção de Dependências (3 pts) [AB#29]
│   ├── 📄 [PBI-02] Modelagem de Entidades Relacionais 3FN e Mapeamentos Fluent API no EF Core (3 pts) [AB#30]
│   └── 📄 [PBI-03] Repositórios Especializados, Unit of Work e Persistência de Fotos em BLOB (3 pts) [AB#200]
│
├── 🏆 [FEATURE 02] Serviços de Aplicação, Integrações Externas e Regras Cívicas [AB#31]
│   ├── 📄 [PBI-04] Resolução Resiliente de Endereços Urbanos via HttpClient e API Externa ViaCEP (3 pts) [AB#32]
│   ├── 📄 [PBI-05] Mobilização Popular, Votação Comunitária e Escalonamento Automático de Prioridade (3 pts) [AB#33]
│   └── 📄 [PBI-06] Trilha de Auditoria Histórica (HIST_CHAMADO) e Transição de Status Operacional (3 pts) [AB#201]
│
├── 🏆 [FEATURE 03] Minimal APIs RESTful, Segurança JWT e Resiliência HTTP [AB#34]
│   ├── 📄 [PBI-07] Autenticação JWT Bearer HS256, Criptografia BCrypt e Controle de Acesso RBAC (3 pts) [AB#35]
│   ├── 📄 [PBI-08] Endpoints de Ocorrências com Filtros Dinâmicos, Paginação e Miniaturas (incluirFoto) (3 pts) [AB#202]
│   └── 📄 [PBI-09] Idempotência de Requisições com Header Idempotency-Key e Rate Limiting Nativo (3 pts) [AB#203]
│
├── 🏆 [FEATURE 04] Observabilidade Corporativa e Integração com Ecossistema Mobile [AB#204]
│   ├── 📄 [PBI-10] Observabilidade com Health Checks Integrados ao Oracle e Logging Estruturado Serilog (3 pts) [AB#205]
│   ├── 📄 [PBI-11] Integração Full-Stack com App Mobile React Native e Compatibilização de Rotas (3 pts) [AB#206]
│   └── 📄 [PBI-12] Estatísticas Consolidadas de Chamados e Filtros Territoriais no Radar (3 pts) [AB#207]
│
└── 🏆 [FEATURE 05] Qualidade de Software, Testes Automatizados e Governança [AB#208]
    ├── 📄 [PBI-13] Suíte de Testes Unitários de Domínio e Aplicação com xUnit no Padrão AAA e Moq (3 pts) [AB#209]
    ├── 📄 [PBI-14] Testes de Integração com WebApplicationFactory, Banco em Memória e Contratos HTTP (3 pts) [AB#210]
    └── 📄 [PBI-15] Documentação OpenAPI/Swagger 3.0, Diagramas de Arquitetura e README Técnico (3 pts) [AB#211]
```

---

## 📊 2. Tabela Resumo do Backlog & Rastreabilidade

| Feature Pai | ID do PBI | Título do Item de Backlog (PBI) | ID Azure Boards | Story Points | Prioridade | Business Value | Commits | Status |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Feature 01** `[AB#28]` | **PBI-01** | Setup da Solução .NET 10, Clean Architecture e Injeção de Dependências | **#29** | 3 pts | 1 - Critical | 100 | 2 | Committed |
| | **PBI-02** | Modelagem de Entidades Relacionais 3FN e Mapeamentos Fluent API no EF Core | **#30** | 3 pts | 1 - Critical | 100 | 2 | Committed |
| | **PBI-03** | Repositórios Especializados, Unit of Work e Persistência de Fotos em BLOB | **#200** | 3 pts | 1 - Critical | 100 | 2 | Committed |
| **Feature 02** `[AB#31]` | **PBI-04** | Resolução Resiliente de Endereços Urbanos via HttpClient e API Externa ViaCEP | **#32** | 3 pts | 1 - Critical | 100 | 1 | Committed |
| | **PBI-05** | Mobilização Popular, Votação Comunitária e Escalonamento Automático de Prioridade | **#33** | 3 pts | 1 - Critical | 100 | 2 | Committed |
| | **PBI-06** | Trilha de Auditoria Histórica (HIST_CHAMADO) e Transição de Status Operacional | **#201** | 3 pts | 1 - Critical | 100 | 3 | Committed |
| **Feature 03** `[AB#34]` | **PBI-07** | Autenticação JWT Bearer HS256, Criptografia BCrypt e Controle de Acesso RBAC | **#35** | 3 pts | 1 - Critical | 100 | 1 | Committed |
| | **PBI-08** | Endpoints de Ocorrências com Filtros Dinâmicos, Paginação e Miniaturas (incluirFoto) | **#202** | 3 pts | 1 - Critical | 100 | 2 | Committed |
| | **PBI-09** | Idempotência de Requisições com Header Idempotency-Key e Rate Limiting Nativo | **#203** | 3 pts | 1 - Critical | 100 | 1 | Committed |
| **Feature 04** `[AB#204]` | **PBI-10** | Observabilidade com Health Checks Integrados ao Oracle e Logging Estruturado Serilog | **#205** | 3 pts | 1 - Critical | 100 | 3 | Committed |
| | **PBI-11** | Integração Full-Stack com App Mobile React Native e Compatibilização de Rotas | **#206** | 3 pts | 1 - Critical | 100 | 3 | Committed |
| | **PBI-12** | Estatísticas Consolidadas de Chamados e Filtros Territoriais no Radar | **#207** | 3 pts | 1 - Critical | 100 | 2 | Committed |
| **Feature 05** `[AB#208]` | **PBI-13** | Suíte de Testes Unitários de Domínio e Aplicação com xUnit no Padrão AAA e Moq | **#209** | 3 pts | 1 - Critical | 100 | 3 | Committed |
| | **PBI-14** | Testes de Integração com WebApplicationFactory, Banco em Memória e Contratos HTTP | **#210** | 3 pts | 1 - Critical | 100 | 2 | Committed |
| | **PBI-15** | Documentação OpenAPI/Swagger 3.0, Diagramas de Arquitetura e README Técnico | **#211** | 3 pts | 1 - Critical | 100 | 4 | Committed |
| **TOTAL CONSOLIDADO** | **5 Features** | **15 PBIs de Backlog** | — | **45 pts** | — | — | **10+ Commits** | **100% Concluído** |

---

## 📦 3. Detalhamento dos Itens de Trabalho (Épico, Features e PBIs)

---

### 🏛️ ÉPICO
* **Work Item Type:** `Epic`
* **Azure Boards ID:** `#27`
* **Title:** `[EPIC] Advanced Business Development with .NET: API RESTful ZelaFix em .NET 10, EF Core Oracle, Resiliência e Integração Mobile`
* **Tags:** `DotNet`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `45`
* **Business Value:** `100`
* **Description:** Construção da API RESTful corporativa ZelaFix em C# e .NET 10 (Minimal APIs) estruturada segundo a Clean Architecture e Domain-Driven Design, contemplando persistência relacional com Entity Framework Core 10 sobre Oracle Database (14 tabelas em 3FN e `DbInitializer` com semeadura automática de usuários RBAC), resolução de endereços resiliente via ViaCEP, gestão de fotos binárias em BLOB, mecanismo de engajamento popular com recálculo dinâmico de prioridade, autenticação segura JWT Bearer HS256 com senhas em BCrypt, RBAC granular, idempotência de requisições, rate limiting nativo, observabilidade com Health Checks customizados, integração completa com o aplicativo mobile React Native e bateria de 106 testes automatizados no padrão AAA.

---

### 🏆 [FEATURE 01] Arquitetura Limpa, Domínio Relacional e Persistência Oracle com EF Core
* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#28`
* **Parent:** `[EPIC] Advanced Business Development with .NET: API RESTful ZelaFix em .NET 10, EF Core Oracle, Resiliência e Integração Mobile` (#27)
* **Title:** `[FEATURE 01] Arquitetura Limpa, Domínio Relacional e Persistência Oracle com EF Core`
* **Tags:** `DotNet`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-08`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Description:** Estruturação da solução modular em camadas desacopladas (Domain, Application, Infrastructure e Api), modelagem conceitual e relacional em 3FN para 14 tabelas no Oracle Database e mapeamento objeto-relacional estrito via Entity Framework Core sem dependência de stored procedures legadas.
* **Acceptance Criteria:**
  - [x] Solução .NET 10 estruturada nos 4 projetos fundamentais da Clean Architecture sem acoplamentos circulares.
  - [x] Modelagem de 14 entidades relacionais com mapeamentos Fluent API em `IEntityTypeConfiguration<T>`.
  - [x] Injeção de dependências configurada para contextos de persistência, repositórios e Unit of Work.
  - [x] Persistência direta de evidências fotográficas em coluna binária `BLOB` (`FOTO`).

#### 🔹 [PBI-01] Setup da Solução .NET 10, Clean Architecture e Injeção de Dependências
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#29`
* **Parent Feature:** `[FEATURE 01] Arquitetura Limpa, Domínio Relacional e Persistência Oracle com EF Core` (#28)
* **Title:** `[PBI-01] Setup da Solução .NET 10, Clean Architecture e Injeção de Dependências`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DotNet`
* **Business Value:** `100`
* **State:** `Committed`
* **Assigned To:** `MR563428@fiap.com.br`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`

##### Descrição (História de Usuário)
> **Como** engenheiro de software backend .NET,  
> **Eu quero** criar a solução em C# e .NET 10 estruturada nos projetos `ZelaFix.Domain`, `ZelaFix.Application`, `ZelaFix.Infrastructure` e `ZelaFix.Api`,  
> **Para que** as regras de negócio de zeladoria urbana fiquem isoladas de detalhes de infraestrutura, bancos de dados e frameworks web.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Solução `ZelaFix.sln` criada com separação estrita de camadas e referências unidirecionais.
- [x] Remoção de scripts obsoletos, arquivos temporários de IDE e templates não utilizados.
- [x] Registro centralizado de serviços e injeção de dependência modular em métodos de extensão de `IServiceCollection`.
- [x] Compilação limpa em .NET 10 com warnings zero e nullable reference types ativo.

##### Commits vinculados (GitHub Repository):
- [`f80ba46`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/f80ba46) — `chore: remover scripts legados, configuracoes de ide e templates desnecessarios` *(vinculado em AB#27 e AB#29)*
- [`d0732c8`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/d0732c8) — `feat(domain): estruturar projeto de dominio, entidades relacionais e regras de negocio de zeladoria` *(vinculado em AB#29)*

---

#### 🔹 [PBI-02] Modelagem de Entidades Relacionais 3FN e Mapeamentos Fluent API no EF Core
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#30`
* **Parent Feature:** `[FEATURE 01] Arquitetura Limpa, Domínio Relacional e Persistência Oracle com EF Core` (#28)
* **Title:** `[PBI-02] Modelagem de Entidades Relacionais 3FN e Mapeamentos Fluent API no EF Core`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DotNet`
* **Business Value:** `100`
* **State:** `Committed`
* **Assigned To:** `MR563428@fiap.com.br`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`

##### Descrição (História de Usuário)
> **Como** arquiteto de dados e desenvolvedor backend,  
> **Eu quero** modelar as entidades de domínio em 3ª Forma Normal com Fluent API no Entity Framework Core,  
> **Para que** o banco Oracle mantenha integridade referencial estrita, constraints semânticas e alta performance de consulta.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] 14 entidades mapeadas: `Chamado`, `Categoria`, `HistChamado`, `VotoChamado`, `Endereco`, `Bairro`, `Cidade`, `Estado`, `Usuario`, `Telefone`, `Status`, `Prioridade`, `OrgaoGoverno` e enum `Cargo`.
- [x] Mapeamentos Fluent API isolados em classes `IEntityTypeConfiguration<T>` definindo nomes exatos de colunas e constraints.
- [x] Configuração de índices de unicidade compostos para evitar votos duplicados (`CHAMADO_ID + USUARIO_ID`) e e-mails duplicados.
- [x] Navegações de relacionamento 1:N e N:1 configuradas com exclusão em cascata restrita para proteção de dados históricos.

##### Commits vinculados (GitHub Repository):
- [`d0732c8`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/d0732c8) — `feat(domain): estruturar projeto de dominio, entidades relacionais e regras de negocio de zeladoria` *(vinculado em AB#30)*
- [`ea8bdd4`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/ea8bdd4) — `feat(domain): alinha modelo relacional 3FN com entidades Prioridade e OrgaoGoverno` *(vinculado em AB#30)*

---

#### 🔹 [PBI-03] Repositórios Especializados, Unit of Work e Persistência de Fotos em BLOB
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#200`
* **Parent Feature:** `[FEATURE 01] Arquitetura Limpa, Domínio Relacional e Persistência Oracle com EF Core` (#28)
* **Title:** `[PBI-03] Repositórios Especializados, Unit of Work e Persistência de Fotos em BLOB`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DotNet`
* **Business Value:** `100`
* **State:** `Committed`
* **Assigned To:** `MR563428@fiap.com.br`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`

##### Descrição (História de Usuário)
> **Como** desenvolvedor backend,  
> **Eu quero** implementar o padrão Repository e Unit of Work gerenciando transações ACID e persistência binária de imagens,  
> **Para que** as evidências fotográficas das ocorrências urbanas sejam gravadas de forma atômica e segura no Oracle sem dependência de storage externo.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `IUnitOfWork` gerenciando transações atômicas e persistência com `CommitAsync()`.
- [x] `IChamadoRepository`, `IUsuarioRepository` e `ICategoriaRepository` com consultas especializadas e paginação otimizada.
- [x] Persistência da foto em coluna `BLOB` (`byte[]`) mapeada com sanitização e conversão segura a partir de Base64.
- [x] Compatibilidade estrita com Oracle 19c (`DatabaseVersion19`) e `DbInitializer` para migração e seed automáticos de domínio e usuários padrão RBAC (`gestor@zelafix.com.br` e `cidadao@zelafix.com.br`).

##### Commits vinculados (GitHub Repository):
- [`39a4f79`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/39a4f79) — `feat(infra): configurar persistencia EF Core para Oracle Database, repositorios e UnitOfWork` *(vinculado em AB#28)*
- [`f5a8305`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/f5a8305) — `fix(api,infra,swagger): expor todos os endpoints no Swagger, compatibilizar EF Core com Oracle 19c, auto-migrar/semear banco e corrigir StatusAnterior` *(vinculado em AB#200)*
- [`8a280bd`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/8a280bd) — `fix(gs2): semear usuários padrão RBAC, completar respostas OpenAPI e alinhar documentação` *(vinculado em AB#200)*

---

### 🏆 [FEATURE 02] Serviços de Aplicação, Integrações Externas e Regras Cívicas
* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#31`
* **Parent:** `[EPIC] Advanced Business Development with .NET: API RESTful ZelaFix em .NET 10, EF Core Oracle, Resiliência e Integração Mobile` (#27)
* **Title:** `[FEATURE 02] Serviços de Aplicação, Integrações Externas e Regras Cívicas`
* **Tags:** `DotNet`
* **Start Date:** `2026-11-07`
* **Target Date:** `2026-11-12`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Description:** Implementação dos casos de uso de zeladoria urbana, integração resiliente com o ViaCEP para preenchimento automático de logradouros, regras de votação comunitária com escalonamento automático de prioridade e rastreabilidade cronológica de transições de status.
* **Acceptance Criteria:**
  - [x] Integração HTTP resiliente com a API ViaCEP com normalização de bairros e cidades na base Oracle.
  - [x] Regra de domínio de apoio comunitário que impede voto do próprio autor e escalona prioridade por engajamento.
  - [x] Trilha de auditoria imutável registrando histórico de status com parecer técnico, data/hora e autor.

#### 🔹 [PBI-04] Resolução Resiliente de Endereços Urbanos via HttpClient e API Externa ViaCEP
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#32`
* **Parent Feature:** `[FEATURE 02] Serviços de Aplicação, Integrações Externas e Regras Cívicas` (#31)
* **Title:** `[PBI-04] Resolução Resiliente de Endereços Urbanos via HttpClient e API Externa ViaCEP`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DotNet`
* **Business Value:** `100`
* **State:** `Committed`
* **Assigned To:** `MR563428@fiap.com.br`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`

##### Descrição (História de Usuário)
> **Como** cidadão cadastrando uma ocorrência urbana,  
> **Eu quero** informar apenas o CEP e número do imóvel,  
> **Para que** a API resolva e preencha automaticamente rua, bairro, cidade e estado a partir do ViaCEP, reduzindo tempo e erros de digitação.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Serviço `ViaCepService` consumindo endpoint público do ViaCEP via `HttpClientFactory` com timeout e tratamento de falhas.
- [x] Normalização inteligente: reutilização de registros de `Bairro`, `Cidade` e `Estado` existentes no Oracle para evitar duplicidade.
- [x] Validação sintática do CEP com expressão regular antes do despacho da requisição externa.
- [x] Fallback gracioso devolvendo mensagem informativa amigável quando o CEP não for localizado.

##### Commits vinculados (GitHub Repository):
- [`048bef7`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/048bef7) — `feat(app): implementar DTOs, mapeadores, interfaces de servicos e integracao ViaCep` *(vinculado em AB#32)*

---

#### 🔹 [PBI-05] Mobilização Popular, Votação Comunitária e Escalonamento Automático de Prioridade
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#33`
* **Parent Feature:** `[FEATURE 02] Serviços de Aplicação, Integrações Externas e Regras Cívicas` (#31)
* **Title:** `[PBI-05] Mobilização Popular, Votação Comunitária e Escalonamento Automático de Prioridade`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DotNet`
* **Business Value:** `100`
* **State:** `Committed`
* **Assigned To:** `MR563428@fiap.com.br`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`

##### Descrição (História de Usuário)
> **Como** morador de um bairro afetado por um problema de zeladoria,  
> **Eu quero** registrar meu apoio a um chamado já aberto por outro munícipe,  
> **Para que** a ocorrência ganhe visibilidade e sua prioridade seja automaticamente elevada na fila de atendimento da subprefeitura.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Registro de voto em `VOTO_CHAMADO` garantindo que um munícipe vote apenas uma vez por chamado (409 Conflict se repetido).
- [x] Validação que impede o próprio autor da ocorrência de registrar voto de apoio no seu próprio chamado (400 Bad Request).
- [x] Bloqueio de apoio popular para chamados que já estejam em status terminal (`CONCLUIDO` ou `REJEITADO`).
- [x] Regra de domínio de escalonamento cívico: chamados com alto volume de apoios têm sua prioridade elevada para `ALTA` ou `URGENTE`.

##### Commits vinculados (GitHub Repository):
- [`048bef7`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/048bef7) — `feat(app): implementar DTOs, mapeadores, interfaces de servicos e integracao ViaCep` *(vinculado em AB#33)*
- [`e3e244c`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/e3e244c) — `refactor(services): remove dependencia do RabbitMQ e implementa regras de negocio civicas e escalonamento de prioridade` *(vinculado em AB#33)*

---

#### 🔹 [PBI-06] Trilha de Auditoria Histórica (HIST_CHAMADO) e Transição de Status Operacional
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#201`
* **Parent Feature:** `[FEATURE 02] Serviços de Aplicação, Integrações Externas e Regras Cívicas` (#31)
* **Title:** `[PBI-06] Trilha de Auditoria Histórica (HIST_CHAMADO) e Transição de Status Operacional`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DotNet`
* **Business Value:** `100`
* **State:** `Committed`
* **Assigned To:** `MR563428@fiap.com.br`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`

##### Descrição (História de Usuário)
> **Como** gestor público municipal ou auditor de transparência,  
> **Eu quero** tramitar o status operacional de um chamado com parecer técnico obrigatório e gravação de histórico imutável,  
> **Para que** todo o ciclo de vida do serviço público possa ser auditado pelo cidadão com total transparência.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Transição de status respeitando a máquina de estados: `PENDENTE` ➔ `EM_ANALISE` ➔ `EM_EXECUCAO` ➔ `CONCLUIDO` (ou `REJEITADO`).
- [x] Criação de registro imutável em `HIST_CHAMADO` contendo data/hora UTC, status anterior, novo status e justificativa técnica.
- [x] Restrição de operação: apenas usuários com perfil `GESTOR` podem movimentar status operacional.
- [x] Atualização síncrona do status mestre na tabela `CHAMADO` dentro da mesma transação do `UnitOfWork`.

##### Commits vinculados (GitHub Repository):
- [`048bef7`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/048bef7) — `feat(app): implementar DTOs, mapeadores, interfaces de servicos e integracao ViaCep` *(vinculado em AB#31)*
- [`4d279f4`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/4d279f4) — `feat(application): enriquece DTOs de chamados, contratos de procedures e repositorios` *(vinculado em AB#31)*

---

### 🏆 [FEATURE 03] Minimal APIs RESTful, Segurança JWT e Resiliência HTTP
* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#34`
* **Parent:** `[EPIC] Advanced Business Development with .NET: API RESTful ZelaFix em .NET 10, EF Core Oracle, Resiliência e Integração Mobile` (#27)
* **Title:** `[FEATURE 03] Minimal APIs RESTful, Segurança JWT e Resiliência HTTP`
* **Tags:** `DotNet`
* **Start Date:** `2026-11-10`
* **Target Date:** `2026-11-15`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Description:** Implementação dos endpoints HTTP em ASP.NET Core Minimal APIs (.NET 10), autenticação e autorização JWT Bearer HS256 com controle RBAC, hash criptográfico de senhas via BCrypt, filtros de validação automática e mecanismos de resiliência HTTP com idempotência e rate limiting.
* **Acceptance Criteria:**
  - [x] Endpoints RESTful mapeados para autenticação, categorias, chamados e estatísticas de zeladoria.
  - [x] Tokens JWT HS256 emitidos com claims de usuário, perfil e expiração configurável.
  - [x] Senhas armazenadas exclusivamente em hash BCrypt saltado e verificação segura no login.
  - [x] Proteção contra submissões repetidas via cabeçalho HTTP `Idempotency-Key` e rate limiting nativo.

#### 🔹 [PBI-07] Autenticação JWT Bearer HS256, Criptografia BCrypt e Controle de Acesso RBAC
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#35`
* **Parent Feature:** `[FEATURE 03] Minimal APIs RESTful, Segurança JWT e Resiliência HTTP` (#34)
* **Title:** `[PBI-07] Autenticação JWT Bearer HS256, Criptografia BCrypt e Controle de Acesso RBAC`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DotNet`
* **Business Value:** `100`
* **State:** `Committed`
* **Assigned To:** `MR563428@fiap.com.br`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`

##### Descrição (História de Usuário)
> **Como** munícipe ou agente público municipal,  
> **Eu quero** me autenticar com credenciais seguras e receber um token JWT assinado digitalmente,  
> **Para que** minhas requisições à API sejam devidamente autorizadas de acordo com o meu perfil de acesso (Cidadão ou Gestor).

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Endpoints `/api/v1/auth/register`, `/api/v1/auth/login` e `/api/v1/auth/me` implementados.
- [x] Criptografia de senhas com `BCrypt.Net-Next` na criação cadastral e comparação com verificação de salt no login.
- [x] Emissão de token JWT Bearer com algoritmo HMAC-SHA256 contendo claims `nameid`, `email`, `role` e `exp`.
- [x] Política de autorização `GestorOnly` exigida nos endpoints administrativos de categorias e tramitação de status.

##### Commits vinculados (GitHub Repository):
- [`894b532`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/894b532) — `feat(api): implementar Minimal APIs RESTful, JWT Bearer, HATEOAS, Idempotency e Rate Limiting` *(vinculado em AB#34 e AB#35)*

---

#### 🔹 [PBI-08] Endpoints de Ocorrências com Filtros Dinâmicos, Paginação e Miniaturas (incluirFoto)
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#202`
* **Parent Feature:** `[FEATURE 03] Minimal APIs RESTful, Segurança JWT e Resiliência HTTP` (#34)
* **Title:** `[PBI-08] Endpoints de Ocorrências com Filtros Dinâmicos, Paginação e Miniaturas (incluirFoto)`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DotNet`
* **Business Value:** `100`
* **State:** `Committed`
* **Assigned To:** `MR563428@fiap.com.br`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`

##### Descrição (História de Usuário)
> **Como** usuário do aplicativo de zeladoria,  
> **Eu quero** listar ocorrências com filtros por status, categoria, bairro e busca textual, escolhendo se desejo carregar as miniaturas de foto,  
> **Para que** o aplicativo renderize o feed urbano de forma fluida sem consumo excessivo de tráfego de dados.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Endpoint `GET /api/v1/chamados` com paginação base 0 (`page`, `pageSize`) e ordenação temporal.
- [x] Filtros combinados via query parameters: `status`, `categoriaId`, `bairroId`, `busca`, `apenasMeus` e `incluirFoto`.
- [x] Parâmetro `incluirFoto=true` projetando a string Base64 da imagem diretamente em `ChamadoResumoResponse` para visualização de miniaturas no feed móvel.
- [x] Endpoint `GET /api/v1/chamados/{id}` retornando a foto completa em Base64 e a trilha histórica imutável de movimentações.

##### Commits vinculados (GitHub Repository):
- [`894b532`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/894b532) — `feat(api): implementar Minimal APIs RESTful, JWT Bearer, HATEOAS, Idempotency e Rate Limiting` *(vinculado em AB#34)*
- [`ee3696b`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/ee3696b) — `docs(readme): atualizar documentacao tecnica, diagramas logico e relacional e integracao mobile` *(vinculado em AB#34)*

---

#### 🔹 [PBI-09] Idempotência de Requisições com Header Idempotency-Key e Rate Limiting Nativo
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#203`
* **Parent Feature:** `[FEATURE 03] Minimal APIs RESTful, Segurança JWT e Resiliência HTTP` (#34)
* **Title:** `[PBI-09] Idempotência de Requisições com Header Idempotency-Key e Rate Limiting Nativo`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DotNet`
* **Business Value:** `100`
* **State:** `Committed`
* **Assigned To:** `MR563428@fiap.com.br`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`

##### Descrição (História de Usuário)
> **Como** arquiteto de sistemas distribuídos,  
> **Eu quero** proteger a API contra submissões duplicadas por instabilidade de rede móvel e contra abusos volumétricos de requisições,  
> **Para que** o sistema preserve integridade de chamados e alta disponibilidade operacional.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Interceptor `IdempotencyFilter` inspecionando o cabeçalho HTTP `Idempotency-Key` em `POST /chamados` e `PATCH /chamados/{id}/status`.
- [x] Armazenamento temporário do código de status e corpo da resposta original, devolvendo cabeçalho `Idempotent-Replayed: true` em requisições repetidas.
- [x] Rate Limiting nativo ASP.NET Core configurado com Fixed Window: 100 req/60s (Global) e 10 req/60s (Autenticação).
- [x] Resposta HTTP 429 Too Many Requests com cabeçalho `Retry-After` ao ultrapassar o limite.

##### Commits vinculados (GitHub Repository):
- [`894b532`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/894b532) — `feat(api): implementar Minimal APIs RESTful, JWT Bearer, HATEOAS, Idempotency e Rate Limiting` *(vinculado em AB#34)*

---

### 🏆 [FEATURE 04] Observabilidade Corporativa e Integração com Ecossistema Mobile
* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#204`
* **Parent:** `[EPIC] Advanced Business Development with .NET: API RESTful ZelaFix em .NET 10, EF Core Oracle, Resiliência e Integração Mobile` (#27)
* **Title:** `[FEATURE 04] Observabilidade Corporativa e Integração com Ecossistema Mobile`
* **Tags:** `DotNet`
* **Start Date:** `2026-11-13`
* **Target Date:** `2026-11-17`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Description:** Implementação das sondas de monitoramento em tempo real (Health Checks de conectividade Oracle e ViaCEP), logs estruturados com Serilog e Correlation ID, padronização de erros RFC 7807 Problem Details e integração full-stack com o aplicativo React Native ZelaFix Mobile.
* **Acceptance Criteria:**
  - [x] Endpoints de health checks `/health`, `/health/ready` e `/health/live` respondendo com diagnósticos detalhados.
  - [x] Serilog gravando logs estruturados em formato JSON com identificador distribuído `X-Correlation-ID`.
  - [x] Contrato REST 100% aderente aos fluxos do app mobile (login, cadastro, radar, detalhes e apoio comunitário).

#### 🔹 [PBI-10] Observabilidade com Health Checks Integrados ao Oracle e Logging Estruturado Serilog
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#205`
* **Parent Feature:** `[FEATURE 04] Observabilidade Corporativa e Integração com Ecossistema Mobile` (#204)
* **Title:** `[PBI-10] Observabilidade com Health Checks Integrados ao Oracle e Logging Estruturado Serilog`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DotNet`
* **Business Value:** `100`
* **State:** `Committed`
* **Assigned To:** `MR563428@fiap.com.br`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`

##### Descrição (História de Usuário)
> **Como** engenheiro de SRE e operações de infraestrutura,  
> **Eu quero** monitorar a integridade da aplicação via health checks e rastrear fluxos de requisição por logs estruturados com Correlation ID,  
> **Para que** incidentes de conectividade com o banco de dados Oracle ou serviços externos sejam diagnosticados instantaneamente.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Verificador customizado de banco Oracle (`OracleDbHealthCheck`) testando `CanConnectAsync()` e pool de conexões.
- [x] Verificador de serviço externo (`ViaCepHealthCheck`) testando disponibilidade da API de CEP.
- [x] Resposta customizada via `HealthResponseWriter` devolvendo JSON estruturado com status geral e latência de cada dependência.
- [x] Middleware `CorrelationIdMiddleware` propagando `X-Correlation-ID` entre cabeçalhos de resposta e contexto do Serilog.

##### Commits vinculados (GitHub Repository):
- [`894b532`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/894b532) — `feat(api): implementar Minimal APIs RESTful, JWT Bearer, HATEOAS, Idempotency e Rate Limiting`
- [`cd487c4`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/cd487c4) — `docs: documenta arquitetura, rubrica GS2, endpoints, healthchecks e execucao local com Docker`

---

#### 🔹 [PBI-11] Integração Full-Stack com App Mobile React Native e Compatibilização de Rotas
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#206`
* **Parent Feature:** `[FEATURE 04] Observabilidade Corporativa e Integração com Ecossistema Mobile` (#204)
* **Title:** `[PBI-11] Integração Full-Stack com App Mobile React Native e Compatibilização de Rotas`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DotNet`
* **Business Value:** `100`
* **State:** `Committed`
* **Assigned To:** `MR563428@fiap.com.br`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`

##### Descrição (História de Usuário)
> **Como** desenvolvedor mobile integrando o app ZelaFix Mobile,  
> **Eu quero** consumir os endpoints padronizados sob o prefixo `/api/v1` com suporte a miniaturas e ordenação cronológica de protocolo,  
> **Para que** a experiência do munícipe nas telas de Radar do Bairro e Acompanhamento de Chamados seja fluida, ágil e estável.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Mapeamento e testes das rotas `/api/v1/auth`, `/api/v1/chamados`, `/api/v1/categorias` e `/api/v1/dashboard`.
- [x] Compatibilidade com requisições com token JWT Bearer no cabeçalho `Authorization`.
- [x] Ordenação da trilha de andamento de protocolo (`HIST_CHAMADO`) das atualizações mais recentes primeiro no app mobile.
- [x] Estabilidade no envio de fotos em Base64 através do payload JSON e eliminação de conflitos de renderização em listas (`FlatList`).

##### Commits vinculados (GitHub Repository):
- [`894b532`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/894b532) — `feat(api): implementar Minimal APIs RESTful, JWT Bearer, HATEOAS, Idempotency e Rate Limiting`
- [`ee3696b`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/ee3696b) — `docs(readme): atualizar documentacao tecnica, diagramas logico e relacional e integracao mobile`

---

#### 🔹 [PBI-12] Estatísticas Consolidadas de Chamados e Filtros Territoriais no Radar
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#207`
* **Parent Feature:** `[FEATURE 04] Observabilidade Corporativa e Integração com Ecossistema Mobile` (#204)
* **Title:** `[PBI-12] Estatísticas Consolidadas de Chamados e Filtros Territoriais no Radar`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DotNet`
* **Business Value:** `100`
* **State:** `Committed`
* **Assigned To:** `MR563428@fiap.com.br`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`

##### Descrição (História de Usuário)
> **Como** gestor da subprefeitura ou cidadão acompanhando indicadores urbanos,  
> **Eu quero** consultar métricas consolidadas de zeladoria e filtrar ocorrências por bairro, categoria e ordenação por apoios,  
> **Para que** o poder público e os moradores identifiquem demandas prioritárias rapidamente.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Endpoint `GET /api/v1/chamados/estatisticas` (e `/chamados/estatisticas`) retornando totais de chamados abertos, em andamento, resolvidos, rejeitados e total de apoios.
- [x] Filtros dinâmicos no repositório EF Core por `BairroId`, `CategoriaId`, `Status`, `Busca` e ordenação (`Recentes` / `MaisApoiados`).
- [x] Consultas agregadas via LINQ no EF Core com projeção direta para alta velocidade de execução.
- [x] Tratamento de exceções e retorno padronizado RFC 7807 em caso de parâmetros inválidos.

##### Commits vinculados (GitHub Repository):
- [`894b532`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/894b532) — `feat(api): implementar Minimal APIs RESTful, JWT Bearer, HATEOAS, Idempotency e Rate Limiting`
- [`f5a8305`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/f5a8305) — `fix(api,infra,swagger): expor todos os endpoints no Swagger, compatibilizar EF Core com Oracle 19c, auto-migrar/semear banco e corrigir StatusAnterior`

---

### 🏆 [FEATURE 05] Qualidade de Software, Testes Automatizados e Governança
* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#208`
* **Parent:** `[EPIC] Advanced Business Development with .NET: API RESTful ZelaFix em .NET 10, EF Core Oracle, Resiliência e Integração Mobile` (#27)
* **Title:** `[FEATURE 05] Qualidade de Software, Testes Automatizados e Governança`
* **Tags:** `DotNet`
* **Start Date:** `2026-11-15`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Description:** Implementação de rigorosa suíte de testes automatizados com xUnit cobrindo cenários unitários e de integração no padrão Arrange-Act-Assert (AAA) com cobertura superior a 91% em todas as camadas, documentação interativa Swagger OpenAPI 3.0 com 23 paths expostos e governança no Render/GitHub.
* **Acceptance Criteria:**
  - [x] 53 testes unitários cobrindo domínio (`98.11%`) e aplicação (`94.20%`) com `ViaCepService`, `FotoImagem` e `RegisterRequest`.
  - [x] 53 testes de integração HTTP utilizando `WebApplicationFactory`, cobrindo `Api` (`95.28%`) e `Infrastructure` (`91.73%`).
  - [x] 106 testes executados com sucesso no `dotnet test` (0 falhas).
  - [x] Swagger OpenAPI expondo todos os 23 paths em 7 grupos incluindo Health Checks, respostas HTTP completas (`400`/`401`/`403`/`404`/`429`/`500`) e rotas diretas Mobile.

#### 🔹 [PBI-13] Suíte de Testes Unitários de Domínio e Aplicação com xUnit no Padrão AAA e Moq
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#209`
* **Parent Feature:** `[FEATURE 05] Qualidade de Software, Testes Automatizados e Governança` (#208)
* **Title:** `[PBI-13] Suíte de Testes Unitários de Domínio e Aplicação com xUnit no Padrão AAA e Moq`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DotNet`
* **Business Value:** `100`
* **State:** `Committed`
* **Assigned To:** `MR563428@fiap.com.br`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`

##### Descrição (História de Usuário)
> **Como** desenvolvedor responsável pela confiabilidade do backend,  
> **Eu quero** testes unitários para a camada de domínio e serviços de aplicação utilizando xUnit e Moq no padrão AAA,  
> **Para que** regras críticas de zeladoria, hashing de senhas e validação de invariantes não sofram regressões.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Projeto `ZelaFix.Tests.Unit` com 53 testes cobrindo domínio (`EnderecoTests`, `StatusTests`, `UsuarioTests`, `DomainEntitiesTests`).
- [x] Testes de aplicação (`AuthServiceTests`, `CategoriaServiceTests`, `ChamadoServiceTests`, `FotoImagemTests`, `TokenServiceTests`, `ViaCepAndRegisterTests`).
- [x] Estrutura estrita do padrão Arrange-Act-Assert em cada caso de teste.
- [x] Cobertura de linhas de `98.11%` no Domínio e `94.20%` na Aplicação.

##### Commits vinculados (GitHub Repository):
- [`e5f9a26`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/e5f9a26) — `test(unit): implementar testes unitarios com xUnit no padrao AAA`
- [`49be863`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/49be863) — `test: atualiza testes unitarios e de integracao validando ciclo de vida, apoio e status`
- [`6979213`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/6979213) — `test,docs: elevar cobertura acima de 91% (106 testes), adicionar evidencias Oracle e atualizar catalogo de endpoints no README`
- [`090f676`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/090f676) — `feat: Só add imagens que estavam faltando no readme`
- [`3aa650d`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/3aa650d) — `feat: Pequena modificação no README`
- [`d627367`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/d627367) — `docs(readme): aprimorar documentacao de integracao mobile, catalogo de endpoints e matriz de rastreabilidade do backlog`
- [`5d8796d`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/5d8796d) — `feat: Pequeno ajuste no readme`
- [`f273ea1`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/f273ea1) — `docs(readme): sincronizar identificadores oficiais do Azure Boards (#27 a #211)`
- [`5e864d9`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/5e864d9) — `build(docker): adicionar Dockerfile multi-stage .NET 10 e suporte a porta dinamica para deploy no Render`
- [`10411be`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/10411be) — `feat: add identificação.txt`
- [`1b71bae`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/1b71bae) — `feat: Só um pequeno ajuste no identificação.txt`
- [`0cc6ff4`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/0cc6ff4) — `chore: remove hardcoded Jwt:Key from appsettings, document Idempotency-Key in Swagger, update identificacao.txt and README (106 tests)`

---

#### 🔹 [PBI-14] Testes de Integração com WebApplicationFactory, Banco em Memória e Contratos HTTP
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#210`
* **Parent Feature:** `[FEATURE 05] Qualidade de Software, Testes Automatizados e Governança` (#208)
* **Title:** `[PBI-14] Testes de Integração com WebApplicationFactory, Banco em Memória e Contratos HTTP`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DotNet`
* **Business Value:** `100`
* **State:** `Committed`
* **Assigned To:** `MR563428@fiap.com.br`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`

##### Descrição (História de Usuário)
> **Como** engenheiro de qualidade e compliance,  
> **Eu quero** executar testes de integração HTTP de ponta a ponta levantando o servidor em memória com `WebApplicationFactory`,  
> **Para que** a comunicação entre pipeline ASP.NET Core, filtros, autenticação JWT, banco de dados e respostas REST seja validada integralmente.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Projeto `ZelaFix.Tests.Integration` com 53 testes usando `CustomWebApplicationFactory` e `RepositoriesAndInfrastructureTests`.
- [x] Testes ponta a ponta de autenticação, categorias, chamados, idempotência (`Idempotent-Replayed: true`), observabilidade e `GlobalExceptionHandler`.
- [x] Cobertura de `95.28%` na API e `91.73%` na Infraestrutura (excluindo migrations DDL geradas).
- [x] Validação end-to-end contra Oracle 19c com as 6 imagens reais da pasta `situacoes-imagens`.

##### Commits vinculados (GitHub Repository):
- [`53dd111`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/53dd111) — `test(integration): implementar testes de integracao com WebApplicationFactory`
- [`6979213`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/6979213) — `test,docs: elevar cobertura acima de 91% (106 testes), adicionar evidencias Oracle e atualizar catalogo de endpoints no README`
- [`090f676`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/090f676) — `feat: Só add imagens que estavam faltando no readme`
- [`3aa650d`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/3aa650d) — `feat: Pequena modificação no README`
- [`d627367`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/d627367) — `docs(readme): aprimorar documentacao de integracao mobile, catalogo de endpoints e matriz de rastreabilidade do backlog`
- [`5d8796d`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/5d8796d) — `feat: Pequeno ajuste no readme`
- [`f273ea1`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/f273ea1) — `docs(readme): sincronizar identificadores oficiais do Azure Boards (#27 a #211)`
- [`5e864d9`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/5e864d9) — `build(docker): adicionar Dockerfile multi-stage .NET 10 e suporte a porta dinamica para deploy no Render`
- [`10411be`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/10411be) — `feat: add identificação.txt`
- [`1b71bae`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/1b71bae) — `feat: Só um pequeno ajuste no identificação.txt`
- [`0cc6ff4`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/0cc6ff4) — `chore: remove hardcoded Jwt:Key from appsettings, document Idempotency-Key in Swagger, update identificacao.txt and README (106 tests)`

---

#### 🔹 [PBI-15] Documentação OpenAPI/Swagger 3.0, Diagramas de Arquitetura e README Técnico
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#211`
* **Parent Feature:** `[FEATURE 05] Qualidade de Software, Testes Automatizados e Governança` (#208)
* **Title:** `[PBI-15] Documentação OpenAPI/Swagger 3.0, Diagramas de Arquitetura e README Técnico`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `DotNet`
* **Business Value:** `100`
* **State:** `Committed`
* **Assigned To:** `MR563428@fiap.com.br`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 2`

##### Descrição (História de Usuário)
> **Como** avaliador acadêmico, gestor ou novo desenvolvedor ingressando no projeto,  
> **Eu quero** documentação técnica completa contendo guia de execução via Docker/Render, prints do Oracle SQL Developer, Swagger completo e diagramas arquiteturais,  
> **Para que** a API possa ser compreendida, executada e integrada rapidamente sem atritos de configuração.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Interface Swagger UI ativa na raiz (`/`) expondo todos os 23 paths em 7 grupos (incluindo Health Checks e rotas Mobile).
- [x] Evidências visuais das tabelas populadas no Oracle Database 19c, Swagger UI e Health Checks em `docs/`.
- [x] Guia de inicialização local com Docker Oracle Free e link de produção no Render documentados em `README.md`.
- [x] Referência explícita e verificação de alinhamento com o app móvel `Mobile-Application-Development-Dot-Net` e seção obrigatória de Declaração de Uso de IA no `README.md`.

##### Commits vinculados (GitHub Repository):
- [`ee3696b`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/ee3696b) — `docs(readme): atualizar documentacao tecnica, diagramas logico e relacional e integracao mobile`
- [`cd487c4`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/cd487c4) — `docs: documenta arquitetura, rubrica GS2, endpoints, healthchecks e execucao local com Docker`
- [`f5a8305`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/f5a8305) — `fix(api,infra,swagger): expor todos os endpoints no Swagger, compatibilizar EF Core com Oracle 19c, auto-migrar/semear banco e corrigir StatusAnterior`
- [`6979213`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/6979213) — `test,docs: elevar cobertura acima de 91% (106 testes), adicionar evidencias Oracle e atualizar catalogo de endpoints no README`
- [`090f676`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/090f676) — `feat: Só add imagens que estavam faltando no readme`
- [`3aa650d`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/3aa650d) — `feat: Pequena modificação no README`
- [`d627367`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/d627367) — `docs(readme): aprimorar documentacao de integracao mobile, catalogo de endpoints e matriz de rastreabilidade do backlog`
- [`5d8796d`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/5d8796d) — `feat: Pequeno ajuste no readme`
- [`f273ea1`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/f273ea1) — `docs(readme): sincronizar identificadores oficiais do Azure Boards (#27 a #211)`
- [`5e864d9`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/5e864d9) — `build(docker): adicionar Dockerfile multi-stage .NET 10 e suporte a porta dinamica para deploy no Render`
- [`10411be`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/10411be) — `feat: add identificação.txt`
- [`1b71bae`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/1b71bae) — `feat: Só um pequeno ajuste no identificação.txt`
- [`0cc6ff4`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/0cc6ff4) — `chore: remove hardcoded Jwt:Key from appsettings, document Idempotency-Key in Swagger, update identificacao.txt and README (106 tests)`
- [`8a280bd`](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net/commit/8a280bd) — `fix(gs2): semear usuários padrão RBAC, completar respostas OpenAPI e alinhar documentação`
