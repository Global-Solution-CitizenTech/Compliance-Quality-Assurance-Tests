# 🤖 Guia Técnico: Automação do Azure Boards & QA

> **Projeto:** CitizenTech — Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  
> **Disciplina:** Compliance, Quality Assurance & Tests  
> **Objetivo:** Orientar desenvolvedores e agentes de IA sobre a arquitetura, regras de negócio e execução dos scripts de sincronização de Backlog Markdown (`.md`), vínculo de commits Git e Casos de Testes no **Azure DevOps / Azure Boards**.

---

## 🎯 1. Visão Geral e Arquitetura

O ecossistema automatiza a leitura e o parsing dos arquivos de Backlog centralizados em `backlog-materias/` para as 7 disciplinas e cria a estrutura hierárquica nativa no Azure Boards seguindo o **Processo Scrum**:

$$\text{Epic} \xrightarrow{\text{Parent}} \text{Feature} \xrightarrow{\text{Parent}} \text{Product Backlog Item (PBI)} \xrightarrow{\text{Parent}} \text{Task}$$
$$\text{Feature} \xleftarrow{\text{Tested By}} \text{Test Case}$$
$$\text{Work Item} \xleftarrow{\text{Hyperlink}} \text{GitHub Commit}$$

---

## 🏛️ 2. Configurações de Ambiente (`.env`)

Arquivo: `Compliance-Quality-Assurance-Tests/automatizar-boards/.env`

```ini
# Organização e Projeto no Azure DevOps
AZURE_DEVOPS_ORG=Global-Solution-CitizenTech
AZURE_DEVOPS_PROJECT=CitizenTech

# Personal Access Token (PAT) com escopos:
# - Work Items (Read & Write)
# - Test Management (Read & Write)
AZURE_DEVOPS_PAT=

# Organização e Repositórios no GitHub
GITHUB_ORG=Global-Solution-CitizenTech
```

---

## 📅 3. Mapeamento de Iteration Paths e Tags das 7 Disciplinas

| Disciplina | Tag no Azure Boards | Iteration Path Alvo | Arquivo de Backlog |
| :--- | :--- | :--- | :--- |
| 📱 **Mobile Application Development** | `Mobile` | `CitizenTech\Sprint 1` | `backlog-materias/BACKLOG_MOBILE.md` |
| ☕ **Java Advanced** | `JavaAdvanced` | `CitizenTech\Sprint 1` | `backlog-materias/BACKLOG_JAVA_ADVANCED.md` |
| 🗄️ **Database Advanced** | `Database` | `CitizenTech\Sprint 1` | `backlog-materias/BACKLOG_DATABASE_ADVANCED.md` |
| 💻 **.NET & Observabilidade** | `DotNet` | `CitizenTech\Sprint 1` | `backlog-materias/BACKLOG_DOT_NET.md` |
| ☁️ **DevOps Tools & Cloud Computing** | `DevOps` | `CitizenTech\Sprint 2` | `backlog-materias/BACKLOG_DEVOPS.md` |
| 🤖 **Disruptive Architectures (IoT/IA)** | `DisruptiveArchitectures` | `CitizenTech\Sprint 2` | `backlog-materias/BACKLOG_DISRUPTIVE_ARCHITECTURES.md` |
| 🛡️ **Compliance, QA & Tests** | `Compliance` | `CitizenTech\Sprint 2` | `backlog-materias/BACKLOG_COMPLIANCE.md` |

---

## 🚀 4. Comandos e Operações do CLI

### 4.1. Orquestrador Geral (`run_sync.py`)
```bash
# Validação de credenciais e acesso:
python run_sync.py --check-auth

# Simulação da carga completa (Dry-Run):
python run_sync.py --all --dry-run

# Importação de todas as 7 disciplinas para a nuvem:
python run_sync.py --all

# Importação de arquivo individual:
python run_sync.py --file BACKLOG_MOBILE.md
```

### 4.2. Casos de Testes Caixa-Preta (`sync_test_cases.py`)
```bash
# Exportar matriz Markdown e simular criação:
python sync_test_cases.py --export-all --dry-run

# Criar os 20 Casos de Teste reais com passos XML no Azure Boards:
python sync_test_cases.py --sync-azure
```

### 4.3. Rastreamento e Vínculo de Commits Git (`link_commits.py`)
```bash
# Escanear os 7 repositórios locais e verificar commits:
python link_commits.py --dry-run

# Vincular commits reais aos Work Items via API REST:
python link_commits.py --scan-all

# Exibir manual de sintaxe de commits automáticos:
python link_commits.py --guide
```

### 4.4. Gestão e Execução no Azure Test Plans (`scripts/azure_qa_cli.py`)
```bash
# Resumo consolidado de execuções e métricas:
python ../scripts/azure_qa_cli.py summary

# Listagem de casos e status:
python ../scripts/azure_qa_cli.py list

# Executar suíte completa simulando Approved com falhas controladas para evidência de bug:
python ../scripts/azure_qa_cli.py run-all --fail-ids 2002 2004
```
