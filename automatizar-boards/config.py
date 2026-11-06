#!/usr/bin/env python3
"""
ZelaFix - Configurações Centrais, Metadados e Catálogo de Testes
Centraliza todas as constantes, mapeamento de integrantes, iterações e matriz de testes.
"""

import os
from typing import Dict, Any, List
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

AZURE_ORG = os.getenv("AZURE_DEVOPS_ORG", "ZelaFixGS")
AZURE_PROJECT = os.getenv("AZURE_DEVOPS_PROJECT", "ZelaFix")
AZURE_PAT = os.getenv("AZURE_DEVOPS_PAT", "")
GITHUB_ORG = os.getenv("GITHUB_ORG", "Global-Solution-CitizenTech")

# Integrantes do Grupo (FIAP - Turma 2TDSPG)
TEAM_MEMBERS = {
    "enzo": {
        "name": "Enzo Okuizumi Miranda de Souza",
        "rm": "561432",
        "email": "RM561432@fiap.com.br"
    },
    "gustavo": {
        "name": "Gustavo Keiji Okada",
        "rm": "563428",
        "email": "MR563428@fiap.com.br"
    },
    "lucas": {
        "name": "Lucas Barros Gouveia",
        "rm": "566422",
        "email": "RM566422@fiap.com.br"
    },
    "luna": {
        "name": "Luna de Carvalho Guimarães",
        "rm": "562290",
        "email": "RM562290@fiap.com.br"
    },
    "milton": {
        "name": "Milton Jakson de Sousa Marcelino",
        "rm": "564836",
        "email": "RM564836@fiap.com.br"
    }
}

# Mapeamento Oficial das 7 Disciplinas da Global Solution 2
DISCIPLINES: Dict[str, Dict[str, Any]] = {
    "mobile": {
        "key": "mobile",
        "name": "Mobile Application Development",
        "tag": "Mobile",
        "iteration": "Sprint 1",
        "owner_email": TEAM_MEMBERS["luna"]["email"],
        "owner_name": TEAM_MEMBERS["luna"]["name"],
        "file": "BACKLOG_MOBILE.md",
        "repo": "Mobile-Application-Development"
    },
    "java": {
        "key": "java",
        "name": "Java Advanced",
        "tag": "JavaAdvanced",
        "iteration": "Sprint 1",
        "owner_email": TEAM_MEMBERS["enzo"]["email"],
        "owner_name": TEAM_MEMBERS["enzo"]["name"],
        "file": "BACKLOG_JAVA_ADVANCED.md",
        "repo": "Java-Advanced"
    },
    "database": {
        "key": "database",
        "name": "Database Advanced",
        "tag": "Database",
        "iteration": "Sprint 1",
        "owner_email": TEAM_MEMBERS["lucas"]["email"],
        "owner_name": TEAM_MEMBERS["lucas"]["name"],
        "file": "BACKLOG_DATABASE_ADVANCED.md",
        "repo": "Database-Advanced"
    },
    "dotnet": {
        "key": "dotnet",
        "name": "Advanced Business Development with .NET",
        "tag": "DotNet",
        "iteration": "Sprint 1",
        "owner_email": TEAM_MEMBERS["gustavo"]["email"],
        "owner_name": TEAM_MEMBERS["gustavo"]["name"],
        "file": "BACKLOG_DOT_NET.md",
        "repo": "Advanced-Business-Development-with-Dot-Net"
    },
    "devops": {
        "key": "devops",
        "name": "DevOps Tools & Cloud Computing",
        "tag": "DevOps",
        "iteration": "Sprint 2",
        "owner_email": TEAM_MEMBERS["milton"]["email"],
        "owner_name": TEAM_MEMBERS["milton"]["name"],
        "file": "BACKLOG_DEVOPS.md",
        "repo": "DevOps-Tools-Cloud-Computing"
    },
    "iot": {
        "key": "iot",
        "name": "Disruptive Architectures (IoT, IoB & IA)",
        "tag": "DisruptiveArchitectures",
        "iteration": "Sprint 2",
        "owner_email": TEAM_MEMBERS["enzo"]["email"],
        "owner_name": TEAM_MEMBERS["enzo"]["name"],
        "file": "BACKLOG_DISRUPTIVE_ARCHITECTURES.md",
        "repo": "Disruptive-Architectures-IoT-IoB-IA"
    },
    "compliance": {
        "key": "compliance",
        "name": "Compliance, Quality Assurance & Tests",
        "tag": "Compliance",
        "iteration": "Sprint 2",
        "owner_email": TEAM_MEMBERS["enzo"]["email"],
        "owner_name": TEAM_MEMBERS["enzo"]["name"],
        "file": "BACKLOG_COMPLIANCE.md",
        "repo": "Compliance-Quality-Assurance-Tests"
    }
}

