# 🗄️ Backlog Master Azure Boards — Global Solution 2026/2: Database Advanced

> **Projeto Integrado:** ZelaFix — Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  
> **Disciplina:** Mastering Relational and Non-Relational Database (FIAP — 2TDSPG)  
> **Epic Principal:** `[EPIC] Database Advanced: Modelagem Relacional Oracle 3FN, Automações PL/SQL e Persistência NoSQL MongoDB`  
> **Responsável / Owner:** Lucas Barros Gouveia (`RM566422@fiap.com.br`)  
> **Start Date:** `2026-11-04`  
> **Target Date:** `2026-11-19`  
> **Padrão:** Azure Boards (Scrum Process: Epic ➔ Feature ➔ PBI)  
> **Diretrizes Estratégicas:** Engenharia de banco de dados relacional em 3ª Forma Normal estrita no Oracle SQL Developer Data Modeler 24.3, script DDL com sequences, constraints e índices de cobertura (`idx_hist_chamado_ativo`), empacotamento avançado em Packages PL/SQL (`PKG_CHAMADO_GESTAO` e `PKG_ENGAJAMENTO_CIDADAO`) com funções compiladas com `PRAGMA UDF`, trilha de auditoria DML com trigger e tabela dedicada (`TRG_AUDIT_CHAMADO`), blocos anônimos com cursores explícitos, persistência poliglota com MongoDB Atlas (coleções `chamados` e `bairros_monitoramento` com validação de `jsonSchema`), matriz de mapeamento relacional para documental e 3 relatórios analíticos de inteligência urbana comparados em SQL e Aggregation Pipeline.

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

## 🏛️ 1. Estrutura Hierárquica no Azure Boards

```text
[EPIC] Database Advanced: Modelagem Relacional Oracle 3FN, Automações PL/SQL e Persistência NoSQL MongoDB
│
├── 🏆 [FEATURE 01] Modelagem Conceitual, Lógica e Relacional no Oracle Data Modeler em 3FN
│   ├── 📄 [PBI-01] Modelo Entidade-Relacionamento (MER), Diagramas Lógico e Relacional 3FN e Normalização Estrita (3 pts)
│   ├── 📄 [PBI-02] Script DDL 3FN com Sequences, Constraints, Índices de Cobertura e Armazenamento BLOB (3 pts)
│   └── 📄 [PBI-03] Blocos Anônimos PL/SQL com Cursores Explícitos, Estruturas de Decisão e Laços (3 pts)
│
├── 🏆 [FEATURE 02] Automação em PL/SQL Avançado (Packages, Procedures e Functions com PRAGMA UDF)
│   ├── 📄 [PBI-04] Package PKG_CHAMADO_GESTAO para Gestão de Ocorrências e Resolução de Status em O(1) (3 pts)
│   └── 📄 [PBI-05] Package PKG_ENGAJAMENTO_CIDADAO para Gestão de Apoios Comunitários e Ranking de Criticidade (3 pts)
│
├── 🏆 [FEATURE 03] Gatilhos & Trilha de Auditoria DML e Integridade Transacional
│   ├── 📄 [PBI-06] Trigger TRG_AUDIT_CHAMADO e Tabela de Auditoria DML com Captura de :OLD vs :NEW (3 pts)
│   └── 📄 [PBI-07] Trigger TRG_VALIDA_VOTO_CHAMADO para Bloqueio de Autovoto e Garantia de Unicidade (3 pts)
│
└── 🏆 [FEATURE 04] Persistência Poliglota com MongoDB Atlas e Relatórios Analíticos Agregados
    ├── 📄 [PBI-08] Provisionamento NoSQL no MongoDB com Coleções Validadas via jsonSchema e Datasets JSON (3 pts)
    ├── 📄 [PBI-09] Matriz de Mapeamento Relacional para Documental e 3 Relatórios Analíticos com Aggregation (3 pts)
    └── 📄 [PBI-10] Documentação Técnica Completa (README.md), Dicionário de Dados e Homologação do Cluster ZelaFix (3 pts)
```

