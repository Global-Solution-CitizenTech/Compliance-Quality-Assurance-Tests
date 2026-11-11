# CitizenTech / ZelaFix — Casos de Teste Funcionais de Sistema

**Disciplina:** Compliance, Quality Assurance & Tests  
**Tipo:** caixa-preta, testes positivos e negativos  
**Versão:** 2.0  
**Status:** casos especificados para execução; não representam resultados de execução.

## 1. Objetivo e critério de elaboração

Especificar casos de teste funcionais para aceitação/homologação do CitizenTech, com sumário de objetivo, preparação, inputs e outputs esperados, e passos que relacionam a ação do testador à resposta do sistema.

A estrutura segue a seção **Compliance, Quality Assurance & Tests** do PDF da Global Solution 2026/2 (págs. 30–32). A meta de 20 casos, com 65% positivos e 35% negativos, vem do [`BACKLOG_COMPLIANCE.md`](../automatizar-boards/backlog-materias/BACKLOG_COMPLIANCE.md): 13 positivos e 7 negativos.

Os resultados esperados abaixo são derivados dos critérios de aceite dos backlogs e das asserções existentes na coleção Postman. Quando uma regra, campo, endereço ou resposta não está definido, isso é indicado — não se presume um código HTTP, mensagem, valor de limiar ou comportamento.

## 2. Fontes consultadas

- [`2TDS Fevereiro - Global Solution 2026-2.pdf`](../../2TDS%20Fevereiro%20-%20Global%20Solution%202026-2.pdf), págs. 30–32: entregáveis, campos do sumário e passos dos Test Cases.
- [`BACKLOG_COMPLIANCE.md`](../automatizar-boards/backlog-materias/BACKLOG_COMPLIANCE.md): meta de 20 testes, itens positivos/negativos e requisitos de cadastro, chamados, filtros, radar, voto e RBAC.
- [`BACKLOG_MOBILE.md`](../automatizar-boards/backlog-materias/BACKLOG_MOBILE.md): navegação, autenticação/sessão, CRUD, GPS, fotos, feed, timeline, voto e cache offline.
- [`BACKLOG_JAVA_ADVANCED.md`](../automatizar-boards/backlog-materias/BACKLOG_JAVA_ADVANCED.md): autenticação, papéis, ciclo de vida, histórico, votação e processamento distribuído.
- [`BACKLOG_DISRUPTIVE_ARCHITECTURES.md`](../automatizar-boards/backlog-materias/BACKLOG_DISRUPTIVE_ARCHITECTURES.md): telemetria MQTT, análise/validação de imagem e integração de alertas.
- [`BACKLOG_DOT_NET.md`](../automatizar-boards/backlog-materias/BACKLOG_DOT_NET.md): despacho de alertas por região/severidade e respostas de criação.
- [`BACKLOG_DATABASE_ADVANCED.md`](../automatizar-boards/backlog-materias/BACKLOG_DATABASE_ADVANCED.md) e [`BACKLOG_DEVOPS.md`](../automatizar-boards/backlog-materias/BACKLOG_DEVOPS.md): recursos de persistência e infraestrutura considerados na definição de escopo.
- [`CitizenTech_QA_Automation.postman_collection.json`](../postman/CitizenTech_QA_Automation.postman_collection.json): sete requests automatizados e respectivos dados/asserts.
- [`CitizenTech_QA_Environment.postman_environment.json`](../postman/CitizenTech_QA_Environment.postman_environment.json): variáveis de ambiente usadas pela coleção.

## 3. Escopo e cobertura por Feature

Os casos cobrem os comportamentos funcionais da aplicação descritos nos backlogs Mobile, Java, IoT/IA e no serviço de alertas .NET. As features de governança/entrega, modelagem física de banco, PL/SQL, infraestrutura/CI-CD, testes unitários e observabilidade são atividades técnicas ou operacionais; seus backlogs não definem, neste repositório, oráculos completos de comportamento funcional de usuário. Não são apresentadas como funcionalidades já testadas por esta matriz.

| Feature descrita nos backlogs do produto | Casos relacionados |
|---|---|
| Mobile 01 — Arquitetura UI, Design System e Navegação por Abas | TC-03 |
| Mobile 02 — Autenticação JWT, Sessão Segura e Cache Offline Resiliente | TC-01–03, TC-14–16 |
| Mobile 03 — CRUD Completo de Chamados Urbanos e Geolocalização GPS | TC-04–07, TC-17 |
| Mobile 04 — Engajamento Cidadão, Votação Comunitária e Documentação/Entrega | TC-08–10, TC-18 |
| Java 01 — Modelagem de Domínio JPA, migrations e Oracle | TC-04–08, como comportamento observado pela API; não valida schema ou migrations diretamente |
| Java 02 — Segurança Stateless, JWT e RBAC | TC-01–03, TC-15–16, TC-19 |
| Java 03 — Regras de negócio, DTOs e endpoints REST | TC-04–09, TC-14, TC-18–19 |
| Java 04 — RabbitMQ, triagem com IA e agregação de votos | TC-09, TC-11, TC-18, TC-20; processamento interno de filas não é inferido pela resposta HTTP |
| Disruptive Architectures 01 — Sensoriamento ESP32/MQTT | TC-12 |
| Disruptive Architectures 02 — IA generativa e visão computacional | TC-11, TC-20 |
| Disruptive Architectures 03 — Integração de alertas | TC-12–13; vínculo entre serviços precisa ser confirmado |
| .NET 01 — API de alertas/notificações municipais | TC-13 |

