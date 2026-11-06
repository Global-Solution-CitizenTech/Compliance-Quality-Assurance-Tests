# 📋 Backlog Master Azure Boards — Global Solution 2026/2: Database Advanced

> **Projeto Integrado:** ZelaFix — Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  
> **Disciplina:** Mastering Relational and Non-Relational Database (FIAP — 2TDSPG)  
> **Epic Principal:** `[EPIC] Database Advanced: Modelagem Relacional Oracle 11g, Automações PL/SQL e Persistência NoSQL MongoDB`  
> **Start Date:** `2026-11-04`  
> **Target Date:** `2026-11-19`  
> **Padrão:** Azure Boards (Scrum Process: Epic ➔ Feature ➔ PBI ➔ Task)  
> **Diretrizes Estratégicas:** Modelagem relacional estrita no Oracle SQL Developer Data Modeler em 3ª Forma Normal (3FN), geração de scripts DDL com integridade referencial, desenvolvimento de Packages, Stored Procedures e Functions em PL/SQL para regras analíticas e prazos SLA, Triggers de auditoria DML na tabela HIST_STATUS e integração com MongoDB para persistência de documentos NoSQL de telemetria urbana.

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
[EPIC] Database Advanced: Modelagem Relacional Oracle 11g, Automações PL/SQL e Persistência NoSQL MongoDB
│
├── 🏆 [FEATURE 01] Modelagem Conceitual, Lógica e Relacional no Oracle Data Modeler
│   ├── 📄 [PBI-01] Elaboração do Modelo Entidade-Relacionamento e Diagrama Relacional 3FN (3 pts)
│   └── 📄 [PBI-02] Geração e Homologação do Script DDL com Constraints e Índices (3 pts)
│
├── 🏆 [FEATURE 02] Automação em PL/SQL (Packages, Stored Procedures e Functions)
│   ├── 📄 [PBI-03] Desenvolvimento da Package PKG_CITIZENTECH_ZELADORIA (3 pts)
│   └── 📄 [PBI-04] Procedures e Functions de Cálculo de SLA e Agregação de Votos (3 pts)
│
├── 🏆 [FEATURE 03] Triggers de Auditoria DML e Histórico de Status de Chamados
│   ├── 📄 [PBI-05] Trigger de Auditoria para Mudança de Status e Alimentação de HIST_STATUS (3 pts)
│   └── 📄 [PBI-06] Trigger de Validação de Regras de Negócio e Unicidade de Votos (3 pts)
│
└── 🏆 [FEATURE 04] Persistência NoSQL com MongoDB e Documentos de Telemetria
    └── 📄 [PBI-07] Modelagem de Collections no MongoDB para Logs de Telemetria IoT e Auditoria (2 pts)
