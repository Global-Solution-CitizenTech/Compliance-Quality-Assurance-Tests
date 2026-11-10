# 📱 Backlog Master Azure Boards — Global Solution 2026/2: Mobile Application Development

> **Projeto Integrado:** ZelaFix — Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  
> **Disciplina:** Mobile Application Development (FIAP — 2TDSPG)  
> **Epic Principal:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa`  
> **Responsável / Owner:** Luna de Carvalho Guimarães (`RM562290@fiap.com.br`)  
> **Start Date:** `2026-11-04`  
> **Target Date:** `2026-11-19`  
> **Padrão:** Azure Boards (Scrum Process: Epic ➔ Feature ➔ PBI)  
> **Diretrizes Estratégicas:** Aplicativo móvel completo desenvolvido em React Native com Expo e TypeScript, contemplando autenticação JWT com sessão persistente, rotas protegidas, mínimo de 7 telas funcionais (Login, Cadastro, Feed do Bairro, Radar com Filtros, Novo Chamado com GPS e Foto, Detalhes com Votação, Meus Chamados, Editar Chamado, Perfil com Edição Cadastral e Sobre o App), integração HTTP com a API Java Spring Boot via Axios e camada de resiliência com cache offline no AsyncStorage.

---

## 👥 Integrantes do Grupo (Ordem Alfabética Estrita)

| Integrante | RM | Turma | Papel / Responsabilidade |
| :--- | :---: | :---: | :--- |
| **Enzo Okuizumi Miranda de Souza** | **561432** | 2TDSPG | IoT, Compliance, Java & Arquitetura Geral |
| **Gustavo Keiji Okada** | **563428** | 2TDSPG | Back-end .NET Enterprise & Minimal APIs |
| **Lucas Barros Gouveia** | **566422** | 2TDSPG | Database Modeling & Engenharia de Dados Oracle |
| **Luna de Carvalho Guimarães** | **562290** | 2TDSPG | **Mobile Application Development (React Native / Expo)** |
| **Milton Jakson de Sousa Marcelino** | **564836** | 2TDSPG | DevOps Tools, Cloud Computing & CI/CD Pipelines |

---

## 🏛️ 1. Estrutura Hierárquica no Azure Boards

```text
[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa
│
├── 🏆 [FEATURE 01] Arquitetura UI, Design System e Navegação por Abas
│   ├── 📄 [PBI-01] Setup Inicial do Projeto Expo com TypeScript e Configuração de Ferramental (3 pts)
│   ├── 📄 [PBI-02] Design System CitizenTech e Tipagens de Domínio da Zeladoria (2 pts)
│   ├── 📄 [PBI-03] Biblioteca de Componentes Reutilizáveis de UI e Modais de Feedback (3 pts)
│   ├── 📄 [PBI-04] Estrutura de Navegação Nativa com React Navigation e Rotas Tipadas (2 pts)
│   ├── 📄 [PBI-05] Prototipação e Telas de Fluxo do Cidadão (Home, Feed do Bairro e Telas Institucionais) (3 pts)
│   └── 📄 [PBI-06] Telas de Perfil do Cidadão, Edição Cadastral e Resiliência de Layout (SafeAreaView) (2 pts)
│
├── 🏆 [FEATURE 02] Autenticação JWT, Sessão Segura e Cache Offline Resiliente
│   ├── 📄 [PBI-07] Configuração do Cliente HTTP Axios com Interceptor JWT e Serviços Base (3 pts)
│   ├── 📄 [PBI-08] Camada de Autenticação, AuthContext e Persistência de Sessão no AsyncStorage (3 pts)
│   └── 📄 [PBI-09] Telas de Login, Cadastro do Cidadão e Proteção de Rotas Privadas (3 pts)
│
├── 🏆 [FEATURE 03] CRUD Completo de Chamados Urbanos e Geolocalização GPS
│   ├── 📄 [PBI-10] Formulário de Registro de Ocorrência com Captura de Coordenadas GPS (3 pts)
│   ├── 📄 [PBI-11] Anexo de Evidências Fotográficas e Otimização de Imagens (3 pts)
│   └── 📄 [PBI-12] Feed de Ocorrências com Filtro por Categoria e Gestão de Chamados (CRUD Completo) (3 pts)
│
└── 🏆 [FEATURE 04] Engajamento Cidadão, Votação Comunitária e Documentação/Entrega
    ├── 📄 [PBI-13] Visualização Detalhada do Chamado, Timeline de Status e Votação Comunitária (+1 Apoio) (3 pts)
    ├── 📄 [PBI-14] Modo Offline Resiliente com Cache de Ocorrências no AsyncStorage (2 pts)
    └── 📄 [PBI-15] Documentação Técnica Completa (README.md) e Vídeo Demonstrativo do App (2 pts)
```

---

## 📊 2. Tabela Resumo do Backlog

| Feature Pai | ID do PBI | Título do Item de Backlog (PBI) | Story Points | Prioridade | Horas Estimadas |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **[FEATURE 01] UI & Navegação** | **PBI-01** | Setup Inicial do Projeto Expo com TypeScript e Configuração de Ferramental | 3 pts | 1 - Critical | 5.0h |
| | **PBI-02** | Design System CitizenTech e Tipagens de Domínio da Zeladoria | 2 pts | 1 - Critical | 4.0h |
| | **PBI-03** | Biblioteca de Componentes Reutilizáveis de UI e Modais de Feedback | 3 pts | 1 - Critical | 6.0h |
| | **PBI-04** | Estrutura de Navegação Nativa com React Navigation e Rotas Tipadas | 2 pts | 1 - Critical | 4.5h |
| | **PBI-05** | Prototipação e Telas de Fluxo do Cidadão (Home, Feed do Bairro e Telas Institucionais) | 3 pts | 1 - Critical | 6.5h |
| | **PBI-06** | Telas de Perfil do Cidadão, Edição Cadastral e Resiliência de Layout (SafeAreaView) | 2 pts | 1 - Critical | 4.0h |
| **[FEATURE 02] Auth & Sessão** | **PBI-07** | Configuração do Cliente HTTP Axios com Interceptor JWT e Serviços Base | 3 pts | 1 - Critical | 5.5h |
| | **PBI-08** | Camada de Autenticação, AuthContext e Persistência de Sessão no AsyncStorage | 3 pts | 1 - Critical | 6.0h |
| | **PBI-09** | Telas de Login, Cadastro do Cidadão e Proteção de Rotas Privadas | 3 pts | 1 - Critical | 6.5h |
| **[FEATURE 03] CRUD & Sensores** | **PBI-10** | Formulário de Registro de Ocorrência com Captura de Coordenadas GPS | 3 pts | 1 - Critical | 7.5h |
| | **PBI-11** | Anexo de Evidências Fotográficas e Otimização de Imagens | 3 pts | 1 - Critical | 6.0h |
| | **PBI-12** | Feed de Ocorrências com Filtro por Categoria e Gestão de Chamados (CRUD Completo) | 3 pts | 1 - Critical | 8.0h |
| **[FEATURE 04] Voto & Entrega** | **PBI-13** | Visualização Detalhada do Chamado, Timeline de Status e Votação Comunitária (+1 Apoio) | 3 pts | 1 - Critical | 6.0h |
| | **PBI-14** | Modo Offline Resiliente com Cache de Ocorrências no AsyncStorage | 2 pts | 2 - High | 4.5h |
| | **PBI-15** | Documentação Técnica Completa (README.md) e Vídeo Demonstrativo do App | 2 pts | 1 - Critical | 5.0h |
| **TOTAL CONSOLIDADO** | **4 Features** | **15 Product Backlog Items (PBIs)** | **37 pts** | — | **84.5h** |

---

## 📦 3. Detalhamento dos Itens de Trabalho

---

### 🏛️ ÉPICO
* **Work Item Type:** `Epic`
* **Title:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa`
* **Tags:** `Mobile, GlobalSolution2, ReactNative, Expo, TypeScript`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `37`
* **Business Value:** `100`
* **Description:** Desenvolvimento do aplicativo móvel ZelaFix em React Native com Expo e TypeScript para viabilizar o relato e acompanhamento transparente de problemas urbanos, integrando autenticação segura JWT, geolocalização por GPS, envio de fotos de evidência, engajamento por votação coletiva em melhorias do bairro e suporte a cache offline resiliente.

---

### 🏆 [FEATURE 01] Arquitetura UI, Design System e Navegação por Abas
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa`
* **Title:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas`
* **Tags:** `Mobile, UI, Navigation, DesignSystem`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-08`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `15`
* **Business Value:** `100`
* **Description:** Estruturação da navegação nativa, design system, componentes visuais e prototipação das telas do aplicativo ZelaFix com TypeScript e SafeAreaView.
* **Acceptance Criteria:**
  - [x] Biblioteca oficial `@react-navigation/native-stack` e `@react-navigation/bottom-tabs` configurada sem controle manual com ifs.
  - [x] Mínimo de 7 telas distintas operacionais no protótipo navegável.
  - [x] Design responsivo com paleta de cores CitizenTech e tipografia consistente.

#### 🔹 [PBI-01] Setup Inicial do Projeto Expo com TypeScript e Configuração de Ferramental
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile, Setup, TypeScript, Expo`

##### Descrição (História de Usuário)
> **Como** equipe de engenharia mobile,  
> **Eu quero** inicializar o projeto com Expo SDK 58, TypeScript configurado em modo estrito e estrutura modular de diretórios,  
> **Para que** tenhamos uma base de código robusta, tipada e livre de falhas de compatibilidade.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Projeto configurado com `expo-status-bar`, `@react-native-async-storage/async-storage` compatível com SDK 58.
- [ ] Arquivo `tsconfig.json` ajustado para compilação estrita e suporte a aliases de importação.
- [ ] Estrutura organizada em pastas: `components/`, `contexts/`, `hooks/`, `navigation/`, `screens/`, `services/`, `theme/`, `types/`.

---

#### 🔹 [PBI-02] Design System CitizenTech e Tipagens de Domínio da Zeladoria
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `2`
* **Tags:** `Mobile, DesignSystem, Theme, Types`

##### Descrição (História de Usuário)
> **Como** designer de produto e desenvolvedor front-end,  
> **Eu quero** centralizar tokens de design (cores, tipografia, espaçamentos) e contratos de tipos TypeScript,  
> **Para que** todas as telas compartilhem uma identidade visual sustentável e consistente.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Paleta de cores definida em `src/theme/colors.ts` (primária verde sustentável, neutros, alertas e badges de status).
- [ ] Escalas de espaçamento (`spacing.ts`) e tipografia hierárquica (`typography.ts`) documentadas.
- [ ] Modelos de dados em `src/types/index.ts`: `Chamado`, `User`, `Category`, `Status`, `Bairro`.

---

#### 🔹 [PBI-03] Biblioteca de Componentes Reutilizáveis de UI e Modais de Feedback
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile, Components, UI, Feedback`

##### Descrição (História de Usuário)
> **Como** cidadão utilizando o app,  
> **Eu quero** interagir com botões responsivos, campos de texto com feedback de erro e modais elegantes,  
> **Para que** a usabilidade seja fluida, rápida e visualmente agradável.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Componentes atômicos: `Button.tsx`, `Input.tsx`, `Header.tsx`, `StatCard.tsx`.
- [ ] Badges especializados: `CategoryBadge.tsx` (ícones temáticos) e `StatusBadge.tsx` (cores semânticas).
- [ ] Componente `ChamadoCard.tsx` exibindo título, categoria, status, fotos e contador de votos.
- [ ] Componentes de estado: `EmptyState.tsx` e modal de confirmação `FeedbackModal.tsx`.

---

#### 🔹 [PBI-04] Estrutura de Navegação Nativa com React Navigation e Rotas Tipadas
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `2`
* **Tags:** `Mobile, ReactNavigation, BottomTabs, Stacks`

##### Descrição (História de Usuário)
> **Como** munícipe que navega pelo ZelaFix,  
> **Eu quero** alternar entre as abas principais e abrir telas secundárias em pilhas de navegação nativas,  
> **Para que** a transição entre telas seja instantânea e intuitiva.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Tipagem de rotas em `src/navigation/types.ts` com suporte a passagem de parâmetros (`chamadoId`, `filtroCategoria`).
- [ ] `TabNavigator.tsx` com ícones vetoriais para: Feed (Home), Radar do Bairro, Novo Chamado, Meus Chamados e Perfil.
- [ ] `AppNavigator.tsx` e `AuthNavigator.tsx` orquestrando o fluxo condicional de acesso.

---

#### 🔹 [PBI-05] Prototipação e Telas de Fluxo do Cidadão (Home, Feed do Bairro e Telas Institucionais)
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile, Screens, Prototype, MockData`

##### Descrição (História de Usuário)
> **Como** munícipe e avaliador acadêmico,  
> **Eu quero** explorar o feed de ocorrências urbanas com dados mockados e consultar informações do projeto na tela Sobre,  
> **Para que** seja possível validar visualmente o layout antes da subida dos microserviços de backend.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] `HomeScreen.tsx` com resumo de indicadores do bairro (estatísticas de chamados abertos, em andamento e resolvidos).
- [ ] `RadarBairroScreen.tsx` com listagem e filtragem inicial por categorias de zeladoria.
- [ ] `SobreAppScreen.tsx` detalhando a proposta CitizenTech, alinhamento com a ODS 11 e créditos dos 5 integrantes.
- [ ] Conjunto de dados simulados em `src/services/mockData.ts` para homologação visual offline.