O nome “Radar” aparece no backlog como feed/relatório analítico, mas não há contrato de tela/API, filtros de localização, conjunto de dados ou resultado esperado suficiente para um caso de radar independente. A cobertura de feed e filtros está em TC-05; a lacuna de radar deve ser resolvida antes de declarar esse comportamento homologado.

### Features técnicas e demais itens de backlog

| Disciplina | Feature | Tratamento nesta matriz |
|---|---|---|
| Database Advanced | Modelagem relacional/3FN e Oracle | TC-04–08 observam efeitos da API; o schema não é verificável por caixa-preta sem contrato externo. |
| Database Advanced | Packages, procedures e functions PL/SQL | Camada interna; não há contrato funcional de entrada/saída no repositório. |
| Database Advanced | Triggers e auditoria DML | Camada interna; histórico visível é coberto em TC-08, não se presume tabela nem detalhe interno. |
| Database Advanced | MongoDB e relatórios analíticos | O backlog cita três relatórios, mas não há dataset, tela/API ou resultados esperados publicados; caso bloqueado até disponibilizar esse oráculo. |
| DevOps | Docker/Compose, IaC/Azure e CI/CD | Features de infraestrutura e operação, não comportamentos funcionais da aplicação para cidadão/gestor. |
| .NET | Observabilidade (métricas, health checks e logs) | Feature operacional; não é critério de aceitação funcional de usuário nesta matriz. |
| .NET | Suíte de testes xUnit | Teste de componente/unidade, explicitamente diferente de teste funcional de sistema caixa-preta. |
| Disruptive Architectures | Documentação técnica e entrega | Entregável documental, não comportamento funcional do sistema. |
| Compliance | Governança Scrum, matriz de testes, Azure Test Plans e rastreabilidade | Entregáveis/processo de QA, não funcionalidades de CitizenTech a serem testadas como usuário final. |

Assim, “cobertura por Feature” refere-se às Features funcionais do produto e integrações descritas nos backlogs. A existência de 24 Features de disciplina não significa 24 funcionalidades externas testáveis: várias são itens de infraestrutura, arquitetura ou processo. Os itens sem contrato e oráculo estão explicitamente identificados acima em vez de receberem casos com resultados inventados.

## 4. Divergências e limites que afetam a execução

1. **Rotas:** a coleção usa `/api/auth/...` e `/api/chamados/...`; o backlog Java descreve rotas sem prefixo `/api`. A coleção usa `/votos`; o PBI Java descreve `/chamados/{id}/apoiar`. Não escolher uma rota como contrato final sem confirmação.
2. **Status inicial:** a coleção espera `ABERTO`; o backlog Java espera `PENDENTE`. A coleção/Postman e Mobile também usam nomenclaturas diferentes das etapas descritas no histórico Java. TC-04 e TC-08 não devem ser aprovados quanto ao status inicial/timeline até a regra ser unificada.
3. **Cadastro:** o exemplo Postman contém `nome`, `email`, `senha`, `cargo` e `telefone`; o PBI Mobile descreve `nome`, `email`, `senha` e `bairro`. Confirmar o contrato de cadastro que será homologado.
4. **Alertas .NET:** o backlog informa região, severidade e HTTP `201` com identificador, mas não inclui neste repositório a rota e o schema do request. TC-13 depende desses dados.
5. **Serviços Mobile, IoT, IA e .NET:** não há implementação do produto nem ambiente de execução neste repositório. As respostas funcionais derivadas dos backlogs são critérios planejados, não resultados observados.

## 5. Preparação geral

1. Executar em ambiente de QA autorizado e isolado; o ambiente Postman define `baseUrl` como `http://localhost:8080`.
2. Criar/usar contas de QA sem dados pessoais reais. A coleção fornece dados de exemplo: `Cidadão QA Teste`, `cidadao.qa@citizentech.org`, `SenhaForte@2026`, cargo `CIDADAO` e telefone `11987654321`. Confirmar se o e-mail está livre antes do cadastro.
3. Guardar os identificadores e o token retornados nas variáveis `usuarioId`, `chamadoId` e `jwtToken`, conforme a coleção.
4. Para cenários de permissão, preparar usuários de teste com os papéis `CIDADAO`, `GESTOR` e `ADMIN`, descritos no backlog Java.
5. Para feed, filtros, edição/exclusão, voto e timeline, preparar chamados de QA com proprietário, categoria, status e histórico conhecidos.
6. Usar `categoriaId: 1` e o endereço/foto do exemplo Postman somente se existirem no ambiente. Para os cenários mobile, conceder ou negar permissões quando indicado.
7. Para IoT, IA e alertas, usar simuladores/dados autorizados. O limiar crítico do sensor deve vir da configuração real do sistema; não há valor numérico definido nos arquivos consultados.
8. Não executar os casos afetados pelas divergências da seção 4 como aprovação final até que o responsável pelo produto confirme o contrato.