```

---

## 📊 2. Tabela Resumo do Backlog

| Feature Pai | ID do PBI | Título do Item de Backlog (PBI) | Story Points | Prioridade | Horas Estimadas |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **[FEATURE 01] Modelagem & DDL** | **PBI-01** | Elaboração do Modelo Entidade-Relacionamento e Diagrama Relacional 3FN | 3 pts | 1 - Critical | 6.5h |
| | **PBI-02** | Geração e Homologação do Script DDL com Constraints e Índices | 3 pts | 1 - Critical | 6.0h |
| **[FEATURE 02] PL/SQL Packages** | **PBI-03** | Desenvolvimento da Package PKG_CITIZENTECH_ZELADORIA | 3 pts | 1 - Critical | 7.5h |
| | **PBI-04** | Procedures e Functions de Cálculo de SLA e Agregação de Votos | 3 pts | 1 - Critical | 7.0h |
| **[FEATURE 03] Triggers & DML** | **PBI-05** | Trigger de Auditoria para Mudança de Status e Alimentação de HIST_STATUS | 3 pts | 1 - Critical | 7.0h |
| | **PBI-06** | Trigger de Validação de Regras de Negócio e Unicidade de Votos | 3 pts | 1 - Critical | 6.0h |
| **[FEATURE 04] NoSQL MongoDB** | **PBI-07** | Modelagem de Collections no MongoDB para Logs de Telemetria IoT e Auditoria | 2 pts | 2 - High | 5.0h |
| **TOTAL CONSOLIDADO** | **4 Features** | **7 PBIs / 20 Child Tasks Técnicas** | **20 pts** | — | **45.0h** |

---

## 📦 3. Detalhamento dos Itens de Trabalho (Épico, Features, PBIs e Tasks)

---

### 🏛️ ÉPICO
* **Work Item Type:** `Epic`
* **Title:** `[EPIC] Database Advanced: Modelagem Relacional Oracle 11g, Automações PL/SQL e Persistência NoSQL MongoDB`
* **Tags:** `Database, ZelaFix, GlobalSolution2, Oracle, PLSQL, MongoDB, DataModeling`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `20`
* **Business Value:** `100`
* **Description:** Projeto e implementação da camada de persistência de dados do ZelaFix, compreendendo a modelagem relacional completa em 3FN no Oracle Data Modeler, automações via PL/SQL (Packages, Functions, Procedures e Triggers de auditoria) e persistência de dados não estruturados no MongoDB para logs e telemetria de sensores.

---

### 🏆 [FEATURE 01] Modelagem Conceitual, Lógica e Relacional no Oracle Data Modeler
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Database Advanced: Modelagem Relacional Oracle 11g, Automações PL/SQL e Persistência NoSQL MongoDB`
* **Title:** `[FEATURE 01] Modelagem Conceitual, Lógica e Relacional no Oracle Data Modeler`
* **Tags:** `Database, DataModeler, 3FN, DDL`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-08`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** Concepção da estrutura de dados relacional com normalização em 3ª Forma Normal, garantindo integridade e ausência de redundâncias.
* **Acceptance Criteria:**
  - [x] Diagramas Lógico e Relacional exportados em PNG de alta resolução.
  - [x] Script DDL executável sem erros no Oracle 11g/19c com criação de tabelas, PKs, FKs e Checks.

#### 🔹 [PBI-01] Elaboração do Modelo Entidade-Relacionamento e Diagrama Relacional 3FN
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Modelagem Conceitual, Lógica e Relacional no Oracle Data Modeler`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Database, MER, RelationalModel`

##### Descrição (História de Usuário)
> **Como** DBA e Arquiteto de Dados,  
> **Eu quero** modelar as entidades Chamado, Categoria, Usuario, Bairro, Endereco, HistStatus e VotoChamado em 3FN,  
> **Para que** o sistema armazene as demandas de zeladoria com consistência transacional e integridade.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Modelagem de entidades e atributos tipados no Oracle Data Modeler.
- [ ] Normalização comprovada até a 3ª Forma Normal.
- [ ] Diagramas lógico e relacional gerados na pasta `docs/`.
---

#### 🔹 [PBI-02] Geração e Homologação do Script DDL com Constraints e Índices
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Modelagem Conceitual, Lógica e Relacional no Oracle Data Modeler`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Database, DDL, SQL, Oracle`

##### Descrição (História de Usuário)
> **Como** desenvolvedor backend,  
> **Eu quero** um script DDL limpo e executável que provisione todas as tabelas e índices no Oracle,  
> **Para que** as aplicações Java e .NET conectem-se a uma base homologada.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Script `citizenTech.ddl` contendo comandos `CREATE TABLE`, `PRIMARY KEY`, `FOREIGN KEY` e `CHECK`.
- [ ] Checks para status de chamado (`ABERTO`, `EM_ANALISE`, `EM_EXECUCAO`, `CONCLUIDO`, `REJEITADO`).
- [ ] Índices únicos para e-mail e pares de unicidade em votos e telefones.
---

### 🏆 [FEATURE 02] Automação em PL/SQL (Packages, Stored Procedures e Functions)
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Database Advanced: Modelagem Relacional Oracle 11g, Automações PL/SQL e Persistência NoSQL MongoDB`
* **Title:** `[FEATURE 02] Automação em PL/SQL (Packages, Stored Procedures e Functions)`
* **Tags:** `Database, PLSQL, Procedures, Packages`
* **Start Date:** `2026-11-08`
* **Target Date:** `2026-11-13`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** Desenvolvimento de lógica de banco em PL/SQL para automatização de cálculos de SLA e relatórios analíticos de demandas urbanas.
* **Acceptance Criteria:**
  - [x] Package PL/SQL com especificação e corpo (`PACKAGE` e `PACKAGE BODY`).
  - [x] Functions para cálculo de prazo limite baseado no tipo de ocorrência.
  - [x] Procedures analíticas para consolidação de chamados por bairro.

#### 🔹 [PBI-03] Desenvolvimento da Package PKG_CITIZENTECH_ZELADORIA
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Automação em PL/SQL (Packages, Stored Procedures e Functions)`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Database, PLSQL, Package`

##### Descrição (História de Usuário)
> **Como** gestor público municipal,  
> **Eu quero** rotinas de banco encapsuladas em packages para processamento em lote de chamados e relatórios consolidados,  
> **Para que** as operações críticas sejam executadas com máxima performance no servidor de banco de dados.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Package `PKG_CITIZENTECH_ZELADORIA` com header e body compilados sem erros.
- [ ] Tratamento de exceções com `PRAGMA EXCEPTION_INIT` e mensagens customizadas.
---