---

#### 🔹 [PBI-06] Telas de Perfil do Cidadão, Edição Cadastral e Resiliência de Layout (SafeAreaView)
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `2`
* **Tags:** `Mobile, Profile, SafeAreaView, UX`

##### Descrição (História de Usuário)
> **Como** munícipe cadastrado no ZelaFix,  
> **Eu quero** acessar minha tela de perfil, visualizar meus dados cadastrais e atualizar minha senha,  
> **Para que** minhas informações estejam sempre corretas e a interface não sofra sobreposição de notch ou barras de status.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] `ProfileScreen.tsx` com visualização de nome, email, telefone, bairro residencial e histórico de chamados criados.
- [ ] Modal/Formulário para alteração de dados cadastrais e senha do usuário.
- [ ] Aplicação estrita de `SafeAreaView` e compensação de padding para dispositivos iOS e Android.

---

### 🏆 [FEATURE 02] Autenticação JWT, Sessão Segura e Cache Offline Resiliente
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa`
* **Title:** `[FEATURE 02] Autenticação JWT, Sessão Segura e Cache Offline Resiliente`
* **Tags:** `Mobile, Auth, JWT, OfflineCache`
* **Start Date:** `2026-11-07`
* **Target Date:** `2026-11-12`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Description:** Sistema completo de login, cadastro, injeção de Bearer Token JWT e camada de persistência local para resiliência offline.
* **Acceptance Criteria:**
  - [x] Login e Cadastro integrados com API Java Spring Boot via Axios.
  - [x] Persistência segura do token JWT no AsyncStorage.
  - [x] Rotas privadas inacessíveis por usuários deslogados.

#### 🔹 [PBI-07] Configuração do Cliente HTTP Axios com Interceptor JWT e Serviços Base
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
- [ ] Instância Axios configurada em `src/services/api.ts` com base URL parametrizada.
- [ ] Interceptor injetando `Authorization: Bearer <token>` em requisições autenticadas.
- [ ] Tratamento centralizado de erros de rede, status 401 (expurgo de sessão) e timeouts.

---

#### 🔹 [PBI-08] Camada de Autenticação, AuthContext e Persistência de Sessão no AsyncStorage
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Autenticação JWT, Sessão Segura e Cache Offline Resiliente`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile, AuthContext, AsyncStorage, Session`

##### Descrição (História de Usuário)
> **Como** cidadão que utiliza frequentemente o app,  
> **Eu quero** que minha sessão de login continue ativa ao reabrir o aplicativo,  
> **Para que** eu não precise redigitar credenciais a cada acesso.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] `AuthContext.tsx` e hook customizado `useAuth.ts` expondo `user`, `token`, `isAuthenticated`, `signIn`, `signUp`, `signOut`.
- [ ] Persistência segura de tokens e dados cadastrais no `AsyncStorage` via `src/services/storageService.ts`.
- [ ] Validação de integridade do token no ciclo de inicialização do app.

---

#### 🔹 [PBI-09] Telas de Login, Cadastro do Cidadão e Proteção de Rotas Privadas
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 02] Autenticação JWT, Sessão Segura e Cache Offline Resiliente`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile, Login, Register, ProtectedRoutes`

##### Descrição (História de Usuário)
> **Como** novo munícipe,  
> **Eu quero** cadastrar minha conta com nome, email, senha e bairro residencial, e efetuar login com retorno de token real,  
> **Para que** minhas solicitações de zeladoria fiquem devidamente identificadas.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] `LoginScreen.tsx` e `RegisterScreen.tsx` com validações de e-mail e força de senha.
- [ ] Botão de preenchimento rápido (Quick Fill) para facilitar os testes da banca avaliadora.
- [ ] Proteção de rotas em `src/navigation/index.tsx`: deslogados só visualizam o stack de autenticação.

---

### 🏆 [FEATURE 03] CRUD Completo de Chamados Urbanos e Geolocalização GPS
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa`
* **Title:** `[FEATURE 03] CRUD Completo de Chamados Urbanos e Geolocalização GPS`
* **Tags:** `Mobile, CRUD, GPS, Camera`
* **Start Date:** `2026-11-09`
* **Target Date:** `2026-11-15`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Description:** Funcionalidade central de registro de ocorrências urbanas com foto, coordenadas georreferenciadas, listagem no feed e filtragem.
* **Acceptance Criteria:**
  - [x] CRUD completo de chamados (Create, Read, Update e Delete).
  - [x] Captura de coordenadas GPS via Expo Location.
  - [x] Upload/Seleção de imagem de evidência via Expo ImagePicker.
  - [x] Filtros dinâmicos por categoria e status no feed principal.