### Dados de referência existentes na automação

Cadastro de exemplo: `nome: "Cidadão QA Teste"`, `email: "cidadao.qa@citizentech.org"`, `senha: "SenhaForte@2026"`, `cargo: "CIDADAO"`, `telefone: "11987654321"`.

Chamado de exemplo: título `Bueiro Entupido Causando Alagamento`; descrição `Bueiro coberto por entulho e folhas após chuva forte.`; endereço `Rua Augusta, 500`; `categoriaId: 1`; foto em `fotoUrl`. A automação não fornece GPS em latitude/longitude nem um upload multipart; esses inputs vêm dos critérios do backlog Mobile e devem ser coletados pelo aplicativo no ambiente.

## 6. Sumário dos Test Cases

| ID | Caso | Tipo | Feature principal |
|---|---|---|---|
| TC-01 | Cadastro válido de cidadão | Positivo | Autenticação |
| TC-02 | Login válido e emissão de token | Positivo | Autenticação |
| TC-03 | Restauração da sessão e navegação pelas telas | Positivo | Sessão e navegação |
| TC-04 | Criar chamado com localização e evidência | Positivo | CRUD, GPS e foto |
| TC-05 | Filtrar feed por categoria e status | Positivo | Feed |
| TC-06 | Editar chamado próprio | Positivo | CRUD |
| TC-07 | Excluir chamado próprio com confirmação | Positivo | CRUD |
| TC-08 | Alterar status como gestor e consultar timeline | Positivo | Gestão e histórico |
| TC-09 | Apoiar chamado com voto comunitário | Positivo | Engajamento |
| TC-10 | Consultar feed offline via cache | Positivo | Resiliência mobile |
| TC-11 | Classificar imagem urbana válida | Positivo | IA |
| TC-12 | Publicar telemetria e gerar alerta em nível crítico | Positivo | IoT/MQTT |
| TC-13 | Despachar alerta municipal por região e severidade | Positivo | Notificações .NET |
| TC-14 | Rejeitar cadastro duplicado ou inválido | Negativo | Autenticação/validação |
| TC-15 | Rejeitar login com senha incorreta | Negativo | Autenticação |
| TC-16 | Impedir rota privada sem sessão válida | Negativo | Autenticação/autorização |
| TC-17 | Tratar localização negada ou fora da área atendida | Negativo | GPS e restrição geográfica |
| TC-18 | Impedir voto repetido na mesma ocorrência | Negativo | Engajamento |
| TC-19 | Impedir cidadão de alterar status de chamado | Negativo | RBAC |
| TC-20 | Rejeitar imagem sem relação com zeladoria | Negativo | Validação de imagem |

## 7. Casos detalhados

### TC-01 — Cadastro válido de cidadão

**Tipo:** Positivo  
**Feature:** Autenticação JWT / cadastro.

- **Objetivo:** Validar o cadastro e a identificação do novo cidadão.
- **Preparação:** API disponível; usar e-mail de QA ainda não cadastrado. Resolver antes a diferença entre os campos do PBI Mobile e do corpo da automação.
- **Inputs:** Request de cadastro conforme contrato aprovado. Para reproduzir a automação: `POST /api/auth/register`, JSON com os campos de referência da seção 5.
- **Outputs esperados:** A coleção espera HTTP `201 Created` e propriedade `id` na resposta, armazenada em `usuarioId`. A coleção não testa `bairro`.

| Passo | Ação do testador | Resposta esperada do sistema |
|---|---|---|
| 1 | Enviar o cadastro válido pelo fluxo/endpoint do ambiente. | O sistema aceita o cadastro; na rota e payload da coleção, responde `201 Created`. |
| 2 | Examinar o corpo da resposta e armazenar o identificador retornado. | A resposta da coleção contém `id`; o valor fica disponível em `usuarioId`. |
| 3 | Registrar o resultado e os campos efetivamente enviados. | Ficam rastreáveis o status e o identificador; nenhuma mensagem não especificada é presumida. |

### TC-02 — Login válido e emissão de token

**Tipo:** Positivo  
**Feature:** Autenticação JWT.

- **Objetivo:** Confirmar login com credenciais válidas e emissão de token.
- **Preparação:** Conta criada e ativa no ambiente.
- **Inputs:** `POST /api/auth/login` conforme a coleção, com e-mail e senha da conta de QA.
- **Outputs esperados:** HTTP `200 OK`, propriedade `token` presente e valor armazenado em `jwtToken`. A automação também mede resposta inferior a 800 ms; esse limite é uma asserção de desempenho e não critério funcional deste caso.