#### 🔹 [PBI-04] Procedures e Functions de Cálculo de SLA e Agregação de Votos
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Automação em PL/SQL (Packages, Stored Procedures e Functions)`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Database, Functions, SLA, Analytics`

##### Descrição (História de Usuário)
> **Como** equipe técnica de atendimento,  
> **Eu quero** uma function PL/SQL que calcule a data de vencimento do SLA a partir da categoria,  
> **Para que** o sistema emita alertas automáticos de prazos estourados.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Function `fn_calcular_previsao_chamado(p_categoria_id, p_dt_abertura) RETURN DATE`.
- [ ] Procedure `sp_consolidar_votos_chamado(p_chamado_id, p_total_votos OUT NUMBER)`.
---

### 🏆 [FEATURE 03] Triggers de Auditoria DML e Histórico de Status de Chamados
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Database Advanced: Modelagem Relacional Oracle 11g, Automações PL/SQL e Persistência NoSQL MongoDB`
* **Title:** `[FEATURE 03] Triggers de Auditoria DML e Histórico de Status de Chamados`
* **Tags:** `Database, Triggers, Audit, DML`
* **Start Date:** `2026-11-10`
* **Target Date:** `2026-11-15`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** Implementação de triggers BEFORE/AFTER para rastreabilidade de alterações e alimentação automática da tabela HIST_STATUS.
* **Acceptance Criteria:**
  - [x] Trigger de auditoria alimentando HIST_STATUS a cada UPDATE na coluna status de CHAMADO.
  - [x] Bloqueio de votos duplicados por meio de trigger/constraint.

#### 🔹 [PBI-05] Trigger de Auditoria para Mudança de Status e Alimentação de HIST_STATUS
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] Triggers de Auditoria DML e Histórico de Status de Chamados`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Database, Trigger, HistStatus`

##### Descrição (História de Usuário)
> **Como** auditor de compliance público,  
> **Eu quero** uma trigger que grave automaticamente em HIST_STATUS qualquer alteração de status de um chamado,  
> **Para que** todas as transições de responsabilidade fiquem registradas de forma imutável.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Trigger `trg_audit_status_chamado` disparada em `AFTER UPDATE OF status ON chamado`.
- [ ] Gravação de `:OLD.status`, `:NEW.status`, data corrente e usuário responsável.
---

#### 🔹 [PBI-06] Trigger de Validação de Regras de Negócio e Unicidade de Votos
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] Triggers de Auditoria DML e Histórico de Status de Chamados`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Database, Trigger, BusinessRules`

##### Descrição (História de Usuário)
> **Como** desenvolvedor,  
> **Eu quero** validações automáticas no banco para impedir reabertura indevida de chamados concluídos,  
> **Para que** o ciclo de vida da ocorrência respeite rigorosamente as políticas de zeladoria.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Bloqueio com `RAISE_APPLICATION_ERROR` caso tentem alterar status de chamado já `CONCLUIDO`.
---

### 🏆 [FEATURE 04] Persistência NoSQL com MongoDB e Documentos de Telemetria
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Database Advanced: Modelagem Relacional Oracle 11g, Automações PL/SQL e Persistência NoSQL MongoDB`
* **Title:** `[FEATURE 04] Persistência NoSQL com MongoDB e Documentos de Telemetria`
* **Tags:** `Database, MongoDB, NoSQL, IoT, Telemetry`
* **Start Date:** `2026-11-13`
* **Target Date:** `2026-11-19`
* **Priority:** `2 - High`
* **Effort (Story Points):** `2`
* **Business Value:** `80`
* **Description:** Modelagem e persistência em banco NoSQL orientado a documentos (MongoDB) para armazenamento de telemetria dos sensores IoT.
* **Acceptance Criteria:**
  - [x] Collection `telemetria_sensores` modelada com schema JSON flexível.
  - [x] Índices geoespaciais (2dsphere) para consulta de sensores por proximidade.

#### 🔹 [PBI-07] Modelagem de Collections no MongoDB para Logs de Telemetria IoT e Auditoria
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 04] Persistência NoSQL com MongoDB e Documentos de Telemetria`
* **Priority:** `2 - High`
* **Effort (Story Points):** `2`
* **Tags:** `Database, MongoDB, Collections`

##### Descrição (História de Usuário)
> **Como** engenheiro de IoT e dados,  
> **Eu quero** salvar leituras de sensores de bueiros e alagamento no MongoDB,  
> **Para que** dados de alta frequência não sobrecarreguem o banco relacional Oracle.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Scripts de inicialização do MongoDB com índices e inserts de exemplo.
- [ ] Estrutura JSON com timestamp, deviceId, metricas e coordenadas.