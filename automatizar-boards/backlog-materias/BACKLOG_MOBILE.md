# 📱 Backlog Master Azure Boards — Global Solution 2026/2: Mobile Application Development

> **Projeto Integrado:** ZelaFix — Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  
> **Disciplina:** Mobile Application Development (FIAP — 2TDSPG)  
> **Repositório GitHub:** [Global-Solution-CitizenTech/Mobile-Application-Development](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development)  
> **APK Android Standalone (EAS Build `8c21e8d0` / `versionCode 14`):** [zelafix.apk](https://expo.dev/artifacts/eas/tAr1dhKfReeHzG0A2MHOEHml5dvbgLnQsfy6LZa33p8.apk)  
> **Organização / Projeto Azure DevOps:** `ZelaFixGS` / `ZelaFix`  
> **Epic Principal:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa` (**AB#1**)  
> **Responsável / Owner:** Luna de Carvalho Guimarães (`RM562290@fiap.com.br`)  
> **Start Date:** `2026-11-04`  
> **Target Date:** `2026-11-19`  
> **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`  
> **Padrão:** Azure Boards (Scrum Process: Epic ➔ Feature ➔ PBI)  
> **Tags:** `Mobile` — todos os Work Items da disciplina utilizam exclusivamente esta tag.  
> **Diretrizes Estratégicas:** Aplicativo móvel multiplataforma em React Native (Expo SDK 58, React 19.3, React Compiler e TypeScript estrito), contemplando autenticação JWT com sessão persistente no `expo-secure-store`, 12 telas (11 fluxos funcionais + Sobre o App), integração HTTP via Axios com a API Java Spring Boot (`https://app-zelafix.azurewebsites.net`) e com o microsserviço ZelaBot IA (`https://disruptive-architectures-iot-iob-ia-mpl5.onrender.com`), cache reativo com TanStack Query v5 (`AppState` + `expo-network`), paginação infinita no Radar do Bairro, formulários validados com Zod v4, GPS via `expo-location`, upload fotográfico `multipart/form-data` com triagem direta por IA (`DeferredResult`), apoio comunitário otimista (`chamadoCache.ts`), RBAC Cidadão/Gestor Público, suíte de 78 testes unitários Node e build Android EAS `versionCode 14`.

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
│   ├── 📄 [PBI-02] Design System CitizenTech, Temas Claro/Escuro, Enums Canônicos e Tipagens Alinhadas à API Java (2 pts) [AB#4]
│   ├── 📄 [PBI-03] Biblioteca de Componentes Reutilizáveis de UI, FeedbackProvider Global e Modais Acessíveis (3 pts) [AB#106]
│   ├── 📄 [PBI-04] Estrutura de Navegação Nativa com React Navigation, Tab Central IA e Rotas Tipadas (2 pts) [AB#107]
│   ├── 📄 [PBI-05] Telas Principais do Cidadão (Welcome, Home, Radar do Bairro e Sobre o App) (3 pts) [AB#108]
│   └── 📄 [PBI-06] Tela de Perfil do Cidadão, Edição Cadastral Alinhada ao Java e SafeAreaView (2 pts) [AB#109]
│
├── 🏆 [FEATURE 02] Autenticação JWT Segura, Validação Zod e Proteção de Rotas Privadas [AB#5]
│   ├── 📄 [PBI-07] Cliente HTTP Axios, Interceptor JWT, Warmup Azure e Normalização RFC 7807 (3 pts) [AB#6]
│   ├── 📄 [PBI-08] Camada de Autenticação, AuthContext Unificado e Persistência no SecureStore (3 pts) [AB#7]
│   └── 📄 [PBI-09] Telas Welcome, Login e Cadastro com useZodForm e Proteção de Rotas Privadas (3 pts) [AB#110]
│
├── 🏆 [FEATURE 03] CRUD Completo de Chamados, TanStack Query v5 e Sensores Nativos [AB#8]
│   ├── 📄 [PBI-10] Formulário de Ocorrência (useChamadoForm) com GPS, Reverse Geocoding e Triagem Direta via DeferredResult (3 pts) [AB#9]
│   ├── 📄 [PBI-11] Anexo de Evidências Fotográficas (Multipart/Form-Data) e Otimização de Imagens (3 pts) [AB#10]
│   └── 📄 [PBI-12] Feed com Paginação Infinita no Radar, Filtros Server-Side e Gestão CRUD com TanStack Query v5 (3 pts) [AB#111]
│
├── 🏆 [FEATURE 04] Engajamento Cidadão, Votação Otimista, Lifecycle Nativo e Entrega [AB#11]
│   ├── 📄 [PBI-13] Detalhes do Chamado, Timeline 5 Estados, Triagem IA, Feedback de Recusa e Apoio Otimista (3 pts) [AB#12]
│   ├── 📄 [PBI-14] Lifecycle Nativo TanStack Query (AppState/expo-network), Testes Unitários e Builds EAS (2 pts) [AB#112]
│   └── 📄 [PBI-15] Documentação Técnica Completa (README.md), Submissão APK (versionCode 14) e Vídeo Demonstrativo (2 pts) [AB#13]
│
└── 🏆 [FEATURE 05] Assistente Conversacional ZelaBot IA, RAG Normativo e Insights por Bairro [AB#180]
    ├── 📄 [PBI-16] Camada de Serviço FastAPI (aiService.ts), Tipos de IA e Aquecimento Render (3 pts) [AB#181]
    ├── 📄 [PBI-17] Hook useZelaBot com Histórico de Sessões, Insights por Bairro e Deleção Otimista (3 pts) [AB#182]
    └── 📄 [PBI-18] Interface Conversacional ZelaBotScreen Integrada à Home, Perfil e Detalhes do Chamado (3 pts) [AB#183]
```

---

## 📊 2. Tabela Resumo do Backlog & Rastreabilidade

| Feature Pai | ID do PBI | Título do Item de Backlog (PBI) | ID Azure Boards | Story Points | Prioridade | Business Value | Commits | Status |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Feature 01** `[AB#2]` | **PBI-01** | Setup Inicial do Projeto Expo com TypeScript, ESLint v9 e Configuração EAS | **#3** | 3 pts | 1 - Critical | 100 | 5 | Committed |
| | **PBI-02** | Design System CitizenTech, Temas Claro/Escuro, Enums Canônicos e Tipagens Alinhadas à API Java | **#4** | 2 pts | 1 - Critical | 100 | 5 | Committed |
| | **PBI-03** | Biblioteca de Componentes Reutilizáveis de UI, FeedbackProvider Global e Modais Acessíveis | **#106** | 3 pts | 1 - Critical | 100 | 3 | Committed |
| | **PBI-04** | Estrutura de Navegação Nativa com React Navigation, Tab Central IA e Rotas Tipadas | **#107** | 2 pts | 1 - Critical | 100 | 2 | Committed |
| | **PBI-05** | Telas Principais do Cidadão (Welcome, Home, Radar do Bairro e Sobre o App) | **#108** | 3 pts | 1 - Critical | 100 | 5 | Committed |
| | **PBI-06** | Tela de Perfil do Cidadão, Edição Cadastral Alinhada ao Java e SafeAreaView | **#109** | 2 pts | 1 - Critical | 100 | 2 | Committed |
| **Feature 02** `[AB#5]` | **PBI-07** | Cliente HTTP Axios, Interceptor JWT, Warmup Azure e Normalização RFC 7807 | **#6** | 3 pts | 1 - Critical | 100 | 3 | Committed |
| | **PBI-08** | Camada de Autenticação, AuthContext Unificado e Persistência no SecureStore | **#7** | 3 pts | 1 - Critical | 100 | 3 | Committed |
| | **PBI-09** | Telas Welcome, Login e Cadastro com useZodForm e Proteção de Rotas Privadas | **#110** | 3 pts | 1 - Critical | 100 | 2 | Committed |
| **Feature 03** `[AB#8]` | **PBI-10** | Formulário de Ocorrência (`useChamadoForm`) com GPS, Reverse Geocoding e Triagem Direta via `DeferredResult` | **#9** | 3 pts | 1 - Critical | 100 | 3 | Committed |
| | **PBI-11** | Anexo de Evidências Fotográficas (Multipart/Form-Data) e Otimização de Imagens | **#10** | 3 pts | 1 - Critical | 100 | 3 | Committed |
| | **PBI-12** | Feed com Paginação Infinita no Radar, Filtros Server-Side e Gestão CRUD com TanStack Query v5 | **#111** | 3 pts | 1 - Critical | 100 | 6 | Committed |
| **Feature 04** `[AB#11]` | **PBI-13** | Detalhes do Chamado, Timeline 5 Estados, Triagem IA, Feedback de Recusa e Apoio Otimista | **#12** | 3 pts | 1 - Critical | 100 | 5 | Committed |
| | **PBI-14** | Lifecycle Nativo TanStack Query (`AppState`/`expo-network`), Testes Unitários e Builds EAS | **#112** | 2 pts | 2 - High | 80 | 11 | Committed |
| | **PBI-15** | Documentação Técnica Completa (`README.md`), Submissão APK (`versionCode 14`) e Vídeo Demonstrativo | **#13** | 2 pts | 1 - Critical | 100 | 13 | Committed |
| **Feature 05** `[AB#180]` | **PBI-16** | Camada de Serviço FastAPI (`aiService.ts`), Tipos de IA e Aquecimento Render | **#181** | 3 pts | 1 - Critical | 100 | 1 | Committed |
| | **PBI-17** | Hook `useZelaBot` com Histórico de Sessões, Insights por Bairro e Deleção Otimista | **#182** | 3 pts | 1 - Critical | 100 | 1 | Committed |
| | **PBI-18** | Interface Conversacional `ZelaBotScreen` Integrada à Home, Perfil e Detalhes do Chamado | **#183** | 3 pts | 1 - Critical | 100 | 1 | Committed |
| **TOTAL CONSOLIDADO** | **5 Features** | **18 PBIs (24 Work Items no Azure Boards)** | **`#1..#13`, `#106..#112`, `#180..#183`** | **49 pts** | — | — | **49 commits únicos** | **100% Sincronizado** |

> **Observação:** o esforço é controlado por Story Points no Azure Boards. A coluna de horas estimadas foi substituída pela rastreabilidade direta dos IDs reais dos Work Items, evitando divergência entre o documento e o board.

---

## 📦 3. Detalhamento dos Itens de Trabalho

---

### 🏛️ ÉPICO

* **Work Item Type:** `Epic`
* **Azure Boards ID:** `#1`
* **Title:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `49`
* **Business Value:** `100`
* **Description:** Desenvolvimento do aplicativo móvel multiplataforma em React Native (Expo SDK 58, React 19.3, React Compiler) e TypeScript estrito, alinhado à ODS 11, integrado 100% aos contratos da API RESTful Java Spring Boot em Azure (`https://app-zelafix.azurewebsites.net`) e ao microsserviço FastAPI ZelaBot IA no Render (`https://disruptive-architectures-iot-iob-ia-mpl5.onrender.com`). Contempla autenticação JWT segura com `expo-secure-store`, formulários reativos tipados com Zod v4, cache reativo via TanStack Query v5 com paginação infinita no Radar e lifecycle nativo (`AppState` + `expo-network`), geolocalização GPS com geocodificação reversa (`expo-location`), envio fotográfico `multipart/form-data` com triagem automática direta pela Spring AI (`DeferredResult`), apoio comunitário otimista (`chamadoCache.ts`), controle RBAC (Cidadão/Gestor Público), suíte de 78 testes unitários Node, auditoria automática de commit Git em tempo de build, assistente conversacional ZelaBot IA com RAG normativo e APK standalone publicado via EAS Build (`versionCode 14`).
* **Acceptance Criteria:**
  - [x] Aplicativo em React Native + Expo SDK 58 + React Compiler + TypeScript estrito (zero `any`, ESLint v9, `type-check` e 78 testes unitários passando).
  - [x] 12 telas (11 fluxos funcionais + Sobre o App) organizadas por stacks/tabs com Dark Mode e Light Mode adaptativos via `AppTheme`.
  - [x] Integração 100% alinhada aos DTOs e rotas da API Java em Azure (`multipart/form-data` + `DeferredResult` + `Page<T>`) e ZelaBot IA no Render.
  - [x] Build Android compilado e publicado via EAS Build (`versionCode 14`, build `8c21e8d0`) com link direto de download do APK.

---

### 🏆 [FEATURE 01] Arquitetura UI, Design System e Navegação por Abas

* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#2`
* **Parent:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa` (`#1`)
* **Title:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Start Date:** `2026-11-04`
* **Target Date:** `2026-11-14`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `15`
* **Business Value:** `100`
* **Description:** Estruturação modular de interface, Design System CitizenTech com temas Claro/Escuro dinâmicos (`AppTheme`) e identidade visual renovada (ícone/splash/logo-mark em verde esmeralda), componentes atômicos padronizados (incluindo `FeedbackProvider`, `SelectPickerModal`, `AuthHeader` e `ChamadoListSeparator`) sem arquivos barrel mortos, navegação nativa tipada com aba central para ZelaBot IA e telas do cidadão com proteção de `SafeAreaView`.
* **Acceptance Criteria:**
  - [x] Navegação oficial `@react-navigation/native-stack` e `@react-navigation/bottom-tabs` com rotas tipadas em `navigation/types.ts` e botão central para ZelaBot IA.
  - [x] Remoção completa de arquivos barrel (`components/index.ts`, `types/index.ts`) e padronização de imports em linha única.
  - [x] Design System Light/Dark em `ThemeContext.tsx` com `semanticConfig.ts` (5 estados, 6 categorias canônicas e `ORGAO_LABELS`) e tokens tipados.
  - [x] Proteção de layout com `SafeAreaView` e `KeyboardAvoidingView` em todas as telas, além de `FeedbackProvider` global.

#### 🔹 [PBI-01] Setup Inicial do Projeto Expo com TypeScript, ESLint v9 e Configuração EAS

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#3`
* **Parent Feature:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas` (`#2`)
* **Title:** `[PBI-01] Setup Inicial do Projeto Expo com TypeScript, ESLint v9 e Configuração EAS`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** equipe de engenharia mobile,  
> **Eu quero** inicializar o projeto com Expo SDK 58, TypeScript estrito, ESLint v9 Flat Config, EAS Build e scripts de verificação automatizados,  
> **Para que** tenhamos uma base padronizada pronta para desenvolvimento contínuo e geração de APK em produção.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Expo SDK 58, TypeScript estrito, `package.json` com scripts `type-check`, `lint` e `test`.
- [x] Configuração limpa em `eslint.config.js`, `tsconfig.json`, `tsconfig.test.json` e `eas.json` para builds Android preview/production.
- [x] Compatibilização de `@react-native-async-storage/async-storage` (`2.2.0`) e dependências Expo SDK 58.
- [x] Estrutura modular em `components/`, `config/`, `contexts/`, `hooks/`, `lib/`, `navigation/`, `screens/`, `services/`, `theme/`, `types/`, `utils/` e `tests/`.

##### Commits vinculados (GitHub Repository):
- [`9ff4ae5`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/9ff4ae5) — `Initial commit` *(vinculado em AB#1 e AB#3)*
- [`c174fc5`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/c174fc5) — `chore: setup inicial do projeto Expo com TypeScript` *(vinculado em AB#3)*
- [`fe82953`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/fe82953) — `fix: compatibiliza versao do AsyncStorage com Expo SDK 58 e corrige url do repositorio` *(vinculado em AB#3)*
- [`56a15ef`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/56a15ef) — `chore(config): configura ambiente Azure/Render, EAS Build, ESLint e dependencias` *(vinculado em AB#3)*
- [`b7778de`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/b7778de) — `fix: Só pequeno ajuste em tsconfig e env` *(vinculado em AB#3)*

---

#### 🔹 [PBI-02] Design System CitizenTech, Temas Claro/Escuro, Enums Canônicos e Tipagens Alinhadas à API Java

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#4`
* **Parent Feature:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas` (`#2`)
* **Title:** `[PBI-02] Design System CitizenTech, Temas Claro/Escuro, Enums Canônicos e Tipagens Alinhadas à API Java`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `2`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** arquiteto mobile,  
> **Eu quero** centralizar tokens semânticos de design Light/Dark, identidade visual renovada e enums/contratos DTO espelhados 1:1 com a API Java,  
> **Para que** o aplicativo compartilhe identidade visual consistente e nunca sofra divergências de contrato JSON.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `ThemeContext.tsx` provendo `AppTheme` completo para Light/Dark mode persistido e hook `useThemedStyles`.
- [x] Renovação de identidade visual (`icon.png`, `splash-icon.png`, `logo-mark.png` e ícones adaptativos Android em `#064E3B`).
- [x] `semanticConfig.ts` com 5 estados oficiais (`PENDENTE`, `EM_ANALISE`, `EM_EXECUCAO`, `CONCLUIDO`, `REJEITADO`), 6 categorias canônicas (`ILUMINACAO_PUBLICA`, `VIAS_E_PAVIMENTACAO`, `DRENAGEM_E_ESGOTO`, `LIMPEZA_URBANA`, `ARVORES_E_PARQUES`, `SINALIZACAO_E_TRANSITO`) e `ORGAO_LABELS` (`getOrgaoLabel`).
- [x] Tipos granulares em `api.ts`, `auth.ts`, `categoria.ts`, `chamado.ts`, `endereco.ts`, `filters.ts`, `ai.ts` e `version.ts` sem barrel morto e sem uso de `any`.

##### Commits vinculados (GitHub Repository):
- [`a59cdd8`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/a59cdd8) — `feat: adiciona sistema de tema CitizenTech e tipagens de dominio` *(vinculado em AB#4)*
- [`c5b9095`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/c5b9095) — `refactor(core): alinha contratos DTO, validacoes Zod, permissoes e servicos HTTP com API Java` *(vinculado em AB#4)*
- [`6a2e085`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/6a2e085) — `feat: Dando um retoque em Mobile!! Agora sim está organizado!!` *(vinculado em AB#4)*
- [`aadd028`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/aadd028) — `feat(brand): renovar identidade visual, icones e splash` *(vinculado em AB#4)*
- [`4bb6c31`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/4bb6c31) — `feat(mobile): centralizar tipos sem barrels, alinhar timeouts e boundary multipart com backend Java` *(vinculado em AB#4)*

---

#### 🔹 [PBI-03] Biblioteca de Componentes Reutilizáveis de UI, FeedbackProvider Global e Modais Acessíveis

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#106`
* **Parent Feature:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas` (`#2`)
* **Title:** `[PBI-03] Biblioteca de Componentes Reutilizáveis de UI, FeedbackProvider Global e Modais Acessíveis`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** cidadão utilizando o app,  
> **Eu quero** interagir com botões responsivos, campos padronizados, seletores modais, cards de ocorrência e feedback visual global consistente,  
> **Para que** a experiência seja fluida, acessível e livre de duplicação de código visual.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `BaseModal/index.tsx` centralizando overlay, rolagem responsiva e `KeyboardAvoidingView` para `FeedbackModal`, `SelectPickerModal`, `StatusChangeModal`, `EditProfileModal` e `ZelaBotHistoryModal`.
- [x] `FeedbackContext.tsx` (`FeedbackProvider` e `useFeedback`) centralizando alertas de erro/sucesso/aviso globalmente em `App.tsx`.
- [x] Componentes modulares: `AuthHeader`, `Button`, `Input`, `Header`, `StatCard`, `EmptyState`, `LoadingSpinner`, `ListSeparator` (`ChamadoListSeparator`), `CategoryBadge`, `CategoryGridSelector`, `StatusBadge`, `ChamadoCard` e `ChamadoFormFields`.
- [x] Imports diretos nos módulos reais sem barrel `src/components/index.ts`.

##### Commits vinculados (GitHub Repository):
- [`729434d`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/729434d) — `feat: cria componentes reutilizaveis de UI e feedbacks visuais` *(vinculado em AB#106)*
- [`516b8b9`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/516b8b9) — `fix(ui): resolve corte de input numerico, foto de poste e bueiro e proporcoes de texto` *(vinculado em AB#106)*
- [`f449639`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/f449639) — `refactor(ui): remove barrels e useAuth legado, padroniza componentes e navegacao` *(vinculado em AB#106)*

---

#### 🔹 [PBI-04] Estrutura de Navegação Nativa com React Navigation, Tab Central IA e Rotas Tipadas

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#107`
* **Parent Feature:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas` (`#2`)
* **Title:** `[PBI-04] Estrutura de Navegação Nativa com React Navigation, Tab Central IA e Rotas Tipadas`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `2`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** munícipe que navega pelo ZelaFix,  
> **Eu quero** alternar entre abas principais (incluindo o atalho central do ZelaBot IA) e navegar para fluxos detalhados e edição via stacks nativos sem loops de navegação,  
> **Para que** a transição entre telas seja rápida e validada em tempo de compilação.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Rotas estritamente tipadas em `navigation/types.ts` (`AppStackParamList`, `AppTabParamList`, `AuthStackParamList`) incluindo `ZelaBotTab` (`{ chamadoId?: number }`), `ChamadoDetails` (`{ id: number }`), `EditarChamado` (`{ id: number }`) e `NovoChamado`.
- [x] `TabNavigator` com botão central destacado para ZelaBot IA e respeito às `SafeAreaInsets` para Início, Radar, ZelaBot IA, Meus e Perfil.
- [x] `AuthNavigator` e `AppNavigator` orquestrados reativamente pelo `NavigationContainer` conectado ao `AppTheme`, com correção de loop de navegação (`popTo('MainTabs', ...)`).

##### Commits vinculados (GitHub Repository):
- [`16e20b7`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/16e20b7) — `feat: implementa telas do fluxo de zeladoria, CRUD e rotas protegidas` *(vinculado em AB#107)*
- [`f449639`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/f449639) — `refactor(ui): remove barrels e useAuth legado, padroniza componentes e navegacao` *(vinculado em AB#107)*
- [`d670b00`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/d670b00) — `feat(mobile): refatorar navegacao, filtros, layout e triagem sincrona com Spring AI` *(vinculado em AB#107)*

---

#### 🔹 [PBI-05] Telas Principais do Cidadão (Welcome, Home, Radar do Bairro e Sobre o App)

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#108`
* **Parent Feature:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas` (`#2`)
* **Title:** `[PBI-05] Telas Principais do Cidadão (Welcome, Home, Radar do Bairro e Sobre o App)`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** munícipe e avaliador acadêmico,  
> **Eu quero** explorar o panorama de zeladoria na Home, consultar demandas no Radar com filtros em modal e verificar dados do projeto na tela Sobre,  
> **Para que** o acompanhamento urbano seja transparente e intuitivo desde o primeiro acesso.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `WelcomeScreen` com identidade visual renovada (`logo-mark.png`), alinhamento à ODS 11 e portas de entrada para Login/Cadastro.
- [x] `HomeScreen` com `HomePanoramaCard`, `HomeCategoryList` e atalho contextual para o ZelaBot IA via hook `useHomeData`.
- [x] `RadarBairroScreen` com `RadarHeaderFilters` e `SelectPickerModal` integrados ao `useRadarData` (filtros de status, categoria, localização e busca textual com debounce).
- [x] `SobreAppScreen` e `TeamMembersCard` exibindo ODS 11, versão, commit hash dinâmico de auditoria e equipe em ordem alfabética estrita.

##### Commits vinculados (GitHub Repository):
- [`16e20b7`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/16e20b7) — `feat: implementa telas do fluxo de zeladoria, CRUD e rotas protegidas` *(vinculado em AB#108)*
- [`edd60a4`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/edd60a4) — `feat(ui): reformula dashboard na home e centraliza demandas e prioridades no radar` *(vinculado em AB#108)*
- [`ba5b3b8`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/ba5b3b8) — `feat: dando uma refatorada em mobile` *(vinculado em AB#108)*
- [`b34bdfc`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/b34bdfc) — `refactor(screens): integra hooks React Query e refatora telas com paridade total de contratos` *(vinculado em AB#108)*
- [`13a7dca`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/13a7dca) — `refactor(mobile): modernize UI design, streamline screens and fix transition white flash` *(vinculado em AB#108)*

---

#### 🔹 [PBI-06] Tela de Perfil do Cidadão, Edição Cadastral Alinhada ao Java e SafeAreaView

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#109`
* **Parent Feature:** `[FEATURE 01] Arquitetura UI, Design System e Navegação por Abas` (`#2`)
* **Title:** `[PBI-06] Tela de Perfil do Cidadão, Edição Cadastral Alinhada ao Java e SafeAreaView`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `2`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** munícipe cadastrado,  
> **Eu quero** visualizar meu perfil, cargo RBAC, estatísticas pessoais, tema do app e atualizar meus dados cadastrais e endereço,  
> **Para que** minhas informações estejam atualizadas no backend Java sem sobreposições de tela.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `ProfileScreen`, `ProfileUserCard` e `ProfileStatsCard` consumindo dados via `useProfileData`.
- [x] `EditProfileModal` validado com `ProfileEditSchema` (Zod) compatível com `UsuarioRequest` (`buildUsuarioRequest`) e `EnderecoRequest` (`buildEnderecoRequest`) da API Java.
- [x] Alternância de tema Light/Dark, atalho para ZelaBot IA / Sobre o App e logout seguro encerrando sessão e limpando `QueryClient`.

##### Commits vinculados (GitHub Repository):
- [`6b7d415`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/6b7d415) — `feat: aplica SafeAreaView para barra de status e adiciona edicao de dados cadastrais e senha` *(vinculado em AB#109)*
- [`b34bdfc`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/b34bdfc) — `refactor(screens): integra hooks React Query e refatora telas com paridade total de contratos` *(vinculado em AB#109)*

---

### 🏆 [FEATURE 02] Autenticação JWT Segura, Validação Zod e Proteção de Rotas Privadas

* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#5`
* **Parent:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa` (`#1`)
* **Title:** `[FEATURE 02] Autenticação JWT Segura, Validação Zod e Proteção de Rotas Privadas`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Start Date:** `2026-11-07`
* **Target Date:** `2026-11-12`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Description:** Sistema completo de login, cadastro com endereço (`EnderecoRequest`) e telefone DDD válido, renovação de token via header `x-novo-token`, persistência criptografada em `expo-secure-store`, hooks `useZodForm` com `bindFieldHelpers` e guarda declarativa de rotas privadas.
* **Acceptance Criteria:**
  - [x] Login, Cadastro e edição de perfil integrados aos endpoints Spring Security (`/login`, `/usuarios`, `/usuarios/me`) da API Java no Azure.
  - [x] Persistência criptografada do token JWT no SecureStore (Android/iOS) com fallback Web no `storageService.ts`.
  - [x] Validação declarativa com Zod v4 via `useZodForm` garantindo 100% de paridade com Bean Validation e `DddValidation` do Java.
  - [x] Rotas privadas protegidas via `AuthContext` e `useAuth` unificado (`CIDADAO` e `GESTOR`).

#### 🔹 [PBI-07] Cliente HTTP Axios, Interceptor JWT, Warmup Azure e Normalização RFC 7807

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#6`
* **Parent Feature:** `[FEATURE 02] Autenticação JWT Segura, Validação Zod e Proteção de Rotas Privadas` (`#5`)
* **Title:** `[PBI-07] Cliente HTTP Axios, Interceptor JWT, Warmup Azure e Normalização RFC 7807`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** arquiteto de software mobile,  
> **Eu quero** centralizar o cliente HTTP Axios com injeção automática de Bearer Token, suporte automático a `FormData`, warmup de cold start no Azure e tratamento padronizado de erros `ProblemDetail`,  
> **Para que** todas as chamadas à API Java sejam resilientes, autenticadas e exibam mensagens de erro claras.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Instância Axios em `api.ts` apontando para `env.apiUrl` (Azure App Service) com timeout de 40s e ajuste automático de `Content-Type: multipart/form-data` para `FormData`.
- [x] Interceptor injetando `Authorization: Bearer` e callback automático (`registerUnauthorizedHandler`) para HTTP 401.
- [x] `authService.ts` capturando header `x-novo-token` após atualização cadastral de usuário (`PUT /usuarios/me`).
- [x] Warmup throttled compartilhado (`createThrottledPing`) em `/actuator/health`, `buildApiAssetUrl` e normalização de erros em `utils/apiError.ts`.

##### Commits vinculados (GitHub Repository):
- [`18b5fdb`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/18b5fdb) — `feat: configura cliente Axios, servicos de API e contexto de autenticacao` *(vinculado em AB#6)*
- [`c5b9095`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/c5b9095) — `refactor(core): alinha contratos DTO, validacoes Zod, permissoes e servicos HTTP com API Java` *(vinculado em AB#6)*
- [`fcc09ac`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/fcc09ac) — `refactor: atualizar endpoints para app-zelafix` *(vinculado em AB#6)*

---

#### 🔹 [PBI-08] Camada de Autenticação, AuthContext Unificado e Persistência no SecureStore

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#7`
* **Parent Feature:** `[FEATURE 02] Autenticação JWT Segura, Validação Zod e Proteção de Rotas Privadas` (`#5`)
* **Title:** `[PBI-08] Camada de Autenticação, AuthContext Unificado e Persistência no SecureStore`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** cidadão que utiliza o ZelaFix,  
> **Eu quero** manter minha sessão JWT armazenada com segurança nativa ao reabrir o app e sincronizada com o cache de dados,  
> **Para que** eu não precise fazer login a cada abertura sem comprometer meus dados sensíveis.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `AuthContext.tsx` expondo `AuthProvider` e hook `useAuth` diretamente (removendo arquivo morto `hooks/useAuth.ts`).
- [x] Armazenamento do JWT via `expo-secure-store` e sessão/tema validados via `StoredUsuarioSchema` em `storageService.ts`.
- [x] Hidratação inicial de sessão (`/usuarios/me`), atualização de usuário autenticado e limpeza automática de `QueryClient` no logout.

##### Commits vinculados (GitHub Repository):
- [`18b5fdb`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/18b5fdb) — `feat: configura cliente Axios, servicos de API e contexto de autenticacao` *(vinculado em AB#7)*
- [`c5b9095`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/c5b9095) — `refactor(core): alinha contratos DTO, validacoes Zod, permissoes e servicos HTTP com API Java` *(vinculado em AB#7)*
- [`f449639`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/f449639) — `refactor(ui): remove barrels e useAuth legado, padroniza componentes e navegacao` *(vinculado em AB#7)*

---

#### 🔹 [PBI-09] Telas Welcome, Login e Cadastro com useZodForm e Proteção de Rotas Privadas

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#110`
* **Parent Feature:** `[FEATURE 02] Autenticação JWT Segura, Validação Zod e Proteção de Rotas Privadas` (`#5`)
* **Title:** `[PBI-09] Telas Welcome, Login e Cadastro com useZodForm e Proteção de Rotas Privadas`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** novo munícipe,  
> **Eu quero** realizar cadastro completo validado em tempo real e autenticar com segurança no ZelaFix,  
> **Para que** eu acesse exclusivamente o painel autenticado após validar minhas credenciais.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Hook genérico memoizado `useZodForm` + `bindFieldHelpers` (zero `any`) conectado a `LoginSchema` e `RegisterSchema` (`DDDS_VALIDOS` e tamanhos exatos da API Java).
- [x] Hooks `useLoginForm` e `useRegisterForm` integrados ao `FeedbackContext` para feedback de erros e sucesso.
- [x] `LoginScreen` (`LoginForm`), `RegisterScreen` (`RegisterForm`) e `WelcomeScreen` com proteção de rotas em `navigation/index.tsx`.

##### Commits vinculados (GitHub Repository):
- [`16e20b7`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/16e20b7) — `feat: implementa telas do fluxo de zeladoria, CRUD e rotas protegidas` *(vinculado em AB#110)*
- [`b34bdfc`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/b34bdfc) — `refactor(screens): integra hooks React Query e refatora telas com paridade total de contratos` *(vinculado em AB#110)*

---

### 🏆 [FEATURE 03] CRUD Completo de Chamados, TanStack Query v5 e Sensores Nativos

* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#8`
* **Parent:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa` (`#1`)
* **Title:** `[FEATURE 03] CRUD Completo de Chamados, TanStack Query v5 e Sensores Nativos`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Start Date:** `2026-11-09`
* **Target Date:** `2026-11-15`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Description:** Gerenciamento completo de ocorrências urbanas utilizando TanStack Query v5 com query keys tipadas (`queryKeys.ts`), paginação infinita no Radar do Bairro (`useInfiniteChamadosList`), filtros server-side paginados (`SpringPageResponse`), captura real de coordenadas GPS e reverse geocoding via `expo-location`, envio fotográfico via `multipart/form-data` (`expo-image-picker`) aguardando classificação direta da Spring AI (`DeferredResult`) em `POST /chamados` sem polling de recusa-recente, e atualização otimista de apoio em `chamadoCache.ts`.
* **Acceptance Criteria:**
  - [x] CRUD completo (`POST /chamados` multipart com `DeferredResult`, `GET` paginado, `PUT`, `PATCH /status`, `DELETE` do autor) integrado à API Java.
  - [x] Hooks `useChamados`, `useInfiniteChamadosList`, `useChamadoForm`, `useMeusChamadosData` e `useRadarData` exibindo todas as cidades por padrão com filtros server-side.
  - [x] Captura automática de CEP, logradouro e número via `expo-location` (`useLocalizacao.ts`) e montagem de `EnderecoRequest` em `buildEnderecoRequest`.
  - [x] Captura e validação de fotos (câmera/galeria, máx. 7 MB, `quality: 0.7`) em `PhotoEvidencePicker.tsx` com envio `multipart/form-data` (`FotoUpload`).

#### 🔹 [PBI-10] Formulário de Ocorrência (useChamadoForm) com GPS, Reverse Geocoding e Triagem Direta via DeferredResult

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#9`
* **Parent Feature:** `[FEATURE 03] CRUD Completo de Chamados, TanStack Query v5 e Sensores Nativos` (`#8`)
* **Title:** `[PBI-10] Formulário de Ocorrência (useChamadoForm) com GPS, Reverse Geocoding e Triagem Direta via DeferredResult`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** munícipe que identifica um problema urbano,  
> **Eu quero** abrir um chamado enviando apenas a foto e a localização (preenchida via GPS) e receber na hora o protocolo classificado pela IA,  
> **Para que** o relato seja rápido, preciso e sem erros manuais de preenchimento ou polling desnecessário.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `NovoChamadoScreen` simplificada com `hideDetails` em `ChamadoFormFields`: cidadão envia foto + endereço e a IA define título, descrição, categoria, prioridade e órgão responsável.
- [x] Integração ao hook `useLocalizacao` (`expo-location`) com reverse geocoding para CEP, rua e número compatíveis com `EnderecoRequest` (`buildEnderecoRequest` em `utils/chamadoMappers.ts`).
- [x] Hook `useChamadoForm` validando criação com `ChamadoCreateSchema` (Zod) e edição com `ChamadoFormSchema`, chamando `POST /chamados` aguardando retorno direto via `DeferredResult` (sem polling de `/chamados/recusa-recente`).

##### Commits vinculados (GitHub Repository):
- [`b34bdfc`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/b34bdfc) — `refactor(screens): integra hooks React Query e refatora telas com paridade total de contratos` *(vinculado em AB#9)*
- [`84aea05`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/84aea05) — `refactor(mobile): adequar abertura e detalhes de chamado ao fluxo assincrono da IA` *(vinculado em AB#9)*
- [`ce4ec9f`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/ce4ec9f) — `refactor(chamados): remover polling de recusa-recente e aguardar retorno direto de POST /chamados` *(vinculado em AB#9)*

---

#### 🔹 [PBI-11] Anexo de Evidências Fotográficas (Multipart/Form-Data) e Otimização de Imagens

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#10`
* **Parent Feature:** `[FEATURE 03] CRUD Completo de Chamados, TanStack Query v5 e Sensores Nativos` (`#8`)
* **Title:** `[PBI-11] Anexo de Evidências Fotográficas (Multipart/Form-Data) e Otimização de Imagens`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** cidadão que registra uma demanda,  
> **Eu quero** tirar uma foto na hora ou selecionar uma imagem da galeria com preview, validação de tamanho e envio leve em `multipart/form-data`,  
> **Para que** o backend Java e a triagem multimodal por IA recebam a evidência sem sobrecarga de payload Base64.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `PhotoEvidencePicker.tsx` integrado ao `expo-image-picker` (câmera e galeria, `quality: 0.7`, `allowsEditing: true`) com preview, remoção e limite de 7 MB (`MAX_IMAGE_BYTES`).
- [x] Conversão para `FotoUpload { uri, name, type }` via `toFotoUpload` e envio como `FormData` em `chamadoService.criar` (`POST /chamados` `multipart/form-data`).
- [x] Exibição segura de imagens persistidas no Oracle BLOB via `GET /chamados/{id}/foto` mapeada por `buildApiAssetUrl` em `mapChamadoResponse`.

##### Commits vinculados (GitHub Repository):
- [`516b8b9`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/516b8b9) — `fix(ui): resolve corte de input numerico, foto de poste e bueiro e proporcoes de texto` *(vinculado em AB#10)*
- [`b34bdfc`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/b34bdfc) — `refactor(screens): integra hooks React Query e refatora telas com paridade total de contratos` *(vinculado em AB#10)*
- [`ce4ec9f`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/ce4ec9f) — `refactor(chamados): remover polling de recusa-recente e aguardar retorno direto de POST /chamados` *(vinculado em AB#10)*

---

#### 🔹 [PBI-12] Feed com Paginação Infinita no Radar, Filtros Server-Side e Gestão CRUD com TanStack Query v5

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#111`
* **Parent Feature:** `[FEATURE 03] CRUD Completo de Chamados, TanStack Query v5 e Sensores Nativos` (`#8`)
* **Title:** `[PBI-12] Feed com Paginação Infinita no Radar, Filtros Server-Side e Gestão CRUD com TanStack Query v5`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** cidadão ativo no ZelaFix,  
> **Eu quero** consultar ocorrências com scroll infinito no Radar exibindo todas as cidades por padrão, filtrar por status/categoria/localização/busca no servidor e gerenciar meus chamados,  
> **Para que** a lista carregue sob demanda, mantenha consistência com a API Java e sem recarregamentos redundantes.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `chamadoService.ts` consumindo `SpringPageResponse { content, page }` com parâmetros server-side `status`, `categoria`, `busca`, `apenasMeus`, `cidade`, `bairro` e `estado`.
- [x] `useInfiniteChamadosList` + `useRadarData` + `RadarBairroScreen` implementando paginação infinita (`onEndReached`, `size: 10`), exibição padrão de todas as cidades e modal de filtros `RadarHeaderFilters`.
- [x] `MeusChamadosScreen` (`useMeusChamadosData`) e `EditarChamadoScreen` compartilhando `useChamadoForm` e `ChamadoFormFields`.
- [x] Controle de permissões em `utils/permissions.ts` (`canAccessMobileApp`, `canEditChamado`, `canChangeChamadoStatus`, `canDeleteChamado` para o autor — zero `ADMIN` no mobile).

##### Commits vinculados (GitHub Repository):
- [`c5b9095`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/c5b9095) — `refactor(core): alinha contratos DTO, validacoes Zod, permissoes e servicos HTTP com API Java` *(vinculado em AB#111)*
- [`b34bdfc`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/b34bdfc) — `refactor(screens): integra hooks React Query e refatora telas com paridade total de contratos` *(vinculado em AB#111)*
- [`b1bbc50`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/b1bbc50) — `feat(radar): exibir todas as cidades por padrao e atualizar README` *(vinculado em AB#111)*
- [`e923201`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/e923201) — `feat: paginacao infinita no radar, ajustes na navbar/home, fix loop de navegacao e enum de categorias` *(vinculado em AB#111)*
- [`ce4ec9f`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/ce4ec9f) — `refactor(chamados): remover polling de recusa-recente e aguardar retorno direto de POST /chamados` *(vinculado em AB#111)*
- [`2b8dc3c`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/2b8dc3c) — `feat: só um pequeno ajuste na página dos meus chamados` *(vinculado em AB#111)*

---

### 🏆 [FEATURE 04] Engajamento Cidadão, Votação Otimista, Lifecycle Nativo e Entrega

* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#11`
* **Parent:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa` (`#1`)
* **Title:** `[FEATURE 04] Engajamento Cidadão, Votação Otimista, Lifecycle Nativo e Entrega`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Start Date:** `2026-11-11`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `7`
* **Business Value:** `100`
* **Description:** Acompanhamento completo de ocorrências com timeline de 5 estados, exibição da classificação gerada pela triagem IA (prioridade e órgão competente), feedback visual em recusas da IA, botão de apoio comunitário com atualização otimista em cache (`chamadoCache.ts` para listas simples e infinitas), lifecycle nativo React Native no TanStack Query (`AppState` + `expo-network`), suíte de 78 testes unitários Node, builds EAS (`versionCode` 2 a 14) e entrega documentada FIAP.
* **Acceptance Criteria:**
  - [x] `ChamadoDetailsScreen` exibindo foto, localização, timeline de 5 estados, prioridade e órgão responsável gerados pela triagem IA.
  - [x] Apoio comunitário otimista em `useChamadoMutations` + `chamadoCache.ts` via `POST /chamados/{id}/apoiar` com rollback em erro.
  - [x] Integração de `AppState` + `expo-network` no `QueryClient` para refetch e pausas conscientes de bateria.
  - [x] Rastreabilidade de versão/commit dinâmico, suíte de 78 testes unitários Node e APK EAS `versionCode 14` publicado.

#### 🔹 [PBI-13] Detalhes do Chamado, Timeline 5 Estados, Triagem IA, Feedback de Recusa e Apoio Otimista

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#12`
* **Parent Feature:** `[FEATURE 04] Engajamento Cidadão, Votação Otimista, Lifecycle Nativo e Entrega` (`#11`)
* **Title:** `[PBI-13] Detalhes do Chamado, Timeline 5 Estados, Triagem IA, Feedback de Recusa e Apoio Otimista`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** morador afetado por uma demanda no bairro,  
> **Eu quero** abrir o detalhe de um chamado, ver a classificação automática da IA (órgão e prioridade), receber feedback claro caso a IA recuse uma foto fora do escopo urbano e apoiar chamados com resposta instantânea,  
> **Para que** demandas coletivas ganhem prioridade sem duplicação de registros.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `ChamadoDetailsScreen` modularizada em `ChamadoSummaryCard`, `ChamadoLocationCard`, `ChamadoTimelineCard`, `ChamadoActionBar` e `StatusChangeModal` (para `GESTOR`).
- [x] Suporte completo aos 5 estados canônicos do Java (`PENDENTE`, `EM_ANALISE`, `EM_EXECUCAO`, `CONCLUIDO`, `REJEITADO`), exibição de prioridade (`getPriorityVisuals`) e órgão competente (`getOrgaoLabel`).
- [x] Botão de apoio com `useMutation` otimista em `useChamadoMutations.ts` + `patchApoioInCache` (`src/lib/chamadoCache.ts`) cobrindo caches `SpringPageResponse` e `InfiniteData`, chamando `POST /chamados/{id}/apoiar`.
- [x] Fluxo de recusa da IA evoluído de modal em `MeusChamados` (`5e635d2`) para resposta imediata de `POST /chamados` com modal global via `FeedbackContext` (`ce4ec9f`).

##### Commits vinculados (GitHub Repository):
- [`c5b9095`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/c5b9095) — `refactor(core): alinha contratos DTO, validacoes Zod, permissoes e servicos HTTP com API Java` *(vinculado em AB#12)*
- [`b34bdfc`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/b34bdfc) — `refactor(screens): integra hooks React Query e refatora telas com paridade total de contratos` *(vinculado em AB#12)*
- [`84aea05`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/84aea05) — `refactor(mobile): adequar abertura e detalhes de chamado ao fluxo assincrono da IA` *(vinculado em AB#12)*
- [`5e635d2`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/5e635d2) — `feat(chamados): exibir modal de recusa da IA em MeusChamados` *(vinculado em AB#12)*
- [`ce4ec9f`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/ce4ec9f) — `refactor(chamados): remover polling de recusa-recente e aguardar retorno direto de POST /chamados` *(vinculado em AB#12)*

---

#### 🔹 [PBI-14] Lifecycle Nativo TanStack Query (AppState/expo-network), Testes Unitários e Builds EAS

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#112`
* **Parent Feature:** `[FEATURE 04] Engajamento Cidadão, Votação Otimista, Lifecycle Nativo e Entrega` (`#11`)
* **Title:** `[PBI-14] Lifecycle Nativo TanStack Query (AppState/expo-network), Testes Unitários e Builds EAS`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Priority:** `2 - High`
* **Effort (Story Points):** `2`
* **Business Value:** `80`

##### Descrição (História de Usuário)
> **Como** usuário e avaliador técnico,  
> **Eu quero** que o cache sincronize automaticamente ao retomar conexão ou foco, que utilitários críticos tenham testes unitários e que o build EAS registre commit Git e versionCode incremental,  
> **Para que** o app seja resiliente a oscilações de rede, testado e 100% auditável na avaliação da FIAP.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `bindReactNativeQueryLifecycle` em `lib/queryClient.ts` conectando `AppState` (`focusManager`) e `expo-network` (`onlineManager`).
- [x] `app.config.js` + `config/version.ts` injetando hash completo/curto do commit Git e branch via `expo-constants` em tempo de build, com React Compiler (`reactCompiler: true`) em `app.json`.
- [x] Suíte de testes unitários com Node test runner (`node --experimental-strip-types --test`) com 78 testes unitários passando em 35 suítes.
- [x] Evolução de releases EAS Build Android APK (`versionCode` 2 ➔ 3 ➔ 5 ➔ 6 ➔ 7 ➔ 8 ➔ 9 ➔ 10 ➔ 11 ➔ 12 ➔ 13 ➔ 14) sem referências legadas ao Firebase, URLs centrais de produção Azure (`apiUrl`) e Render (`aiUrl`) em `src/config/env.ts`, desacoplamento de telas/tipos sem barrels, remoção de casts inseguros e migração de splash screen (`expo-splash-screen` + `expo-font`).

##### Commits vinculados (GitHub Repository):
- [`56a15ef`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/56a15ef) — `chore(config): configura ambiente Azure/Render, EAS Build, ESLint e dependencias` *(vinculado em AB#112)*
- [`6a2e085`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/6a2e085) — `feat: Dando um retoque em Mobile!! Agora sim está organizado!!` *(vinculado em AB#112)*
- [`b34bdfc`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/b34bdfc) — `refactor(screens): integra hooks React Query e refatora telas com paridade total de contratos` *(vinculado em AB#112)*
- [`5c4ef7f`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/5c4ef7f) — `chore(build): incrementar versionCode para 2` *(vinculado em AB#112)*
- [`e3cb942`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/e3cb942) — `chore(build): preparar APK versionCode 3 e remover referencias ao Firebase` *(vinculado em AB#112)*
- [`e5bc448`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/e5bc448) — `chore(build): incrementar versionCode para 5` *(vinculado em AB#112)*
- [`ce4ec9f`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/ce4ec9f) — `refactor(chamados): remover polling de recusa-recente e aguardar retorno direto de POST /chamados` *(vinculado em AB#112)*
- [`58a2cfd`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/58a2cfd) — `chore(release): preparar versionCode 6 e atualizar contratos no README` *(vinculado em AB#112)*
- [`7f731d1`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/7f731d1) — `feat(mobile): expandir suite de testes unitarios, unificar imports e suportar tipos do node` *(vinculado em AB#112)*
- [`44a19ff`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/44a19ff) — `chore(release): bump versionCode to 8 para novo APK com endpoint atualizado` *(vinculado em AB#112)*
- [`e070f89`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/e070f89) — `refactor(mobile): desacoplar telas, centralizar tipos sem barrels, eliminar casts inseguros e corrigir bugs de runtime (versionCode 9)` *(vinculado em AB#112)*
- [`dae3f99`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/dae3f99) — `fix(expo): migrar splash screen para plugin expo-splash-screen e adicionar expo-font` *(vinculado em AB#112)*
- [`0763f75`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/0763f75) — `chore(release): bump versionCode to 10 para APK com expo-splash-screen e expo-font` *(vinculado em AB#112)*
- [`628e487`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/628e487) — `fix(mobile): corrigir teclado e markdown/enums no ZelaBot, travar campos durante envio e preparar versionCode 11` *(vinculado em AB#112)*
- [`85c3fe4`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/85c3fe4) — `fix(mobile): corrigir layout do BaseModal e StatusChangeModal com teclado no Android (versionCode 12)` *(vinculado em AB#112)*
- [`77492e1`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/77492e1) — `fix(mobile): restringir edicao e exclusao de chamados apenas ao gestor (versionCode 13)` *(vinculado em AB#112)*
- [`0ffba5b`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/0ffba5b) — `fix(mobile): corrigir dirty-state de formularios, timeout 95s e filtro de bairro no ZelaBot (versionCode 14)` *(vinculado em AB#112)*

---

#### 🔹 [PBI-15] Documentação Técnica Completa (README.md), Submissão APK (versionCode 14) e Vídeo Demonstrativo

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#13`
* **Parent Feature:** `[FEATURE 04] Engajamento Cidadão, Votação Otimista, Lifecycle Nativo e Entrega` (`#11`)
* **Title:** `[PBI-15] Documentação Técnica Completa (README.md), Submissão APK (versionCode 14) e Vídeo Demonstrativo`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `2`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** banca examinadora e professores da FIAP,  
> **Eu quero** consultar documentação técnica detalhada, links oficiais de download do APK standalone (`versionCode 14`) e roteiro oficial de entrega,  
> **Para que** seja comprovado o atendimento rigoroso a todos os critérios da Global Solution 2026/2.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `README.md` e `identificacao.txt` documentando stack, 12 telas, contratos REST atualizados (`POST /chamados` `multipart/form-data` + `DeferredResult`, rotas `GESTOR`), credenciais de teste, declaração de uso de IA, nomes completos dos integrantes e instalação standalone.
- [x] Publicação oficial do APK `versionCode 14` via EAS Build (`8c21e8d0`, commit `0ffba5b`) com link direto de artefato (`tAr1dhKfReeHzG0A2MHOEHml5dvbgLnQsfy6LZa33p8.apk`) e painel Expo.
- [x] Tela `SobreAppScreen` exibindo versão, commit hash dinâmico e equipe em ordem alfabética estrita.
- [x] Estrutura preparada para link do vídeo demonstrativo cobrindo autenticação, telas principais, sensores GPS/câmera, CRUD, RBAC e ZelaBot IA.

##### Commits vinculados (GitHub Repository):
- [`0eade37`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/0eade37) — `docs: adiciona modelo do arquivo texto de entrega oficial da GS` *(vinculado em AB#13)*
- [`c4eb868`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/c4eb868) — `docs: adiciona documentacao da arquitetura e instrucoes no README` *(vinculado em AB#13)*
- [`d69b517`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/d69b517) — `docs: atualiza documentacao da entrega e sincroniza commit hash de auditoria` *(vinculado em AB#13)*
- [`3b9c388`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/3b9c388) — `docs: corrigir referencia de NetInfo para expo-network` *(vinculado em AB#13)*
- [`307e1a2`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/307e1a2) — `docs: adicionar links oficiais e instalacao do APK` *(vinculado em AB#13)*
- [`824a547`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/824a547) — `docs: remover Firebase e atualizar dados de entrega do APK` *(vinculado em AB#13)*
- [`8ccee66`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/8ccee66) — `docs(mobile): padronizar README e links rapidos` *(vinculado em AB#13)*
- [`6aae45e`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/6aae45e) — `docs(mobile): atualizar arquitetura e endpoints da triagem assincrona no README` *(vinculado em AB#13)*
- [`dda6a69`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/dda6a69) — `docs(mobile): atualizar links oficiais do APK versionCode 5 no README` *(vinculado em AB#13)*
- [`34bbf4c`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/34bbf4c) — `docs: atualizar link do APK versionCode 6 (EAS Build 718280c9)` *(vinculado em AB#13)*
- [`9b97e97`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/9b97e97) — `docs: atualizar link do APK versionCode 7 (EAS Build e9e4c709)` *(vinculado em AB#13)*
- [`9b22136`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/9b22136) — `docs: atualizar link do APK versionCode 13 (EAS Build ba71cba6)` *(vinculado em AB#13)*
- [`1c4b160`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/1c4b160) — `docs: atualizar link do APK versionCode 9 (EAS Build 39a21c29)` *(vinculado em AB#13)*
- [`2f300c8`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/2f300c8) — `docs: atualizar link do APK versionCode 13 (EAS Build d6f6ece9)` *(vinculado em AB#13)*
- [`d7a7fc1`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/d7a7fc1) — `docs: atualizar credenciais de teste, declaracao de IA e nomes completos dos integrantes` *(vinculado em AB#13)*
- [`dc4f3ba`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/dc4f3ba) — `docs: atualizar link do APK versionCode 14 no README e identificacao.txt` *(vinculado em AB#13)*

---

### 🏆 [FEATURE 05] Assistente Conversacional ZelaBot IA, RAG Normativo e Insights por Bairro

* **Work Item Type:** `Feature`
* **Azure Boards ID:** `#180`
* **Parent:** `[EPIC] Mobile Application Development: Aplicativo ZelaFix para Engajamento Cidadão e Zeladoria Urbana Colaborativa` (`#1`)
* **Title:** `[FEATURE 05] Assistente Conversacional ZelaBot IA, RAG Normativo e Insights por Bairro`
* **State:** `In Progress`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Start Date:** `2026-11-11`
* **Target Date:** `2026-11-19`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `9`
* **Business Value:** `100`
* **Description:** Implementação completa do assistente inteligente ZelaBot IA integrado ao microsserviço Python FastAPI (`deploy_zelafixai_render` em `env.aiUrl`), contemplando warmup throttled em `/health`, chat com RAG normativo em `/ai/chat`, contexto automático por chamado (`chamadoId`), insights preditivos por bairro em `/ai/insights` e gestão completa de sessões e histórico em `/ai/sessions` e `/ai/history`.
* **Acceptance Criteria:**
  - [x] Serviço `aiService.ts` alinhado 100% aos contratos Pydantic do FastAPI no Render.
  - [x] Hook `useZelaBot` gerenciando mensagens, sessões, histórico, insights e deleção otimista.
  - [x] `ZelaBotScreen` modularizada com renderização de fontes RAG, alertas de bairro e modal de histórico.
  - [x] Atalhos integrados na `TabNavigator` (aba central), `HomeScreen`, `ProfileScreen` e `ChamadoDetailsScreen`.

#### 🔹 [PBI-16] Camada de Serviço FastAPI (aiService.ts), Tipos de IA e Aquecimento Render

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#181`
* **Parent Feature:** `[FEATURE 05] Assistente Conversacional ZelaBot IA, RAG Normativo e Insights por Bairro` (`#180`)
* **Title:** `[PBI-16] Camada de Serviço FastAPI (aiService.ts), Tipos de IA e Aquecimento Render`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** desenvolvedor mobile e integrador de IA,  
> **Eu quero** consumir o microsserviço FastAPI no Render com contratos tipados e pré-aquecimento throttled no endpoint `/health`,  
> **Para que** as respostas do chat RAG e dos insights por bairro sejam rápidas e resilientes a cold starts.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] Tipagens em `src/types/ai.ts` espelhando `ChatRequest`, `ChatResponse`, `AiMessage`, `AiChatSession` e `AiInsightItem` do FastAPI.
- [x] `aiService.ts` reutilizando `createThrottledPing` para aquecer `/health` de `env.aiUrl`.
- [x] Chamadas aos endpoints `/ai/chat`, `/ai/insights`, `/ai/sessions`, `/ai/history` e `DELETE /ai/sessions/{session_id}` com injeção de Bearer JWT.

##### Commits vinculados (GitHub Repository):
- [`4acbbc9`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/4acbbc9) — `feat(ai): adiciona chat ZelaBot IA com RAG normativo, insights por bairro e historico` *(vinculado em AB#181)*

---

#### 🔹 [PBI-17] Hook useZelaBot com Histórico de Sessões, Insights por Bairro e Deleção Otimista

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#182`
* **Parent Feature:** `[FEATURE 05] Assistente Conversacional ZelaBot IA, RAG Normativo e Insights por Bairro` (`#180`)
* **Title:** `[PBI-17] Hook useZelaBot com Histórico de Sessões, Insights por Bairro e Deleção Otimista`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** cidadão usando o assistente urbano,  
> **Eu quero** alternar entre conversas salvas, receber alertas por bairro e remover sessões antigas com feedback imediato,  
> **Para que** eu obtenha orientações contextualizadas sobre zeladoria e normas municipais sem perder o histórico.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `useZelaBot.ts` unificando envio de mensagens, contexto opcional de `chamadoId` e seleção automática de sessão.
- [x] Carregamento de insights por bairro (`/ai/insights`) e sugestões rápidas adaptadas ao contexto.
- [x] Exclusão otimista de sessões com restauração segura em caso de erro (reportado via `FeedbackContext`) e troca automática para nova conversa.

##### Commits vinculados (GitHub Repository):
- [`4acbbc9`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/4acbbc9) — `feat(ai): adiciona chat ZelaBot IA com RAG normativo, insights por bairro e historico` *(vinculado em AB#182)*

---

#### 🔹 [PBI-18] Interface Conversacional ZelaBotScreen Integrada à Home, Perfil e Detalhes do Chamado

* **Work Item Type:** `Product Backlog Item`
* **Azure Boards ID:** `#183`
* **Parent Feature:** `[FEATURE 05] Assistente Conversacional ZelaBot IA, RAG Normativo e Insights por Bairro` (`#180`)
* **Title:** `[PBI-18] Interface Conversacional ZelaBotScreen Integrada à Home, Perfil e Detalhes do Chamado`
* **State:** `Committed`
* **Iteration Path:** `ZelaFix\Release 1 - Global Solution\Semana 1`
* **Tags:** `Mobile`
* **Assigned To:** `RM562290@fiap.com.br`
* **Priority:** `1 - Critical`
* **Effort (Story Points):** `3`
* **Business Value:** `100`

##### Descrição (História de Usuário)
> **Como** munícipe navegando pelo ZelaFix,  
> **Eu quero** abrir o chat ZelaBot tanto pelo atalho principal quanto diretamente dentro de um chamado específico,  
> **Para que** a IA responda dúvidas sobre leis urbanas, SLA e andamento usando o contexto da ocorrência.

##### Critérios de Aceite (Acceptance Criteria / Definition of Done)
- [x] `ZelaBotScreen.tsx` compondo `ZelaBotInsightsBanner`, `ZelaBotMessageBubble`, `ZelaBotInputBar` e `ZelaBotHistoryModal` via `BaseModal`.
- [x] Exibição de fontes/citações RAG retornadas pelo backend IA e estado de carregamento acessível.
- [x] Atalhos de navegação adicionados na `TabNavigator` (botão central), `HomeScreen`, `ProfileScreen` e `ChamadoDetailsScreen` (enviando `chamadoId`).

##### Commits vinculados (GitHub Repository):
- [`4acbbc9`](https://github.com/Global-Solution-CitizenTech/Mobile-Application-Development/commit/4acbbc9) — `feat(ai): adiciona chat ZelaBot IA com RAG normativo, insights por bairro e historico` *(vinculado em AB#183)*