---

## 📊 2. Tabela Resumo do Backlog

| Feature Pai | ID do PBI | Título do Item de Backlog (PBI) | Story Points | Prioridade | Horas Estimadas |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **[FEATURE 01] Modelagem & DDL** | **PBI-01** | Modelo Entidade-Relacionamento (MER), Diagramas Lógico e Relacional 3FN | 3 pts | 1 - Critical | 7.0h |
| | **PBI-02** | Script DDL 3FN com Sequences, Constraints, Índices de Cobertura e BLOB | 3 pts | 1 - Critical | 6.5h |
| | **PBI-03** | Blocos Anônimos PL/SQL com Cursores Explícitos, Estruturas de Decisão e Laços | 3 pts | 1 - Critical | 5.5h |
| **[FEATURE 02] PL/SQL Packages** | **PBI-04** | Package PKG_CHAMADO_GESTAO para Gestão de Ocorrências e Resolução em O(1) | 3 pts | 1 - Critical | 8.0h |
| | **PBI-05** | Package PKG_ENGAJAMENTO_CIDADAO para Apoios Comunitários e Ranking | 3 pts | 1 - Critical | 7.5h |
| **[FEATURE 03] Triggers & Auditoria**| **PBI-06** | Trigger TRG_AUDIT_CHAMADO e Tabela de Auditoria DML (:OLD vs :NEW) | 3 pts | 1 - Critical | 6.5h |
| | **PBI-07** | Trigger TRG_VALIDA_VOTO_CHAMADO para Bloqueio de Autovoto e Unicidade | 3 pts | 1 - Critical | 6.0h |
| **[FEATURE 04] NoSQL MongoDB** | **PBI-08** | Provisionamento NoSQL no MongoDB com jsonSchema e Datasets JSON | 3 pts | 1 - Critical | 7.0h |
| | **PBI-09** | Matriz de Mapeamento Relacional para Documental e 3 Relatórios Analíticos | 3 pts | 1 - Critical | 8.0h |
| | **PBI-10** | Documentação Técnica Completa (README.md), Dicionário de Dados e Cluster | 3 pts | 1 - Critical | 6.0h |
| **TOTAL CONSOLIDADO** | **4 Features** | **10 Product Backlog Items (PBIs)** | **30 pts** | — | **68.0h** |

---

## 📦 3. Detalhamento dos Itens de Trabalho

---

### 🏛️ ÉPICO
* **Work Item Type:** `Epic`
* **Title:** `[EPIC] Database Advanced: Modelagem Relacional Oracle 3FN, Automações PL/SQL e Persistência NoSQL MongoDB`
* **Tags:** `Database, GlobalSolution2, Oracle, PLSQL, MongoDB, 3FN, NoSQL`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `30`
* **Business Value:** `100`
* **Description:** Engenharia completa da camada de dados do ZelaFix atendendo aos 70 pontos da rubrica da disciplina: modelagem relacional estrita em 3FN no Oracle SQL Developer Data Modeler com 11 tabelas, script DDL (`2TDSPG_2026_CodigoSql_ZelaFix.sql`) com sequences, constraints e índices de cobertura, pacotes PL/SQL avançados (`PKG_CHAMADO_GESTAO` e `PKG_ENGAJAMENTO_CIDADAO`) com funções otimizadas via `PRAGMA UDF`, trilha de auditoria DML com triggers e tabela dedicada (`TRG_AUDIT_CHAMADO`), blocos anônimos com cursores explícitos, persistência poliglota com MongoDB Atlas (coleções validadas com `jsonSchema` e datasets JSON de ocorrências e bairros) e relatórios analíticos de inteligência urbana comparando SQL relacional e Aggregation Pipeline NoSQL.

---

