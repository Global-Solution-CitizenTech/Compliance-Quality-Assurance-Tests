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
AZURE_DEVOPS_ORG=ZelaFixGS
AZURE_DEVOPS_PROJECT=ZelaFix

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
| 📱 **Mobile Application Development** | `Mobile` | `ZelaFix\Release 1 - Global Solution\Semana 1` | `backlog-materias/BACKLOG_MOBILE.md` |
| ☕ **Java Advanced** | `JavaAdvanced` | `ZelaFix\Release 1 - Global Solution\Semana 1` | `backlog-materias/BACKLOG_JAVA_ADVANCED.md` |
| 🗄️ **Database Advanced** | `Database` | `ZelaFix\Release 1 - Global Solution\Semana 1` | `backlog-materias/BACKLOG_DATABASE_ADVANCED.md` |
| 💻 **Advanced Business Dev. with .NET** | `DotNet` | `ZelaFix\Release 1 - Global Solution\Semana 2` | `backlog-materias/BACKLOG_DOT_NET.md` |
| ☁️ **DevOps Tools & Cloud Computing** | `DevOps` | `ZelaFix\Release 1 - Global Solution\Semana 2` | `backlog-materias/BACKLOG_DEVOPS.md` |
| 🤖 **Disruptive Architectures (IoT/IA)** | `DisruptiveArchitectures` | `ZelaFix\Release 1 - Global Solution\Semana 2` | `backlog-materias/BACKLOG_DISRUPTIVE_ARCHITECTURES.md` |
| 🛡️ **Compliance, QA & Tests** | `Compliance` | `ZelaFix\Release 1 - Global Solution\Semana 2` | `backlog-materias/BACKLOG_COMPLIANCE.md` |

---

## 🚀 4. Comandos e Operações do CLI Unificado (`run_sync.py`)

### 4.1. Validação de Contrato e Status
```bash
# Validar contrato obrigatório dos 7 backlogs locais:
python run_sync.py --validate

# Testar conectividade com o Azure DevOps:
python run_sync.py --check-auth

# Exibir painel de controle e distribuição de Work Items:
python run_sync.py --status
```

### 4.2. Smart Upsert (Atualização Inteligente sem Duplicar)
```bash
# Simulação da atualização de todos os 7 backlogs (Dry-Run):
python run_sync.py --update --dry-run

# Atualizar todos os 7 backlogs na nuvem (aplica diffs em itens existentes e cria novos):
python run_sync.py --update

# Atualizar apenas uma disciplina específica:
python run_sync.py --update --discipline java
python run_sync.py --update --discipline mobile
python run_sync.py --update --discipline database
```

### 4.3. Rastreabilidade de Commits e Governança Scrum
```bash
# Escanear os 7 repositórios e vincular commits recentes aos Work Items:
python run_sync.py --commits

# Aplicar atribuição de responsáveis por tag e estados Scrum (In Progress / Committed):
python run_sync.py --govern

# Instalar post-commit hooks nos 7 repositórios locais para auto-vínculo com tag AB#<ID>:
python run_sync.py --hooks

# Pipeline completo (Carga/Sync + Commits + Governança):
python run_sync.py --full
```