| Passo | Ação do testador | Resposta esperada do sistema |
|---|---|---|
| 1 | Enviar o login com credenciais corretas. | A coleção espera HTTP `200 OK`. |
| 2 | Examinar o JSON e armazenar o token retornado em `jwtToken`. | Existe a propriedade `token`, conforme a automação. |
| 3 | Registrar o tempo observado separadamente, se executado pelo Postman. | O limite de 800 ms é reportado como medição de desempenho, sem alterar o resultado funcional. |

### TC-03 — Restauração da sessão e navegação pelas telas

**Tipo:** Positivo  
**Feature:** UI, perfil, sessão segura e navegação Mobile.

- **Objetivo:** Confirmar a navegação entre telas, a persistência da sessão e a visualização/edição do perfil do cidadão.
- **Preparação:** Login válido; token persistido pelo aplicativo no armazenamento local.
- **Inputs:** Fechar e reabrir o app com a mesma sessão; navegar pelas telas citadas no backlog Mobile (feed, radar/filtros, novo chamado, detalhe, meus chamados, perfil e sobre).
- **Outputs esperados:** A sessão é restaurada; as telas previstas são navegáveis; o perfil permite visualizar os dados e salvar uma alteração permitida; a opção de sair encerra a sessão. A interface respeita as áreas seguras do dispositivo. O backlog não define tela inicial nem mensagens específicas. Rotas privadas sem sessão são testadas no TC-16.

| Passo | Ação do testador | Resposta esperada do sistema |
|---|---|---|
| 1 | Fazer login no aplicativo com a conta de QA. | A autenticação é concluída e a sessão fica ativa. |
| 2 | Encerrar e reabrir o aplicativo sem limpar os dados locais. | O app valida/restaura a sessão persistida. |
| 3 | Navegar pelas telas listadas no input do caso e contar as telas distintas operacionais. | As telas são abertas sem erro de navegação; a meta do backlog é de pelo menos sete telas operacionais. |
| 4 | Em Perfil, conferir os dados cadastrais e alterar um campo com valor válido para a conta de QA. | O formulário permite a edição descrita no backlog e salva a alteração. |
| 5 | Reabrir o Perfil e verificar o valor alterado; inspecionar as telas em dispositivo com área segura/notch. | O novo valor é exibido e o conteúdo não fica sobreposto às áreas seguras; o backlog não define dimensões de tela específicas. |
| 6 | Acionar a opção de sair (`signOut`) e, em seguida, tentar abrir uma tela privada. | A sessão é encerrada e a navegação volta ao fluxo de autenticação. |

### TC-04 — Criar chamado com localização e evidência

**Tipo:** Positivo  
**Feature:** CRUD de chamados, GPS e anexos.

- **Objetivo:** Registrar uma ocorrência com localização e evidência fotográfica.
- **Preparação:** Usuário autenticado; permissão de localização concedida; categoria existente; GPS e câmera/galeria disponíveis.
- **Inputs:** Título, descrição e categoria de QA; localização obtida pelo dispositivo e foto capturada ou selecionada. O Postman fornece exemplo textual de chamado e espera HTTP `201`, mas não automatiza GPS nem upload do app.
- **Outputs esperados:** Chamado criado e localização/evidência associadas à solicitação. A coleção espera HTTP `201 Created`; o status inicial não é critério aprovado enquanto a divergência `ABERTO`/`PENDENTE` não for resolvida.

| Passo | Ação do testador | Resposta esperada do sistema |
|---|---|---|
| 1 | No app, iniciar novo chamado, preencher título/descrição/categoria e permitir a obtenção de localização. | O app obtém latitude/longitude e geocodifica endereço/bairro conforme o PBI Mobile. |
| 2 | Capturar/selecionar uma foto e conferir o preview; remover ou substituir a imagem e selecionar a evidência final. | O preview é exibido e as opções de remover/substituir funcionam antes do envio, conforme o PBI Mobile. |
| 3 | Enviar o chamado com a evidência final. | A imagem selecionada e a localização são incluídas no fluxo de criação. |
| 4 | Consultar o chamado em “Meus Chamados”. | A solicitação aparece como criada; no request automatizado correspondente, espera-se `201`. |
| 5 | Conferir o status inicial separadamente. | Registrar o valor observado; não aprovar o status até resolver `ABERTO` versus `PENDENTE`. |

### TC-05 — Filtrar feed por categoria e status

**Tipo:** Positivo  
**Feature:** Feed de ocorrências.

- **Objetivo:** Verificar filtros dinâmicos no feed por categoria e status.
- **Preparação:** Feed com registros de QA conhecidos para mais de uma categoria e status.
- **Inputs:** Selecionar uma categoria disponível (o backlog cita Vias, Iluminação, Saneamento e Limpeza) e um status existente no ambiente.
- **Outputs esperados:** O feed apresenta ocorrências compatíveis com os filtros selecionados. O backlog não define paginação, ordenação ou mensagem para resultado vazio.