### 🏆 [FEATURE 01] Modelagem Conceitual, Lógica e Relacional no Oracle Data Modeler em 3FN
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Database Advanced: Modelagem Relacional Oracle 3FN, Automações PL/SQL e Persistência NoSQL MongoDB`
* **Title:** `[FEATURE 01] Modelagem Conceitual, Lógica e Relacional no Oracle Data Modeler em 3FN`
* **Tags:** `Database, DataModeler, 3FN, Oracle, DDL`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-08`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Description:** Concepção da arquitetura relacional em 3FN no Oracle Data Modeler 24.3, provisionamento DDL corporativo com sequences e constraints e execução de blocos anônimos para relatórios administrativos.
* **Acceptance Criteria:**
  - [x] Diagramas Lógico e Relacional exportados em PNG de alta resolução na pasta `docs/`.
  - [x] Script DDL `2TDSPG_2026_CodigoSql_ZelaFix.sql` executável sem erros no Oracle com 11 tabelas e sequences.
  - [x] 2 blocos anônimos PL/SQL utilizando IF, LOOP e cursores explícitos implementados.

#### 🔹 [PBI-01] Modelo Entidade-Relacionamento (MER), Diagramas Lógico e Relacional 3FN
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Modelagem Conceitual, Lógica e Relacional no Oracle Data Modeler em 3FN`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Database, MER, RelationalModel, 3FN`

##### Descrição (História de Usuário)
> **Como** DBA e Arquiteto de Dados,  
> **Eu quero** modelar as entidades da zeladoria urbana no Oracle Data Modeler 24.3 garantindo normalização estrita até a 3ª Forma Normal,  
> **Para que** todas as relações de autoria, localização territorial, histórico de status e apoios comunitários sejam íntegras e sem redundâncias.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Modelagem de 11 entidades no Data Modeler: `usuario`, `cargo_usuario`, `chamado`, `hist_chamado`, `status`, `categoria`, `voto_chamado`, `endereco`, `bairro`, `cidade`, `estado`, `telefone`.
- [ ] Normalização estrita 3FN: status vigente desacoplado de `chamado` e mantido no histórico `hist_chamado`.
- [ ] Exportação de diagramas conceituais em `docs/logical.png` e `docs/relational.png`.

---

#### 🔹 [PBI-02] Script DDL 3FN com Sequences, Constraints, Índices de Cobertura e BLOB
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Modelagem Conceitual, Lógica e Relacional no Oracle Data Modeler em 3FN`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Database, DDL, SQL, Oracle, Sequences, BLOB`

##### Descrição (História de Usuário)
> **Como** engenheiro de banco de dados,  
> **Eu quero** gerar o script DDL executável com sequences, chaves primárias, estrangeiras, índices de cobertura e campo BLOB para fotos,  
> **Para que** as aplicações Java e .NET tenham uma base de dados homologada e de alta performance de I/O.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Script `2TDSPG_2026_CodigoSql_ZelaFix.sql` contendo DDL completo e carga inicial de dados.
- [ ] Coluna `foto BLOB` na tabela `chamado` para armazenamento nativo de evidências fotográficas.
- [ ] Índice composto de cobertura `idx_hist_chamado_ativo` sobre `(chamado_id_chamado, id_hist DESC, status_id_status)`.
- [ ] Constraint de unicidade `voto_chamado_un UNIQUE (chamado_id_chamado, usuario_id_usuario)` suprindo a necessidade de índices redundantes.

---

#### 🔹 [PBI-03] Blocos Anônimos PL/SQL com Cursores Explícitos, Estruturas de Decisão e Laços
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Modelagem Conceitual, Lógica e Relacional no Oracle Data Modeler em 3FN`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Database, AnonymousBlock, PLSQL, Cursor, Loop`

