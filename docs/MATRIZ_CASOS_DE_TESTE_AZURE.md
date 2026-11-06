# 📋 Matriz de Casos de Testes Manuais - ZelaFix
> **Projeto:** ZelaFix - Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  
> **Padrão:** Azure Test Plans & Azure Boards (Caixa-Preta Funcional)  
> **Organização:** `ZelaFixGS` | **Projeto:** `ZelaFix`  

---

## 📊 Resumo Executivo da Matriz
- **Total de Casos de Teste:** 20
- **Casos Positivos (Caminho Feliz):** 13 (65%)
- **Casos Negativos (Validação & Exceções):** 7 (35%)

---

## 📑 Detalhamento Completo dos 20 Casos de Teste

### TC-01: [Positivo]: Cadastro de Cidadão Válido com Bairro Residencial
- **Tipo:** `Positivo` | **Prioridade:** `P1` | **Feature:** `Autenticação e Gestão de Usuários`
- **Objetivo:** Validar o processo de adesão de um novo cidadão na plataforma ZelaFix, assegurando integridade relacional.
- **Pré-condições:** Banco de dados Oracle ativo; e-mail não existente na base.
- **Dados de Entrada:** `{'nome': 'Enzo Okuizumi', 'email': 'enzo.cidadao@zelafix.org', 'senha': 'SenhaForte@2026', 'bairroId': 1}`
- **Resultado Esperado:** Status HTTP 201 Created; registro persistido na tabela USUARIO com senha criptografada em BCrypt.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Acessar a tela de cadastro no app mobile ZelaFix | Formulário exibido com campos limpos. |
| 2 | Preencher nome, e-mail, senha e selecionar o bairro | Campos validados com sucesso sem mensagens de erro. |
| 3 | Clicar no botão 'Cadastrar Cidadão' | Requisição POST /api/v1/auth/register enviada ao backend. |
| 4 | Verificar resposta do sistema | Mensagem de sucesso exibida e redirecionamento para tela de Login. |

---

### TC-02: [Negativo]: Tentativa de Cadastro com E-mail Duplicado
- **Tipo:** `Negativo` | **Prioridade:** `P1` | **Feature:** `Autenticação e Gestão de Usuários`
- **Objetivo:** Garantir a unicidade cadastral de e-mails, bloqueando duplicidades com resposta amigável.
- **Pré-condições:** Usuário 'enzo.cidadao@zelafix.org' previamente cadastrado.
- **Dados de Entrada:** `{'email': 'enzo.cidadao@zelafix.org', 'nome': 'Enzo Duplicado'}`
- **Resultado Esperado:** Status HTTP 409 Conflict; mensagem de erro orientando recuperação de senha.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Preencher o formulário com o e-mail já existente | Dados digitados sem bloqueio prévio no cliente. |
| 2 | Submeter o formulário de cadastro | API retorna HTTP 409 Conflict. |
| 3 | Verificar feedback na interface móvel | Alerta 'Este e-mail já está em uso'. |

---

### TC-03: [Positivo]: Autenticação de Cidadão e Emissão de Bearer Token JWT
- **Tipo:** `Positivo` | **Prioridade:** `P1` | **Feature:** `Autenticação e Gestão de Usuários`
- **Objetivo:** Validar a autenticação stateless e o recebimento de token JWT assinado.
- **Pré-condições:** Usuário cadastrado com credenciais válidas.
- **Dados de Entrada:** `{'email': 'enzo.cidadao@zelafix.org', 'senha': 'SenhaForte@2026'}`
- **Resultado Esperado:** Status HTTP 200 OK com payload contendo token JWT e tempo de expiração.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Informar e-mail e senha corretos na tela de login | Campos preenchidos e botão habilitado. |
| 2 | Pressionar 'Entrar no ZelaFix' | POST /api/v1/auth/login processado com sucesso. |
| 3 | Verificar armazenamento seguro | Token salvo no AsyncStorage e usuário direcionado à Home. |

---

### TC-04: [Negativo]: Autenticação com Senha Incorreta
- **Tipo:** `Negativo` | **Prioridade:** `P1` | **Feature:** `Autenticação e Gestão de Usuários`
- **Objetivo:** Assegurar que credenciais inválidas sejam rejeitadas sem expor detalhes internos.
- **Pré-condições:** Conta existente cadastrada.
- **Dados de Entrada:** `{'email': 'enzo.cidadao@zelafix.org', 'senha': 'SenhaErradaTotal'}`
- **Resultado Esperado:** Status HTTP 401 Unauthorized; mensagem 'E-mail ou senha inválidos'.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Inserir senha incorreta na tela de login | Campo senha aceita entrada mascarada. |
| 2 | Tentar autenticar | Mensagem amigável de credenciais inválidas exibida. |