# 20 Casos de Testes Funcionais Caixa-Preta (65% Positivos / 35% Negativos)
TEST_CASES_DATA: List[Dict[str, Any]] = [
    {
        "id_code": "TC-01",
        "title": "[Positivo]: Cadastro de Cidadão Válido com Bairro Residencial",
        "type": "Positivo",
        "feature_name": "Autenticação e Gestão de Usuários",
        "target_feature_id": 5,
        "priority": 1,
        "objective": "Validar o processo de adesão de um novo cidadão na plataforma ZelaFix, assegurando integridade relacional.",
        "preconditions": "Banco de dados Oracle ativo; e-mail não existente na base.",
        "inputs": {"nome": "Enzo Okuizumi", "email": "enzo.cidadao@zelafix.org", "senha": "SenhaForte@2026", "bairroId": 1},
        "expected_output": "Status HTTP 201 Created; registro persistido na tabela USUARIO com senha criptografada em BCrypt.",
        "steps": [
            {"action": "Acessar a tela de cadastro no app mobile ZelaFix", "expected": "Formulário exibido com campos limpos."},
            {"action": "Preencher nome, e-mail, senha e selecionar o bairro", "expected": "Campos validados com sucesso sem mensagens de erro."},
            {"action": "Clicar no botão 'Cadastrar Cidadão'", "expected": "Requisição POST /api/v1/auth/register enviada ao backend."},
            {"action": "Verificar resposta do sistema", "expected": "Mensagem de sucesso exibida e redirecionamento para tela de Login."}
        ]
    },
    {
        "id_code": "TC-02",
        "title": "[Negativo]: Tentativa de Cadastro com E-mail Duplicado",
        "type": "Negativo",
        "feature_name": "Autenticação e Gestão de Usuários",
        "target_feature_id": 5,
        "priority": 1,
        "objective": "Garantir a unicidade cadastral de e-mails, bloqueando duplicidades com resposta amigável.",
        "preconditions": "Usuário 'enzo.cidadao@zelafix.org' previamente cadastrado.",
        "inputs": {"email": "enzo.cidadao@zelafix.org", "nome": "Enzo Duplicado"},
        "expected_output": "Status HTTP 409 Conflict; mensagem de erro orientando recuperação de senha.",
        "steps": [
            {"action": "Preencher o formulário com o e-mail já existente", "expected": "Dados digitados sem bloqueio prévio no cliente."},
            {"action": "Submeter o formulário de cadastro", "expected": "API retorna HTTP 409 Conflict."},
            {"action": "Verificar feedback na interface móvel", "expected": "Alerta 'Este e-mail já está em uso'."}
        ]
    },
    {
        "id_code": "TC-03",
        "title": "[Positivo]: Autenticação de Cidadão e Emissão de Bearer Token JWT",
        "type": "Positivo",
        "feature_name": "Autenticação e Gestão de Usuários",
        "target_feature_id": 5,
        "priority": 1,
        "objective": "Validar a autenticação stateless e o recebimento de token JWT assinado.",
        "preconditions": "Usuário cadastrado com credenciais válidas.",
        "inputs": {"email": "enzo.cidadao@zelafix.org", "senha": "SenhaForte@2026"},
        "expected_output": "Status HTTP 200 OK com payload contendo token JWT e tempo de expiração.",
        "steps": [
            {"action": "Informar e-mail e senha corretos na tela de login", "expected": "Campos preenchidos e botão habilitado."},
            {"action": "Pressionar 'Entrar no ZelaFix'", "expected": "POST /api/v1/auth/login processado com sucesso."},
            {"action": "Verificar armazenamento seguro", "expected": "Token salvo no AsyncStorage e usuário direcionado à Home."}
        ]
    },
    {
        "id_code": "TC-04",
        "title": "[Negativo]: Autenticação com Senha Incorreta",
        "type": "Negativo",
        "feature_name": "Autenticação e Gestão de Usuários",
        "target_feature_id": 5,
        "priority": 1,
        "objective": "Assegurar que credenciais inválidas sejam rejeitadas sem expor detalhes internos.",
        "preconditions": "Conta existente cadastrada.",
        "inputs": {"email": "enzo.cidadao@zelafix.org", "senha": "SenhaErradaTotal"},
        "expected_output": "Status HTTP 401 Unauthorized; mensagem 'E-mail ou senha inválidos'.",
        "steps": [
            {"action": "Inserir senha incorreta na tela de login", "expected": "Campo senha aceita entrada mascarada."},
            {"action": "Tentar autenticar", "expected": "Mensagem amigável de credenciais inválidas exibida."}
        ]
    },
    {
        "id_code": "TC-05",
        "title": "[Positivo]: Realização de Logout e Revogação de Sessão Local",
        "type": "Positivo",
        "feature_name": "Autenticação e Gestão de Usuários",
        "target_feature_id": 5,
        "priority": 2,
        "objective": "Verificar a limpeza de tokens e término seguro de sessão.",
        "preconditions": "Usuário logado no aplicativo.",
        "inputs": {"acao": "clique_sair"},
        "expected_output": "Token JWT expurgado do armazenamento local e redirecionamento para tela de login.",
        "steps": [
            {"action": "Navegar até a aba Perfil e clicar em 'Sair da Conta'", "expected": "Confirmação de logout solicitada."},
            {"action": "Confirmar logout", "expected": "Token apagado e navegação resetada para tela inicial de autenticação."}
        ]
    },
    {
        "id_code": "TC-06",
        "title": "[Positivo]: Abertura de Chamado Urbano com Foto e Coordenadas GPS",
        "type": "Positivo",
        "feature_name": "Gestão de Ocorrências e Zeladoria",
        "target_feature_id": 8,
        "priority": 1,
        "objective": "Validar o fluxo completo de registro de problema urbano pelo cidadão com GPS e foto.",
        "preconditions": "Usuário autenticado; permissão de câmera e localização concedida.",
        "inputs": {"titulo": "Buraco na via", "descricao": "Cratera na faixa direita", "categoriaId": 1, "latitude": -23.5615, "longitude": -46.6559},
        "expected_output": "Status HTTP 201 Created; chamado persistido com status inicial 'ABERTO'.",
        "steps": [
            {"action": "Tocar na aba 'Novo Chamado'", "expected": "GPS captura latitude e longitude automaticamente."},
            {"action": "Anexar foto da câmera", "expected": "Preview da imagem exibido na tela."},
            {"action": "Selecionar categoria e digitar descrição", "expected": "Campos validados com sucesso."},
            {"action": "Confirmar envio do chamado", "expected": "Chamado salvo com protocolo gerado e exibido no feed."}
        ]
    },
    {
        "id_code": "TC-07",
        "title": "[Negativo]: Tentativa de Registro com Campos Obrigatórios em Branco",
        "type": "Negativo",
        "feature_name": "Gestão de Ocorrências e Zeladoria",
        "target_feature_id": 8,
        "priority": 1,
        "objective": "Garantir a integridade dos dados impedindo chamados sem descrição ou categoria.",
        "preconditions": "Usuário autenticado.",
        "inputs": {"titulo": "", "descricao": "", "categoriaId": None},
        "expected_output": "HTTP 400 Bad Request; validação no cliente e servidor informando pendências.",
        "steps": [
            {"action": "Submeter formulário com campos em branco", "expected": "Bordas dos campos destacadas em vermelho."},
            {"action": "Verificar persistência", "expected": "Nenhum chamado criado no banco de dados."}
        ]
    },
    {
        "id_code": "TC-08",
        "title": "[Negativo]: Registro com Coordenadas Fora dos Limites Municipais",
        "type": "Negativo",
        "feature_name": "Gestão de Ocorrências e Zeladoria",
        "target_feature_id": 8,
        "priority": 2,
        "objective": "Validar restrição geográfica impedindo chamados fora do município atendido.",
        "preconditions": "Usuário autenticado.",
        "inputs": {"latitude": 0.0, "longitude": 0.0},
        "expected_output": "HTTP 422 Unprocessable Entity; mensagem de localização inválida.",
        "steps": [
            {"action": "Enviar coordenadas fora do município", "expected": "Validação de geofencing rejeita o envio."},
            {"action": "Checar mensagem", "expected": "Alerta 'Localização fora da área de cobertura do ZelaFix'."}
        ]
    },
    {
        "id_code": "TC-09",
        "title": "[Positivo]: Filtragem de Chamados por Categoria no Feed",
        "type": "Positivo",
        "feature_name": "Radar e Consulta de Ocorrências",
        "target_feature_id": 8,
        "priority": 2,
        "objective": "Garantir a consulta responsiva e filtragem correta no feed comunitário.",
        "preconditions": "Chamados de múltiplas categorias cadastrados.",
        "inputs": {"categoria": "ILUMINACAO_PUBLICA"},
        "expected_output": "Lista contendo apenas ocorrências da categoria selecionada.",
        "steps": [
            {"action": "Acessar feed e clicar no filtro 'Iluminação'", "expected": "Feed atualiza instantaneamente."},
            {"action": "Inspecionar cartões exibidos", "expected": "100% dos itens são de Iluminação Pública."}
        ]
    },
    {
        "id_code": "TC-10",
        "title": "[Positivo]: Busca Instantânea Textual de Ocorrências",
        "type": "Positivo",
        "feature_name": "Radar e Consulta de Ocorrências",
        "target_feature_id": 8,
        "priority": 2,
        "objective": "Validar busca por palavra-chave no feed de ocorrências.",
        "preconditions": "Feed populado.",
        "inputs": {"termo": "Paulista"},
        "expected_output": "Exibição de ocorrências cujo título, descrição ou logradouro contenham o termo digitado.",
        "steps": [
            {"action": "Digitar 'Paulista' no campo de busca", "expected": "Debounce filtra os cartões com sucesso."}
        ]
    },
    {
        "id_code": "TC-11",
        "title": "[Positivo]: Registro de Voto de Apoio em Ocorrência Coletiva",
        "type": "Positivo",
        "feature_name": "Engajamento Cidadão e Votação",
        "target_feature_id": 11,
        "priority": 1,
        "objective": "Permitir que cidadãos apoiem ocorrências existentes, aumentando a prioridade de atendimento.",
        "preconditions": "Chamado aberto existente; cidadão logado que ainda não votou.",
        "inputs": {"chamadoId": 1},
        "expected_output": "HTTP 200 OK; contador de votos incrementado em 1 unidade.",
        "steps": [
            {"action": "Abrir detalhe do chamado e tocar no botão 'Apoiar Chamado'", "expected": "POST /api/v1/chamados/1/votos enviado."},
            {"action": "Observar contador", "expected": "Número de votos atualiza na tela e botão muda para 'Apoiado'."}
        ]
    },
    {
        "id_code": "TC-12",
        "title": "[Negativo]: Bloqueio de Voto Duplicado pelo Mesmo Cidadão",
        "type": "Negativo",
        "feature_name": "Engajamento Cidadão e Votação",
        "target_feature_id": 11,
        "priority": 2,
        "objective": "Assegurar que cada cidadão possa votar apenas uma vez em cada chamado.",
        "preconditions": "Cidadão já registrou voto no chamado.",
        "inputs": {"chamadoId": 1},
        "expected_output": "HTTP 409 Conflict ou toggle seguro; bloqueio de contagem adicional.",
        "steps": [
            {"action": "Tentar votar novamente no mesmo chamado", "expected": "Sistema avisa que o voto já foi computado."}
        ]
    },
    {
        "id_code": "TC-13",
        "title": "[Positivo]: Transição de Status para 'EM_EXECUCAO' pelo Gestor Público",
        "type": "Positivo",
        "feature_name": "Painel do Gestor e Ciclo de Vida",
        "target_feature_id": 21,
        "priority": 1,
        "objective": "Validar avanço no ciclo de vida de chamado por usuário com perfil ADMIN/GESTOR.",
        "preconditions": "Usuário autenticado com role ADMIN; chamado no status ABERTO.",
        "inputs": {"chamadoId": 1, "novoStatus": "EM_EXECUCAO"},
        "expected_output": "Status atualizado e registro inserido na tabela HISTORICO_STATUS.",
        "steps": [
            {"action": "Gestor seleciona o chamado e altera status para 'EM_EXECUCAO'", "expected": "PATCH enviado com token de gestor."},
            {"action": "Verificar timeline", "expected": "Data e autor da alteração gravados no histórico."},
            {"action": "Consultar no app mobile", "expected": "Cidadão visualiza status atualizado em amarelo."}
        ]
    },
    {
        "id_code": "TC-14",
        "title": "[Negativo]: Bloqueio de Cidadão Comum ao Tentar Alterar Status de Chamado",
        "type": "Negativo",
        "feature_name": "Painel do Gestor e Ciclo de Vida",
        "target_feature_id": 21,
        "priority": 1,
        "objective": "Assegurar que apenas gestores públicos possam modificar status de atendimento.",
        "preconditions": "Usuário logado com role USER (Cidadão comum).",
        "inputs": {"novoStatus": "CONCLUIDO"},
        "expected_output": "HTTP 403 Forbidden; acesso negado pelo Spring Security.",
        "steps": [
            {"action": "Cidadão tenta invocar endpoint administrativo de alteração de status", "expected": "HTTP 403 Forbidden retornado."},
            {"action": "Checar status no banco", "expected": "Status permanece inalterado."}
        ]
    },
    {
        "id_code": "TC-15",
        "title": "[Positivo]: Conclusão de Ocorrência ('CONCLUIDO') com Data de Fechamento",
        "type": "Positivo",
        "feature_name": "Painel do Gestor e Ciclo de Vida",
        "target_feature_id": 21,
        "priority": 1,
        "objective": "Homologar a finalização do atendimento de zeladoria urbana.",
        "preconditions": "Chamado em status EM_EXECUCAO.",
        "inputs": {"novoStatus": "CONCLUIDO"},
        "expected_output": "Chamado atualizado para CONCLUIDO com timestamp de encerramento preenchido.",
        "steps": [
            {"action": "Gestor marca chamado como 'CONCLUIDO'", "expected": "Chamado arquivado como atendido."},
            {"action": "Verificar no banco de dados", "expected": "Campo DATA_CONCLUSAO preenchido com SYSDATE."}
        ]
    },
    {
        "id_code": "TC-16",
        "title": "[Positivo]: Emissão de Alerta Automático de Alagamento via Sensor IoT",
        "type": "Positivo",
        "feature_name": "Sensoriamento Urbano e IoT",
        "target_feature_id": 59,
        "priority": 1,
        "objective": "Validar ingestão de dados de telemetria de sensores ESP32 via broker MQTT.",
        "preconditions": "Broker MQTT ativo; sensor publicando telemetria crítica.",
        "inputs": {"topico": "zelafix/sensores/bueiro_12", "nivelAguaCm": 95.0},
        "expected_output": "Notificação push e chamado de urgência gerado automaticamente.",
        "steps": [
            {"action": "Publicar payload MQTT simulando bueiro entupido com nível crítico", "expected": "Backend processa a mensagem do broker."},
            {"action": "Verificar fila de alertas", "expected": "Alerta crítico disparado aos gestores da região."}
        ]
    },
    {
        "id_code": "TC-17",
        "title": "[Positivo]: Classificação de Severidade de Ocorrência por IA Generativa",
        "type": "Positivo",
        "feature_name": "Inteligência Artificial e Triagem",
        "target_feature_id": 62,
        "priority": 2,
        "objective": "Validar triagem automática de imagens urbanas usando visão computacional e IA.",
        "preconditions": "Microsserviço de IA ativo com modelo de visão configurado.",
        "inputs": {"imagem": "fio_eletrico_caido.jpg"},
        "expected_output": "Retorno de classificação 'ALTA_URGENCIA' e tag 'Risco à Vida'.",
        "steps": [
            {"action": "Enviar foto de fio caído à API de IA", "expected": "Modelo analisa a imagem e identifica o risco elétrico."},
            {"action": "Verificar metadata do chamado", "expected": "Score de urgência atribuído automaticamente como 0.95."}
        ]
    },
    {
        "id_code": "TC-18",
        "title": "[Negativo]: Rejeição de Imagem Irrelevante / Não-Urbana por IA",
        "type": "Negativo",
        "feature_name": "Inteligência Artificial e Triagem",
        "target_feature_id": 62,
        "priority": 2,
        "objective": "Evitar spam e imagens descontextualizadas no banco de zeladoria urbana.",
        "preconditions": "Serviço de triagem por IA ativo.",
        "inputs": {"imagem": "meme_internet.jpg"},
        "expected_output": "Classificação 'CONTEUDO_IRRELEVANTE'; alerta ao cidadão solicitando foto do local.",
        "steps": [
            {"action": "Submeter imagem de desenho/meme sem relação urbana", "expected": "IA detecta ausência de elementos de infraestrutura."},
            {"action": "Checar resposta", "expected": "Feedback 'Por favor, envie uma foto nítida do problema urbano'."}
        ]
    },
    {
        "id_code": "TC-19",
        "title": "[Positivo]: Abertura do App em Modo Offline e Exibição de Cache Local",
        "type": "Positivo",
        "feature_name": "Resiliência e Cache Offline",
        "target_feature_id": 5,
        "priority": 1,
        "objective": "Garantir a disponibilidade do aplicativo mesmo em caso de perda temporária de internet.",
        "preconditions": "Dados previamente sincronizados no AsyncStorage.",
        "inputs": {"conexao": "OFFLINE"},
        "expected_output": "Interface abre normalmente exibindo banner 'Modo Offline' e dados em cache.",
        "steps": [
            {"action": "Ativar Modo Avião no smartphone e abrir o app ZelaFix", "expected": "App inicializa sem crash."},
            {"action": "Visualizar tela inicial", "expected": "Lista de ocorrências salvas localmente é exibida com badge 'Offline'."}
        ]
    },
    {
        "id_code": "TC-20",
        "title": "[Positivo]: Sincronização Automática ao Restabelecer Conectividade",
        "type": "Positivo",
        "feature_name": "Resiliência e Cache Offline",
        "target_feature_id": 5,
        "priority": 1,
        "objective": "Homologar a transição suave de volta ao modo online com revalidação de dados.",
        "preconditions": "App aberto em modo offline.",
        "inputs": {"conexao": "ONLINE_RESTABELECIDA"},
        "expected_output": "Banner offline desaparece e novas ocorrências do servidor são incorporadas ao feed.",
        "steps": [
            {"action": "Desativar Modo Avião com o app aberto", "expected": "NetInfo detecta reconexão."},
            {"action": "Aguardar sincronização", "expected": "Feed atualizado automaticamente com as novidades da API."}
        ]
    }
]