##### Descrição (História de Usuário)
> **Como** analista de dados municipal,  
> **Eu quero** blocos anônimos PL/SQL com cursores explícitos para processamento em lote de chamados e bairros com estruturas IF/THEN/ELSE e loops,  
> **Para que** seja possível gerar relatórios operacionais consolidados no terminal via DBMS_OUTPUT.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Bloco Anônimo 1: Varredura de ocorrências abertas com cursor explícito e classificação de criticidade com `IF/ELSIF/ELSE`.
- [ ] Bloco Anônimo 2: Cursor com parâmetros para totalização de votos e chamados por bairro com laço `LOOP/EXIT WHEN`.
- [ ] Saídas formatadas com `DBMS_OUTPUT.PUT_LINE` demonstrando o processamento em lote.

---

### 🏆 [FEATURE 02] Automação em PL/SQL Avançado (Packages, Procedures e Functions com PRAGMA UDF)
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Database Advanced: Modelagem Relacional Oracle 3FN, Automações PL/SQL e Persistência NoSQL MongoDB`
* **Title:** `[FEATURE 02] Automação em PL/SQL Avançado (Packages, Procedures e Functions com PRAGMA UDF)`
* **Tags:** `Database, PLSQL, Packages, PragmaUDF, Procedures`
* **Start Date:** `2026-11-08`
* **Target Date:** `2026-11-13`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** Implementação de regras de negócio em pacotes PL/SQL estruturados (`PKG_CHAMADO_GESTAO` e `PKG_ENGAJAMENTO_CIDADAO`), contendo procedures de ciclo de vida e functions de alta performance compiladas com `PRAGMA UDF`.
* **Acceptance Criteria:**
  - [x] Mínimo de 2 pacotes PL/SQL completos (Spec + Body) em `2TDSPG_2026_Pacotes_ZelaFix.sql`.
  - [x] Function `fn_obter_status_atual` com `PRAGMA UDF` resolvendo status vigente em O(1).
  - [x] Procedures para abertura de chamados, atualização de status e registro de votos.

#### 🔹 [PBI-04] Package PKG_CHAMADO_GESTAO para Gestão de Ocorrências e Resolução em O(1)
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Automação em PL/SQL Avançado (Packages, Procedures e Functions com PRAGMA UDF)`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Database, Package, ChamadoGestao, PragmaUDF`

##### Descrição (História de Usuário)
> **Como** equipe de zeladoria municipal,  
> **Eu quero** procedures e functions empacotadas para gerenciar a abertura e transição de status das ocorrências com alta performance,  
> **Para que** as operações de negócio ocorram diretamente no banco com validações e sem overhead de context-switch.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Especificação e corpo do pacote `PKG_CHAMADO_GESTAO` compilados com sucesso.
- [ ] Procedure `pr_abrir_chamado` realizando inserção em `chamado` e inserção inicial em `hist_chamado` em transação atômica.
- [ ] Procedure `pr_atualizar_status_chamado` validando integridade e registrando a transição em `hist_chamado`.
- [ ] Function `fn_obter_status_atual` com `PRAGMA UDF` utilizando o índice de cobertura para responder em $\mathcal{O}(1)$.

---

#### 🔹 [PBI-05] Package PKG_ENGAJAMENTO_CIDADAO para Apoios Comunitários e Ranking
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Automação em PL/SQL Avançado (Packages, Procedures e Functions com PRAGMA UDF)`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Database, Package, Engajamento, Votos, Ranking`

##### Descrição (História de Usuário)
> **Como** gestor de políticas públicas,  
> **Eu quero** rotinas de banco para gerenciar apoios comunitários e classificar a criticidade de cada bairro,  
> **Para que** a prefeitura possa priorizar investimentos nos bairros com maior concentração de problemas.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Especificação e corpo do pacote `PKG_ENGAJAMENTO_CIDADAO` compilados com sucesso.
- [ ] Procedure `pr_registrar_voto` validando a existência do chamado e impedindo duplicidade.
- [ ] Function `fn_calcular_total_votos` retornando a quantidade consolidada de apoios de um chamado.
- [ ] Function `fn_classificar_criticidade_bairro` retornando o nível de atenção (BAIXO, MÉDIO, CRÍTICO) a partir do volume de ocorrências.

---

### 🏆 [FEATURE 03] Gatilhos & Trilha de Auditoria DML e Integridade Transacional
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Database Advanced: Modelagem Relacional Oracle 3FN, Automações PL/SQL e Persistência NoSQL MongoDB`
* **Title:** `[FEATURE 03] Gatilhos & Trilha de Auditoria DML e Integridade Transacional`
* **Tags:** `Database, Triggers, Audit, DML, Security`
* **Start Date:** `2026-11-10`
* **Target Date:** `2026-11-15`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** Implementação de triggers de integridade transacional e trilha de auditoria DML alimentando tabela dedicada com captura de `:OLD` vs `:NEW`.
* **Acceptance Criteria:**
  - [x] Tabela `AUDITORIA_DML_CHAMADO` criada para rastreabilidade de operações DML.
  - [x] Trigger `TRG_AUDIT_CHAMADO` capturando usuário, data, tipo de operação (I/U/D) e valores anteriores vs novos.
  - [x] Trigger `TRG_VALIDA_VOTO_CHAMADO` impedindo autovoto e votos em chamados concluídos ou rejeitados.