| Passo | Ação do testador | Resposta esperada do sistema |
|---|---|---|
| 1 | Abrir o feed e registrar quais chamados correspondem à combinação de filtros escolhida. | O feed apresenta os registros disponíveis antes do filtro. |
| 2 | Selecionar uma categoria e um status existentes. | A lista é atualizada de acordo com os filtros selecionados. |
| 3 | Conferir cada item exibido com o conjunto de QA preparado. | Nenhum item fora da combinação escolhida é exibido; não avaliar ordenação/paginação sem requisito aprovado. |

### TC-06 — Editar chamado próprio

**Tipo:** Positivo  
**Feature:** CRUD de chamados.

- **Objetivo:** Atualizar os campos editáveis de uma solicitação criada pelo usuário.
- **Preparação:** Usuário autenticado; chamado próprio existente e aberto para edição.
- **Inputs:** Novo título, descrição e categoria válidos, campos citados no PBI Mobile.
- **Outputs esperados:** Os dados alterados são exibidos no chamado após salvar. O backlog não fornece rota ou código HTTP para atualização mobile.

| Passo | Ação do testador | Resposta esperada do sistema |
|---|---|---|
| 1 | Abrir “Meus Chamados” e selecionar um chamado próprio. | O app mostra a opção/tela de edição descrita no backlog. |
| 2 | Alterar título, descrição e categoria e salvar. | O sistema aceita a atualização. |
| 3 | Reabrir o detalhe do chamado. | Os valores exibidos correspondem aos novos valores enviados. |

### TC-07 — Excluir chamado próprio com confirmação

**Tipo:** Positivo  
**Feature:** CRUD de chamados.

- **Objetivo:** Excluir uma solicitação própria mediante confirmação.
- **Preparação:** Chamado descartável de QA criado pelo usuário autenticado.
- **Inputs:** Selecionar exclusão e confirmar no diálogo. A coleção aceita `DELETE /api/chamados/{{chamadoId}}` com HTTP `200` ou `204`.
- **Outputs esperados:** A solicitação é removida; o app pede confirmação antes da exclusão. A resposta automatizada aceita `200 OK` ou `204 No Content`.

| Passo | Ação do testador | Resposta esperada do sistema |
|---|---|---|
| 1 | Abrir o chamado de QA e acionar excluir. | O sistema apresenta o diálogo de confirmação descrito no backlog. |
| 2 | Confirmar a exclusão. | O chamado é removido; a automação aceita HTTP `200` ou `204`. |
| 3 | Atualizar “Meus Chamados”. | O chamado excluído deixa de aparecer na lista. |

### TC-08 — Alterar status como gestor e consultar timeline

**Tipo:** Positivo  
**Feature:** Gestão de chamados e histórico.

- **Objetivo:** Confirmar que um gestor altera o status e que a transição fica visível no histórico/timeline.
- **Preparação:** Chamado de QA existente; sessão com papel `GESTOR`; estado atual do chamado anotado antes do teste.
- **Inputs:** `PATCH /api/chamados/{{chamadoId}}/status` com `{"status":"EM_EXECUCAO","observacoes":"Equipe de desobstrução de galerias enviada ao local."}`, conforme a coleção; o prefixo `/api` está sujeito à divergência documentada na seção 4.
- **Outputs esperados:** A coleção espera HTTP `200` e `status: EM_EXECUCAO`; o backlog Java exige registro de cada transição no histórico. A nomenclatura da timeline Mobile deve ser compatibilizada com os estados Java antes do aceite.

| Passo | Ação do testador | Resposta esperada do sistema |
|---|---|---|
| 1 | Autenticar como gestor e consultar `GET /api/chamados/{{chamadoId}}`, anotando o status atual. | A coleção espera HTTP `200` e propriedades `id`, `titulo`, `status` e `dtAbertura` na resposta. |
| 2 | Solicitar a alteração para `EM_EXECUCAO` no endpoint de status configurado no ambiente. | A coleção espera HTTP `200` e retorno do status solicitado. |
| 3 | Consultar novamente o chamado e abrir sua timeline. | A alteração aparece no estado/histórico conforme o backlog; registrar a representação observada sem equiparar estados divergentes automaticamente. |

### TC-09 — Apoiar chamado com voto comunitário

**Tipo:** Positivo  
**Feature:** Engajamento e votação comunitária.

- **Objetivo:** Registrar apoio de cidadão em ocorrência existente.
- **Preparação:** Cidadão autenticado e chamado de QA existente, ainda não apoiado por essa conta.
- **Inputs:** Acionar “+1 Apoio” no detalhe. A coleção usa `POST /api/chamados/{{chamadoId}}/votos` sem body e aceita HTTP `200` ou `201`; o PBI Java descreve outra rota.
- **Outputs esperados:** A automação aceita `200` ou `201`; o backlog Mobile espera incremento visual do apoio. A rota final precisa ser confirmada conforme seção 4.

