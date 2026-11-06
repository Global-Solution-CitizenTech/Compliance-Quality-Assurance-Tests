# 🏛️ Matriz de Casos de Testes Manuais — CitizenTech
> **Projeto:** CitizenTech — Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  
> **Disciplina:** Compliance, Quality Assurance & Tests (2TDSPG)  
> **Norma:** Padrão Oficial Azure Boards & Test Plans (Cobertura Caixa-Preta 100%)

---

## 📊 Sumário Executivo de Cobertura de Testes

- **Total de Casos de Teste Mapeados:** 20
- **Casos Positivos (Caminho Feliz):** 13 (65%)
- **Casos Negativos (Exceções / Borda):** 7 (35%)
- **Técnica Aplicada:** Dados de Entrada Controlados (Predefined Inputs)
- **Rastreabilidade:** 100% vinculado aos critérios de aceite das Features no Azure Boards

---

## 📋 Tabela Resumo dos Casos de Teste Estruturados por Feature

| ID | Título do Caso de Teste | Tipo | Feature de Referência | Prioridade |
| :---: | :--- | :---: | :--- | :---: |
| **TC-01** | TC-01 [Positivo]: Cadastro de Cidadão Válido com Bairro Residencial | 🟢 Positivo | Autenticação e Gestão de Usuários | Alta |
| **TC-02** | TC-02 [Negativo]: Tentativa de Cadastro com E-mail Duplicado | 🔴 Negativo | Autenticação e Gestão de Usuários | Alta |
| **TC-03** | TC-03 [Positivo]: Autenticação de Cidadão e Emissão de Bearer Token JWT | 🟢 Positivo | Autenticação e Gestão de Usuários | Alta |
| **TC-04** | TC-04 [Negativo]: Autenticação com Senha Incorreta | 🔴 Negativo | Autenticação e Gestão de Usuários | Alta |
| **TC-05** | TC-05 [Positivo]: Realização de Logout e Revogação de Sessão Local | 🟢 Positivo | Autenticação e Gestão de Usuários | Média |
| **TC-06** | TC-06 [Positivo]: Abertura de Chamado Urbano com Foto e Coordenadas GPS | 🟢 Positivo | Gestão de Ocorrências e Zeladoria | Alta |
| **TC-07** | TC-07 [Negativo]: Tentativa de Registro com Campos Obrigatórios em Branco | 🔴 Negativo | Gestão de Ocorrências e Zeladoria | Alta |
| **TC-08** | TC-08 [Negativo]: Registro com Coordenadas Fora dos Limites Municipais | 🔴 Negativo | Gestão de Ocorrências e Zeladoria | Média |
| **TC-09** | TC-09 [Positivo]: Filtragem de Chamados por Categoria no Feed | 🟢 Positivo | Radar e Consulta de Ocorrências | Média |
| **TC-10** | TC-10 [Positivo]: Busca Instantânea Textual de Ocorrências | 🟢 Positivo | Radar e Consulta de Ocorrências | Média |
| **TC-11** | TC-11 [Positivo]: Registro de Voto de Apoio em Ocorrência Coletiva | 🟢 Positivo | Engajamento Cidadão e Votação | Alta |
| **TC-12** | TC-12 [Negativo]: Bloqueio de Voto Duplicado pelo Mesmo Cidadão | 🔴 Negativo | Engajamento Cidadão e Votação | Alta |
| **TC-13** | TC-13 [Positivo]: Transição de Status para 'EM_EXECUCAO' pelo Gestor Público | 🟢 Positivo | Painel do Gestor e Ciclo de Vida | Alta |
| **TC-14** | TC-14 [Negativo]: Bloqueio de Cidadão Comum ao Tentar Alterar Status de Chamado | 🔴 Negativo | Painel do Gestor e Ciclo de Vida | Alta |
| **TC-15** | TC-15 [Positivo]: Conclusão de Ocorrência ('CONCLUIDO') com Data de Fechamento | 🟢 Positivo | Painel do Gestor e Ciclo de Vida | Média |
| **TC-16** | TC-16 [Positivo]: Emissão de Alerta Automático de Alagamento via Sensor IoT | 🟢 Positivo | Sensoriamento Urbano e IoT | Média |
| **TC-17** | TC-17 [Positivo]: Classificação de Severidade de Ocorrência por IA Generativa | 🟢 Positivo | Inteligência Artificial e Triagem | Média |
| **TC-18** | TC-18 [Negativo]: Rejeição de Imagem Irrelevante / Não-Urbana por IA | 🔴 Negativo | Inteligência Artificial e Triagem | Média |
| **TC-19** | TC-19 [Positivo]: Abertura do App em Modo Offline e Exibição de Cache Local | 🟢 Positivo | Resiliência e Cache Offline | Média |
| **TC-20** | TC-20 [Positivo]: Sincronização Automática ao Restabelecer Conectividade | 🟢 Positivo | Resiliência e Cache Offline | Média |