#### 🔹 [PBI-06] Trigger TRG_AUDIT_CHAMADO e Tabela de Auditoria DML (:OLD vs :NEW)
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] Gatilhos & Trilha de Auditoria DML e Integridade Transacional`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Database, Triggers, DML, Auditoria`

##### Descrição (História de Usuário)
> **Como** auditor de compliance e segurança da informação,  
> **Eu quero** que qualquer operação de INSERT, UPDATE ou DELETE na tabela `chamado` gere um registro imutável com os dados antigos e novos,  
> **Para que** todas as modificações sejam rastreáveis e estejam em conformidade com as diretrizes da LGPD e governança pública.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Tabela `AUDITORIA_DML_CHAMADO` com colunas `id_audit`, `dt_operacao`, `usuario_db`, `tipo_operacao`, `id_chamado`, `titulo_old`, `titulo_new`.
- [ ] Trigger `TRG_AUDIT_CHAMADO` disparada `AFTER INSERT OR UPDATE OR DELETE ON chamado`.
- [ ] Captura de `USER`, `SYSTIMESTAMP` e valores `:OLD` vs `:NEW`.

---

#### 🔹 [PBI-07] Trigger TRG_VALIDA_VOTO_CHAMADO para Bloqueio de Autovoto e Unicidade
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] Gatilhos & Trilha de Auditoria DML e Integridade Transacional`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Database, Triggers, ValidaVoto, Integridade`

##### Descrição (História de Usuário)
> **Como** gestor do aplicativo de zeladoria,  
> **Eu quero** uma trigger BEFORE INSERT que impeça o cidadão de votar no próprio chamado que ele mesmo abriu e bloqueie votos em chamados já encerrados,  
> **Para que** o engajamento popular seja legítimo e não haja fraude na priorização de demandas.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Trigger `TRG_VALIDA_VOTO_CHAMADO` disparada `BEFORE INSERT ON voto_chamado`.
- [ ] Validação impedindo que `usuario_id_usuario` seja o autor de `chamado.usuario_id_usuario` com `RAISE_APPLICATION_ERROR(-20001)`.
- [ ] Validação impedindo votos em chamados com status `CONCLUIDO` ou `REJEITADO` com `RAISE_APPLICATION_ERROR(-20002)`.

---