#### 🔹 [PBI-10] Formulário de Registro de Ocorrência com Captura de Coordenadas GPS
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] CRUD Completo de Chamados Urbanos e Geolocalização GPS`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile, NovoChamado, GPS, Location`

##### Descrição (História de Usuário)
> **Como** munícipe que identifica um buraco perigoso na rua,  
> **Eu quero** abrir um chamado onde minhas coordenadas GPS sejam obtidas automaticamente pelo sensor do celular,  
> **Para que** a equipe municipal localize exatamente onde o conserto deve ser realizado.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] `NovoChamadoScreen.tsx` integrado com a biblioteca `expo-location`.
- [ ] Solicitação de permissão de acesso à geolocalização com tratamento gracioso de recusa.
- [ ] Obtenção automática de latitude, longitude e geocodificação reversa de logradouro/bairro.

---

#### 🔹 [PBI-11] Anexo de Evidências Fotográficas e Otimização de Imagens
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] CRUD Completo de Chamados Urbanos e Geolocalização GPS`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile, Camera, ImagePicker, Evidence`

##### Descrição (História de Usuário)
> **Como** cidadão que documenta uma falha de iluminação ou vazamento,  
> **Eu quero** tirar uma foto na hora ou escolher uma foto da galeria para comprovar o chamado,  
> **Para que** a prefeitura possa dimensionar a equipe e os equipamentos necessários.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Integração com `expo-image-picker` para captura com a câmera ou escolha na galeria.
- [ ] Exibição de preview da imagem selecionada com opção de remover ou substituir antes do envio.
- [ ] Otimização e compressão da imagem para envio leve na requisição HTTP.