---

## 🔍 Detalhamento dos Casos de Testes com Dados Controlados e Passos

### 🧪 TC-01: TC-01 [Positivo]: Cadastro de Cidadão Válido com Bairro Residencial
- **Tipo:** 🟢 Positivo
- **Feature Vinculada:** Autenticação e Gestão de Usuários
- **Objetivo:** Validar o processo de adesão de um novo cidadão na plataforma CitizenTech, assegurando a consistência relacional na tabela USUARIO e integridade com a tabela BAIRRO.
- **Pré-condições (Preparação):** Sistema mobile ou Swagger em execução; banco de dados Oracle populado com bairros prévios.
- **Dados de Entrada Controlados (Inputs):**
  - `nome`: `Enzo Administrador QA`
  - `email`: `enzo.cidadao@citizentech.org`
  - `senha`: `SenhaForte@2026`
  - `confirmarSenha`: `SenhaForte@2026`
  - `telefone`: `(11) 98765-4321`
  - `bairroId`: `1`
  - `cargo`: `CIDADAO`
- **Resultado Esperado (Outputs):** Status HTTP 201 Created; ID do usuário gerado com sucesso; senha criptografada via BCrypt; perfil CIDADAO atribuído.

| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |
| :-: | :--- | :--- |
| 1 | `Acessar a tela inicial do aplicativo e clicar em 'Cadastre-se'` | Formulário de cadastro exibido com campos em branco e validações ativas. |
| 2 | `Informar nome completo, e-mail institucional e senha com confirmação` | Máscara de senha ativa e indicador de complexidade satisfeito. |
| 3 | `Selecionar o bairro de residência e informar o telefone celular` | Bairro validado contra a base de dados oficial municipal. |
| 4 | `Clicar no botão 'Concluir Cadastro'` | Alerta de sucesso exibido e redirecionamento para tela de Login. |

---

### 🧪 TC-02: TC-02 [Negativo]: Tentativa de Cadastro com E-mail Duplicado
- **Tipo:** 🔴 Negativo
- **Feature Vinculada:** Autenticação e Gestão de Usuários
- **Objetivo:** Verificar a resiliência do sistema contra duplicidade de e-mail (Constraint Unique na tabela USUARIO).
- **Pré-condições (Preparação):** Usuário 'enzo.cidadao@citizentech.org' previamente cadastrado na base.
- **Dados de Entrada Controlados (Inputs):**
  - `email`: `enzo.cidadao@citizentech.org`
  - `senha`: `OutraSenha@123`
- **Resultado Esperado (Outputs):** Status HTTP 409 Conflict ou 400 Bad Request; mensagem amigável 'E-mail já registrado no sistema'; nenhum registro órfão persistido.

| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |
| :-: | :--- | :--- |
| 1 | `Acessar o formulário de cadastro de novo usuário` | Formulário exibido pronto para entrada. |
| 2 | `Preencher dados utilizando e-mail já existente` | Campos preenchidos normalmente. |
| 3 | `Clicar em 'Concluir Cadastro'` | Validação rejeita o envio e exibe alerta: 'Este e-mail já está em uso por outro cidadão'. |

---