---

### TC-05: [Positivo]: Realização de Logout e Revogação de Sessão Local
- **Tipo:** `Positivo` | **Prioridade:** `P2` | **Feature:** `Autenticação e Gestão de Usuários`
- **Objetivo:** Verificar a limpeza de tokens e término seguro de sessão.
- **Pré-condições:** Usuário logado no aplicativo.
- **Dados de Entrada:** `{'acao': 'clique_sair'}`
- **Resultado Esperado:** Token JWT expurgado do armazenamento local e redirecionamento para tela de login.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Navegar até a aba Perfil e clicar em 'Sair da Conta' | Confirmação de logout solicitada. |
| 2 | Confirmar logout | Token apagado e navegação resetada para tela inicial de autenticação. |

---

### TC-06: [Positivo]: Abertura de Chamado Urbano com Foto e Coordenadas GPS
- **Tipo:** `Positivo` | **Prioridade:** `P1` | **Feature:** `Gestão de Ocorrências e Zeladoria`
- **Objetivo:** Validar o fluxo completo de registro de problema urbano pelo cidadão com GPS e foto.
- **Pré-condições:** Usuário autenticado; permissão de câmera e localização concedida.
- **Dados de Entrada:** `{'titulo': 'Buraco na via', 'descricao': 'Cratera na faixa direita', 'categoriaId': 1, 'latitude': -23.5615, 'longitude': -46.6559}`
- **Resultado Esperado:** Status HTTP 201 Created; chamado persistido com status inicial 'ABERTO'.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Tocar na aba 'Novo Chamado' | GPS captura latitude e longitude automaticamente. |
| 2 | Anexar foto da câmera | Preview da imagem exibido na tela. |
| 3 | Selecionar categoria e digitar descrição | Campos validados com sucesso. |
| 4 | Confirmar envio do chamado | Chamado salvo com protocolo gerado e exibido no feed. |

---

### TC-07: [Negativo]: Tentativa de Registro com Campos Obrigatórios em Branco
- **Tipo:** `Negativo` | **Prioridade:** `P1` | **Feature:** `Gestão de Ocorrências e Zeladoria`
- **Objetivo:** Garantir a integridade dos dados impedindo chamados sem descrição ou categoria.
- **Pré-condições:** Usuário autenticado.
- **Dados de Entrada:** `{'titulo': '', 'descricao': '', 'categoriaId': None}`
- **Resultado Esperado:** HTTP 400 Bad Request; validação no cliente e servidor informando pendências.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Submeter formulário com campos em branco | Bordas dos campos destacadas em vermelho. |
| 2 | Verificar persistência | Nenhum chamado criado no banco de dados. |

---

### TC-08: [Negativo]: Registro com Coordenadas Fora dos Limites Municipais
- **Tipo:** `Negativo` | **Prioridade:** `P2` | **Feature:** `Gestão de Ocorrências e Zeladoria`
- **Objetivo:** Validar restrição geográfica impedindo chamados fora do município atendido.
- **Pré-condições:** Usuário autenticado.
- **Dados de Entrada:** `{'latitude': 0.0, 'longitude': 0.0}`
- **Resultado Esperado:** HTTP 422 Unprocessable Entity; mensagem de localização inválida.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Enviar coordenadas fora do município | Validação de geofencing rejeita o envio. |
| 2 | Checar mensagem | Alerta 'Localização fora da área de cobertura do ZelaFix'. |

---

### TC-09: [Positivo]: Filtragem de Chamados por Categoria no Feed
- **Tipo:** `Positivo` | **Prioridade:** `P2` | **Feature:** `Radar e Consulta de Ocorrências`
- **Objetivo:** Garantir a consulta responsiva e filtragem correta no feed comunitário.
- **Pré-condições:** Chamados de múltiplas categorias cadastrados.
- **Dados de Entrada:** `{'categoria': 'ILUMINACAO_PUBLICA'}`
- **Resultado Esperado:** Lista contendo apenas ocorrências da categoria selecionada.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Acessar feed e clicar no filtro 'Iluminação' | Feed atualiza instantaneamente. |
| 2 | Inspecionar cartões exibidos | 100% dos itens são de Iluminação Pública. |

---

