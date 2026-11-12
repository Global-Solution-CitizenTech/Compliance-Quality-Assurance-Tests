# 📱 Backlog Master Azure Boards — Global Solution 2026/2: Mobile Application Development

> **Projeto Integrado:** ZelaFix — Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  
> **Disciplina:** Mobile Application Development (FIAP — 2TDSPG)  
> **Epic Principal:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa` (AB#1)  
> **Responsável / Owner:** Luna de Carvalho Guimarães (`RM562290@fiap.com.br`)  
> **Start Date:** `2026-11-04`  
> **Target Date:** `2026-11-19`  
> **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`  
> **Padrão:** Azure Boards (Scrum Process: Epic ➔ Feature ➔ PBI)  
> **Tags:** `Mobile` — todos os Work Items da disciplina utilizam exclusivamente esta tag.  
> **Diretrizes Estratégicas:** Aplicativo móvel completo desenvolvido em React Native com Expo SDK 58 e TypeScript, contemplando autenticação JWT com sessão persistente no SecureStore, rotas protegidas, 11 telas funcionais, integração HTTP com a API Java Spring Boot via Axios, cache reativo com TanStack Query v5, formulários validados com Zod v4, geolocalização GPS, evidências fotográficas em Base64, apoio comunitário otimista, controle RBAC e assistente conversacional ZelaBot IA com RAG normativo.

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
[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa [AB#1]
│
├── 🏆 [FEATURE 01] Arquitetura UI, Design System e Navegação por Abas [AB#2]
│   ├── 📄 [PBI-01] Setup Inicial do Projeto Expo com TypeScript, ESLint v9 e Configuração EAS (3 pts) [AB#3]
│   ├── 📄 [PBI-02] Design System CitizenTech, Temas Claro/Escuro e Tipagens Alinhadas à API Java (2 pts) [AB#4]
│   ├── 📄 [PBI-03] Biblioteca de Componentes Reutilizáveis de UI e Modais Acessíveis (3 pts) [AB#106]
│   ├── 📄 [PBI-04] Estrutura de Navegação Nativa com React Navigation e Rotas Tipadas (2 pts) [AB#107]
│   ├── 📄 [PBI-05] Telas Principais do Cidadão (Welcome, Home, Radar do Bairro e Sobre o App) (3 pts) [AB#108]
│   └── 📄 [PBI-06] Tela de Perfil do Cidadão, Edição Cadastral Alinhada ao Java e SafeAreaView (2 pts) [AB#109]
│
├── 🏆 [FEATURE 02] Autenticação JWT Segura, Validação Zod e Proteção de Rotas Privadas [AB#5]
│   ├── 📄 [PBI-07] Cliente HTTP Axios, Interceptor JWT, Warmup Azure e Normalização RFC 7807 (3 pts) [AB#6]
│   ├── 📄 [PBI-08] Camada de Autenticação, AuthContext Unificado e Persistência no SecureStore (3 pts) [AB#7]
│   └── 📄 [PBI-09] Telas Welcome, Login e Cadastro com useZodForm e Proteção de Rotas Privadas (3 pts) [AB#110]
│
├── 🏆 [FEATURE 03] CRUD Completo de Chamados, TanStack Query v5 e Sensores Nativos [AB#8]
│   ├── 📄 [PBI-10] Formulário de Ocorrência (useChamadoForm) com GPS e Reverse Geocoding (3 pts) [AB#9]
│   ├── 📄 [PBI-11] Anexo de Evidências Fotográficas Base64 e Otimização de Imagens (3 pts) [AB#10]
│   └── 📄 [PBI-12] Feed Paginado, Filtros Server-Side e Gestão CRUD com TanStack Query v5 (3 pts) [AB#111]
│
├── 🏆 [FEATURE 04] Engajamento Cidadão, Votação Otimista, Lifecycle Nativo e Entrega [AB#11]
│   ├── 📄 [PBI-13] Detalhes do Chamado, Timeline 6 Estados, Triagem IA e Apoio Otimista (3 pts) [AB#12]
│   ├── 📄 [PBI-14] Lifecycle Nativo TanStack Query (AppState/expo-network) e Auditoria Dinâmica de Build (2 pts) [AB#112]
│   └── 📄 [PBI-15] Documentação Técnica Completa (README.md), Submissão e Vídeo Demonstrativo (2 pts) [AB#13]
│
└── 🏆 [FEATURE 05] Assistente Conversacional ZelaBot IA, RAG Normativo e Insights por Bairro [AB#180]
    ├── 📄 [PBI-16] Camada de Serviço FastAPI (aiService.ts), Tipos de IA e Aquecimento Render (3 pts) [AB#181]
    ├── 📄 [PBI-17] Hook useZelaBot com Histórico de Sessões, Insights por Bairro e Deleção Otimista (3 pts) [AB#182]
    └── 📄 [PBI-18] Interface Conversacional ZelaBotScreen Integrada à Home, Perfil e Detalhes do Chamado (3 pts) [AB#183]
```

---

## 📊 2. Tabela Resumo do Backlog

| Feature Pai | ID do PBI | Título do Item de Backlog (PBI) | Story Points | Prioridade | ID Azure Boards |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **[FEATURE 01] UI & Navegação** | **PBI-01** | Setup Inicial do Projeto Expo com TypeScript, ESLint v9 e Configuração EAS | 3 pts | 1 - Critical | **#3** |
| | **PBI-02** | Design System CitizenTech, Temas Claro/Escuro e Tipagens Alinhadas à API Java | 2 pts | 1 - Critical | **#4** |
| | **PBI-03** | Biblioteca de Componentes Reutilizáveis de UI e Modais Acessíveis | 3 pts | 1 - Critical | **#106** |
| | **PBI-04** | Estrutura de Navegação Nativa com React Navigation e Rotas Tipadas | 2 pts | 1 - Critical | **#107** |
| | **PBI-05** | Telas Principais do Cidadão (Welcome, Home, Radar do Bairro e Sobre o App) | 3 pts | 1 - Critical | **#108** |
| | **PBI-06** | Tela de Perfil do Cidadão, Edição Cadastral Alinhada ao Java e SafeAreaView | 2 pts | 1 - Critical | **#109** |
| **[FEATURE 02] Auth & Sessão** | **PBI-07** | Cliente HTTP Axios, Interceptor JWT, Warmup Azure e Normalização RFC 7807 | 3 pts | 1 - Critical | **#6** |
| | **PBI-08** | Camada de Autenticação, AuthContext Unificado e Persistência no SecureStore | 3 pts | 1 - Critical | **#7** |
| | **PBI-09** | Telas Welcome, Login e Cadastro com useZodForm e Proteção de Rotas Privadas | 3 pts | 1 - Critical | **#110** |
| **[FEATURE 03] CRUD & Sensores** | **PBI-10** | Formulário de Ocorrência (useChamadoForm) com GPS e Reverse Geocoding | 3 pts | 1 - Critical | **#9** |
| | **PBI-11** | Anexo de Evidências Fotográficas Base64 e Otimização de Imagens | 3 pts | 1 - Critical | **#10** |
| | **PBI-12** | Feed Paginado, Filtros Server-Side e Gestão CRUD com TanStack Query v5 | 3 pts | 1 - Critical | **#111** |
| **[FEATURE 04] Voto & Entrega** | **PBI-13** | Detalhes do Chamado, Timeline 6 Estados, Triagem IA e Apoio Otimista | 3 pts | 1 - Critical | **#12** |
| | **PBI-14** | Lifecycle Nativo TanStack Query (AppState/expo-network) e Auditoria Dinâmica de Build | 2 pts | 2 - High | **#112** |
| | **PBI-15** | Documentação Técnica Completa (README.md), Submissão e Vídeo Demonstrativo | 2 pts | 1 - Critical | **#13** |
| **[FEATURE 05] ZelaBot & IA** | **PBI-16** | Camada de Serviço FastAPI (aiService.ts), Tipos de IA e Aquecimento Render | 3 pts | 1 - Critical | **#181** |
| | **PBI-17** | Hook useZelaBot com Histórico de Sessões, Insights por Bairro e Deleção Otimista | 3 pts | 1 - Critical | **#182** |
| | **PBI-18** | Interface Conversacional ZelaBotScreen Integrada à Home, Perfil e Detalhes do Chamado | 3 pts | 1 - Critical | **#183** |
| **TOTAL CONSOLIDADO** | **5 Features** | **18 Product Backlog Items (PBIs)** | **49 pts** | — | — |

> **Observação:** o esforço é controlado por Story Points no Azure Boards. A coluna de horas estimadas foi substituída pela rastreabilidade direta dos IDs reais dos Work Items, evitando divergência entre o documento e o board.

---

## 📦 3. Detalhamento dos Itens de Trabalho

---

### 🏛️ ÉPICO
* **Work Item Type:** `Epic`
* **Azure Boards ID:** `#1`
* **Title:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa`
* **Tags:** `Mobile`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `49`
* **Business Value:** `100`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Description:** Desenvolvimento do aplicativo móvel multiplataforma em React Native (Expo SDK 58) e TypeScript, alinhado à ODS 11, integrado 100% aos contratos da API RESTful Java Spring Boot em Azure e ao microsserviço FastAPI ZelaBot IA no Render. Contempla autenticação JWT segura com `expo-secure-store`, formulários reativos tipados com Zod, cache reativo via TanStack Query v5 com lifecycle nativo (`AppState` + `expo-network`), geolocalização GPS com geocodificação reversa, evidências fotográficas em Base64, apoio comunitário otimista, controle RBAC (Cidadão/Gestor/Admin), auditoria automática de commit Git em tempo de build e assistente conversacional ZelaBot IA com RAG normativo.
* **Acceptance Criteria:**
  - [x] Aplicativo em React Native + Expo SDK 58 + TypeScript estrito (zero `any`, ESLint v9 e `tsc` passando sem erros).
  - [x] Mínimo de 11 telas funcionais organizadas por stacks/tabs com Dark Mode e Light Mode adaptativos via `AppTheme`.
  - [x] Integração 100% alinhada aos DTOs e rotas da API Java em Azure e ZelaBot IA no Render.
  - [x] Build Android verificado via Expo export e `eas.json` configurado para geração de APK.

---

### 🏆 [FEATURE 01] Arquitetura UI, Design System e Navegação por Abas
* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#2`
* **Parent:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa` (#1)
* **Title:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas`
* **Tags:** `Mobile`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-08`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `15`
* **Business Value:** `100`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Description:** Estruturação modular de interface, Design System CitizenTech com temas Claro/Escuro dinâmicos (`AppTheme`), componentes atômicos padronizados sem arquivos barrel mortos, navegação nativa tipada e telas do cidadão com proteção de `SafeAreaView`.
* **Acceptance Criteria:**
  - [x] Navegação oficial `@react-navigation/native-stack` e `@react-navigation/bottom-tabs` com rotas tipadas em `navigation/types.ts`.
  - [x] Remoção completa de arquivos barrel (`components/index.ts`, `types/index.ts`) e padronização de imports em linha única.
  - [x] Design System Light/Dark em `ThemeContext.tsx` com `semanticConfig.ts` e tokens tipados.
  - [x] Proteção de layout com `SafeAreaView` e `KeyboardAvoidingView` em todas as telas.

#### 🔹 [PBI-01] Setup Inicial do Projeto Expo com TypeScript, ESLint v9 e Configuração EAS
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#3`
* **Parent Feature:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas` (#2)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`

##### Descrição (História de Usuário)
> **Como** equipe de engenharia mobile,  
> **Eu quero** inicializar o projeto com Expo SDK 58, TypeScript estrito, ESLint v9 Flat Config, EAS Build e scripts de verificação automatizados,  
> **Para que** tenhamos uma base padronizada pronta para desenvolvimento contínuo e geração de APK em produção.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Expo SDK 58, TypeScript estrito, `package.json` com scripts `type-check` e `lint`.
- [x] Configuração limpa em `eslint.config.js`, `tsconfig.json` e `eas.json` para builds Android preview/production.
- [x] Estrutura modular em `components/`, `config/`, `contexts/`, `hooks/`, `lib/`, `navigation/`, `screens/`, `services/`, `theme/`, `types/` e `utils/`.
- [x] Compilação `tsc --noEmit` e `eslint .` passando com zero erros e zero warnings.

---

#### 🔹 [PBI-02] Design System CitizenTech, Temas Claro/Escuro e Tipagens Alinhadas à API Java
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#4`
* **Parent Feature:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas` (#2)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `2`
* **Tags:** `Mobile`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`

##### Descrição (História de Usuário)
> **Como** arquiteto mobile,  
> **Eu quero** centralizar tokens semânticos de design Light/Dark e espelhar 1:1 os contratos DTO e `PageModel` da API Java,  
> **Para que** o aplicativo compartilhe identidade visual consistente e nunca sofra divergências de contrato JSON.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `ThemeContext.tsx` provendo `AppTheme` completo para Light/Dark mode persistido e hook `useThemedStyles`.
- [x] Escalas e configurações em `colors.ts`, `spacing.ts`, `typography.ts` e `semanticConfig.ts` com 6 estados de chamado (`PENDENTE`, `ABERTO`, `EM_ANALISE`, `EM_EXECUCAO`, `CONCLUIDO`, `REJEITADO`).
- [x] Tipos granulares em `api.ts`, `auth.ts`, `categoria.ts`, `chamado.ts` e `ai.ts` sem barrel morto e sem uso de `any`.

---

#### 🔹 [PBI-03] Biblioteca de Componentes Reutilizáveis de UI e Modais Acessíveis
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#106`
* **Parent Feature:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas` (#2)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`

##### Descrição (História de Usuário)
> **Como** cidadão utilizando o app,  
> **Eu quero** interagir com botões responsivos, campos padronizados, cards de ocorrência e modais consistentes,  
> **Para que** a experiência seja fluida, acessível e livre de duplicação de código visual.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `BaseModal/index.tsx` centralizando overlay, rolagem responsiva e `KeyboardAvoidingView` para `FeedbackModal`, `StatusChangeModal`, `EditProfileModal` e `ZelaBotHistoryModal`.
- [x] Componentes modulares: `Button`, `Input`, `Header`, `StatCard`, `EmptyState`, `LoadingSpinner`, `CategoryBadge` e `StatusBadge`.
- [x] `ChamadoCard` e `ChamadoFormFields` compartilhando campos de formulário entre criação e edição sem duplicação.
- [x] Imports diretos nos módulos reais sem barrel `src/components/index.ts`.

---

#### 🔹 [PBI-04] Estrutura de Navegação Nativa com React Navigation e Rotas Tipadas
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#107`
* **Parent Feature:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas` (#2)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `2`
* **Tags:** `Mobile`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`

##### Descrição (História de Usuário)
> **Como** munícipe que navega pelo ZelaFix,  
> **Eu quero** alternar entre abas principais e navegar para fluxos detalhados, edição e assistente IA via stacks nativos,  
> **Para que** a transição entre telas seja rápida e validada em tempo de compilação.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Rotas estritamente tipadas em `navigation/types.ts` incluindo `ZelaBot` (`{ chamadoId?: number }`), `ChamadoDetails` (`{ id: number }`) e `EditarChamado` (`{ id: number }`).
- [x] `TabNavigator` com ícones vetoriais e respeito às `SafeAreaInsets` para Home, Radar, Novo, Meus Chamados e Perfil.
- [x] `AuthNavigator` (Welcome, Login, Register) e `AppNavigator` orquestrados reativamente pelo `NavigationContainer` conectado ao `AppTheme`.

---

#### 🔹 [PBI-05] Telas Principais do Cidadão (Welcome, Home, Radar do Bairro e Sobre o App)
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#108`
* **Parent Feature:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas` (#2)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`

##### Descrição (História de Usuário)
> **Como** munícipe e avaliador acadêmico,  
> **Eu quero** explorar o panorama de zeladoria na Home, consultar demandas no Radar e verificar dados do projeto na tela Sobre,  
> **Para que** o acompanhamento urbano seja transparente e intuitivo desde o primeiro acesso.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `HomeScreen` com `HomePanoramaCard`, `HomeCategoryList` e atalho contextual para o ZelaBot IA via hook `useHomeData`.
- [x] `RadarBairroScreen` com `FilterChipRow` e `RadarHeaderFilters` integrados ao `useRadarData` (filtros de status, categoria, busca textual e fila de triagem do gestor).
- [x] `SobreAppScreen` e `TeamMembersCard` exibindo ODS 11, versão e commit hash dinâmico de auditoria.

---

#### 🔹 [PBI-06] Tela de Perfil do Cidadão, Edição Cadastral Alinhada ao Java e SafeAreaView
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#109`
* **Parent Feature:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas` (#2)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `2`
* **Tags:** `Mobile`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`

##### Descrição (História de Usuário)
> **Como** munícipe cadastrado,  
> **Eu quero** visualizar meu perfil, cargo RBAC, tema do app e atualizar meus dados cadastrais e endereço,  
> **Para que** minhas informações estejam atualizadas no backend Java sem sobreposições de tela.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `ProfileScreen` e `ProfileUserCard` consumindo dados via `useProfileData`.
- [x] `EditProfileModal` validado com `ProfileEditSchema` (Zod) compatível com `UsuarioRequest` e `EnderecoRequest` da API Java.
- [x] Alternância de tema Light/Dark, atalho para ZelaBot IA e logout seguro encerrando sessão e limpando `QueryClient`.

---

### 🏆 [FEATURE 02] Autenticação JWT Segura, Validação Zod e Proteção de Rotas Privadas
* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#5`
* **Parent:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa` (#1)
* **Title:** `[FEATURE 02] Autenticação JWT Segura, Validação Zod e Proteção de Rotas Privadas`
* **Tags:** `Mobile`
* **Start Date:** `2026-11-07`
* **Target Date:** `2026-11-12`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Description:** Sistema completo de login, cadastro com endereço e telefone DDD válido, renovação de token via header `x-novo-token`, persistência criptografada em `expo-secure-store`, hooks `useZodForm` e guarda declarativa de rotas privadas.
* **Acceptance Criteria:**
  - [x] Login, Cadastro e edição de perfil integrados aos endpoints Spring Security da API Java no Azure.
  - [x] Persistência criptografada do token JWT no SecureStore (Android/iOS) com fallback Web no `storageService.ts`.
  - [x] Validação declarativa com Zod v4 via `useZodForm` garantindo 100% de paridade com Bean Validation e `DddValidation` do Java.
  - [x] Rotas privadas protegidas via `AuthContext` e `useAuth` unificado.

#### 🔹 [PBI-07] Cliente HTTP Axios, Interceptor JWT, Warmup Azure e Normalização RFC 7807
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#6`
* **Parent Feature:** `[FEATURE 02] Autenticação JWT Segura, Validação Zod e Proteção de Rotas Privadas` (#5)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`

##### Descrição (História de Usuário)
> **Como** arquiteto de software mobile,  
> **Eu quero** centralizar o cliente HTTP Axios com injeção automática de Bearer Token, warmup de cold start no Azure e tratamento padronizado de erros `ProblemDetail`,  
> **Para que** todas as chamadas à API Java sejam resilientes, autenticadas e exibam mensagens de erro claras.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Instância Axios em `api.ts` apontando para `env.apiUrl` (Azure App Service) sem arquivos `.env` soltos.
- [x] Interceptor injetando `Authorization: Bearer` e callback automático para HTTP 401.
- [x] `authService.ts` capturando header `x-novo-token` após atualização cadastral de usuário.
- [x] Warmup throttled compartilhado (`createThrottledPing`) em `/actuator/health` e normalização de erros em `utils/apiError.ts`.

---

#### 🔹 [PBI-08] Camada de Autenticação, AuthContext Unificado e Persistência no SecureStore
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#7`
* **Parent Feature:** `[FEATURE 02] Autenticação JWT Segura, Validação Zod e Proteção de Rotas Privadas` (#5)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`

##### Descrição (História de Usuário)
> **Como** cidadão que utiliza o ZelaFix,  
> **Eu quero** manter minha sessão JWT armazenada com segurança nativa ao reabrir o app e sincronizada com o cache de dados,  
> **Para que** eu não precise fazer login a cada abertura sem comprometer meus dados sensíveis.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `AuthContext.tsx` expondo `AuthProvider` e hook `useAuth` diretamente (removendo arquivo morto `hooks/useAuth.ts`).
- [x] Armazenamento do JWT via `expo-secure-store` e sessão/tema via `storageService.ts`.
- [x] Hidratação inicial de sessão (`/usuarios/me`), atualização de usuário autenticado e limpeza automática de `QueryClient` no logout.

---

#### 🔹 [PBI-09] Telas Welcome, Login e Cadastro com useZodForm e Proteção de Rotas Privadas
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#110`
* **Parent Feature:** `[FEATURE 02] Autenticação JWT Segura, Validação Zod e Proteção de Rotas Privadas` (#5)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`

##### Descrição (História de Usuário)
> **Como** novo munícipe,  
> **Eu quero** realizar cadastro completo validado em tempo real e autenticar com segurança no ZelaFix,  
> **Para que** eu acesse exclusivamente o painel autenticado após validar minhas credenciais.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Hook genérico memoizado `useZodForm` (zero `any`) conectado a `LoginSchema` e `RegisterSchema` (`DDDS_VALIDOS` e tamanhos exatos da API Java).
- [x] Hooks `useLoginForm` e `useRegisterForm` com feedback visual e preenchimento rápido para avaliação.
- [x] `LoginScreen` (`LoginForm`), `RegisterScreen` (`RegisterForm`) e `WelcomeScreen` com proteção de rotas em `navigation/index.tsx`.

---

### 🏆 [FEATURE 03] CRUD Completo de Chamados, TanStack Query v5 e Sensores Nativos
* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#8`
* **Parent:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa` (#1)
* **Title:** `[FEATURE 03] CRUD Completo de Chamados, TanStack Query v5 e Sensores Nativos`
* **Tags:** `Mobile`
* **Start Date:** `2026-11-09`
* **Target Date:** `2026-11-15`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Description:** Gerenciamento completo de ocorrências urbanas utilizando TanStack Query v5 com query keys tipadas, filtros server-side paginados (`PagedModel`), captura real de coordenadas GPS e reverse geocoding via `expo-location`, além de evidências fotográficas em Base64 via `expo-image-picker`.
* **Acceptance Criteria:**
  - [x] CRUD completo (POST, GET paginado, PUT, DELETE com RBAC ADMIN) integrado à API Java.
  - [x] Hooks `useChamados`, `useChamadoForm`, `useMeusChamadosData` e `useRadarData` usando `queryKeys.ts` e filtros server-side.
  - [x] Captura automática de CEP, logradouro e número via `expo-location` (`useLocalizacao.ts`), com bairro/cidade usados como contexto visual da localização.
  - [x] Captura e otimização de fotos via câmera/galeria em `PhotoEvidencePicker.tsx` com conversão limpa de Base64.

#### 🔹 [PBI-10] Formulário de Ocorrência (useChamadoForm) com GPS e Reverse Geocoding
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#9`
* **Parent Feature:** `[FEATURE 03] CRUD Completo de Chamados, TanStack Query v5 e Sensores Nativos` (#8)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`

##### Descrição (História de Usuário)
> **Como** munícipe que identifica um problema urbano,  
> **Eu quero** preencher automaticamente meu endereço e CEP a partir do sensor GPS do aparelho ao abrir um chamado,  
> **Para que** a prefeitura localize com precisão o local da ocorrência sem erros manuais.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `NovoChamadoScreen` integrado ao hook `useLocalizacao` (`expo-location`) e tratamento amigável de permissão negada.
- [x] Preenchimento automático de CEP, logradouro e número compatíveis com `EnderecoRequest` da API Java; bairro e cidade são exibidos como contexto da localização capturada.
- [x] Hook unificado `useChamadoForm` validando formulário via `ChamadoFormSchema` (Zod) em conjunto com `CategoryGridSelector` e `ChamadoFormFields`.

---

#### 🔹 [PBI-11] Anexo de Evidências Fotográficas Base64 e Otimização de Imagens
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#10`
* **Parent Feature:** `[FEATURE 03] CRUD Completo de Chamados, TanStack Query v5 e Sensores Nativos` (#8)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`

##### Descrição (História de Usuário)
> **Como** cidadão que registra uma demanda,  
> **Eu quero** tirar uma foto na hora ou selecionar uma imagem da galeria com preview e compressão automática,  
> **Para que** o backend Java e a triagem multimodal por IA recebam a evidência leve e padronizada.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `PhotoEvidencePicker.tsx` integrado ao `expo-image-picker` (câmera e galeria) com preview e remoção.
- [x] Conversão e limpeza de prefixo data URI via `stripDataUriPrefix` em `utils/chamadoMappers.ts` conforme esperado pela API Java.
- [x] Compressão otimizada para evitar payloads excessivos no transporte HTTP Base64.

---

#### 🔹 [PBI-12] Feed Paginado, Filtros Server-Side e Gestão CRUD com TanStack Query v5
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#111`
* **Parent Feature:** `[FEATURE 03] CRUD Completo de Chamados, TanStack Query v5 e Sensores Nativos` (#8)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`

##### Descrição (História de Usuário)
> **Como** cidadão ativo no ZelaFix,  
> **Eu quero** consultar ocorrências do bairro paginadas, filtrar por status/categoria/busca, editar meus chamados e excluir itens autorizados,  
> **Para que** a lista esteja sempre sincronizada com a API Java e sem recarregamentos redundantes.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `chamadoService.ts` consumindo `PagedModel { content, page }` com parâmetros server-side `status`, `categoria`, `busca` e `apenasMeus`.
- [x] `MeusChamadosScreen` (`useMeusChamadosData`) e `EditarChamadoScreen` compartilhando `useChamadoForm` e `ChamadoFormFields`.
- [x] Controle de permissões em `utils/permissions.ts`: `canDeleteChamado` restrito a ADMIN e gestão de edição/status validada.

---

### 🏆 [FEATURE 04] Engajamento Cidadão, Votação Otimista, Lifecycle Nativo e Entrega
* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#11`
* **Parent:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa` (#1)
* **Title:** `[FEATURE 04] Engajamento Cidadão, Votação Otimista, Lifecycle Nativo e Entrega`
* **Tags:** `Mobile`
* **Start Date:** `2026-11-11`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `7`
* **Business Value:** `100`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Description:** Acompanhamento completo de ocorrências com timeline de 6 estados, exibição de parecer de triagem IA, botão de apoio comunitário com atualização otimista em cache, lifecycle nativo React Native no TanStack Query e auditoria técnica da entrega FIAP.
* **Acceptance Criteria:**
  - [x] `ChamadoDetailsScreen` exibindo foto, localização, timeline de 6 estados e parecer estruturado da triagem por IA.
  - [x] Apoio comunitário otimista em `useChamadoMutations` via `POST /chamados/{id}/apoiar` com rollback em erro.
  - [x] Integração de `AppState` + `expo-network` no `QueryClient` para refetch e pausas conscientes de bateria.
  - [x] Rastreabilidade de versão/commit dinâmico e documentação técnica completa.

#### 🔹 [PBI-13] Detalhes do Chamado, Timeline 6 Estados, Triagem IA e Apoio Otimista
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#12`
* **Parent Feature:** `[FEATURE 04] Engajamento Cidadão, Votação Otimista, Lifecycle Nativo e Entrega` (#11)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`

##### Descrição (História de Usuário)
> **Como** morador afetado por uma demanda no bairro,  
> **Eu quero** abrir o detalhe de um chamado, ver a triagem da IA e apoiá-lo com resposta instantânea na interface,  
> **Para que** demandas coletivas ganhem prioridade sem duplicação de registros.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `ChamadoDetailsScreen` modularizada em `ChamadoSummaryCard`, `ChamadoIaTriageCard` (`parseTriagemIa` / `getLatestParecer`), `ChamadoLocationCard`, `ChamadoTimelineCard` e `ChamadoActionBar`.
- [x] Suporte completo aos 6 estados do Java (`PENDENTE`, `ABERTO`, `EM_ANALISE`, `EM_EXECUCAO`, `CONCLUIDO`, `REJEITADO`) e modal RBAC `StatusChangeModal` para GESTOR/ADMIN.
- [x] Botão de apoio com `useMutation` otimista em `useChamadoMutations.ts` chamando `POST /chamados/{id}/apoiar`.

---

#### 🔹 [PBI-14] Lifecycle Nativo TanStack Query (AppState/expo-network) e Auditoria Dinâmica de Build
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#112`
* **Parent Feature:** `[FEATURE 04] Engajamento Cidadão, Votação Otimista, Lifecycle Nativo e Entrega` (#11)
* **Priority:** `2 - High`
* **Effort (Story Points):** `2`
* **Tags:** `Mobile`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`

##### Descrição (História de Usuário)
> **Como** usuário e avaliador técnico,  
> **Eu quero** que o cache sincronize automaticamente ao retomar conexão ou foco e que o build registre commit Git e URLs de produção,  
> **Para que** o app seja resiliente a oscilações de rede e 100% auditável na avaliação da FIAP.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `bindReactNativeQueryLifecycle` em `lib/queryClient.ts` conectando `AppState` (`focusManager`) e `expo-network` (`onlineManager`).
- [x] `app.config.js` + `config/version.ts` injetando hash completo/curto do commit Git e branch via `expo-constants` em tempo de build.
- [x] URLs centrais de produção Azure (`apiUrl`) e Render (`aiUrl`) configuradas em `src/config/env.ts` com `eas.json` para preview APK.

---

#### 🔹 [PBI-15] Documentação Técnica Completa (README.md), Submissão e Vídeo Demonstrativo
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#13`
* **Parent Feature:** `[FEATURE 04] Engajamento Cidadão, Votação Otimista, Lifecycle Nativo e Entrega` (#11)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `2`
* **Tags:** `Mobile`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`

##### Descrição (História de Usuário)
> **Como** banca examinadora e professores da FIAP,  
> **Eu quero** consultar documentação técnica detalhada, roteiro de entrega oficial e demonstração em vídeo do aplicativo,  
> **Para que** seja comprovado o atendimento rigoroso a todos os critérios da Global Solution 2026/2.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `README.md` e `ENTREGA_GS_2026_2.txt` documentando stack, arquitetura e instruções de execução.
- [x] Tela `SobreAppScreen` exibindo versão, commit hash dinâmico e equipe em ordem alfabética estrita.
- [x] Roteiro e vídeo demonstrativo cobrindo autenticação, telas principais, sensores GPS/câmera, CRUD, RBAC e ZelaBot IA.

---

### 🏆 [FEATURE 05] Assistente Conversacional ZelaBot IA, RAG Normativo e Insights por Bairro
* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#180`
* **Parent:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa` (#1)
* **Title:** `[FEATURE 05] Assistente Conversacional ZelaBot IA, RAG Normativo e Insights por Bairro`
* **Tags:** `Mobile`
* **Start Date:** `2026-11-11`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Description:** Implementação completa do assistente inteligente ZelaBot IA integrado ao microsserviço Python FastAPI (`deploy_zelafixai_render` em `env.aiUrl`), contemplando warmup throttled em `/health`, chat com RAG normativo em `/ai/chat`, contexto automático por chamado (`chamadoId`), insights preditivos por bairro em `/ai/insights` e gestão completa de sessões e histórico em `/ai/sessions` e `/ai/history`.
* **Acceptance Criteria:**
  - [x] Serviço `aiService.ts` alinhado 100% aos contratos Pydantic do FastAPI no Render.
  - [x] Hook `useZelaBot` gerenciando mensagens, sessões, histórico, insights e deleção otimista.
  - [x] `ZelaBotScreen` modularizada com renderização de fontes RAG, alertas de bairro e modal de histórico.
  - [x] Atalhos integrados na `HomeScreen`, `ProfileScreen` e `ChamadoDetailsScreen`.

#### 🔹 [PBI-16] Camada de Serviço FastAPI (aiService.ts), Tipos de IA e Aquecimento Render
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#181`
* **Parent Feature:** `[FEATURE 05] Assistente Conversacional ZelaBot IA, RAG Normativo e Insights por Bairro` (#180)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`

##### Descrição (História de Usuário)
> **Como** desenvolvedor mobile e integrador de IA,  
> **Eu quero** consumir o microsserviço FastAPI no Render com contratos tipados e pré-aquecimento throttled no endpoint `/health`,  
> **Para que** as respostas do chat RAG e dos insights por bairro sejam rápidas e resilientes a cold starts.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Tipagens em `src/types/ai.ts` espelhando `ChatRequest`, `ChatResponse`, `AiMessage`, `AiChatSession` e `AiInsightItem` do FastAPI.
- [x] `aiService.ts` reutilizando `createThrottledPing` para aquecer `/health` de `env.aiUrl`.
- [x] Chamadas aos endpoints `/ai/chat`, `/ai/insights`, `/ai/sessions`, `/ai/history` e `DELETE /ai/sessions/{session_id}` com injeção de Bearer JWT.

---

#### 🔹 [PBI-17] Hook useZelaBot com Histórico de Sessões, Insights por Bairro e Deleção Otimista
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#182`
* **Parent Feature:** `[FEATURE 05] Assistente Conversacional ZelaBot IA, RAG Normativo e Insights por Bairro` (#180)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`

##### Descrição (História de Usuário)
> **Como** cidadão usando o assistente urbano,  
> **Eu quero** alternar entre conversas salvas, receber alertas por bairro e remover sessões antigas com feedback imediato,  
> **Para que** eu obtenha orientações contextualizadas sobre zeladoria e normas municipais sem perder o histórico.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `useZelaBot.ts` unificando envio de mensagens, contexto opcional de `chamadoId` e seleção automática de sessão.
- [x] Carregamento de insights por bairro (`/ai/insights`) e sugestões rápidas adaptadas ao contexto.
- [x] Exclusão otimista de sessões com restauração segura em caso de erro e troca automática para nova conversa.

---

#### 🔹 [PBI-18] Interface Conversacional ZelaBotScreen Integrada à Home, Perfil e Detalhes do Chamado
* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#183`
* **Parent Feature:** `[FEATURE 05] Assistente Conversacional ZelaBot IA, RAG Normativo e Insights por Bairro` (#180)
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Tags:** `Mobile`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`

##### Descrição (História de Usuário)
> **Como** munícipe navegando pelo ZelaFix,  
> **Eu quero** abrir o chat ZelaBot tanto pelo atalho principal quanto diretamente dentro de um chamado específico,  
> **Para que** a IA responda dúvidas sobre leis urbanas, SLA e andamento usando o contexto da ocorrência.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `ZelaBotScreen.tsx` compondo `ZelaBotInsightsBanner`, `ZelaBotMessageBubble`, `ZelaBotInputBar` e `ZelaBotHistoryModal` via `BaseModal`.
- [x] Exibição de fontes/citações RAG retornadas pelo backend IA e estado de carregamento acessível.
- [x] Atalhos de navegação adicionados na `HomeScreen`, `ProfileScreen` e `ChamadoDetailsScreen` (enviando `chamadoId`).