### 🧪 TC-03: TC-03 [Positivo]: Autenticação de Cidadão e Emissão de Bearer Token JWT
- **Tipo:** 🟢 Positivo
- **Feature Vinculada:** Autenticação e Gestão de Usuários
- **Objetivo:** Garantir a autenticação de credenciais válidas e a geração de Token JWT estruturado para proteção de rotas privadas.
- **Pré-condições (Preparação):** Conta de cidadão previamente homologada.
- **Dados de Entrada Controlados (Inputs):**
  - `email`: `enzo.cidadao@citizentech.org`
  - `senha`: `SenhaForte@2026`
- **Resultado Esperado (Outputs):** HTTP 200 OK; Payload JSON contendo campo 'token' com JWT válido (header.payload.signature) e objeto do usuário autenticado.

| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |
| :-: | :--- | :--- |
| 1 | `Acessar a tela de login do aplicativo` | Campos de e-mail e senha visíveis. |
| 2 | `Digitar as credenciais de teste válidas` | Validação de formato aceita as entradas. |
| 3 | `Clicar em 'Entrar no Sistema'` | Spinner de carregamento exibido; transição imediata para o Feed do Bairro. |

---

### 🧪 TC-04: TC-04 [Negativo]: Autenticação com Senha Incorreta
- **Tipo:** 🔴 Negativo
- **Feature Vinculada:** Autenticação e Gestão de Usuários
- **Objetivo:** Verificar se tentativas de autenticação com senha inválida são rejeitadas conforme normas de segurança OWASP.
- **Pré-condições (Preparação):** Usuário existente na base.
- **Dados de Entrada Controlados (Inputs):**
  - `email`: `enzo.cidadao@citizentech.org`
  - `senha`: `SenhaTotalmenteErrada123`
- **Resultado Esperado (Outputs):** Status HTTP 401 Unauthorized; mensagem genérica 'E-mail ou senha inválidos' sem expor detalhes internos da infraestrutura.

| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |
| :-: | :--- | :--- |
| 1 | `Informar e-mail válido com senha intencionalmente incorreta` | Dados digitados sem bloqueio prévio de frontend. |
| 2 | `Clicar no botão 'Entrar'` | Exibição de toast de erro com mensagem de credenciais inválidas; permanência na tela de login. |

---

### 🧪 TC-05: TC-05 [Positivo]: Realização de Logout e Revogação de Sessão Local
- **Tipo:** 🟢 Positivo
- **Feature Vinculada:** Autenticação e Gestão de Usuários
- **Objetivo:** Validar a limpeza atômica de tokens JWT do armazenamento seguro (AsyncStorage) ao encerrar a sessão.
- **Pré-condições (Preparação):** Cidadão autenticado na tela de Perfil.
- **Dados de Entrada Controlados (Inputs):**
  - `acao`: `Acionamento do botão 'Sair da Conta'`
- **Resultado Esperado (Outputs):** Token JWT expurgado do armazenamento local; redirecionamento forçado para a tela de Login.

| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |
| :-: | :--- | :--- |
| 1 | `Navegar até a aba de 'Perfil'` | Exibição dos dados do cidadão e botão de encerramento de sessão. |
| 2 | `Clicar no botão 'Sair da Conta' e confirmar no modal` | Sessão finalizada imediatamente e tela de login exibida. |

---

### 🧪 TC-06: TC-06 [Positivo]: Abertura de Chamado Urbano com Foto e Coordenadas GPS
- **Tipo:** 🟢 Positivo
- **Feature Vinculada:** Gestão de Ocorrências e Zeladoria
- **Objetivo:** Homologar o registro completo de ocorrência de zeladoria municipal na tabela CHAMADO com metadados georreferenciados.
- **Pré-condições (Preparação):** Cidadão autenticado com permissão de geolocalização concedida.
- **Dados de Entrada Controlados (Inputs):**
  - `titulo`: `Buraco Profundo na Faixa da Direita`
  - `descricao`: `Cratera aberta após fortes chuvas, causando risco iminente de acidentes e danos a veículos.`
  - `enderecoRef`: `Av. Paulista, 1106 - Próximo à estação Trianon`
  - `categoriaId`: `1`
  - `latitude`: `-23.5629`
  - `longitude`: `-46.6544`
  - `fotoUrl`: `https://storage.citizentech.org/evidencias/buraco_paulista.jpg`