---

#### 🔹 [PBI-12] Feed de Ocorrências com Filtro por Categoria e Gestão de Chamados (CRUD Completo)
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 03] CRUD Completo de Chamados Urbanos e Geolocalização GPS`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile, Feed, CRUD, MeusChamados`

##### Descrição (História de Usuário)
> **Como** cidadão ativo no ZelaFix,  
> **Eu quero** visualizar meus chamados em aberto, editar dados se necessário e excluir solicitações duplicadas,  
> **Para que** eu tenha total controle sobre o ciclo de vida das minhas demandas de zeladoria.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] `MeusChamadosScreen.tsx` listando chamados criados pelo usuário autenticado.
- [ ] `EditarChamadoScreen.tsx` permitindo atualizar título, descrição e categoria (Update).
- [ ] Funcionalidade de exclusão com diálogo de confirmação via `FeedbackModal.tsx` (Delete).
- [ ] Feed geral com pull-to-refresh e chips de filtragem por categoria (Vias, Iluminação, Saneamento, Limpeza).

---

### 🏆 [FEATURE 04] Engajamento Cidadão, Votação Comunitária e Documentação/Entrega
* **Work Item Type:** `Feature`
* **Parent:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa`
* **Title:** `[FEATURE 04] Engajamento Cidadão, Votação Comunitária e Documentação/Entrega`
* **Tags:** `Mobile, Voto, Offline, Documentation`
* **Start Date:** `2026-11-13`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `7`
* **Business Value:** `100`
* **Description:** Telas de acompanhamento detalhado de ocorrências com histórico de status, mecanismo de apoio comunitário e documentação oficial da entrega.
* **Acceptance Criteria:**
  - [x] Tela detalhada do chamado exibindo timeline e histórico de alterações.
  - [x] Mecanismo de votação (+1) para priorização pública.
  - [x] Suporte a cache offline em caso de falha de conexão.
  - [x] README.md padronizado com prints, instruções de execução e link do vídeo gravado.

#### 🔹 [PBI-13] Visualização Detalhada do Chamado, Timeline de Status e Votação Comunitária (+1 Apoio)
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 04] Engajamento Cidadão, Votação Comunitária e Documentação/Entrega`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile, Details, Timeline, Upvote`

##### Descrição (História de Usuário)
> **Como** morador do bairro afetado por uma demanda,  
> **Eu quero** abrir o detalhe de um chamado já aberto por outro vizinho e votar com '+1 Apoio',  
> **Para que** a prefeitura identifique que o problema atinge dezenas de moradores sem criar chamados duplicados.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] `ChamadoDetailsScreen.tsx` exibindo foto em alta resolução, autor, data, bairro e status.
- [ ] Linha do tempo visual (Timeline) indicando a progressão: Aberto ➔ Em Análise ➔ Em Andamento ➔ Concluído.
- [ ] Botão de Upvote com incremento visual imediato e chamada de endpoint `POST /api/chamados/{id}/votos`.

---

#### 🔹 [PBI-14] Modo Offline Resiliente com Cache de Ocorrências no AsyncStorage
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 04] Engajamento Cidadão, Votação Comunitária e Documentação/Entrega`
* **Priority:** `2 - High`
* **Effort (Story Points):** `2`
* **Tags:** `Mobile, Offline, Cache, Resilience`