### 🏆 [FEATURE 04] Persistência Poliglota com MongoDB Atlas e Relatórios Analíticos Agregados
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Database Advanced: Modelagem Relacional Oracle 3FN, Automações PL/SQL e Persistência NoSQL MongoDB`
* **Title:** `[FEATURE 04] Persistência Poliglota com MongoDB Atlas e Relatórios Analíticos Agregados`
* **Tags:** `Database, MongoDB, NoSQL, Aggregation, Relatorios`
* **Start Date:** `2026-11-13`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Description:** Persistência NoSQL orientada a documentos no MongoDB Atlas, scripts de criação e validação via `jsonSchema`, datasets JSON com mais de 10 documentos, matriz de mapeamento relacional->documental e 3 relatórios analíticos comparados em SQL e MongoDB Aggregation Pipeline.
* **Acceptance Criteria:**
  - [x] Scripts `setup_mongodb_chamados.js` e `setup_mongodb_bairros.js` com validação de `jsonSchema`.
  - [x] Carga de no mínimo 10 documentos comprovada (13 documentos inseridos).
  - [x] Matriz de mapeamento de transição conceitual fundamentando Embedding vs Referencing.
  - [x] 3 relatórios analíticos em `consultas_relatorios_mongodb.js` comparados diretamente com queries SQL Oracle equivalentes.

#### 🔹 [PBI-08] Provisionamento NoSQL no MongoDB com jsonSchema e Datasets JSON
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 04] Persistência Poliglota com MongoDB Atlas e Relatórios Analíticos Agregados`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Database, MongoDB, JsonSchema, Datasets`

##### Descrição (História de Usuário)
> **Como** engenheiro de dados NoSQL,  
> **Eu quero** criar as coleções `chamados` e `bairros_monitoramento` no MongoDB com regras de validação `jsonSchema` e popular com datasets ricos,  
> **Para que** a persistência não relacional garanta tipos estritos de dados e possibilite leituras em O(1) pelo aplicativo mobile.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Validador `validator: { $jsonSchema: ... }` configurado em `setup_mongodb_chamados.js` e `setup_mongodb_bairros.js`.
- [ ] Datasets `chamados_dataset.json` e `bairros_dataset.json` contendo 13 documentos completos com localização e histórico embutidos.
- [ ] Script mestre `setup_completo_mongodb.js` executando a carga automatizada e testes de integridade.

---

#### 🔹 [PBI-09] Matriz de Mapeamento Relacional para Documental e 3 Relatórios Analíticos
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 04] Persistência Poliglota com MongoDB Atlas e Relatórios Analíticos Agregados`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Database, MongoDB, Aggregation, Analytics, SQLvsNoSQL`

##### Descrição (História de Usuário)
> **Como** cientista de dados e gestor público,  
> **Eu quero** uma matriz comparativa entre os modelos relacional e documental, e 3 relatórios analíticos com Aggregation Pipeline comparados com queries Oracle SQL,  
> **Para que** possamos extrair inteligência de negócios sobre ocorrências mais votadas, gargalos por categoria e monitoramento territorial dos bairros.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Matriz de mapeamento fundamentando embedding de `historico` e `votos` e referencing de `bairros`.
- [ ] Relatório 1: Ocorrências ativas mais votadas (Radar do Bairro) comparado em SQL e MongoDB.
- [ ] Relatório 2: Agrupamento por categoria e volume com `$group` e `$cond`.
- [ ] Relatório 3: Panorama territorial de bairros cruzando métricas operacionais.

---

#### 🔹 [PBI-10] Documentação Técnica Completa (README.md), Dicionário de Dados e Cluster
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 04] Persistência Poliglota com MongoDB Atlas e Relatórios Analíticos Agregados`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Database, Documentation, README, Cluster`

##### Descrição (História de Usuário)
> **Como** avaliador acadêmico da FIAP,  
> **Eu quero** um README minucioso contendo a tabela de rastreabilidade dos 70 pontos da disciplina, diagramas e instruções de execução,  
> **Para que** a entrega técnica possa ser homologada e executada com transparência e clareza.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] `README.md` completo no repositório `Database-Advanced` com tabela dos 70 pontos.
- [ ] Diagramas DER e instruções de conexão ao Oracle e MongoDB Atlas.
- [ ] Arquivo de texto de submissão acadêmica formatado conforme padrão da FIAP.