- **Resultado Esperado (Outputs):** Status HTTP 201 Created; ID do chamado gerado; status inicial 'ABERTO'; data de previsão calculada automaticamente com base no prazo da categoria.

| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |
| :-: | :--- | :--- |
| 1 | `Clicar no botão '+' (Novo Chamado) na barra de navegação` | Tela de cadastro de ocorrência exibida. |
| 2 | `Preencher título, descrição detalhada e selecionar a categoria 'Vias Públicas'` | Campos validados com sucesso. |
| 3 | `Acionar 'Usar Minha Localização Atual' e anexar foto de comprovação` | Coordenadas GPS capturadas e preview da imagem carregado. |
| 4 | `Clicar em 'Publicar Chamado'` | Ocorrência cadastrada com sucesso e listada no topo do Feed do Bairro. |

---

### 🧪 TC-07: TC-07 [Negativo]: Tentativa de Registro com Campos Obrigatórios em Branco
- **Tipo:** 🔴 Negativo
- **Feature Vinculada:** Gestão de Ocorrências e Zeladoria
- **Objetivo:** Validar a blindagem contra chamados incompletos ou sem dados mínimos de triagem.
- **Pré-condições (Preparação):** Cidadão na tela de criação de chamado.
- **Dados de Entrada Controlados (Inputs):**
  - `titulo`: ``
  - `descricao`: ``
  - `categoriaId`: `None`
- **Resultado Esperado (Outputs):** HTTP 400 Bad Request; erros de Bean Validation com mensagens descritivas para cada campo ausente.

| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |
| :-: | :--- | :--- |
| 1 | `Acessar formulário de novo chamado` | Formulário exibido com botão 'Publicar' desabilitado ou sujeito a validação. |
| 2 | `Tentar submeter o formulário sem preencher nenhum campo` | Exibição de marcações em vermelho nos campos obrigatórios e alerta ao usuário. |

---

### 🧪 TC-08: TC-08 [Negativo]: Registro com Coordenadas Fora dos Limites Municipais
- **Tipo:** 🔴 Negativo
- **Feature Vinculada:** Gestão de Ocorrências e Zeladoria
- **Objetivo:** Verificar se coordenadas GPS incongruentes ou fora da jurisdição do município são identificadas.
- **Pré-condições (Preparação):** Cidadão autenticado.
- **Dados de Entrada Controlados (Inputs):**
  - `latitude`: `0.0`
  - `longitude`: `0.0`
  - `enderecoRef`: `Oceano Atlântico`
- **Resultado Esperado (Outputs):** HTTP 422 Unprocessable Entity; mensagem 'As coordenadas informadas estão fora do território municipal coberto pela plataforma'.

| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |
| :-: | :--- | :--- |
| 1 | `Informar coordenadas zeradas ou fora do município atendido` | Frontend detecta incoerência geográfica. |
| 2 | `Tentar concluir a abertura do chamado` | Sistema solicita revisão do endereço e impede o envio de dados fictícios. |

---

### 🧪 TC-09: TC-09 [Positivo]: Filtragem de Chamados por Categoria no Feed
- **Tipo:** 🟢 Positivo
- **Feature Vinculada:** Radar e Consulta de Ocorrências
- **Objetivo:** Assegurar que a filtragem por chips de categoria reflita instantaneamente na listagem sem recarregamento completo.
- **Pré-condições (Preparação):** Base com chamados de múltiplas categorias (Iluminação, Vias, Saneamento).
- **Dados de Entrada Controlados (Inputs):**
  - `categoriaFiltro`: `Iluminação Pública`
- **Resultado Esperado (Outputs):** Lista filtrada contendo estritamente chamados onde categoria_id corresponde a 'Iluminação Pública'.

| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |
| :-: | :--- | :--- |
| 1 | `Acessar a tela inicial (Feed do Bairro)` | Listagem geral de chamados exibida. |
| 2 | `Tocar no chip de filtro 'Iluminação Pública'` | Lista atualizada exibindo apenas ocorrências de postes apagados e fios caídos. |

