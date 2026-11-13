# 🏛️ CitizenTech — Compliance, Quality Assurance & Tests
> **FIAP Global Solution 2026/2 • Turmas de Fevereiro (2TDSPG)**  
> **Tema:** CitizenTech — Tecnologia com o cidadão no centro da inovação (ODS 11 – Cidades Sustentáveis)  
> **Disciplina:** Compliance, Quality Assurance & Tests  
> **Plataforma Oficial:** Microsoft Azure DevOps (Azure Boards & Test Plans)  

---

## 👥 Integrantes do Grupo

| Nome Completo | RM | Turma | GitHub | LinkedIn |
| :--- | :---: | :---: | :--- | :--- |
| **Enzo Okuizumi** | **561432** | 2TDSPG | [@EnzoOkuizumiFiap](https://github.com/EnzoOkuizumiFiap) | [LinkedIn](https://www.linkedin.com/in/enzo-okuizumi-b60292256/) |
| **Gustavo Okada** | **563428** | 2TDSPG | [@Gdev3356](https://github.com/Gdev3356) | [LinkedIn](https://www.linkedin.com/in/gustavo-okada-53a3b8359/) |
| **Lucas Barros Gouveia** | **566422** | 2TDSPG | [@LuzBGouveia](https://github.com/LuzBGouveia) | [LinkedIn](https://www.linkedin.com/in/lucas-barros-gouveia-09b147355/) |
| **Luna de Carvalho Guimarães** | **562290** | 2TDSPG | [@lunaguima](https://github.com/lunaguima) | [LinkedIn](https://www.linkedin.com/in/luna-guimar%C3%A3es-b0ba82309/) |
| **Milton Marcelino** | **564836** | 2TDSPG | [@MiltonMarcelino](https://github.com/MiltonMarcelino) | [LinkedIn](https://www.linkedin.com/in/milton-marcelino-250298142) |

---

## 🔗 Links Oficiais Obrigatórios de Entrega (Global Solution 2)

| Recurso | Descrição | Link Oficial |
| :--- | :--- | :--- |
| 📋 **Azure Boards & Test Plans (QA)** | Acesso aos Planos de Testes Manuais com dados controlados | https://dev.azure.com/ZelaFixGS/ZelaFix |
| 🐙 **Repositório Oficial (Branch `develop`)** | Código de QA, matriz de testes e scripts | https://github.com/Global-Solution-CitizenTech/Compliance-Quality-Assurance-Tests |
| ☕ **Repositório Java (Branch `develop`)** | Backend Spring Boot, persistência relacional e suíte de testes | https://github.com/Global-Solution-CitizenTech/Java-Advanced |

## 🔗 Vídeo de Demonstração (Global Solution 2)

*(Link do YouTube será inserido após gravação)*

---

## 🌐 Links do Ecossistema Integrado (Java, DevOps & Nuvem Azure)

| Componente | Descrição | Link |
| :--- | :--- | :--- |
| 🌐 **API em Produção (Azure Web App)** | Endpoint base do App Service provisionado na nuvem | https://app-zelafix-561432.azurewebsites.net |
| ⚙️ **Worker IA em Produção (Azure Web App)** | Worker assíncrono com Spring AI (Azure AI Foundry) | https://app-zelafix-worker-561432.azurewebsites.net |
| 📖 **Swagger UI Interativo (OpenAPI 3.0)** | Documentação interativa de todos os endpoints REST | https://app-zelafix-561432.azurewebsites.net/swagger-ui.html |
| 🩺 **Actuator Health (Observabilidade)** | Healthcheck em tempo real (Oracle + RabbitMQ + Liveness) | https://app-zelafix-561432.azurewebsites.net/actuator/health |
| 🚀 **Repositório GitHub (DevOps & Cloud)** | Pipelines de CI/CD, IaC Bash e infraestrutura em nuvem | https://github.com/Global-Solution-CitizenTech/DevOps-Tools-Cloud-Computing |

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

## 🧪 Casos de Teste Funcionais (Azure Test Plans)

Os 24 casos de teste cadastrados no **Azure DevOps (`ZelaFixGS/ZelaFix`)** cobrem autenticação/RBAC, catálogo/endereços, chamados, triagem assíncrona do Worker e ZelaBot IA:

| ID | Caso de Teste | Suíte | Tipo |
| :---: | :--- | :--- | :---: |
| **TC-01** | Autenticar contas de QA dos perfis ADMIN, GESTOR e CIDADAO | `api-auth-rbac` | Positivo |
| **TC-02** | Rejeitar login com credenciais inválidas | `api-auth-rbac` | Negativo |
| **TC-03** | Bloquear endpoint protegido sem token | `api-auth-rbac` | Negativo |
| **TC-04** | Rejeitar token JWT inválido | `api-auth-rbac` | Negativo |
| **TC-05** | Impedir CIDADAO de criar categoria | `api-auth-rbac` | Negativo |
| **TC-06** | Impedir CIDADAO de alterar status de chamado | `api-auth-rbac` | Negativo |
| **TC-07** | Consultar categorias e status disponíveis | `api-catalog-adress` | Positivo |
| **TC-08** | Criar categoria como ADMIN | `api-catalog-adress` | Positivo |
| **TC-09** | Rejeitar categoria com nome vazio | `api-catalog-adress` | Negativo |
| **TC-10** | Criar e consultar endereço por ID | `api-catalog-adress` | Positivo |
| **TC-11** | Rejeitar CEP em formato inválido | `api-catalog-adress` | Negativo |
| **TC-12** | Impedir CIDADAO de listar endereços administrativos | `api-catalog-adress` | Negativo |
| **TC-13** | Criar chamado com foto Base64 | `api-chamados` | Positivo |
| **TC-14** | Criar chamado multipart e recuperar foto | `api-chamados` | Positivo |
| **TC-15** | Rejeitar chamado com dados inválidos | `api-chamados` | Negativo |
| **TC-16** | Consultar chamados com paginação e filtro do próprio usuário | `api-chamados` | Positivo |
| **TC-17** | Atualizar ciclo de status e consultar histórico | `api-chamados` | Positivo |
| **TC-18** | Excluir chamado como ADMIN e confirmar remoção | `api-chamados` | Positivo |
| **TC-19** | Confirmar triagem assíncrona do Worker no histórico do chamado | `worker-ai` | Positivo |
| **TC-20** | Responder consulta ZelaBot com contexto normativo | `zelabot-ai` | Positivo |
| **TC-21** | Acionar guardrail para risco vital | `zelabot-ai` | Positivo |
| **TC-22** | Manter escopo cívico diante de solicitação de código | `zelabot-ai` | Negativo |
| **TC-23** | Gerar triagem técnica para cratera com engajamento | `zelabot-ai` | Positivo |
| **TC-24** | Gerar insights preventivos para bairro | `zelabot-ai` | Positivo |

Consulte a [matriz completa de casos de teste](./docs/MATRIZ_CASOS_DE_TESTE_AZURE.md) para detalhes de pré-condições, entradas, saídas esperadas e passos.
