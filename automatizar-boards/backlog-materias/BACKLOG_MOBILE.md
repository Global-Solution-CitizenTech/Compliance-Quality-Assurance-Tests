# 📋 Backlog Master Azure Boards — Global Solution 2026/2: Mobile Application Development

> **Projeto Integrado:** ZelaFix — Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  
> **Disciplina:** Mobile Application Development (FIAP — 2TDSPG)  
> **Epic Principal:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa`  
> **Start Date:** `2026-11-04`  
> **Target Date:** `2026-11-19`  
> **Padrão:** Azure Boards (Scrum Process: Epic ➔ Feature ➔ PBI ➔ Task)  
> **Diretrizes Estratégicas:** Aplicativo móvel completo desenvolvido em React Native com Expo e TypeScript, contemplando autenticação JWT com sessão persistente, rotas protegidas, mínimo de 7 telas funcionais (Login, Cadastro, Feed do Bairro, Novo Chamado com GPS e Foto, Detalhes com Votação, Radar do Bairro, Perfil e Sobre o App), integração HTTP com a API Java Spring Boot via Axios e camada de resiliência com cache offline no AsyncStorage.

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
[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa
│
├── 🏆 [FEATURE 01] Arquitetura UI, Design System e Navegação por Abas
│   ├── 📄 [PBI-01] Configuração do React Navigation e Estrutura de Telas Base (3 pts)
│   └── 📄 [PBI-02] Componentização Reutilizável, Design System e Telas Institucionais (2 pts)
│
├── 🏆 [FEATURE 02] Autenticação JWT, Sessão Segura e Cache Offline Resiliente
│   ├── 📄 [PBI-03] Camada de Serviço HTTP Axios com Interceptor JWT e Tratamento de Erros (3 pts)
│   └── 📄 [PBI-04] Fluxos de Login, Cadastro do Cidadão e Persistência no AsyncStorage (3 pts)
│
├── 🏆 [FEATURE 03] CRUD Completo de Chamados Urbanos e Geolocalização GPS
│   ├── 📄 [PBI-05] Registro de Novo Chamado com Foto e Captura de Coordenadas GPS (3 pts)
│   └── 📄 [PBI-06] Feed de Ocorrências com Filtro por Categoria e Radar do Bairro (3 pts)
│
└── 🏆 [FEATURE 04] Engajamento Cidadão, Votação Comunitária e Detalhes da Ocorrência
    ├── 📄 [PBI-07] Detalhes do Chamado, Timeline de Status e Voto de Apoio Coletivo (3 pts)
    └── 📄 [PBI-08] Documentação Técnica (README.md) e Vídeo Demonstrativo do App (2 pts)
```

---

## 📊 2. Tabela Resumo do Backlog

| Feature Pai | ID do PBI | Título do Item de Backlog (PBI) | Story Points | Prioridade | Horas Estimadas |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **[FEATURE 01] UI & Navegação** | **PBI-01** | Configuração do React Navigation e Estrutura de Telas Base | 3 pts | 1 - Critical | 6.5h |
| | **PBI-02** | Componentização Reutilizável, Design System e Telas Institucionais | 2 pts | 1 - Critical | 5.0h |
| **[FEATURE 02] Auth & Cache** | **PBI-03** | Camada de Serviço HTTP Axios com Interceptor JWT e Tratamento de Erros | 3 pts | 1 - Critical | 5.5h |
| | **PBI-04** | Fluxos de Login, Cadastro do Cidadão e Persistência no AsyncStorage | 3 pts | 1 - Critical | 7.0h |
| **[FEATURE 03] CRUD & GPS** | **PBI-05** | Registro de Novo Chamado com Foto e Captura de Coordenadas GPS | 3 pts | 1 - Critical | 8.5h |
| | **PBI-06** | Feed de Ocorrências com Filtro por Categoria e Radar do Bairro | 3 pts | 1 - Critical | 7.5h |
| **[FEATURE 04] Voto & Entrega**| **PBI-07** | Detalhes do Chamado, Timeline de Status e Voto de Apoio Coletivo | 3 pts | 1 - Critical | 6.5h |
| | **PBI-08** | Documentação Técnica (README.md) e Vídeo Demonstrativo do App | 2 pts | 2 - High | 4.0h |
| **TOTAL CONSOLIDADO** | **4 Features** | **8 PBIs / 22 Child Tasks Técnicas** | **22 pts** | — | **50.5h** |

---

## 📦 3. Detalhamento dos Itens de Trabalho (Épico, Features, PBIs e Tasks)

---

