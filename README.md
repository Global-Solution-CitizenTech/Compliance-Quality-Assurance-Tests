# 🏛️ CitizenTech — Compliance, Quality Assurance & Tests
> **FIAP Global Solution 2026/2 • Turmas de Fevereiro (2TDSPG)**  
> **Tema:** CitizenTech — Tecnologia com o cidadão no centro da inovação (ODS 11 – Cidades Sustentáveis)  
> **Disciplina:** Compliance, Quality Assurance & Tests  
> **Plataforma Oficial:** Microsoft Azure DevOps (Azure Boards & Test Plans)  

---

## 👥 Integrantes do Grupo (Ordem Alfabética Estrita)

> ⚠️ **Regra Institucional da Banca FIAP:** Todos os documentos, PDFs e READMEs mantêm estritamente a ordem alfabética dos integrantes do grupo.

| Nome Completo | RM | Turma | GitHub | LinkedIn |
| :--- | :---: | :---: | :--- | :--- |
| **Enzo Okuizumi** | **561432** | 2TDSPG | [@EnzoOkuizumiFiap](https://github.com/EnzoOkuizumiFiap) | [LinkedIn](https://www.linkedin.com/in/enzo-okuizumi-b60292256/) |
| **Gustavo Okada** | **563428** | 2TDSPG | [@Gdev3356](https://github.com/Gdev3356) | [LinkedIn](https://www.linkedin.com/in/gustavo-okada-53a3b8359/) |
| **Lucas Barros Gouveia** | **566422** | 2TDSPG | [@LuzBGouveia](https://github.com/LuzBGouveia) | [LinkedIn](https://www.linkedin.com/in/lucas-barros-gouveia-09b147355/) |
| **Luna de Carvalho Guimarães** | **562290** | 2TDSPG | [@lunaguima](https://github.com/lunaguima) | [LinkedIn](https://www.linkedin.com/in/luna-guimar%C3%A3es-b0ba82309/) |
| **Milton Marcelino** | **564836** | 2TDSPG | [@MiltonMarcelino](https://github.com/MiltonMarcelino) | [LinkedIn](https://www.linkedin.com/in/milton-marcelino-250298142) |

---

## 🔗 Repositórios Oficiais do Ecossistema CitizenTech

| Disciplina | Repositório no GitHub |
| :--- | :--- |
| 📱 **Mobile Application Development** | [Global-Solution-CitizenTech/Mobile-Application-Development](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development) |
| ☕ **Java Advanced** | [Global-Solution-CitizenTech/Java-Advanced](https://github.com/Global-Solution-CitizenTech/Java-Advanced) |
| 🗄️ **Database Advanced** | [Global-Solution-CitizenTech/Database-Advanced](https://github.com/Global-Solution-CitizenTech/Database-Advanced) |
| 🔷 **Advanced Business Development with .NET** | [Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net](https://github.com/Global-Solution-CitizenTech/Advanced-Business-Development-with-Dot-Net) |
| 🚀 **DevOps Tools & Cloud Computing** | [Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing](https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing) |
| 🤖 **Disruptive Architectures (IoT & IA)** | [Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA](https://github.com/Global-Solution-CitizenTech/Disruptive-Architectures-IoT-IoB-IA) |
| 🛡️ **Compliance, QA & Tests (ATUAL)** | [Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests](https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests) |

---

## 🎯 Atendimento Integral à Rubrica da Global Solution 2 (100 Pontos)

Conforme o edital oficial (págs 29–35 de `2TDS Fevereiro - Global Solution 2026-2.pdf`), a entrega é avaliada em 5 critérios rigorosos:

| Item | Critério de Avaliação | Pontos | Evidência Comprovada no Projeto CitizenTech |
| :---: | :--- | :---: | :--- |
| **01** | **Estrutura de Projeto (Scrum)** | **20 pts** | Backlog unificado contendo **7 Epics, 24 Features, 46 PBIs e 131 Tasks** com títulos consistentes e tags padronizadas. |
| **02** | **Descrição & Critérios de Aceite por Feature** | **20 pts** | Todas as Features com `System.Description` no padrão User Story e `AcceptanceCriteria` no campo nativo do Azure DevOps. |
| **03** | **Lista de Test Cases Positivos e Negativos** | **20 pts** | Suíte de **20 Casos de Teste Caixa-Preta** cobrindo fluxos felizes (65%) e cenários de exceção/validação/limites (35%). |
| **04** | **Sumário dos Test Cases** | **20 pts** | Todos os casos documentados com **Objetivo, Preparação (Pré-condições), Dados de Entrada Controlados (Inputs) e Outputs Esperados**. |
| **05** | **Passos Detalhados dos Test Cases** | **20 pts** | Sequenciamento minucioso no campo XML `Microsoft.VSTS.TCM.Steps` relacionando Ação do Testador x Resposta Esperada do Sistema. |
| **TOTAL** | **Pontuação Total do Projeto** | **100 pts** | **100% de Aderência com Dossiê PDF, Prints e Link de Administrador** |

---

## 📂 Estrutura de Diretórios de Compliance & QA

Toda a governança de backlog e qualidade está centralizada neste repositório:

```text
Compliance-Quality-Assurance-Tests/
│
├── automatizar-boards/
│   ├── backlog-materias/                      # 📌 Backlogs centralizados das 7 disciplinas
│   │   ├── BACKLOG_COMPLIANCE.md
│   │   ├── BACKLOG_MOBILE.md
│   │   ├── BACKLOG_JAVA_ADVANCED.md
│   │   ├── BACKLOG_DATABASE_ADVANCED.md
│   │   ├── BACKLOG_DOT_NET.md
│   │   ├── BACKLOG_DEVOPS.md
│   │   └── BACKLOG_DISRUPTIVE_ARCHITECTURES.md
│   ├── run_sync.py                            # Orquestrador geral de importação e sincronização
│   ├── azure_boards_sync.py                   # Cliente REST oficial da API do Azure Boards
│   ├── parser_backlog.py                      # Parser Markdown de Epics, Features, PBIs e Tasks
│   ├── link_commits.py                        # Vinculador de commits Git dos 7 repositórios aos Work Items
│   ├── sync_test_cases.py                     # Sincronizador da suíte de 20 Casos de Teste no Azure
│   ├── clean_azure_boards.py                  # Script utilitário para limpeza e reset do Board
│   └── .env.example                           # Modelo de configuração de PAT e organização
│
├── docs/
│   ├── PLANO_DE_TESTES_AZURE_BOARDS.md        # Documento oficial do Plano de Testes Manuais
│   └── MATRIZ_CASOS_DE_TESTE_AZURE.md         # Matriz detalhada dos 20 casos de teste caixa-preta
│
├── postman/
│   ├── CitizenTech_QA_Automation.postman_collection.json # Suíte E2E automatizada para API Java
│   └── CitizenTech_QA_Environment.postman_environment.json # Variáveis de ambiente (Local e Cloud)
│
├── scripts/
│   └── azure_qa_cli.py                        # CLI de inspeção, execução (Passed/Failed) e relatórios
│
├── identificacao.txt                          # Arquivo institucional obrigatório (RM, Nome, Turma)
└── README.md                                  # Documentação principal
```

---

## 🚀 Como Executar as Automações

### 1. Pré-requisitos
- Python 3.10 ou superior
- Personal Access Token (PAT) gerado no Azure DevOps com permissões:
  - `Work Items (Read & Write)`
  - `Test Management (Read & Write)`

Configure seu arquivo `automatizar-boards/.env`:
```ini
AZURE_DEVOPS_ORG=SuaOrganizacaoAzure
AZURE_DEVOPS_PROJECT=CitizenTech
AZURE_DEVOPS_PAT=seu_pat_aqui
GITHUB_ORG=Global-Solution-CitizenTech
```

### 2. Testar Autenticação com o Azure DevOps
```bash
cd automatizar-boards
python run_sync.py --check-auth
```

### 3. Simulação (Dry-Run) e Importação dos Backlogs
```bash
# Simular carga de todos os 7 backlogs sem criar nada na nuvem:
python run_sync.py --all --dry-run

# Importar uma matéria específica:
python run_sync.py --file BACKLOG_MOBILE.md
python run_sync.py --file BACKLOG_JAVA_ADVANCED.md
python run_sync.py --file BACKLOG_COMPLIANCE.md

# Importar TODAS as 7 matérias de uma vez no Azure Boards:
python run_sync.py --all
```

### 4. Sincronizar Casos de Teste (Test Cases) no Azure Boards
```bash
# Simulação local com exportação da matriz Markdown:
python sync_test_cases.py --export-all --dry-run

# Criação real dos 20 Casos de Testes no Azure Boards:
python sync_test_cases.py --sync-azure
```

### 5. Vincular Commits Git dos 7 Repositórios aos Work Items
```bash
# Escaneia os 7 repositórios irmãos e exibe commits identificados:
python link_commits.py --dry-run

# Vincula os commits reais via REST API:
python link_commits.py --scan-all

# Exibir guia de boas práticas de commits (AB#ID):
python link_commits.py --guide
```

### 6. Gestão e Execução no Azure Test Plans (CLI de QA)
```bash
cd ../scripts

# Exibir painel consolidado com métricas de execução:
python azure_qa_cli.py summary

# Listar todos os casos de teste e status:
python azure_qa_cli.py list

# Visualizar detalhes e passos XML de um caso específico:
python azure_qa_cli.py show <TC_ID>

# Executar suíte completa (marcando Passed e gerando falha controlada para evidência de bug):
python azure_qa_cli.py run-all --fail-ids <TC_ID_FALHA>

# Resetar casos de teste para Active:
python azure_qa_cli.py reset-all
```

---

## 🧪 Casos de Teste Funcionais

> A tabela legada foi ocultada por conter expectativas não confirmadas. Use a matriz atual; divergências e lacunas estão documentadas nela.

<!-- Amostra legada mantida apenas no histórico; usar a matriz atual. -->
<!--
| ID | Caso de Teste | Tipo | Feature Vinculada | Objetivo Principal | Entrada Controlada (Inputs) | Saída Esperada |
| :---: | :--- | :---: | :--- | :--- | :--- | :--- |
| **TC-01** | Cadastro de Cidadão Válido | 🟢 Positivo | Autenticação e Usuários | Validar criação de munícipe | `email`: `"enzo.cidadao@citizentech.org"` | HTTP 201 Created, ID gerado |
| **TC-02** | Cadastro com E-mail Duplicado | 🔴 Negativo | Autenticação e Usuários | Testar constraint de unicidade | `email` duplicado | HTTP 409 Conflict amigável |
| **TC-03** | Login e Emissão de JWT | 🟢 Positivo | Autenticação e Usuários | Validar segurança e Bearer token | `senha`: `"SenhaForte@2026"` | HTTP 200 OK, Token JWT válido |
| **TC-04** | Login com Senha Incorreta | 🔴 Negativo | Autenticação e Usuários | Testar rejeição OWASP | Senha incorreta | HTTP 401 Unauthorized genérico |
| **TC-06** | Abertura de Chamado com Foto e GPS | 🟢 Positivo | Gestão de Ocorrências | Homologar registro de zeladoria | `lat: -23.5629, lng: -46.6544` | HTTP 201 Created, Status Aberto |
| **TC-07** | Chamado com Campos Nulos | 🔴 Negativo | Gestão de Ocorrências | Validar Bean Validation | Título e categoria vazios | HTTP 400 Bad Request detalhado |
| **TC-08** | Coordenadas Fora do Município | 🔴 Negativo | Gestão de Ocorrências | Testar limite geográfico | Coordenadas zeradas/fora | HTTP 422 Unprocessable Entity |
| **TC-11** | Voto Comunitário em Chamado | 🟢 Positivo | Engajamento e Votação | Apoiar solicitação do bairro | `chamadoId: 101, usuarioId: 5` | HTTP 200 OK, contador N+1 |
| **TC-12** | Voto Duplicado do Mesmo Cidadão | 🔴 Negativo | Engajamento e Votação | Garantir unicidade de voto | Segundo voto no mesmo chamado | HTTP 409 Conflict |
| **TC-13** | Transição para 'EM_EXECUCAO' | 🟢 Positivo | Painel do Gestor | Auditoria de histórico | `novoStatus: "EM_EXECUCAO"` | HTTP 200, gravado em `HIST_STATUS` |
| **TC-14** | Cidadão Alterando Status | 🔴 Negativo | Painel do Gestor | Testar segurança RBAC | Token de cidadão comum | HTTP 403 Forbidden |
| **TC-16** | Telemetria IoT Alagamento | 🟢 Positivo | Sensoriamento IoT | Ingestão de sensor ESP32 | `distancia_cm: 5.2` (crítico) | Chamado de emergência criado |
| **TC-17** | Classificação de Imagem via IA | 🟢 Positivo | Inteligência Artificial | Triagem visual automática | Foto de fio elétrico caído | Categoria sugerida e Urgência Alta |
| **TC-19** | Cache Offline no Mobile | 🟢 Positivo | Resiliência Mobile | Abrir app sem internet | Modo Avião ativado | App abre com dados em cache local |

-->

Consulte a [matriz completa de casos de teste](./docs/MATRIZ_CASOS_DE_TESTE_AZURE.md), que registra os critérios rastreáveis e as divergências pendentes.

---

## 📋 Checklist Oficial para a Entrega da Global Solution 2

Para submissão no Portal FIAP até **19/11/2026, às 23h55**, gere o arquivo `.zip` contendo:
1. `identificacao.txt` (RM, Nome, Turma).
2. **Arquivo PDF único** unificando o Plano de Projeto Scrum e o Plano de Testes contendo obrigatoriamente:
   - Print da tela principal de Backlogs no Azure DevOps (exibindo Epics e Features).
   - Prints das telas de detalhe das Features e PBIs com critérios de aceite.
   - Print da tela Boards com os Test Cases vinculados por Feature.
   - Print da tela de Sumário e Passos de cada Test Case criado.
   - Gráficos analíticos de execução do Azure Test Plans (pizza de Passed/Failed).
   - **Link oficial do Azure Boards** com o professor convidado como **ADMINISTRATOR** no projeto.