##### Descrição (História de Usuário)
> **Como** munícipe navegando em áreas com instabilidade de sinal 4G/5G,  
> **Eu quero** continuar visualizando os chamados do feed em modo offline,  
> **Para que** a experiência do aplicativo não trave nem exiba telas brancas de erro.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] Cache local dos últimos chamados gravado em `AsyncStorage` via `storageService.ts`.
- [ ] Fallback transparente para o cache quando requisições HTTP retornarem erro de rede ou timeout.
- [ ] Banner sutil avisando o usuário sobre dados carregados em modo offline.

---

#### 🔹 [PBI-15] Documentação Técnica Completa (README.md) e Vídeo Demonstrativo do App
* **Work Item Type:** `Product Backlog Item`
* **Parent Feature:** `[FEATURE 04] Engajamento Cidadão, Votação Comunitária e Documentação/Entrega`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `2`
* **Tags:** `Mobile, Documentation, Video, FIAP`

##### Descrição (História de Usuário)
> **Como** banca examinadora e professores avaliadores da FIAP,  
> **Eu quero** acessar um README.md minucioso com guia de instalação e assistir a um vídeo narrado de até 5 minutos no YouTube,  
> **Para que** seja comprovado o atendimento rigoroso aos 7 critérios avaliativos da Global Solution.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [ ] `README.md` no repositório mobile com stack, diagrama arquitetural, tabela de telas, guia de build e credenciais de teste.
- [ ] Roteiro e gravação de vídeo narrado no YouTube demonstrando autenticação, 7+ telas, GPS, foto e CRUD.
- [ ] Arquivo de texto formatado conforme o padrão oficial de submissão do portal da FIAP.