### TC-10: [Positivo]: Busca Instantânea Textual de Ocorrências
- **Tipo:** `Positivo` | **Prioridade:** `P2` | **Feature:** `Radar e Consulta de Ocorrências`
- **Objetivo:** Validar busca por palavra-chave no feed de ocorrências.
- **Pré-condições:** Feed populado.
- **Dados de Entrada:** `{'termo': 'Paulista'}`
- **Resultado Esperado:** Exibição de ocorrências cujo título, descrição ou logradouro contenham o termo digitado.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Digitar 'Paulista' no campo de busca | Debounce filtra os cartões com sucesso. |

---

### TC-11: [Positivo]: Registro de Voto de Apoio em Ocorrência Coletiva
- **Tipo:** `Positivo` | **Prioridade:** `P1` | **Feature:** `Engajamento Cidadão e Votação`
- **Objetivo:** Permitir que cidadãos apoiem ocorrências existentes, aumentando a prioridade de atendimento.
- **Pré-condições:** Chamado aberto existente; cidadão logado que ainda não votou.
- **Dados de Entrada:** `{'chamadoId': 1}`
- **Resultado Esperado:** HTTP 200 OK; contador de votos incrementado em 1 unidade.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Abrir detalhe do chamado e tocar no botão 'Apoiar Chamado' | POST /api/v1/chamados/1/votos enviado. |
| 2 | Observar contador | Número de votos atualiza na tela e botão muda para 'Apoiado'. |

---

### TC-12: [Negativo]: Bloqueio de Voto Duplicado pelo Mesmo Cidadão
- **Tipo:** `Negativo` | **Prioridade:** `P2` | **Feature:** `Engajamento Cidadão e Votação`
- **Objetivo:** Assegurar que cada cidadão possa votar apenas uma vez em cada chamado.
- **Pré-condições:** Cidadão já registrou voto no chamado.
- **Dados de Entrada:** `{'chamadoId': 1}`
- **Resultado Esperado:** HTTP 409 Conflict ou toggle seguro; bloqueio de contagem adicional.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Tentar votar novamente no mesmo chamado | Sistema avisa que o voto já foi computado. |

---

### TC-13: [Positivo]: Transição de Status para 'EM_EXECUCAO' pelo Gestor Público
- **Tipo:** `Positivo` | **Prioridade:** `P1` | **Feature:** `Painel do Gestor e Ciclo de Vida`
- **Objetivo:** Validar avanço no ciclo de vida de chamado por usuário com perfil ADMIN/GESTOR.
- **Pré-condições:** Usuário autenticado com role ADMIN; chamado no status ABERTO.
- **Dados de Entrada:** `{'chamadoId': 1, 'novoStatus': 'EM_EXECUCAO'}`
- **Resultado Esperado:** Status atualizado e registro inserido na tabela HISTORICO_STATUS.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Gestor seleciona o chamado e altera status para 'EM_EXECUCAO' | PATCH enviado com token de gestor. |
| 2 | Verificar timeline | Data e autor da alteração gravados no histórico. |
| 3 | Consultar no app mobile | Cidadão visualiza status atualizado em amarelo. |

---

### TC-14: [Negativo]: Bloqueio de Cidadão Comum ao Tentar Alterar Status de Chamado
- **Tipo:** `Negativo` | **Prioridade:** `P1` | **Feature:** `Painel do Gestor e Ciclo de Vida`
- **Objetivo:** Assegurar que apenas gestores públicos possam modificar status de atendimento.
- **Pré-condições:** Usuário logado com role USER (Cidadão comum).
- **Dados de Entrada:** `{'novoStatus': 'CONCLUIDO'}`
- **Resultado Esperado:** HTTP 403 Forbidden; acesso negado pelo Spring Security.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Cidadão tenta invocar endpoint administrativo de alteração de status | HTTP 403 Forbidden retornado. |
| 2 | Checar status no banco | Status permanece inalterado. |

---

### TC-15: [Positivo]: Conclusão de Ocorrência ('CONCLUIDO') com Data de Fechamento
- **Tipo:** `Positivo` | **Prioridade:** `P1` | **Feature:** `Painel do Gestor e Ciclo de Vida`
- **Objetivo:** Homologar a finalização do atendimento de zeladoria urbana.
- **Pré-condições:** Chamado em status EM_EXECUCAO.
- **Dados de Entrada:** `{'novoStatus': 'CONCLUIDO'}`
- **Resultado Esperado:** Chamado atualizado para CONCLUIDO com timestamp de encerramento preenchido.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Gestor marca chamado como 'CONCLUIDO' | Chamado arquivado como atendido. |
| 2 | Verificar no banco de dados | Campo DATA_CONCLUSAO preenchido com SYSDATE. |

