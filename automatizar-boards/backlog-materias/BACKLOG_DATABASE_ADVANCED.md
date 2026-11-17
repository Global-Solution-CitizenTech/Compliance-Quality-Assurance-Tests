# 🗄️ ZelaFix — Backlog Master Azure Boards: Database Advanced

> **Projeto Integrado:** ZelaFix — Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  
> **Disciplina:** Mastering Relational and Non-Relational Database (FIAP — 2TDSPG)  
> **Repositório GitHub:** [Global-Solution-CitizenTech/Database-Advanced](https://github.com/Global-Solution-CitizenTech/Database-Advanced)  
> **Organização / Projeto Azure DevOps:** `ZelaFixGS` / `ZelaFix`  
> **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`  
> **Tag Oficial:** `Database`  
> **Responsible Owner:** `RM566422@fiap.com.br` (Lucas Barros Gouveia)  
> **Epic Principal:** `[EPIC] Database Advanced: Modelagem Relacional Oracle 3FN, Automações PL/SQL e Persistência NoSQL MongoDB` (**AB#36**)  
> **Start Date:** `2026-11-04`  
> **Target Date:** `2026-11-19`  
> **Padrão:** Azure Boards (Scrum Process: Epic ➔ Feature ➔ PBI)  
> **Diretrizes Estratégicas:** Engenharia de banco de dados relacional em 3ª Forma Normal estrita no Oracle SQL Developer Data Modeler 24.3 com **13 tabelas** (`estado`, `cidade`, `bairro`, `endereco`, `usuario`, `telefone`, `categoria`, `status`, `prioridade`, `orgao_governo`, `chamado`, `hist_chamado`, `voto_chamado`) + tabela de auditoria DML (`auditoria_dml_chamado`), script DDL (`2TDSPG_2026_CodigoSql_ZelaFix.sql`) com identity columns, `CHECK` constraints alinhadas aos 5 ENUMs da API Java (`cargo`, `categoria`, `status`, `prioridade`, `orgao_governo`) e índices de cobertura (`idx_hist_chamado_ativo`), empacotamento avançado em Packages PL/SQL (`PKG_CHAMADO_GESTAO` e `PKG_ENGAJAMENTO_CIDADAO`) com `PRAGMA UDF`, conversão **100% manual para JSON em CLOB** (`fn_converter_chamado_json`), **subtotais e total geral feitos à mão** via quebra de grupo (`pr_relatorio_subtotal_bairros`), tratamento específico de exceções (`PRAGMA EXCEPTION_INIT`), trilha de auditoria DML (`TRG_AUDIT_CHAMADO`), validação cívica de voto (`TRG_VALIDA_VOTO_CHAMADO`), blocos anônimos com cursores explícitos, persistência poliglota com MongoDB Atlas (`chamados` e `bairros_monitoramento` com validação `$jsonSchema`, 13 documentos em datasets JSON e scripts modulares para Compass/`mongosh`) e 3 relatórios analíticos comparados em SQL Oracle e Aggregation Pipeline.

---

## 👥 Integrantes do Grupo (Ordem Alfabética Estrita)

| Integrante | RM | Turma | Papel / Responsabilidade |
| :--- | :---: | :---: | :--- |
| **Enzo Okuizumi Miranda de Souza** | **561432** | 2TDSPG | Java Advanced (Microsserviços, RabbitMQ, Spring AI) & Compliance |
| **Gustavo Keiji Okada** | **563428** | 2TDSPG | Back-end .NET Enterprise & Minimal APIs |
| **Lucas Barros Gouveia** | **566422** | 2TDSPG | **Database Modeling, Engenharia Oracle 3FN, PL/SQL & MongoDB** |
| **Luna de Carvalho Guimarães** | **562290** | 2TDSPG | Mobile Application Development (React Native / Expo) |
| **Milton Jakson de Sousa Marcelino** | **564836** | 2TDSPG | DevOps Tools, Cloud Computing & CI/CD Pipelines |

---

## 🌳 1. Estrutura Hierárquica no Azure Boards

```text
📌 [EPIC] Database Advanced: Modelagem Relacional Oracle 3FN, Automações PL/SQL e Persistência NoSQL MongoDB
│
├── 🏆 [FEATURE 01] Modelagem Conceitual, Lógica e Relacional no Oracle Data Modeler em 3FN
│   ├── 🔹 [PBI-01] Modelo Entidade-Relacionamento (MER), Diagramas Lógico e Relacional 3FN (3 pts)
│   ├── 🔹 [PBI-02] Script DDL 3FN com Sequences, Constraints, Índices de Cobertura e BLOB (3 pts)
│   └── 🔹 [PBI-03] Blocos Anônimos PL/SQL com Cursores Explícitos, Estruturas de Decisão e Laços (3 pts)
│
├── 🏆 [FEATURE 02] Automação em PL/SQL Avançado (Packages, Procedures e Functions com PRAGMA UDF)
│   ├── 🔹 [PBI-04] Package PKG_CHAMADO_GESTAO para Gestão de Ocorrências e Resolução em O(1) (3 pts)
│   └── 🔹 [PBI-05] Package PKG_ENGAJAMENTO_CIDADAO para Apoios Comunitários e Ranking (3 pts)
│
├── 🏆 [FEATURE 03] Gatilhos & Trilha de Auditoria DML e Integridade Transacional
│   ├── 🔹 [PBI-06] Trigger TRG_AUDIT_CHAMADO e Tabela de Auditoria DML (:OLD vs :NEW) (3 pts)
│   └── 🔹 [PBI-07] Trigger TRG_VALIDA_VOTO_CHAMADO para Bloqueio de Autovoto e Unicidade (3 pts)
│
└── 🏆 [FEATURE 04] Persistência Poliglota com MongoDB Atlas e Relatórios Analíticos Agregados
    ├── 🔹 [PBI-08] Provisionamento NoSQL no MongoDB com jsonSchema e Datasets JSON (3 pts)
    ├── 🔹 [PBI-09] Matriz de Mapeamento Relacional para Documental e 3 Relatórios Analíticos (3 pts)
    └── 🔹 [PBI-10] Documentação Técnica Completa (README.md), Dicionário de Dados e Cluster (3 pts)
```

---

## 📊 2. Tabela Resumo do Backlog & Rastreabilidade

| Feature Pai | ID do PBI | Título do Item de Backlog (PBI) | ID Azure Boards | Story Points | Prioridade | Business Value | Horas Estimadas | Status |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **[FEATURE 01] Modelagem & DDL** `[AB#37]` | **PBI-01** | Modelo Entidade-Relacionamento (MER), Diagramas Lógico e Relacional 3FN | **#38** | 3 pts | 1 - Critical | 100 | 7.0h | Committed |
| | **PBI-02** | Script DDL 3FN com Sequences, Constraints, Índices de Cobertura e BLOB | **#39** | 3 pts | 1 - Critical | 100 | 6.5h | Committed |
| | **PBI-03** | Blocos Anônimos PL/SQL com Cursores Explícitos, Estruturas de Decisão e Laços | **#119** | 3 pts | 1 - Critical | 100 | 5.5h | Committed |
| **[FEATURE 02] PL/SQL Packages** `[AB#40]` | **PBI-04** | Package PKG_CHAMADO_GESTAO para Gestão de Ocorrências e Resolução em O(1) | **#41** | 3 pts | 1 - Critical | 100 | 8.0h | Committed |
| | **PBI-05** | Package PKG_ENGAJAMENTO_CIDADAO para Apoios Comunitários e Ranking | **#42** | 3 pts | 1 - Critical | 100 | 7.5h | Committed |
| **[FEATURE 03] Triggers & Auditoria** `[AB#43]` | **PBI-06** | Trigger TRG_AUDIT_CHAMADO e Tabela de Auditoria DML (:OLD vs :NEW) | **#44** | 3 pts | 1 - Critical | 100 | 6.5h | Committed |
| | **PBI-07** | Trigger TRG_VALIDA_VOTO_CHAMADO para Bloqueio de Autovoto e Unicidade | **#45** | 3 pts | 1 - Critical | 100 | 6.0h | Committed |
| **[FEATURE 04] NoSQL MongoDB** `[AB#46]` | **PBI-08** | Provisionamento NoSQL no MongoDB com jsonSchema e Datasets JSON | **#47** | 3 pts | 1 - Critical | 100 | 7.0h | Committed |
| | **PBI-09** | Matriz de Mapeamento Relacional para Documental e 3 Relatórios Analíticos | **#120** | 3 pts | 1 - Critical | 100 | 8.0h | Committed |
| | **PBI-10** | Documentação Técnica Completa (README.md), Dicionário de Dados e Cluster | **#121** | 3 pts | 1 - Critical | 100 | 6.0h | Committed |
| **TOTAL CONSOLIDADO** | **4 Features** | **10 PBIs (15 Work Items no Azure Boards)** | **`#36`..`#47`, `#119`..`#121`** | **30 pts** | — | — | **68.0h** | **100% Sincronizado** |

---

## 📦 3. Detalhamento dos Itens de Trabalho (Épico, Features e PBIs)

---

### 🏛️ ÉPICO

* **Work Item Type:** `Epic`
* **Azure Boards ID:** `#36`
* **Title:** `[EPIC] Database Advanced: Modelagem Relacional Oracle 3FN, Automações PL/SQL e Persistência NoSQL MongoDB`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Database`
* **Assigned To:** `RM566422@fiap.com.br`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `30`
* **Business Value:** `100`
* **Description:** Engenharia completa da camada de dados do ZelaFix atendendo integralmente à rubrica da disciplina: modelagem relacional estrita em 3FN no Oracle SQL Developer Data Modeler 24.3 com **13 tabelas** (`estado`, `cidade`, `bairro`, `endereco`, `usuario`, `telefone`, `categoria`, `status`, `prioridade`, `orgao_governo`, `chamado`, `hist_chamado`, `voto_chamado`), script DDL (`2TDSPG_2026_CodigoSql_ZelaFix.sql`) com identity columns, `CHECK` constraints alinhadas aos ENUMs Java, índices de cobertura (`idx_hist_chamado_ativo`) e carga realista de sementes, pacotes PL/SQL avançados (`PKG_CHAMADO_GESTAO` e `PKG_ENGAJAMENTO_CIDADAO`) com `PRAGMA UDF`, conversão manual de JSON em `CLOB` (`fn_converter_chamado_json`), subtotais e total geral manuais via quebra de grupo (`pr_relatorio_subtotal_bairros`), tratamento específico de exceções (`PRAGMA EXCEPTION_INIT`), trilha de auditoria DML (`TRG_AUDIT_CHAMADO` + `AUDITORIA_DML_CHAMADO`) e validação cívica (`TRG_VALIDA_VOTO_CHAMADO`), blocos anônimos com cursores explícitos, persistência poliglota no MongoDB Atlas (coleções `chamados` e `bairros_monitoramento` validadas com `$jsonSchema`, 13 documentos JSON e scripts modulares para Compass/`mongosh`) e 3 relatórios analíticos comparando SQL Oracle e Aggregation Pipeline NoSQL.
* **Acceptance Criteria:**
  - [x] Modelagem conceitual, lógica e relacional 3FN com 13 tabelas exportada em `data modeler/citizenTech.ddl`, `docs/logical.png` e `docs/relational.png`.
  - [x] Script DDL (`2TDSPG_2026_CodigoSql_ZelaFix.sql`) idempotente, alinhado aos 5 ENUMs Java (`cargo`, `categoria`, `status`, `prioridade`, `orgao_governo`) e com carga inicial completa.
  - [x] Pacotes PL/SQL (`PKG_CHAMADO_GESTAO`, `PKG_ENGAJAMENTO_CIDADAO`), triggers (`TRG_AUDIT_CHAMADO`, `TRG_VALIDA_VOTO_CHAMADO`), blocos anônimos e suíte de testes (`2TDSPG_2026_Pacotes_ZelaFix.sql`) sem funções nativas JSON/ROLLUP e sem `WHEN OTHERS` isolado.
  - [x] Persistência NoSQL MongoDB Atlas (`mongodb/`) com validadores `$jsonSchema`, datasets (`chamados_dataset.json` + `bairros_dataset.json`) e 3 relatórios analíticos equivalentes ao Oracle SQL.

---

### 🏆 [FEATURE 01] Modelagem Conceitual, Lógica e Relacional no Oracle Data Modeler em 3FN

* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#37`
* **Parent:** `[EPIC] Database Advanced: Modelagem Relacional Oracle 3FN, Automações PL/SQL e Persistência NoSQL MongoDB` (`#36`)
* **Title:** `[FEATURE 01] Modelagem Conceitual, Lógica e Relacional no Oracle Data Modeler em 3FN`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Database`
* **Assigned To:** `RM566422@fiap.com.br`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-13`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Description:** Concepção da arquitetura relacional em 3FN com 13 tabelas no Oracle SQL Developer Data Modeler 24.3, provisionamento DDL corporativo com identity columns, `CHECK` constraints alinhadas aos ENUMs Java, índices de cobertura e execução de blocos anônimos PL/SQL para relatórios administrativos e auditoria de SLA.
* **Acceptance Criteria:**
  - [x] Diagramas Lógico e Relacional de 13 tabelas exportados em PNG de alta resolução em `docs/logical.png` e `docs/relational.png` e DDL `data modeler/citizenTech.ddl`.
  - [x] Script DDL `2TDSPG_2026_CodigoSql_ZelaFix.sql` executável de forma idempotente no Oracle com 13 tabelas 3FN + `auditoria_dml_chamado`, FKs, índices e carga inicial.
  - [x] 2 blocos anônimos PL/SQL utilizando `IF/ELSIF/ELSE`, `LOOP`, cursores explícitos e suíte de integração em `2TDSPG_2026_Pacotes_ZelaFix.sql`.

---

#### 🔹 [PBI-01] Modelo Entidade-Relacionamento (MER), Diagramas Lógico e Relacional 3FN

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#38`
* **Parent Feature:** `[FEATURE 01] Modelagem Conceitual, Lógica e Relacional no Oracle Data Modeler em 3FN` (`#37`)
* **Title:** `[PBI-01] Modelo Entidade-Relacionamento (MER), Diagramas Lógico e Relacional 3FN`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Database`
* **Assigned To:** `RM566422@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** DBA e Arquiteto de Dados,  
> **Eu quero** modelar as 13 entidades da zeladoria urbana no Oracle Data Modeler 24.3 garantindo normalização estrita até a 3ª Forma Normal,  
> **Para que** todas as relações de autoria, localização territorial, prioridade, órgão governamental, histórico de status e apoios comunitários sejam íntegras e sem redundâncias.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Modelagem de 13 entidades no Data Modeler (`citizenTech.dmd` e `citizenTech.ddl`): `estado`, `cidade`, `bairro`, `endereco`, `usuario`, `telefone`, `categoria`, `status`, `prioridade`, `orgao_governo`, `chamado`, `hist_chamado` e `voto_chamado`.
- [x] Normalização estrita 3FN: status vigente desacoplado de `chamado` e mantido em `hist_chamado`; atributos `prioridade` (`prioridade_id_prioridade`) e `orgao_governo` (`orgao_governo_id_orgao`) normalizados em tabelas próprias com FKs em `chamado`.
- [x] Exportação de diagramas conceituais/físicos atualizados em `docs/logical.png` e `docs/relational.png`.

##### Commits vinculados (GitHub Repository):
- [`9df0325`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/9df0325) — `Initial commit` *(vinculado em AB#38 e AB#36)*
- [`6f944bf`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/6f944bf) — `feat: Subindo diagrama base do projeto.` *(vinculado em AB#38)*
- [`2a09190`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/2a09190) — `feat: Dando aquela reorganizada na modelagem!` *(vinculado em AB#38)*
- [`90565f0`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/90565f0) — `feat: Removendo comentário da modelagem` *(vinculado em AB#38)*
- [`90c91b8`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/90c91b8) — `feat: Alterando modelagem` *(expansão para 13 tabelas com `prioridade` e `orgao_governo`, 30 constraints e novos diagramas `logical.png`/`relational.png` — vinculado em AB#38)*

---

#### 🔹 [PBI-02] Script DDL 3FN com Sequences, Constraints, Índices de Cobertura e BLOB

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#39`
* **Parent Feature:** `[FEATURE 01] Modelagem Conceitual, Lógica e Relacional no Oracle Data Modeler em 3FN` (`#37`)
* **Title:** `[PBI-02] Script DDL 3FN com Sequences, Constraints, Índices de Cobertura e BLOB`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Database`
* **Assigned To:** `RM566422@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** engenheiro de banco de dados,  
> **Eu quero** gerar o script DDL executável com identity/sequences, chaves primárias, estrangeiras, `CHECK` constraints alinhadas aos ENUMs da API Java, índices de cobertura e campo BLOB para fotos,  
> **Para que** as aplicações Java, .NET e IA tenham uma base de dados homologada, consistente e de alta performance de I/O.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Script `2TDSPG_2026_CodigoSql_ZelaFix.sql` idempotente (Parte 0 com drop seguro) contendo DDL completo das 13 tabelas 3FN + `auditoria_dml_chamado` e carga inicial de sementes (5 estados, 5 cidades, 5 bairros, 5 endereços, 5 usuários BCrypt, 5 telefones, 6 categorias, 5 status, 4 prioridades, 6 órgãos, 8 chamados, 16 históricos e 8 votos).
- [x] Coluna `foto BLOB NOT NULL` na tabela `chamado` para armazenamento nativo de evidências fotográficas (10 colunas fiéis ao `citizenTech.ddl`).
- [x] Índice composto de cobertura `idx_hist_chamado_ativo` sobre `(chamado_id_chamado, id_hist DESC, status_id_status)` além de índices em FKs (`idx_chamado_prioridade`, `idx_chamado_orgao`, etc.) e `voto_chamado_un UNIQUE (chamado_id_chamado, usuario_id_usuario)`.
- [x] `CHECK` constraints e sementes alinhadas aos 5 ENUMs Java (`cargo` `CIDADAO`/`GESTOR`/`ADMIN`, `categoria` `ILUMINACAO_PUBLICA`..`SINALIZACAO_E_TRANSITO`, `status` `PENDENTE`..`REJEITADO`, `prioridade` `BAIXA`..`URGENTE`, `orgao_governo` `SECRETARIA_OBRAS`..`SANEAMENTO_BASICO`).

##### Commits vinculados (GitHub Repository):
- [`1937385`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/1937385) — `feat: algumas alterações no banco!` *(vinculado em AB#39)*
- [`02387ba`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/02387ba) — `fix: arrumando alguns detalhes` *(vinculado em AB#39)*
- [`fa19184`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/fa19184) — `feat: Add comentário e dando uma ajustada nos IDs, é isso!` *(vinculado em AB#39)*
- [`1167137`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/1167137) — `feat: Dando uma baita refatorada na modelagem e também add scripts SQL` *(vinculado em AB#39)*
- [`0d261f7`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/0d261f7) — `feat(oracle): refatorar DDL 3FN com indices de cobertura e pacotes PL/SQL com pragma UDF` *(vinculado em AB#39)*
- [`3a9ba3e`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/3a9ba3e) — `feat(db,nosql): alinhar modelagem 13 tabelas, prioridade/orgao_governo e scripts MongoDB` *(vinculado em AB#39)*
- [`46a8d46`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/46a8d46) — `chore: align SQL comments, PL/SQL report width, MongoDB dataset and README with Java enums` *(vinculado em AB#39)*

---

#### 🔹 [PBI-03] Blocos Anônimos PL/SQL com Cursores Explícitos, Estruturas de Decisão e Laços

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#119`
* **Parent Feature:** `[FEATURE 01] Modelagem Conceitual, Lógica e Relacional no Oracle Data Modeler em 3FN` (`#37`)
* **Title:** `[PBI-03] Blocos Anônimos PL/SQL com Cursores Explícitos, Estruturas de Decisão e Laços`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Database`
* **Assigned To:** `RM566422@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** analista de dados municipal,  
> **Eu quero** blocos anônimos PL/SQL com cursores explícitos para processamento em lote de chamados e bairros com estruturas IF/THEN/ELSE e loops, além de suíte de testes de integração idempotente,  
> **Para que** seja possível gerar diagnósticos territoriais, auditar SLAs comprometidos e validar todas as rotinas via DBMS_OUTPUT com `ROLLBACK` seguro.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Bloco Anônimo 1 (Monitoramento Territorial Urbano): cursor explícito `c_analise_territorial`, laço `LOOP/EXIT WHEN`, cálculo de taxa de resolução, invocação de `fn_classificar_criticidade_bairro` e classificação com `IF/ELSIF/ELSE` (`CRITICO`, `ALERTA`, `NORMAL`).
- [x] Bloco Anônimo 2 (Auditoria de SLA de Atendimento): cursor explícito `c_chamados_sla` com `FOR r IN`, detecção de ocorrências abertas há mais de 3 dias, contagem de apoios comunitários e exceção customizada `e_nenhum_ativo`.
- [x] Suíte de Testes de Integração (Parte 5 de `2TDSPG_2026_Pacotes_ZelaFix.sql`) validando abertura/transição/JSON manual, voto/autovoto, subtotais manuais e auditoria DML com `ROLLBACK` ao final.

##### Commits vinculados (GitHub Repository):
- [`1167137`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/1167137) — `feat: Dando uma baita refatorada na modelagem e também add scripts SQL` *(vinculado em AB#119)*
- [`13b1bf9`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/13b1bf9) — `fix(plsql): refatorar testes, otimizar fn_obter_status_atual e sincronizar documentacao` *(vinculado em AB#119)*

---

### 🏆 [FEATURE 02] Automação em PL/SQL Avançado (Packages, Procedures e Functions com PRAGMA UDF)

* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#40`
* **Parent:** `[EPIC] Database Advanced: Modelagem Relacional Oracle 3FN, Automações PL/SQL e Persistência NoSQL MongoDB` (`#36`)
* **Title:** `[FEATURE 02] Automação em PL/SQL Avançado (Packages, Procedures e Functions com PRAGMA UDF)`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Database`
* **Assigned To:** `RM566422@fiap.com.br`
* **Start Date:** `2026-11-08`
* **Target Date:** `2026-11-14`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** Implementação de regras de negócio em pacotes PL/SQL estruturados (`PKG_CHAMADO_GESTAO` e `PKG_ENGAJAMENTO_CIDADAO`), contendo procedures de ciclo de vida, functions compiladas com `PRAGMA UDF`, conversão **100% manual para JSON em CLOB**, relatório territorial com **quebra de grupo e subtotais/total geral feitos à mão** e tratamento explícito de exceções via `PRAGMA EXCEPTION_INIT`.
* **Acceptance Criteria:**
  - [x] 2 pacotes PL/SQL completos (Spec + Body) em `2TDSPG_2026_Pacotes_ZelaFix.sql`.
  - [x] Function `fn_obter_status_atual` com `PRAGMA UDF` resolvendo status vigente em O(1) via `ORDER BY h.id_hist DESC FETCH FIRST 1 ROW ONLY` sobre `idx_hist_chamado_ativo`.
  - [x] Conversão manual para JSON (`fn_converter_chamado_json`) e subtotais manuais por bairro (`pr_relatorio_subtotal_bairros`) sem funções nativas JSON ou `ROLLUP`.

---

#### 🔹 [PBI-04] Package PKG_CHAMADO_GESTAO para Gestão de Ocorrências e Resolução em O(1)

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#41`
* **Parent Feature:** `[FEATURE 02] Automação em PL/SQL Avançado (Packages, Procedures e Functions com PRAGMA UDF)` (`#40`)
* **Title:** `[PBI-04] Package PKG_CHAMADO_GESTAO para Gestão de Ocorrências e Resolução em O(1)`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Database`
* **Assigned To:** `RM566422@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** equipe de zeladoria municipal,  
> **Eu quero** procedures e functions empacotadas para gerenciar a abertura atômica, transição de status, resolução de status em O(1) e serialização manual em JSON das ocorrências,  
> **Para que** as operações de negócio ocorram diretamente no banco com validações de FKs/privilégios e zero overhead de context-switch.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Especificação e corpo de `PKG_CHAMADO_GESTAO` compilados com exceções customizadas `PRAGMA EXCEPTION_INIT` (`-20001` a `-20009`, incluindo `e_prioridade_inexistente` e `e_orgao_inexistente`).
- [x] Procedure `pr_abrir_chamado` recebendo `p_id_prioridade` e `p_id_orgao`, validando foto BLOB e todas as FKs, gravando `chamado` (`RETURNING id_chamado INTO v_novo_id`) e registro inicial `PENDENTE` em `hist_chamado` atomicamente.
- [x] Procedure `pr_atualizar_status_chamado` restringindo transição a usuários com `cargo = 'GESTOR'` e registrando histórico auditável.
- [x] Function `fn_obter_status_atual` (`PRAGMA UDF`) utilizando `ORDER BY h.id_hist DESC FETCH FIRST 1 ROW ONLY` sobre `idx_hist_chamado_ativo` em O(1).
- [x] Function `fn_converter_chamado_json` construindo JSON manualmente em `CLOB` via `DBMS_LOB.CREATETEMPORARY` / `WRITEAPPEND` (sem `JSON_OBJECT`/`JSON_ARRAYAGG`), incluindo objetos aninhados (`categoria`, `prioridade`, `orgaoGoverno`, `cidadao`, `localizacao`) e array `historicoStatus` via cursor explícito.

##### Commits vinculados (GitHub Repository):
- [`0d261f7`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/0d261f7) — `feat(oracle): refatorar DDL 3FN com indices de cobertura e pacotes PL/SQL com pragma UDF` *(vinculado em AB#41)*
- [`8f2285b`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/8f2285b) — `feat(plsql): refatorar pacotes com conversao manual para JSON, subtotais a mao e excecoes especificas` *(vinculado em AB#41)*
- [`13b1bf9`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/13b1bf9) — `fix(plsql): refatorar testes, otimizar fn_obter_status_atual e sincronizar documentacao` *(vinculado em AB#41)*
- [`3a9ba3e`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/3a9ba3e) — `feat(db,nosql): alinhar modelagem 13 tabelas, prioridade/orgao_governo e scripts MongoDB` *(vinculado em AB#41)*

---

#### 🔹 [PBI-05] Package PKG_ENGAJAMENTO_CIDADAO para Apoios Comunitários e Ranking

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#42`
* **Parent Feature:** `[FEATURE 02] Automação em PL/SQL Avançado (Packages, Procedures e Functions com PRAGMA UDF)` (`#40`)
* **Title:** `[PBI-05] Package PKG_ENGAJAMENTO_CIDADAO para Apoios Comunitários e Ranking`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Database`
* **Assigned To:** `RM566422@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** gestor de políticas públicas,  
> **Eu quero** rotinas de banco para gerenciar apoios comunitários, classificar criticidade de bairros e emitir relatório territorial com quebra de grupo e subtotais manuais,  
> **Para que** a prefeitura priorize investimentos nos bairros mais críticos sem depender de funções mágicas de agregação.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Especificação e corpo de `PKG_ENGAJAMENTO_CIDADAO` compilados com exceções específicas (`-20010` a `-20016`, `DUP_VAL_ON_INDEX`, `ZERO_DIVIDE`, `NO_DATA_FOUND`).
- [x] Procedure `pr_registrar_voto` validando existência do chamado/munícipe, bloqueando autovoto (`e_autovoto_proibido`) e chamados encerrados (`CONCLUIDO`/`REJEITADO` -> `e_chamado_fechado`).
- [x] Functions `fn_calcular_total_votos` (`PRAGMA UDF`) e `fn_classificar_criticidade_bairro` (`CRITICO`, `ALERTA`, `NORMAL`).
- [x] Procedure `pr_relatorio_subtotal_bairros` implementando quebra de grupo clássica (Control Break) com acumuladores manuais (`v_sub_*`, `v_tot_*`), cálculo manual da taxa de resolução (%) e largura de colunas alinhada aos ENUMs de categoria (`SINALIZACAO_E_TRANSITO` / `VIAS_E_PAVIMENTACAO`).

##### Commits vinculados (GitHub Repository):
- [`0d261f7`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/0d261f7) — `feat(oracle): refatorar DDL 3FN com indices de cobertura e pacotes PL/SQL com pragma UDF` *(vinculado em AB#42)*
- [`8f2285b`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/8f2285b) — `feat(plsql): refatorar pacotes com conversao manual para JSON, subtotais a mao e excecoes especificas` *(vinculado em AB#42)*
- [`46a8d46`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/46a8d46) — `chore: align SQL comments, PL/SQL report width, MongoDB dataset and README with Java enums` *(vinculado em AB#42)*

---

### 🏆 [FEATURE 03] Gatilhos & Trilha de Auditoria DML e Integridade Transacional

* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#43`
* **Parent:** `[EPIC] Database Advanced: Modelagem Relacional Oracle 3FN, Automações PL/SQL e Persistência NoSQL MongoDB` (`#36`)
* **Title:** `[FEATURE 03] Gatilhos & Trilha de Auditoria DML e Integridade Transacional`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Database`
* **Assigned To:** `RM566422@fiap.com.br`
* **Start Date:** `2026-11-10`
* **Target Date:** `2026-11-15`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** Implementação de triggers de integridade transacional e trilha de auditoria DML alimentando tabela dedicada com captura de `:OLD` vs `:NEW` em formato JSON manual e bloqueio de autovoto/votos em chamados encerrados no nível do SGBD.
* **Acceptance Criteria:**
  - [x] Tabela `AUDITORIA_DML_CHAMADO` criada para rastreabilidade de operações DML.
  - [x] Trigger `TRG_AUDIT_CHAMADO` capturando usuário, data, tipo de operação (`INSERT`/`UPDATE`/`DELETE`) e valores `:OLD` vs `:NEW` incluindo `id_prioridade` e `id_orgao`.
  - [x] Trigger `TRG_VALIDA_VOTO_CHAMADO` impedindo autovoto e votos em chamados `CONCLUIDO` ou `REJEITADO`.

---

#### 🔹 [PBI-06] Trigger TRG_AUDIT_CHAMADO e Tabela de Auditoria DML (:OLD vs :NEW)

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#44`
* **Parent Feature:** `[FEATURE 03] Gatilhos & Trilha de Auditoria DML e Integridade Transacional` (`#43`)
* **Title:** `[PBI-06] Trigger TRG_AUDIT_CHAMADO e Tabela de Auditoria DML (:OLD vs :NEW)`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Database`
* **Assigned To:** `RM566422@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** auditor de compliance e segurança da informação,  
> **Eu quero** que qualquer operação de INSERT, UPDATE ou DELETE na tabela `chamado` gere um registro imutável com os dados antigos e novos em JSON,  
> **Para que** todas as modificações sejam rastreáveis e estejam em conformidade com as diretrizes da LGPD e governança pública.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Tabela `auditoria_dml_chamado` com colunas `id_auditoria`, `nome_usuario`, `tipo_operacao`, `data_hora_operacao`, `valores_anteriores` e `valores_novos`.
- [x] Trigger `trg_audit_chamado` disparada `AFTER INSERT OR UPDATE OR DELETE ON chamado` com captura de `USER`, `SYSTIMESTAMP` e snapshots `:OLD` vs `:NEW` incluindo `id_prioridade` e `id_orgao`.
- [x] Tratamento explícito de `VALUE_ERROR` na trigger e verificação automatizada no Teste 4 da suíte de integração.

##### Commits vinculados (GitHub Repository):
- [`0d261f7`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/0d261f7) — `feat(oracle): refatorar DDL 3FN com indices de cobertura e pacotes PL/SQL com pragma UDF` *(vinculado em AB#44)*
- [`8f2285b`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/8f2285b) — `feat(plsql): refatorar pacotes com conversao manual para JSON, subtotais a mao e excecoes especificas` *(vinculado em AB#44)*
- [`3a9ba3e`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/3a9ba3e) — `feat(db,nosql): alinhar modelagem 13 tabelas, prioridade/orgao_governo e scripts MongoDB` *(vinculado em AB#44)*

---

#### 🔹 [PBI-07] Trigger TRG_VALIDA_VOTO_CHAMADO para Bloqueio de Autovoto e Unicidade

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#45`
* **Parent Feature:** `[FEATURE 03] Gatilhos & Trilha de Auditoria DML e Integridade Transacional` (`#43`)
* **Title:** `[PBI-07] Trigger TRG_VALIDA_VOTO_CHAMADO para Bloqueio de Autovoto e Unicidade`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Database`
* **Assigned To:** `RM566422@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** gestor do aplicativo de zeladoria,  
> **Eu quero** uma trigger BEFORE INSERT que impeça o cidadão de votar no próprio chamado que ele mesmo abriu e bloqueie votos em chamados já encerrados,  
> **Para que** o engajamento popular seja legítimo e não haja fraude na priorização de demandas.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Trigger `trg_valida_voto_chamado` disparada `BEFORE INSERT ON voto_chamado`.
- [x] Validação impedindo que `:NEW.usuario_id_usuario` seja o autor de `chamado.usuario_id_usuario` com `RAISE_APPLICATION_ERROR(-20012)`.
- [x] Validação impedindo votos em chamados com status `CONCLUIDO` ou `REJEITADO` (via `fn_obter_status_atual`) com `RAISE_APPLICATION_ERROR(-20011)` e teste de captura no Teste 2.

##### Commits vinculados (GitHub Repository):
- [`0d261f7`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/0d261f7) — `feat(oracle): refatorar DDL 3FN com indices de cobertura e pacotes PL/SQL com pragma UDF` *(vinculado em AB#45)*
- [`13b1bf9`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/13b1bf9) — `fix(plsql): refatorar testes, otimizar fn_obter_status_atual e sincronizar documentacao` *(vinculado em AB#45)*

---

### 🏆 [FEATURE 04] Persistência Poliglota com MongoDB Atlas e Relatórios Analíticos Agregados

* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#46`
* **Parent:** `[EPIC] Database Advanced: Modelagem Relacional Oracle 3FN, Automações PL/SQL e Persistência NoSQL MongoDB` (`#36`)
* **Title:** `[FEATURE 04] Persistência Poliglota com MongoDB Atlas e Relatórios Analíticos Agregados`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Database`
* **Assigned To:** `RM566422@fiap.com.br`
* **Start Date:** `2026-11-10`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Description:** Persistência NoSQL orientada a documentos no MongoDB Atlas (`zelafix`), scripts modulares essenciais para MongoDB Compass (`>_MONGOSH`) e `mongosh` CLI (`setup_mongodb_chamados.js`, `setup_mongodb_bairros.js`, `consultas_relatorios_mongodb.js`), validação `$jsonSchema` alinhada aos ENUMs Java, datasets JSON (8 chamados + 5 bairros = 13 documentos), matriz de mapeamento relacional->documental e 3 relatórios analíticos comparados em SQL e MongoDB Aggregation Pipeline.
* **Acceptance Criteria:**
  - [x] Scripts `setup_mongodb_chamados.js` e `setup_mongodb_bairros.js` com validação `$jsonSchema` (ENUMs Java), índices estratégicos e compatibilidade Compass/`mongosh`.
  - [x] Carga de 13 documentos JSON comprovada (`chamados_dataset.json`: 8 chamados; `bairros_dataset.json`: 5 bairros).
  - [x] Matriz de mapeamento de transição conceitual fundamentando Embedding vs Referencing e Desnormalização Controlada.
  - [x] 3 relatórios analíticos em `consultas_relatorios_mongodb.js` comparados diretamente com queries SQL Oracle equivalentes.

---

#### 🔹 [PBI-08] Provisionamento NoSQL no MongoDB com jsonSchema e Datasets JSON

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#47`
* **Parent Feature:** `[FEATURE 04] Persistência Poliglota com MongoDB Atlas e Relatórios Analíticos Agregados` (`#46`)
* **Title:** `[PBI-08] Provisionamento NoSQL no MongoDB com jsonSchema e Datasets JSON`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Database`
* **Assigned To:** `RM566422@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** engenheiro de dados NoSQL,  
> **Eu quero** criar as coleções `chamados` e `bairros_monitoramento` no MongoDB com regras de validação `$jsonSchema` alinhadas aos ENUMs Java e popular com datasets ricos via scripts essenciais para Compass e `mongosh`,  
> **Para que** a persistência não relacional garanta tipos estritos de dados e possibilite leituras em O(1) pelo aplicativo mobile.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Validador `validator: { $jsonSchema: ... }` configurado em `setup_mongodb_chamados.js` e `setup_mongodb_bairros.js` com enums estritos (`categoria`, `status_atual`, `triagem_ia.prioridade`, `triagem_ia.orgao_sugerido`, `criticidade`).
- [x] Datasets `chamados_dataset.json` (8 ocorrências com `cidadao`, `localizacao`, `historico`, `votos` e `triagem_ia`) e `bairros_dataset.json` (5 bairros com `indicadores_principais` alinhados ao `CategoriaEnum`) totalizando 13 documentos.
- [x] Simplificação dos artefatos NoSQL mantendo apenas os scripts modulares essenciais para execução direta no MongoDB Compass (`>_MONGOSH`) e `mongosh` CLI com criação de índices estratégicos.

##### Commits vinculados (GitHub Repository):
- [`e4396fb`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/e4396fb) — `feat(mongodb): adicionar datasets de chamados e bairros, dependencias e protecao gitignore` *(vinculado em AB#47)*
- [`6df5e99`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/6df5e99) — `feat(mongodb): implementar scripts de setup, validadores jsonSchema, indices e relatorios analiticos` *(vinculado em AB#47)*
- [`a0025d8`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/a0025d8) — `chore(mongodb): simplificar artefatos nosql mantendo apenas scripts essenciais para compass e mongosh` *(vinculado em AB#47)*
- [`3a9ba3e`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/3a9ba3e) — `feat(db,nosql): alinhar modelagem 13 tabelas, prioridade/orgao_governo e scripts MongoDB` *(vinculado em AB#47)*
- [`46a8d46`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/46a8d46) — `chore: align SQL comments, PL/SQL report width, MongoDB dataset and README with Java enums` *(vinculado em AB#47)*

---

#### 🔹 [PBI-09] Matriz de Mapeamento Relacional para Documental e 3 Relatórios Analíticos

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#120`
* **Parent Feature:** `[FEATURE 04] Persistência Poliglota com MongoDB Atlas e Relatórios Analíticos Agregados` (`#46`)
* **Title:** `[PBI-09] Matriz de Mapeamento Relacional para Documental e 3 Relatórios Analíticos`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Database`
* **Assigned To:** `RM566422@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** cientista de dados e gestor público,  
> **Eu quero** uma matriz comparativa entre os modelos relacional e documental, e 3 relatórios analíticos com Aggregation Pipeline comparados com queries Oracle SQL,  
> **Para que** possamos extrair inteligência de negócios sobre ocorrências mais votadas, gargalos por categoria e monitoramento territorial dos bairros.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Matriz de mapeamento fundamentando Embedding (`cidadao`, `localizacao`, `triagem_ia`, `historico`, `votos`), Desnormalização Controlada (`total_votos`) e Referencing Lógico (`bairros_monitoramento` via `id_bairro`).
- [x] Relatório 1: Ocorrências ativas mais votadas (Radar do Bairro com `find`/`$nin`) comparado em SQL Oracle e MongoDB.
- [x] Relatório 2: Agrupamento por categoria urbana e volume com `$group` e `$cond` (alinhado aos enums `LIMPEZA_URBANA`, `DRENAGEM_E_ESGOTO`, etc.).
- [x] Relatório 3: Panorama territorial de criticidade por bairro com `$group`, `$project` (`$round`, `$multiply`, `$divide`) e `$sort` em equivalência matemática com o Oracle SQL.

##### Commits vinculados (GitHub Repository):
- [`6df5e99`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/6df5e99) — `feat(mongodb): implementar scripts de setup, validadores jsonSchema, indices e relatorios analiticos` *(vinculado em AB#120)*
- [`3a9ba3e`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/3a9ba3e) — `feat(db,nosql): alinhar modelagem 13 tabelas, prioridade/orgao_governo e scripts MongoDB` *(vinculado em AB#120)*

---

#### 🔹 [PBI-10] Documentação Técnica Completa (README.md), Dicionário de Dados e Cluster

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#121`
* **Parent Feature:** `[FEATURE 04] Persistência Poliglota com MongoDB Atlas e Relatórios Analíticos Agregados` (`#46`)
* **Title:** `[PBI-10] Documentação Técnica Completa (README.md), Dicionário de Dados e Cluster`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Database`
* **Assigned To:** `RM566422@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** avaliador acadêmico da FIAP,  
> **Eu quero** um README padronizado contendo links diretos para os artefatos, diagramas oficiais, arquitetura de 13 tabelas, packages PL/SQL, matriz de mapeamento, relatórios comparados e guia de execução Oracle + MongoDB Atlas,  
> **Para que** a entrega técnica possa ser homologada e executada com transparência e clareza.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `README.md` completo no repositório `Database-Advanced` padronizado no modelo CitizenTech com links diretos, diagramas `logical.png`/`relational.png`, documentação das 13 tabelas 3FN, ENUMs Java e arquitetura PL/SQL.
- [x] Guia passo a passo de execução no Oracle Database e no MongoDB Atlas (via Compass `>_MONGOSH` e CLI `mongosh`) com evidências reais de saída dos 3 relatórios.
- [x] Remoção de seções de edital e sincronização completa das tabelas comparativas com os valores finais em uppercase enum.

##### Commits vinculados (GitHub Repository):
- [`009329e`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/009329e) — `docs(readme): atualizar documentacao com diagramas oficiais, matriz de mapeamento e instrucoes do cluster zelafix` *(vinculado em AB#121)*
- [`13b1bf9`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/13b1bf9) — `fix(plsql): refatorar testes, otimizar fn_obter_status_atual e sincronizar documentacao` *(vinculado em AB#121)*
- [`a0025d8`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/a0025d8) — `chore(mongodb): simplificar artefatos nosql mantendo apenas scripts essenciais para compass e mongosh` *(vinculado em AB#121)*
- [`451351b`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/451351b) — `docs(db): padronizar README com links diretos e remover secoes de edital` *(vinculado em AB#121)*
- [`3a9ba3e`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/3a9ba3e) — `feat(db,nosql): alinhar modelagem 13 tabelas, prioridade/orgao_governo e scripts MongoDB` *(vinculado em AB#121)*
- [`46a8d46`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/46a8d46) — `chore: align SQL comments, PL/SQL report width, MongoDB dataset and README with Java enums` *(vinculado em AB#121)*
- [`6a6c157`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/6a6c157) — `feat: só uma pequena atualização no script de mongo` *(vinculado em AB#121)*
- [`d3ea34e`](https://github.com/Global-Solution-CitizenTech/Database-Advanced/commit/d3ea34e) — `feat: Alguns pequenos ajustes no script de DB e identificação.txt` *(vinculado em AB#121)*