---

### 🧪 TC-10: TC-10 [Positivo]: Busca Instantânea Textual de Ocorrências
- **Tipo:** 🟢 Positivo
- **Feature Vinculada:** Radar e Consulta de Ocorrências
- **Objetivo:** Validar a barra de busca por palavras-chave com debounce para redução de carga no backend.
- **Pré-condições (Preparação):** Feed com ocorrências carregadas.
- **Dados de Entrada Controlados (Inputs):**
  - `termoBusca`: `Paulista`
- **Resultado Esperado (Outputs):** Listagem filtrada contendo chamados que possuam 'Paulista' no título, descrição ou endereço de referência.

| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |
| :-: | :--- | :--- |
| 1 | `Digitar 'Paulista' na barra de busca superior` | Resultados filtrados dinamicamente na tela em tempo real. |

---

### 🧪 TC-11: TC-11 [Positivo]: Registro de Voto de Apoio em Ocorrência Coletiva
- **Tipo:** 🟢 Positivo
- **Feature Vinculada:** Engajamento Cidadão e Votação
- **Objetivo:** Homologar o mecanismo de votação cidadã na tabela VOTO_CHAMADO para priorização democrática de serviços públicos.
- **Pré-condições (Preparação):** Cidadão autenticado navegando no detalhe de um chamado aberto por outro munícipe.
- **Dados de Entrada Controlados (Inputs):**
  - `chamadoId`: `101`
  - `usuarioId`: `5`
- **Resultado Esperado (Outputs):** Status HTTP 200 OK; registro inserido na tabela VOTO_CHAMADO; contador de votos incrementado de N para N+1.

| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |
| :-: | :--- | :--- |
| 1 | `Abrir os detalhes do chamado #101 na tela ChamadoDetailsScreen` | Exibição dos dados do chamado e botão 'Apoiar esta solicitação (+1)'. |
| 2 | `Tocar no botão de apoio/voto` | Ícone altera para destacado e contador de apoios sobe imediatamente. |

---

### 🧪 TC-12: TC-12 [Negativo]: Bloqueio de Voto Duplicado pelo Mesmo Cidadão
- **Tipo:** 🔴 Negativo
- **Feature Vinculada:** Engajamento Cidadão e Votação
- **Objetivo:** Garantir a unicidade do voto (Constraint Unique na tabela VOTO_CHAMADO para par chamado_id + usuario_id).
- **Pré-condições (Preparação):** Cidadão já registrou voto no chamado #101.
- **Dados de Entrada Controlados (Inputs):**
  - `chamadoId`: `101`
  - `usuarioId`: `5`
- **Resultado Esperado (Outputs):** Status HTTP 409 Conflict ou remoção do voto (toggle unvote); em nenhuma hipótese o cidadão acumula múltiplos votos.

| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |
| :-: | :--- | :--- |
| 1 | `Tentar acionar o botão de apoio novamente na mesma ocorrência` | Sistema remove o voto anterior ou informa que o munícipe já apoiou esta causa. |

---

### 🧪 TC-13: TC-13 [Positivo]: Transição de Status para 'EM_EXECUCAO' pelo Gestor Público
- **Tipo:** 🟢 Positivo
- **Feature Vinculada:** Painel do Gestor e Ciclo de Vida
- **Objetivo:** Homologar a mudança de status por autoridade pública competente com rastreamento histórico na tabela HIST_STATUS.
- **Pré-condições (Preparação):** Usuário autenticado com perfil 'GESTOR'; chamado #101 em status 'ABERTO'.
- **Dados de Entrada Controlados (Inputs):**
  - `chamadoId`: `101`
  - `novoStatus`: `EM_EXECUCAO`
  - `observacoes`: `Equipe de pavimentação deslocada para o local com previsão de conclusão em 48h.`
- **Resultado Esperado (Outputs):** HTTP 200 OK; status do chamado atualizado; registro gerado em HIST_STATUS com st_anterior='ABERTO', st_novo='EM_EXECUCAO', data da mudança e ID do gestor.

| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |
| :-: | :--- | :--- |
| 1 | `Acessar console administrativo como GESTOR` | Painel de gestão de chamados do município exibido. |
| 2 | `Selecionar o chamado #101 e alterar o status para 'EM_EXECUCAO'` | Campo de observações habilitado. |
| 3 | `Inserir justificativa de despacho e salvar` | Linha do tempo atualizada com o novo status e histórico auditado. |

---

### 🧪 TC-14: TC-14 [Negativo]: Bloqueio de Cidadão Comum ao Tentar Alterar Status de Chamado
- **Tipo:** 🔴 Negativo
- **Feature Vinculada:** Painel do Gestor e Ciclo de Vida
- **Objetivo:** Verificar se o controle de acesso RBAC impede que munícipes sem perfil administrativo alterem o ciclo de vida de ocorrências.
- **Pré-condições (Preparação):** Cidadão autenticado com perfil 'CIDADAO'.
- **Dados de Entrada Controlados (Inputs):**
  - `chamadoId`: `101`
  - `metodo`: `PATCH /api/chamados/101/status`
  - `body`: `{'status': 'CONCLUIDO'}`
- **Resultado Esperado (Outputs):** Status HTTP 403 Forbidden; mensagem 'Acesso negado: apenas gestores públicos podem alterar o status de chamados'.

| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |
| :-: | :--- | :--- |
| 1 | `Disparar requisição de alteração de status com token de cidadão` | Interceptador de segurança Spring Security atua imediatamente. |
| 2 | `Analisar a resposta da API` | Resposta 403 Forbidden recebida sem nenhuma alteração no banco de dados. |

---

### 🧪 TC-15: TC-15 [Positivo]: Conclusão de Ocorrência ('CONCLUIDO') com Data de Fechamento
- **Tipo:** 🟢 Positivo
- **Feature Vinculada:** Painel do Gestor e Ciclo de Vida
- **Objetivo:** Assegurar que a finalização de chamado preenche a dt_conclusao e notifica o cidadão autor.
- **Pré-condições (Preparação):** Chamado em status 'EM_EXECUCAO'.
- **Dados de Entrada Controlados (Inputs):**
  - `chamadoId`: `101`
  - `novoStatus`: `CONCLUIDO`
  - `observacoes`: `Reparo asfáltico executado com sucesso e via desobstruída.`
- **Resultado Esperado (Outputs):** HTTP 200 OK; chamado atualizado para 'CONCLUIDO'; coluna dt_conclusao gravada com timestamp atual.

| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |
| :-: | :--- | :--- |
| 1 | `Gestor marca chamado como 'CONCLUIDO' e anexa comprovante` | Chamado é movido para o histórico de resolvidos. |
| 2 | `Consultar chamado no aplicativo` | Tag verde 'Resolvido' exibida com data de conclusão visível. |

---

### 🧪 TC-16: TC-16 [Positivo]: Emissão de Alerta Automático de Alagamento via Sensor IoT
- **Tipo:** 🟢 Positivo
- **Feature Vinculada:** Sensoriamento Urbano e IoT
- **Objetivo:** Validar a ingestão de telemetria MQTT de bueiro inteligente disparando abertura de ocorrência crítica.
- **Pré-condições (Preparação):** Broker MQTT ativo; sensor ESP32 monitorando nível de água.
- **Dados de Entrada Controlados (Inputs):**
  - `topico`: `citizentech/sensores/bueiro_12`
  - `payload`: `{'distancia_cm': 5.2, 'nivel_critico': True, 'bairroId': 2}`
- **Resultado Esperado (Outputs):** Ingestão bem-sucedida; chamado com categoria 'Alagamento Iminente' gerado automaticamente no sistema.

| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |
| :-: | :--- | :--- |
| 1 | `Simular publicação MQTT de sensor com nível de lâmina d'água perigoso` | Serviço consumidor processa o payload JSON. |
| 2 | `Verificar painel de chamados municipais` | Alerta vermelho de urgência emitido aos agentes da Defesa Civil. |

---