### 🏛️ ÉPICO
* **Work Item Type:** `Epic`
* **Title:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa`
* **Tags:** `Mobile, ZelaFix, GlobalSolution2, ReactNative, Expo, TypeScript`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `22`
* **Business Value:** `100`
* **Description:** Desenvolvimento do aplicativo móvel ZelaFix em React Native com Expo e TypeScript para viabilizar o relato e acompanhamento transparente de problemas urbanos, integrando autenticação segura JWT, geolocalização por GPS, envio de fotos de evidência, engajamento por votação coletiva em melhorias do bairro e suporte a cache offline resiliente.

---

### 🏆 [FEATURE 01] Arquitetura UI, Design System e Navegação por Abas
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa`
* **Title:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas`
* **Tags:** `Mobile, ZelaFix, UI, Navigation`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-08`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `5`
* **Business Value:** `100`
* **Description:** Estruturação da navegação nativa e componentes visuais do aplicativo ZelaFix com TypeScript e SafeAreaView.
* **Acceptance Criteria:**
  - [x] Biblioteca oficial `@react-navigation/native-stack` e `@react-navigation/bottom-tabs` configurada sem controle manual com ifs.
  - [x] Mínimo de 7 telas distintas operacionais.
  - [x] Design responsivo com suporte a modo escuro/claro e acessibilidade.

#### 🔹 [PBI-01] Configuração do React Navigation e Estrutura de Telas Base
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile, Navigation, Architecture`

##### Descrição (História de Usuário)
> **Como** munícipe que utiliza o ZelaFix,  
> **Eu quero** navegar com facilidade entre o feed do bairro, meus chamados e meu perfil através de abas intuitivas,  
> **Para que** eu encontre rapidamente as funções essenciais de zeladoria urbana.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Mapeamento e tipagem de rotas em `src/types/navigation.ts`.
- [ ] Bottom Tabs para Home, Radar, Novo Chamado e Perfil.
- [ ] Transições fluidas sem flickering ou quebra de navegação.
---

#### 🔹 [PBI-02] Componentização Reutilizável, Design System e Telas Institucionais
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `2`
* **Tags:** `Mobile, DesignSystem, UI`

##### Descrição (História de Usuário)
> **Como** desenvolvedor frontend mobile,  
> **Eu quero** criar uma biblioteca de componentes reutilizáveis (botões, cards, inputs e badges de status),  
> **Para que** o aplicativo mantenha consistência visual e código limpo (DRY).

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Componentes padronizados em `src/components/`.
- [ ] Badges coloridos por status de chamado (Verde: Resolvido, Amarelo: Em Andamento, Azul: Aberto).
- [ ] Tela 'Sobre o App' exibindo informações da equipe e alinhamento com a ODS 11 da ONU.
---

### 🏆 [FEATURE 02] Autenticação JWT, Sessão Segura e Cache Offline Resiliente
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa`
* **Title:** `[FEATURE 02] Autenticação JWT, Sessão Segura e Cache Offline Resiliente`
* **Tags:** `Mobile, ZelaFix, Auth, JWT, OfflineCache`
* **Start Date:** `2026-11-07`
* **Target Date:** `2026-11-12`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** Sistema completo de login, cadastro, injeção de Bearer Token JWT e camada de persistência local para resiliência offline.
* **Acceptance Criteria:**
  - [x] Login e Cadastro integrados com API Java Spring Boot via Axios.
  - [x] Persistência segura do token JWT no AsyncStorage.
  - [x] Rotas privadas inacessíveis por usuários deslogados.
  - [x] Suporte a cache offline em caso de falha de conexão.

#### 🔹 [PBI-03] Camada de Serviço HTTP Axios com Interceptor JWT e Tratamento de Erros
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Autenticação JWT, Sessão Segura e Cache Offline Resiliente`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile, Axios, Security, JWT`

##### Descrição (História de Usuário)
> **Como** arquiteto de software mobile,  
> **Eu quero** configurar o cliente HTTP Axios com interceptors de requisição e resposta,  
> **Para que** os tokens de autorização sejam injetados automaticamente e erros 401 redirecionem para o login.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Interceptor injetando `Authorization: Bearer <token>` em requisições autenticadas.
- [ ] Tratamento centralizado de erros de rede e timeouts.
- [ ] Detecção de status 401 com expurgo automático da sessão.
---

#### 🔹 [PBI-04] Fluxos de Login, Cadastro do Cidadão e Persistência no AsyncStorage
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Autenticação JWT, Sessão Segura e Cache Offline Resiliente`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile, AuthContext, AsyncStorage`

##### Descrição (História de Usuário)
> **Como** munícipe,  
> **Eu quero** criar minha conta com nome, e-mail, telefone e bairro residencial, e realizar login com persistência de sessão,  
> **Para que** eu não precise redigitar minhas credenciais a cada abertura do aplicativo.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Telas LoginScreen e RegisterScreen com validação de campos.
- [ ] AuthContext provendo estado de autenticação reativo em todo o app.
- [ ] Botão de preenchimento automático para agilizar testes da banca examinadora.
---