| Passo | Ação do testador | Resposta esperada do sistema |
|---|---|---|
| 1 | Abrir o detalhe de um chamado ainda não apoiado. | O detalhe exibe a ação de apoio conforme o PBI Mobile. |
| 2 | Acionar “+1 Apoio”. | O sistema registra o voto; a automação aceita HTTP `200` ou `201` na rota nela configurada. |
| 3 | Conferir o contador exibido. | O incremento visual imediato descrito pelo backlog é apresentado. |

### TC-10 — Consultar feed offline via cache

**Tipo:** Positivo  
**Feature:** Cache offline resiliente.

- **Objetivo:** Confirmar que chamados previamente carregados continuam visíveis quando há falha de conexão.
- **Preparação:** Carregar o feed online pelo menos uma vez; confirmar que há chamados de QA em cache.
- **Inputs:** Interromper conexão ou simular falha/timeout de rede e abrir/atualizar o feed.
- **Outputs esperados:** O app usa os últimos chamados armazenados no cache local e apresenta banner informando modo offline. Não se presume sincronização de escritas offline.

| Passo | Ação do testador | Resposta esperada do sistema |
|---|---|---|
| 1 | Com conexão, carregar o feed com chamados de QA. | O feed é exibido e seus últimos chamados ficam disponíveis para leitura offline. |
| 2 | Interromper a conexão e solicitar novamente o feed. | O app apresenta os dados em cache em vez de tela branca de erro. |
| 3 | Conferir a indicação de conectividade. | O banner sutil de modo offline descrito no backlog aparece. |

### TC-11 — Classificar imagem urbana válida

**Tipo:** Positivo  
**Feature:** Microsserviço de IA e visão computacional.

- **Objetivo:** Verificar a análise de imagem relacionada à zeladoria urbana.
- **Preparação:** Serviço IA disponível e imagem de QA que retrate ocorrência urbana; endpoint do backlog disponível em `/api/v1/analyze-image`.
- **Inputs:** Enviar imagem conforme contrato ativo (multipart/form-data ou URL; ambas as opções aparecem no backlog).
- **Outputs esperados:** JSON estruturado com `categoria_sugerida`, `gravidade` e `resumo`/justificativa; valores de gravidade pertencem a `BAIXA`, `MEDIA`, `ALTA` ou `CRITICA`. O backlog não especifica a classificação correta de uma imagem de exemplo.

| Passo | Ação do testador | Resposta esperada do sistema |
|---|---|---|
| 1 | Enviar a imagem de QA pelo método de entrada suportado. | O serviço aceita a solicitação para análise. |
| 2 | Examinar o JSON de resposta. | Existem os campos de categoria, gravidade e resumo/justificativa descritos no backlog. |
| 3 | Validar o valor de gravidade. | O valor pertence ao conjunto definido; não se presume categoria ou prioridade específica sem oráculo aprovado. |

### TC-12 — Publicar telemetria e gerar alerta em nível crítico

**Tipo:** Positivo  
**Feature:** Sensoriamento ESP32/MQTT e integração de alertas.

- **Objetivo:** Verificar publicação de telemetria pelo sensor e emissão do alerta quando o nível atinge o patamar crítico configurado.
- **Preparação:** ESP32/Wokwi conectado ao broker de QA; tópico de referência `citizentech/sensores/bueiro`; limiar crítico obtido da configuração aprovada.
- **Inputs:** Leitura simulada que atinja o limiar crítico. O backlog define campos `deviceId`, `distancia_cm`, `nivel_critico` e `timestamp`, mas não define um valor numérico para o limiar.
- **Outputs esperados:** Mensagem JSON publicada periodicamente com os campos descritos e alerta emitido ao atingir o limiar crítico. A integração exata do alerta ao backend deve estar disponível no ambiente.

| Passo | Ação do testador | Resposta esperada do sistema |
|---|---|---|
| 1 | Iniciar o circuito/simulador com leitura abaixo do limiar configurado. | O sensor publica telemetria JSON no tópico documentado. |
| 2 | Conferir a presença de `deviceId`, `distancia_cm`, `nivel_critico` e `timestamp`. | Os quatro campos definidos no backlog estão presentes. |
| 3 | Simular leitura que atinja o limiar crítico configurado. | O sistema emite o alerta previsto; registra-se a evidência recebida no componente integrado. |

### TC-13 — Despachar alerta municipal por região e severidade

**Tipo:** Positivo  
**Feature:** API de alertas/notificações municipais (.NET).

- **Objetivo:** Confirmar a criação de um alerta direcionado a uma região e severidade.
- **Preparação:** Serviço de notificação disponível; contrato OpenAPI/Swagger do ambiente consultado para obter rota e schema, ausentes nos arquivos deste repositório.
- **Inputs:** Request válido conforme contrato publicado, com região/bairro e uma severidade descrita no backlog: `Informativo`, `Alerta` ou `Emergência`.
- **Outputs esperados:** HTTP `201 Created` e identificador único do despacho, conforme critério de aceite do backlog.

