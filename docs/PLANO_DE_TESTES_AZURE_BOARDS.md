# 📋 Plano de Testes de Software — Azure Boards & Test Plans
## 🏛️ Projeto: CitizenTech — Zeladoria Urbana Colaborativa
> **FIAP Global Solution 2026/2** • Turmas de Fevereiro (2TDSPG)  
> **Disciplina:** Compliance, Quality Assurance & Tests  
> **Plataforma Oficial:** Microsoft Azure DevOps (Azure Boards & Test Plans)

---

## 👥 Integrantes do Grupo (Ordem Alfabética)

| Nome Completo | RM | Turma | Papel no Projeto / Governança QA |
| :--- | :---: | :---: | :--- |
| **Enzo Okuizumi** | **561432** | 2TDSPG | Governança Scrum, Gestão Azure DevOps e Automação de Testes |
| **Gustavo Okada** | **563428** | 2TDSPG | Arquitetura .NET, Testes Unitários AAA e Observabilidade |
| **Lucas Barros Gouveia** | **566422** | 2TDSPG | Database Advanced (Oracle PL/SQL, Triggers DML e MongoDB) |
| **Luna de Carvalho Guimarães** | **562290** | 2TDSPG | Mobile Development (React Native, Rotas Protegidas e Cache) |
| **Milton Jakson de Sousa Marcelino** | **564836** | 2TDSPG | DevOps & Cloud (Docker/Azure) e Disruptive IoT/GenAI |

---

## 🎯 1. Escopo e Estratégia de Qualidade de Software

O presente plano formaliza as diretrizes de garantia de qualidade para a solução **CitizenTech**, contemplando:
1. **Governança Ágil no Azure Boards:** Estruturação estrita da hierarquia Scrum (Epics ➔ Features ➔ PBIs ➔ Tasks).
2. **Cobertura Funcional Caixa-Preta:** Homologação com cenários positivos (caminho feliz) e negativos (validação de erros, restrições e limites).
3. **Técnica de Dados de Entrada Controlados:** Uso de parâmetros estáticos previamente acordados para garantir repetibilidade na auditoria da banca examinadora.
4. **Rastreabilidade de Código (Git Commits):** Vínculo formal dos commits dos 7 repositórios aos itens de trabalho do Azure Boards.
5. **Evidências no Azure Test Plans:** Execução de casos com status Passed e Failed controlados para validação de métricas de bug tracking.

---

## 📊 2. Resumo da Suíte de Casos de Testes no Azure Test Plans

| Domínio Funcional / Suíte | Total de Casos | Positivos | Negativos | Foco de Avaliação |
| :--- | :---: | :---: | :---: | :--- |
| **Autenticação e Usuários** | 5 | 3 | 2 | Segurança JWT, cadastro com validação e controle de senhas |
| **Abertura de Chamados** | 3 | 1 | 2 | Inserção de ocorrências, coordenadas GPS e fotos de comprovação |
| **Radar e Consultas** | 2 | 2 | 0 | Filtragem por categoria, busca textual e debounce |
| **Engajamento & Votos** | 2 | 1 | 1 | Voto comunitário em chamados e bloqueio de votos duplicados |
| **Ciclo de Vida do Chamado** | 3 | 2 | 1 | Transição de status por gestores, auditoria DML e controle RBAC |
| **Sensoriamento IoT** | 1 | 1 | 0 | Telemetria MQTT de bueiro inteligente com alerta de alagamento |
| **IA Generativa & Triagem** | 2 | 1 | 1 | Classificação de fotos de ocorrências e filtragem de conteúdo |
| **Resiliência Mobile & Cache** | 2 | 2 | 0 | Operação offline resiliente e reconciliação com o backend |
| **TOTAL CONSOLIDADO** | **20** | **13 (65%)** | **7 (35%)** | **100% de Cobertura das Features da Solução** |

---

## 🛠️ 3. Ferramentas e Procedimentos Operacionais

- **Azure Boards:** Gerenciamento do Backlog, sprints e rastreabilidade de requisitos.
- **Azure Test Plans:** Execução de casos de testes manuais e emissão de gráficos analíticos.
- **Postman:** Suíte automatizada de testes de integração contra a API Java Spring Boot.
- **Scripts de Automação Python:** Sincronização automatizada e extração de evidências via REST API oficial da Microsoft.

> 📌 *Consulte a matriz completa e detalhada em [`docs/MATRIZ_CASOS_DE_TESTE_AZURE.md`](./MATRIZ_CASOS_DE_TESTE_AZURE.md).*