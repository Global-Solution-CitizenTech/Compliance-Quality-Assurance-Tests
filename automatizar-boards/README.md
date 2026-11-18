# 🚀 Automação de Backlog para o Azure Boards (Python)

Este módulo automatiza a leitura, validação estrita e sincronização dos arquivos de Backlog em Markdown (`.md`) das 7 disciplinas da **FIAP Global Solution 2026/2 — CitizenTech (ZelaFix)** no **Azure Boards** (`ZelaFixGS/ZelaFix`), seguindo o processo **Scrum**:

```text
👑 Epic
│
└── 🏆 Feature (vinculada ao Epic via System.LinkTypes.Hierarchy-Reverse)
    │
    └── 📄 Product Backlog Item (PBI com Story Points, Prioridade, Tag da Disciplina e HTML)
```

---

## 🎯 Destaques do Automatizador

1. **Remoção Automática de Ícones/Emojis:** Títulos de Epics, Features e PBIs são higienizados para o padrão formal do Azure DevOps (`clean_title`).
2. **Validação Estrita de Contrato (`parser_backlog.py`):** Garante presença obrigatória de `Start Date`, `Target Date`, `Tags` exclusivas por disciplina, `Effort (Story Points) > 0`, `Priority (1..4)`, `Business Value > 0`, `Description` e `Acceptance Criteria`.
3. **Campos Oficiais Mapeados:**
   - `System.Title`: Título formal limpo sem emojis.
   - `System.Description`: História de Usuário limpa em bloco `<div>` com `<br/>`.
   - `Microsoft.VSTS.Common.AcceptanceCriteria`: Critérios de aceite enviados no campo próprio dedicado.
   - `Microsoft.VSTS.Scheduling.Effort`: Story points numéricos agregados em todos os níveis.
   - `Microsoft.VSTS.Common.BusinessValue`: Valor de negócio mapeado pela prioridade (`100`, `80`, `50`, `20`).
   - `Microsoft.VSTS.Common.Priority`: Prioridade numérica de `1` (Critical) a `4` (Low).
   - `System.Tags`: Tag exclusiva por disciplina (`Mobile`, `JavaAdvanced`, `Database`, `DotNet`, `DevOps`, `DisruptiveArchitectures`, `Compliance`).
   - `System.IterationPath`: Iterações oficiais `ZelaFix\Release 1 - Global Solution\Semana 1` e `Semana 2`.
4. **Vínculos Hierárquicos e Rastreabilidade:** Criação dos links pai/filho nativos (`System.LinkTypes.Hierarchy-Reverse`) e vínculo de commits/PRs (`Hyperlink` GitHub e `ArtifactLink` Azure Repos).
5. 📖 **Guia Técnico:** Consulte [`INSTRUCOES_AUTOMACAO_AZURE_BOARDS.md`](./INSTRUCOES_AUTOMACAO_AZURE_BOARDS.md) para detalhes arquiteturais e de governança.

---

## ⚙️ Configuração

1. Copie `.env.example` para `.env` e configure as credenciais:
```ini
AZURE_DEVOPS_ORG=ZelaFixGS
AZURE_DEVOPS_PROJECT=ZelaFix
AZURE_DEVOPS_PAT=seu_personal_access_token_aqui
GITHUB_ORG=Global-Solution-CitizenTech
```

### 🔑 Como gerar o Personal Access Token (PAT) no Azure DevOps:
1. Acesse: `https://dev.azure.com/ZelaFixGS`
2. No canto superior direito, clique em **User settings** ➔ **Personal access tokens**.
3. Clique em **+ New Token**.
4. Em **Scopes**, selecione **Custom defined** ➔ marque **Work Items (Read & Write)** e **Test Management (Read & Write)**.
5. Copie o token gerado para a variável `AZURE_DEVOPS_PAT=` no arquivo `.env`.

---

## 💻 Comandos de Execução

Abra o terminal dentro da pasta `Compliance-Quality-Assurance-Tests/automatizar-boards`:

```powershell
# 1. Validar contrato obrigatório dos 7 backlogs locais:
python run_sync.py --validate

# 2. Testar conexão com o Azure DevOps:
python run_sync.py --check-auth

# 3. Consultar painel de status do Azure Boards:
python run_sync.py --status

# 4. Simular ou aplicar Smart Upsert (sem duplicar itens):
python run_sync.py --update --dry-run
python run_sync.py --update
python run_sync.py --update --discipline java

# 5. Vincular commits e aplicar governança:
python run_sync.py --commits
python run_sync.py --govern
```