### 🧪 TC-17: TC-17 [Positivo]: Classificação de Severidade de Ocorrência por IA Generativa
- **Tipo:** 🟢 Positivo
- **Feature Vinculada:** Inteligência Artificial e Triagem
- **Objetivo:** Homologar a triagem automática de imagens de chamados via LLM/Visão Computacional para categorização preditiva.
- **Pré-condições (Preparação):** Microsserviço Python FastAPI ativo com endpoint de IA disponível.
- **Dados de Entrada Controlados (Inputs):**
  - `imagemUrl`: `https://storage.citizentech.org/evidencias/fio_eletrico_caido.jpg`
- **Resultado Esperado (Outputs):** HTTP 200 OK; JSON com sugestão de categoria 'Risco Elétrico', nível de urgência 'ALTO' e resumo descritivo.

| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |
| :-: | :--- | :--- |
| 1 | `Cidadão anexa foto de fio de alta tensão rompido` | Preview carregado no app. |
| 2 | `IA processa a imagem em background` | Campo de categoria sugere automaticamente 'Rede Elétrica e Iluminação' com tag de urgência. |

---

### 🧪 TC-18: TC-18 [Negativo]: Rejeição de Imagem Irrelevante / Não-Urbana por IA
- **Tipo:** 🔴 Negativo
- **Feature Vinculada:** Inteligência Artificial e Triagem
- **Objetivo:** Garantir que a IA filtre imagens que não contenham problemas de infraestrutura pública.
- **Pré-condições (Preparação):** Serviço de IA operacional.
- **Dados de Entrada Controlados (Inputs):**
  - `imagemUrl`: `https://storage.citizentech.org/evidencias/meme_internet.jpg`
- **Resultado Esperado (Outputs):** Status de triagem 'REVISAO_NECESSARIA'; mensagem 'A foto anexada não parece retratar um problema de infraestrutura urbana'.

| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |
| :-: | :--- | :--- |
| 1 | `Cidadão anexa imagem sem conteúdo de zeladoria` | IA detecta baixa aderência semântica com o catálogo de zeladoria. |
| 2 | `Sistema alerta o munícipe` | Solicitação de foto real do local para prosseguimento. |

---

### 🧪 TC-19: TC-19 [Positivo]: Abertura do App em Modo Offline e Exibição de Cache Local
- **Tipo:** 🟢 Positivo
- **Feature Vinculada:** Resiliência e Cache Offline
- **Objetivo:** Garantir que a experiência do munícipe não seja bloqueada por tela em branco ou crash caso esteja sem sinal de internet.
- **Pré-condições (Preparação):** Aplicativo aberto anteriormente com chamados sincronizados no AsyncStorage.
- **Dados de Entrada Controlados (Inputs):**
  - `estadoRede`: `Modo Avião ativado (Sem conectividade)`
- **Resultado Esperado (Outputs):** Aplicativo abre sem travar; exibe banner amarelo 'Modo Offline - Exibindo dados salvos localmente'; chamados previamente salvos são renderizados.

| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |
| :-: | :--- | :--- |
| 1 | `Ativar Modo Avião no smartphone e abrir o app CitizenTech` | App inicializa sem crash. |
| 2 | `Visualizar a aba 'Home / Feed'` | Chamados em cache são exibidos com indicador visual de dados locais. |

---

### 🧪 TC-20: TC-20 [Positivo]: Sincronização Automática ao Restabelecer Conectividade
- **Tipo:** 🟢 Positivo
- **Feature Vinculada:** Resiliência e Cache Offline
- **Objetivo:** Validar a reconciliação e atualização transparente de dados quando a rede é restaurada.
- **Pré-condições (Preparação):** Aplicativo operando em modo offline.
- **Dados de Entrada Controlados (Inputs):**
  - `estadoRede`: `Conexão Wi-Fi / 4G restabelecida`
- **Resultado Esperado (Outputs):** Banner de offline desaparece; Axios dispara consulta à API Java; listagem é atualizada com dados do servidor em background.

| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |
| :-: | :--- | :--- |
| 1 | `Desativar o Modo Avião com o app aberto` | Detector de rede identifica conexão ativa. |
| 2 | `Observar o feed` | Atualização reativa de dados sem necessidade de reiniciar a aplicação. |

---