### 🏆 [FEATURE 03] CRUD Completo de Chamados Urbanos e Geolocalização GPS
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa`
* **Title:** `[FEATURE 03] CRUD Completo de Chamados Urbanos e Geolocalização GPS`
* **Tags:** `Mobile, ZelaFix, CRUD, GPS, Camera`
* **Start Date:** `2026-11-09`
* **Target Date:** `2026-11-15`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `6`
* **Business Value:** `100`
* **Description:** Funcionalidade central de registro de ocorrências urbanas com foto, coordenadas georreferenciadas, listagem no feed e filtragem.
* **Acceptance Criteria:**
  - [x] CRUD completo de chamados (Create, Read, Update e Delete).
  - [x] Captura de coordenadas GPS via Expo Location.
  - [x] Upload/Seleção de imagem de evidência via Expo ImagePicker.
  - [x] Filtros dinâmicos por categoria e status no feed principal.

#### 🔹 [PBI-05] Registro de Novo Chamado com Foto e Captura de Coordenadas GPS
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] CRUD Completo de Chamados Urbanos e Geolocalização GPS`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile, NovoChamado, GPS, Camera`

##### Descrição (História de Usuário)
> **Como** cidadão que identifica um buraco ou bueiro entupido na rua,  
> **Eu quero** abrir um chamado anexando uma foto e minhas coordenadas GPS exatas,  
> **Para que** a equipe de zeladoria municipal localize e repare o problema com rapidez.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Tela NovoChamadoScreen com formulário intuitivo e seleção de categoria.
- [ ] Integração com `expo-location` para preenchimento de latitude/longitude e endereço aproximado.
- [ ] Integração com `expo-image-picker` para foto de comprovação.
- [ ] Envio de `POST /api/chamados` com dados completos.
---

#### 🔹 [PBI-06] Feed de Ocorrências com Filtro por Categoria e Radar do Bairro
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] CRUD Completo de Chamados Urbanos e Geolocalização GPS`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile, Feed, Radar, Filter`

##### Descrição (História de Usuário)
> **Como** morador do bairro,  
> **Eu quero** visualizar um feed com as ocorrências da minha região filtradas por categoria (Vias, Iluminação, Saneamento),  
> **Para que** eu fique ciente dos problemas em andamento e prazos de resolução.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Listagem dinâmica em `HomeScreen.tsx` com pull-to-refresh.
- [ ] Chips horizontais de filtro rápido por categoria.
- [ ] Tela `RadarBairroScreen.tsx` exibindo chamados georreferenciados próximos.
---

### 🏆 [FEATURE 04] Engajamento Cidadão, Votação Comunitária e Detalhes da Ocorrência
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa`
* **Title:** `[FEATURE 04] Engajamento Cidadão, Votação Comunitária e Detalhes da Ocorrência`
* **Tags:** `Mobile, ZelaFix, Voto, Timeline, Documentation`
* **Start Date:** `2026-11-13`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `5`
* **Business Value:** `100`
* **Description:** Telas de acompanhamento detalhado de ocorrências com histórico de status, mecanismo de apoio comunitário e documentação oficial da entrega.
* **Acceptance Criteria:**
  - [x] Tela detalhada do chamado exibindo timeline e histórico de alterações.
  - [x] Mecanismo de votação (+1) para priorização pública.
  - [x] README.md padronizado com prints, instruções de execução e link do vídeo gravado.

#### 🔹 [PBI-07] Detalhes do Chamado, Timeline de Status e Voto de Apoio Coletivo
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 04] Engajamento Cidadão, Votação Comunitária e Detalhes da Ocorrência`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile, Details, Voto, StatusHistory`

##### Descrição (História de Usuário)
> **Como** munícipe engajado,  
> **Eu quero** abrir um chamado comunitário e clicar em 'Apoiar (+1)', bem como acompanhar a timeline de reparo,  
> **Para que** demandas coletivas ganhem maior visibilidade diante da prefeitura.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Exibição de ChamadoDetailsScreen com imagem, mapa, autor e descrição completa.
- [ ] Botão de apoio chamando `POST /api/chamados/{id}/votos` com feedback imediato.
- [ ] Timeline visual com datas de abertura, previsão e conclusão.
---

#### 🔹 [PBI-08] Documentação Técnica (README.md) e Vídeo Demonstrativo do App
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 04] Engajamento Cidadão, Votação Comunitária e Detalhes da Ocorrência`
* **Priority:** `2 - High`
* **Effort (Story Points):** `2`
* **Tags:** `Mobile, Documentation, Video`

##### Descrição (História de Usuário)
> **Como** avaliador da FIAP,  
> **Eu quero** acessar um README.md minucioso e assistir a um vídeo gravado demonstrando todas as telas e fluxos do app,  
> **Para que** eu possa homologar a entrega com total clareza e sem barreiras de ambiente.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] README.md completo com arquitetura, bibliotecas, instruções de execução e credenciais.
- [ ] Vídeo demonstrativo narrado no YouTube comprovando login, cadastro, GPS, fotos e votos.
- [ ] Hash de commit de referência destacado no topo da documentação.