| Passo | Ação do testador | Resposta esperada do sistema |
|---|---|---|
| 1 | Consultar a documentação ativa e enviar alerta válido para uma região de QA. | O serviço processa os critérios de região e severidade. |
| 2 | Examinar a resposta. | HTTP `201 Created` e identificador de despacho conforme o backlog. |
| 3 | Registrar região, severidade e ID retornados. | O resultado fica rastreável; não se presume entrega por canal (push, SMS ou outro) não especificado. |

### TC-14 — Rejeitar cadastro duplicado ou inválido

**Tipo:** Negativo  
**Feature:** Autenticação e validação.

- **Objetivo:** Cobrir duplicidade de e-mail e entrada inválida de cadastro, cenários indicados no backlog Compliance.
- **Preparação:** Conta de QA já existente para duplicidade; outro e-mail não cadastrado para os subcasos de validação.
- **Inputs:** Executar separadamente: (a) cadastro repetido com o mesmo e-mail; (b) campos de cadastro vazios; (c) e-mail malformado ou senha que não atenda à validação de força configurada na aplicação. O limite de força não é definido nos arquivos.
- **Outputs esperados:** Requisições inválidas/duplicadas são rejeitadas e não criam conta. Código e formato da mensagem não definidos; não presumir `409` ou `400`.

| Passo | Ação do testador | Resposta esperada do sistema |
|---|---|---|
| 1 | Reenviar cadastro com e-mail existente. | O cadastro duplicado é rejeitado sem criar uma segunda conta. |
| 2 | Enviar cadastro vazio usando e-mail ainda não cadastrado. | O sistema não aceita a entrada vazia. |
| 3 | Enviar e-mail inválido e senha que a própria validação da aplicação classifique como insuficiente. | A validação impede o cadastro; registrar o resultado sem presumir regra de tamanho ou mensagem. |

### TC-15 — Rejeitar login com senha incorreta

**Tipo:** Negativo  
**Feature:** Autenticação.

- **Objetivo:** Validar a rejeição de credencial inválida.
- **Preparação:** Conta de QA existente.
- **Inputs:** E-mail existente e senha incorreta em `POST /api/auth/login` conforme a coleção; confirmar a rota final, pois o backlog Java omite o prefixo `/api`.
- **Outputs esperados:** HTTP `401 Unauthorized`, especificado no PBI Java para credenciais inválidas; nenhum token deve ser emitido.

| Passo | Ação do testador | Resposta esperada do sistema |
|---|---|---|
| 1 | Enviar login com e-mail válido e senha incorreta. | O sistema rejeita a autenticação; o backlog Java especifica HTTP `401`. |
| 2 | Examinar a resposta. | Não há token de acesso utilizável. |
| 3 | Registrar corpo e código observados. | A mensagem é evidência observada, não critério, até existir contrato de erro aprovado. |

### TC-16 — Impedir rota privada sem sessão válida

**Tipo:** Negativo  
**Feature:** Autenticação e proteção de rotas.

- **Objetivo:** Impedir navegação para áreas privadas sem login ou após expiração/invalidade da sessão.
- **Preparação:** Dispositivo/app sem sessão ativa; para a variação de expiração, token inválido/expirado controlado pelo ambiente.
- **Inputs:** Abrir rota privada sem autenticar ou repetir request protegido com token inválido.
- **Outputs esperados:** No app, usuário deslogado vê somente o stack de autenticação. Para HTTP `401`, o interceptor deve expurgar a sessão e redirecionar ao login, conforme PBI Mobile.

| Passo | Ação do testador | Resposta esperada do sistema |
|---|---|---|
| 1 | Sem login, tentar abrir uma rota privada. | A rota privada não é exibida; permanece disponível apenas o stack de autenticação. |
| 2 | Com sessão expirada/inválida, acionar um fluxo protegido. | Ao receber `401`, o app remove a sessão e direciona o usuário para login. |
| 3 | Tentar novamente a rota privada sem autenticar. | O acesso continua impedido. |

### TC-17 — Tratar localização negada ou fora da área atendida

**Tipo:** Negativo  
**Feature:** Geolocalização GPS.

- **Objetivo:** Verificar os dois cenários de borda citados nos backlogs: recusa de permissão do GPS e tentativa de localização fora dos limites atendidos.
- **Preparação:** Usuário autenticado; dispositivo de QA com permissão de GPS controlável; limite geográfico oficial e ponto de teste externo fornecidos pelo responsável do produto.
- **Inputs:** Executar separadamente (a) negar permissão de localização; (b) iniciar chamado com posição de teste fora do limite geográfico configurado. Não inventar coordenadas ou fronteiras.
- **Outputs esperados:** (a) A recusa é tratada graciosamente, sem falha do app; o fluxo alternativo não está especificado. (b) A restrição geográfica é aplicada, sem registrar chamado fora da área. Código HTTP e mensagem não definidos.