---

### TC-16: [Positivo]: Emissão de Alerta Automático de Alagamento via Sensor IoT
- **Tipo:** `Positivo` | **Prioridade:** `P1` | **Feature:** `Sensoriamento Urbano e IoT`
- **Objetivo:** Validar ingestão de dados de telemetria de sensores ESP32 via broker MQTT.
- **Pré-condições:** Broker MQTT ativo; sensor publicando telemetria crítica.
- **Dados de Entrada:** `{'topico': 'zelafix/sensores/bueiro_12', 'nivelAguaCm': 95.0}`
- **Resultado Esperado:** Notificação push e chamado de urgência gerado automaticamente.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Publicar payload MQTT simulando bueiro entupido com nível crítico | Backend processa a mensagem do broker. |
| 2 | Verificar fila de alertas | Alerta crítico disparado aos gestores da região. |

---

### TC-17: [Positivo]: Classificação de Severidade de Ocorrência por IA Generativa
- **Tipo:** `Positivo` | **Prioridade:** `P2` | **Feature:** `Inteligência Artificial e Triagem`
- **Objetivo:** Validar triagem automática de imagens urbanas usando visão computacional e IA.
- **Pré-condições:** Microsserviço de IA ativo com modelo de visão configurado.
- **Dados de Entrada:** `{'imagem': 'fio_eletrico_caido.jpg'}`
- **Resultado Esperado:** Retorno de classificação 'ALTA_URGENCIA' e tag 'Risco à Vida'.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Enviar foto de fio caído à API de IA | Modelo analisa a imagem e identifica o risco elétrico. |
| 2 | Verificar metadata do chamado | Score de urgência atribuído automaticamente como 0.95. |

---

### TC-18: [Negativo]: Rejeição de Imagem Irrelevante / Não-Urbana por IA
- **Tipo:** `Negativo` | **Prioridade:** `P2` | **Feature:** `Inteligência Artificial e Triagem`
- **Objetivo:** Evitar spam e imagens descontextualizadas no banco de zeladoria urbana.
- **Pré-condições:** Serviço de triagem por IA ativo.
- **Dados de Entrada:** `{'imagem': 'meme_internet.jpg'}`
- **Resultado Esperado:** Classificação 'CONTEUDO_IRRELEVANTE'; alerta ao cidadão solicitando foto do local.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Submeter imagem de desenho/meme sem relação urbana | IA detecta ausência de elementos de infraestrutura. |
| 2 | Checar resposta | Feedback 'Por favor, envie uma foto nítida do problema urbano'. |

---

### TC-19: [Positivo]: Abertura do App em Modo Offline e Exibição de Cache Local
- **Tipo:** `Positivo` | **Prioridade:** `P1` | **Feature:** `Resiliência e Cache Offline`
- **Objetivo:** Garantir a disponibilidade do aplicativo mesmo em caso de perda temporária de internet.
- **Pré-condições:** Dados previamente sincronizados no AsyncStorage.
- **Dados de Entrada:** `{'conexao': 'OFFLINE'}`
- **Resultado Esperado:** Interface abre normalmente exibindo banner 'Modo Offline' e dados em cache.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Ativar Modo Avião no smartphone e abrir o app ZelaFix | App inicializa sem crash. |
| 2 | Visualizar tela inicial | Lista de ocorrências salvas localmente é exibida com badge 'Offline'. |

---

### TC-20: [Positivo]: Sincronização Automática ao Restabelecer Conectividade
- **Tipo:** `Positivo` | **Prioridade:** `P1` | **Feature:** `Resiliência e Cache Offline`
- **Objetivo:** Homologar a transição suave de volta ao modo online com revalidação de dados.
- **Pré-condições:** App aberto em modo offline.
- **Dados de Entrada:** `{'conexao': 'ONLINE_RESTABELECIDA'}`
- **Resultado Esperado:** Banner offline desaparece e novas ocorrências do servidor são incorporadas ao feed.

| Passo | Ação do Testador | Resposta Esperada do Sistema |
| :---: | :--- | :--- |
| 1 | Desativar Modo Avião com o app aberto | NetInfo detecta reconexão. |
| 2 | Aguardar sincronização | Feed atualizado automaticamente com as novidades da API. |

---