| Passo | Ação do testador | Resposta esperada do sistema |
|---|---|---|
| 1 | Cenário A: iniciar novo chamado e negar a permissão de localização. | O app trata a recusa sem travar ou encerrar inesperadamente. |
| 2 | Registrar as opções oferecidas após a recusa. | Não exigir fallback manual ou envio sem coordenadas, pois isso não está especificado. |
| 3 | Cenário B: com o limite oficial carregado, tentar registrar chamado usando o ponto externo de QA. | A solicitação fora da área não é registrada; a resposta/código são anotados sem presumir formato. |

### TC-18 — Impedir voto repetido na mesma ocorrência

**Tipo:** Negativo  
**Feature:** Apoio comunitário.

- **Objetivo:** Garantir a regra de bloqueio de votos repetidos para o mesmo cidadão e chamado, explicitada no PBI Java.
- **Preparação:** Cidadão autenticado e chamado já apoiado uma vez pela mesma conta.
- **Inputs:** Repetir a ação “+1 Apoio” no mesmo chamado.
- **Outputs esperados:** O segundo voto não é registrado e não gera segundo incremento. Código HTTP e mensagem de rejeição não especificados.

| Passo | Ação do testador | Resposta esperada do sistema |
|---|---|---|
| 1 | Registrar o primeiro apoio no chamado conforme TC-09. | O primeiro apoio é aceito. |
| 2 | Tentar apoiar novamente com a mesma conta. | O sistema bloqueia voto repetido, conforme o PBI Java. |
| 3 | Aguardar ao menos um ciclo de flush do agregador (o backlog Java descreve `fixedDelay = 3000 ms`) e consultar o contador/dados visíveis. | Não ocorre segundo incremento atribuível à mesma conta; não reprovar por leitura imediata antes da agregação assíncrona. |

### TC-19 — Impedir cidadão de alterar status

**Tipo:** Negativo  
**Feature:** RBAC e gestão de chamados.

- **Objetivo:** Verificar que um usuário `CIDADAO` não altera status reservado à gestão municipal.
- **Preparação:** Chamado existente; autenticar com conta de papel `CIDADAO` e registrar o status atual.
- **Inputs:** Solicitar alteração para `EM_EXECUCAO` no fluxo de gestão. A coleção contém request de atualização, mas não testa papéis; o PBI Java determina que atualização de status é restrita a agentes municipais/gestores.
- **Outputs esperados:** Operação não autorizada e status inalterado. O código HTTP não é fixado pelos arquivos para este caso.

| Passo | Ação do testador | Resposta esperada do sistema |
|---|---|---|
| 1 | Consultar o chamado como cidadão e anotar o status. | O sistema apresenta o status antes da tentativa. |
| 2 | Tentar alterar o status com a sessão `CIDADAO`. | A operação é recusada pelo controle de papéis. |
| 3 | Consultar novamente o chamado. | O status permanece igual ao valor anterior. |

### TC-20 — Rejeitar imagem sem relação com zeladoria

**Tipo:** Negativo  
**Feature:** IA e validação de imagens.

- **Objetivo:** Confirmar que imagem irrelevante é identificada como inadequada para uma ocorrência urbana.
- **Preparação:** Serviço de análise disponível; usar imagem de QA não sensível de tipo expressamente citado no backlog (por exemplo, uma selfie ou meme), sem conteúdo de terceiros.
- **Inputs:** Enviar imagem não relacionada à zeladoria ao fluxo/API aprovado de análise.
- **Outputs esperados:** `is_valid_incident: false` e recomendação para o cidadão enviar outra foto, conforme critérios de aceite do PBI. Não há código HTTP ou texto exato definidos.

| Passo | Ação do testador | Resposta esperada do sistema |
|---|---|---|
| 1 | Enviar a imagem irrelevante de QA ao fluxo de análise. | O serviço processa a imagem para validação. |
| 2 | Examinar a resposta estruturada. | O resultado indica `is_valid_incident: false`. |
| 3 | Conferir a orientação ao usuário. | É recomendada uma nova foto; não exigir texto literal não especificado. |

## 8. Registro de execução

Para cada execução, registrar ambiente, build/versão, data, dados utilizados, resultado (`Passed`, `Failed` ou `Blocked`) e evidência. Os casos desta matriz são especificações; nenhum foi executado contra o sistema nesta entrega.

- TC-01, TC-02, TC-04, TC-07, TC-09 e parte de TC-08 reproduzem as verificações de sucesso da coleção Postman.
- TC-03, TC-05–06, TC-08, TC-10–13 e TC-17–20 derivam de critérios de aceite dos backlogs; precisam do aplicativo/serviços correspondentes para execução.
- TC-01–02, TC-04, TC-07–09, TC-14–15 e TC-18–19 dependem da confirmação das rotas/payloads divergentes apontadas na seção 4; TC-04 e TC-08 também dependem da unificação dos estados do chamado.
- TC-12 requer a configuração real do limiar crítico e TC-13 requer o contrato da API .NET; sem esses dados, os casos não são executáveis de forma reprodutível.
- A asserção Postman de login inferior a 800 ms é suplementar e deve ser classificada como desempenho, não como resultado funcional.
