#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🏛️ CitizenTech — Automação de Casos de Testes no Azure Boards & Test Plans
=============================================================================
Script para geração, sincronização e exportação da Matriz de Casos de Testes
Funcionais Caixa-Preta (Positivos e Negativos) com Dados Controlados.

FIAP Global Solution 2026/2 — CitizenTech
Disciplina: Compliance, Quality Assurance & Tests
=============================================================================
"""

import os
import sys
import json
import html
import base64
import argparse
import urllib.request
import urllib.parse
import urllib.error
from typing import Dict, List, Any, Optional

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def load_env_file() -> dict:
    candidates = [
        os.path.join(os.path.dirname(__file__), ".env"),
        os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"),
        os.path.join(os.getcwd(), ".env")
    ]
    env_vars = {}
    for p in candidates:
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        env_vars[k.strip()] = v.strip().strip("'\"")
            break
    return env_vars


# =============================================================================
# CATÁLOGO DE CASOS DE TESTE CITIZENTECH (20 CASOS CAIXA-PRETA)
# =============================================================================

TEST_CASES_DATA = [
    # -------------------------------------------------------------------------
    # SUÍTE 1: Autenticação, Usuários & Segurança RBAC
    # -------------------------------------------------------------------------
    {
        "id_code": "TC-01",
        "title": "TC-01 [Positivo]: Cadastro de Cidadão Válido com Bairro Residencial",
        "type": "Positivo",
        "feature_name": "Autenticação e Gestão de Usuários",
        "priority": 1,
        "objective": "Validar o processo de adesão de um novo cidadão na plataforma CitizenTech, assegurando a consistência relacional na tabela USUARIO e integridade com a tabela BAIRRO.",
        "preconditions": "Sistema mobile ou Swagger em execução; banco de dados Oracle populado com bairros prévios.",
        "inputs": {
            "nome": "Enzo Administrador QA",
            "email": "enzo.cidadao@citizentech.org",
            "senha": "SenhaForte@2026",
            "confirmarSenha": "SenhaForte@2026",
            "telefone": "(11) 98765-4321",
            "bairroId": 1,
            "cargo": "CIDADAO"
        },
        "expected_output": "Status HTTP 201 Created; ID do usuário gerado com sucesso; senha criptografada via BCrypt; perfil CIDADAO atribuído.",
        "steps": [
            {"action": "Acessar a tela inicial do aplicativo e clicar em 'Cadastre-se'", "expected": "Formulário de cadastro exibido com campos em branco e validações ativas."},
            {"action": "Informar nome completo, e-mail institucional e senha com confirmação", "expected": "Máscara de senha ativa e indicador de complexidade satisfeito."},
            {"action": "Selecionar o bairro de residência e informar o telefone celular", "expected": "Bairro validado contra a base de dados oficial municipal."},
            {"action": "Clicar no botão 'Concluir Cadastro'", "expected": "Alerta de sucesso exibido e redirecionamento para tela de Login."}
        ]
    },
    {
        "id_code": "TC-02",
        "title": "TC-02 [Negativo]: Tentativa de Cadastro com E-mail Duplicado",
        "type": "Negativo",
        "feature_name": "Autenticação e Gestão de Usuários",
        "priority": 1,
        "objective": "Verificar a resiliência do sistema contra duplicidade de e-mail (Constraint Unique na tabela USUARIO).",
        "preconditions": "Usuário 'enzo.cidadao@citizentech.org' previamente cadastrado na base.",
        "inputs": {
            "email": "enzo.cidadao@citizentech.org",
            "senha": "OutraSenha@123"
        },
        "expected_output": "Status HTTP 409 Conflict ou 400 Bad Request; mensagem amigável 'E-mail já registrado no sistema'; nenhum registro órfão persistido.",
        "steps": [
            {"action": "Acessar o formulário de cadastro de novo usuário", "expected": "Formulário exibido pronto para entrada."},
            {"action": "Preencher dados utilizando e-mail já existente", "expected": "Campos preenchidos normalmente."},
            {"action": "Clicar em 'Concluir Cadastro'", "expected": "Validação rejeita o envio e exibe alerta: 'Este e-mail já está em uso por outro cidadão'."}
        ]
    },
    {
        "id_code": "TC-03",
        "title": "TC-03 [Positivo]: Autenticação de Cidadão e Emissão de Bearer Token JWT",
        "type": "Positivo",
        "feature_name": "Autenticação e Gestão de Usuários",
        "priority": 1,
        "objective": "Garantir a autenticação de credenciais válidas e a geração de Token JWT estruturado para proteção de rotas privadas.",
        "preconditions": "Conta de cidadão previamente homologada.",
        "inputs": {
            "email": "enzo.cidadao@citizentech.org",
            "senha": "SenhaForte@2026"
        },
        "expected_output": "HTTP 200 OK; Payload JSON contendo campo 'token' com JWT válido (header.payload.signature) e objeto do usuário autenticado.",
        "steps": [
            {"action": "Acessar a tela de login do aplicativo", "expected": "Campos de e-mail e senha visíveis."},
            {"action": "Digitar as credenciais de teste válidas", "expected": "Validação de formato aceita as entradas."},
            {"action": "Clicar em 'Entrar no Sistema'", "expected": "Spinner de carregamento exibido; transição imediata para o Feed do Bairro."}
        ]
    },
    {
        "id_code": "TC-04",
        "title": "TC-04 [Negativo]: Autenticação com Senha Incorreta",
        "type": "Negativo",
        "feature_name": "Autenticação e Gestão de Usuários",
        "priority": 1,
        "objective": "Verificar se tentativas de autenticação com senha inválida são rejeitadas conforme normas de segurança OWASP.",
        "preconditions": "Usuário existente na base.",
        "inputs": {
            "email": "enzo.cidadao@citizentech.org",
            "senha": "SenhaTotalmenteErrada123"
        },
        "expected_output": "Status HTTP 401 Unauthorized; mensagem genérica 'E-mail ou senha inválidos' sem expor detalhes internos da infraestrutura.",
        "steps": [
            {"action": "Informar e-mail válido com senha intencionalmente incorreta", "expected": "Dados digitados sem bloqueio prévio de frontend."},
            {"action": "Clicar no botão 'Entrar'", "expected": "Exibição de toast de erro com mensagem de credenciais inválidas; permanência na tela de login."}
        ]
    },
    {
        "id_code": "TC-05",
        "title": "TC-05 [Positivo]: Realização de Logout e Revogação de Sessão Local",
        "type": "Positivo",
        "feature_name": "Autenticação e Gestão de Usuários",
        "priority": 2,
        "objective": "Validar a limpeza atômica de tokens JWT do armazenamento seguro (AsyncStorage) ao encerrar a sessão.",
        "preconditions": "Cidadão autenticado na tela de Perfil.",
        "inputs": {
            "acao": "Acionamento do botão 'Sair da Conta'"
        },
        "expected_output": "Token JWT expurgado do armazenamento local; redirecionamento forçado para a tela de Login.",
        "steps": [
            {"action": "Navegar até a aba de 'Perfil'", "expected": "Exibição dos dados do cidadão e botão de encerramento de sessão."},
            {"action": "Clicar no botão 'Sair da Conta' e confirmar no modal", "expected": "Sessão finalizada imediatamente e tela de login exibida."}
        ]
    },

    # -------------------------------------------------------------------------
    # SUÍTE 2: Registro e Abertura de Chamados Urbanos
    # -------------------------------------------------------------------------
    {
        "id_code": "TC-06",
        "title": "TC-06 [Positivo]: Abertura de Chamado Urbano com Foto e Coordenadas GPS",
        "type": "Positivo",
        "feature_name": "Gestão de Ocorrências e Zeladoria",
        "priority": 1,
        "objective": "Homologar o registro completo de ocorrência de zeladoria municipal na tabela CHAMADO com metadados georreferenciados.",
        "preconditions": "Cidadão autenticado com permissão de geolocalização concedida.",
        "inputs": {
            "titulo": "Buraco Profundo na Faixa da Direita",
            "descricao": "Cratera aberta após fortes chuvas, causando risco iminente de acidentes e danos a veículos.",
            "enderecoRef": "Av. Paulista, 1106 - Próximo à estação Trianon",
            "categoriaId": 1,
            "latitude": -23.5629,
            "longitude": -46.6544,
            "fotoUrl": "https://storage.citizentech.org/evidencias/buraco_paulista.jpg"
        },
        "expected_output": "Status HTTP 201 Created; ID do chamado gerado; status inicial 'ABERTO'; data de previsão calculada automaticamente com base no prazo da categoria.",
        "steps": [
            {"action": "Clicar no botão '+' (Novo Chamado) na barra de navegação", "expected": "Tela de cadastro de ocorrência exibida."},
            {"action": "Preencher título, descrição detalhada e selecionar a categoria 'Vias Públicas'", "expected": "Campos validados com sucesso."},
            {"action": "Acionar 'Usar Minha Localização Atual' e anexar foto de comprovação", "expected": "Coordenadas GPS capturadas e preview da imagem carregado."},
            {"action": "Clicar em 'Publicar Chamado'", "expected": "Ocorrência cadastrada com sucesso e listada no topo do Feed do Bairro."}
        ]
    },
    {
        "id_code": "TC-07",
        "title": "TC-07 [Negativo]: Tentativa de Registro com Campos Obrigatórios em Branco",
        "type": "Negativo",
        "feature_name": "Gestão de Ocorrências e Zeladoria",
        "priority": 1,
        "objective": "Validar a blindagem contra chamados incompletos ou sem dados mínimos de triagem.",
        "preconditions": "Cidadão na tela de criação de chamado.",
        "inputs": {
            "titulo": "",
            "descricao": "",
            "categoriaId": None
        },
        "expected_output": "HTTP 400 Bad Request; erros de Bean Validation com mensagens descritivas para cada campo ausente.",
        "steps": [
            {"action": "Acessar formulário de novo chamado", "expected": "Formulário exibido com botão 'Publicar' desabilitado ou sujeito a validação."},
            {"action": "Tentar submeter o formulário sem preencher nenhum campo", "expected": "Exibição de marcações em vermelho nos campos obrigatórios e alerta ao usuário."}
        ]
    },
    {
        "id_code": "TC-08",
        "title": "TC-08 [Negativo]: Registro com Coordenadas Fora dos Limites Municipais",
        "type": "Negativo",
        "feature_name": "Gestão de Ocorrências e Zeladoria",
        "priority": 2,
        "objective": "Verificar se coordenadas GPS incongruentes ou fora da jurisdição do município são identificadas.",
        "preconditions": "Cidadão autenticado.",
        "inputs": {
            "latitude": 0.0,
            "longitude": 0.0,
            "enderecoRef": "Oceano Atlântico"
        },
        "expected_output": "HTTP 422 Unprocessable Entity; mensagem 'As coordenadas informadas estão fora do território municipal coberto pela plataforma'.",
        "steps": [
            {"action": "Informar coordenadas zeradas ou fora do município atendido", "expected": "Frontend detecta incoerência geográfica."},
            {"action": "Tentar concluir a abertura do chamado", "expected": "Sistema solicita revisão do endereço e impede o envio de dados fictícios."}
        ]
    },

    # -------------------------------------------------------------------------
    # SUÍTE 3: Radar do Bairro, Feed e Filtros de Categoria
    # -------------------------------------------------------------------------
    {
        "id_code": "TC-09",
        "title": "TC-09 [Positivo]: Filtragem de Chamados por Categoria no Feed",
        "type": "Positivo",
        "feature_name": "Radar e Consulta de Ocorrências",
        "priority": 2,
        "objective": "Assegurar que a filtragem por chips de categoria reflita instantaneamente na listagem sem recarregamento completo.",
        "preconditions": "Base com chamados de múltiplas categorias (Iluminação, Vias, Saneamento).",
        "inputs": {
            "categoriaFiltro": "Iluminação Pública"
        },
        "expected_output": "Lista filtrada contendo estritamente chamados onde categoria_id corresponde a 'Iluminação Pública'.",
        "steps": [
            {"action": "Acessar a tela inicial (Feed do Bairro)", "expected": "Listagem geral de chamados exibida."},
            {"action": "Tocar no chip de filtro 'Iluminação Pública'", "expected": "Lista atualizada exibindo apenas ocorrências de postes apagados e fios caídos."}
        ]
    },
    {
        "id_code": "TC-10",
        "title": "TC-10 [Positivo]: Busca Instantânea Textual de Ocorrências",
        "type": "Positivo",
        "feature_name": "Radar e Consulta de Ocorrências",
        "priority": 2,
        "objective": "Validar a barra de busca por palavras-chave com debounce para redução de carga no backend.",
        "preconditions": "Feed com ocorrências carregadas.",
        "inputs": {
            "termoBusca": "Paulista"
        },
        "expected_output": "Listagem filtrada contendo chamados que possuam 'Paulista' no título, descrição ou endereço de referência.",
        "steps": [
            {"action": "Digitar 'Paulista' na barra de busca superior", "expected": "Resultados filtrados dinamicamente na tela em tempo real."}
        ]
    },

    # -------------------------------------------------------------------------
    # SUÍTE 4: Engajamento Comunitário & Votos (VOTO_CHAMADO)
    # -------------------------------------------------------------------------
    {
        "id_code": "TC-11",
        "title": "TC-11 [Positivo]: Registro de Voto de Apoio em Ocorrência Coletiva",
        "type": "Positivo",
        "feature_name": "Engajamento Cidadão e Votação",
        "priority": 1,
        "objective": "Homologar o mecanismo de votação cidadã na tabela VOTO_CHAMADO para priorização democrática de serviços públicos.",
        "preconditions": "Cidadão autenticado navegando no detalhe de um chamado aberto por outro munícipe.",
        "inputs": {
            "chamadoId": 101,
            "usuarioId": 5
        },
        "expected_output": "Status HTTP 200 OK; registro inserido na tabela VOTO_CHAMADO; contador de votos incrementado de N para N+1.",
        "steps": [
            {"action": "Abrir os detalhes do chamado #101 na tela ChamadoDetailsScreen", "expected": "Exibição dos dados do chamado e botão 'Apoiar esta solicitação (+1)'."},
            {"action": "Tocar no botão de apoio/voto", "expected": "Ícone altera para destacado e contador de apoios sobe imediatamente."}
        ]
    },
    {
        "id_code": "TC-12",
        "title": "TC-12 [Negativo]: Bloqueio de Voto Duplicado pelo Mesmo Cidadão",
        "type": "Negativo",
        "feature_name": "Engajamento Cidadão e Votação",
        "priority": 1,
        "objective": "Garantir a unicidade do voto (Constraint Unique na tabela VOTO_CHAMADO para par chamado_id + usuario_id).",
        "preconditions": "Cidadão já registrou voto no chamado #101.",
        "inputs": {
            "chamadoId": 101,
            "usuarioId": 5
        },
        "expected_output": "Status HTTP 409 Conflict ou remoção do voto (toggle unvote); em nenhuma hipótese o cidadão acumula múltiplos votos.",
        "steps": [
            {"action": "Tentar acionar o botão de apoio novamente na mesma ocorrência", "expected": "Sistema remove o voto anterior ou informa que o munícipe já apoiou esta causa."}
        ]
    },

    # -------------------------------------------------------------------------
    # SUÍTE 5: Gestão de Ciclo de Vida e Auditoria (HIST_STATUS)
    # -------------------------------------------------------------------------
    {
        "id_code": "TC-13",
        "title": "TC-13 [Positivo]: Transição de Status para 'EM_EXECUCAO' pelo Gestor Público",
        "type": "Positivo",
        "feature_name": "Painel do Gestor e Ciclo de Vida",
        "priority": 1,
        "objective": "Homologar a mudança de status por autoridade pública competente com rastreamento histórico na tabela HIST_STATUS.",
        "preconditions": "Usuário autenticado com perfil 'GESTOR'; chamado #101 em status 'ABERTO'.",
        "inputs": {
            "chamadoId": 101,
            "novoStatus": "EM_EXECUCAO",
            "observacoes": "Equipe de pavimentação deslocada para o local com previsão de conclusão em 48h."
        },
        "expected_output": "HTTP 200 OK; status do chamado atualizado; registro gerado em HIST_STATUS com st_anterior='ABERTO', st_novo='EM_EXECUCAO', data da mudança e ID do gestor.",
        "steps": [
            {"action": "Acessar console administrativo como GESTOR", "expected": "Painel de gestão de chamados do município exibido."},
            {"action": "Selecionar o chamado #101 e alterar o status para 'EM_EXECUCAO'", "expected": "Campo de observações habilitado."},
            {"action": "Inserir justificativa de despacho e salvar", "expected": "Linha do tempo atualizada com o novo status e histórico auditado."}
        ]
    },
    {
        "id_code": "TC-14",
        "title": "TC-14 [Negativo]: Bloqueio de Cidadão Comum ao Tentar Alterar Status de Chamado",
        "type": "Negativo",
        "feature_name": "Painel do Gestor e Ciclo de Vida",
        "priority": 1,
        "objective": "Verificar se o controle de acesso RBAC impede que munícipes sem perfil administrativo alterem o ciclo de vida de ocorrências.",
        "preconditions": "Cidadão autenticado com perfil 'CIDADAO'.",
        "inputs": {
            "chamadoId": 101,
            "metodo": "PATCH /api/chamados/101/status",
            "body": {"status": "CONCLUIDO"}
        },
        "expected_output": "Status HTTP 403 Forbidden; mensagem 'Acesso negado: apenas gestores públicos podem alterar o status de chamados'.",
        "steps": [
            {"action": "Disparar requisição de alteração de status com token de cidadão", "expected": "Interceptador de segurança Spring Security atua imediatamente."},
            {"action": "Analisar a resposta da API", "expected": "Resposta 403 Forbidden recebida sem nenhuma alteração no banco de dados."}
        ]
    },
    {
        "id_code": "TC-15",
        "title": "TC-15 [Positivo]: Conclusão de Ocorrência ('CONCLUIDO') com Data de Fechamento",
        "type": "Positivo",
        "feature_name": "Painel do Gestor e Ciclo de Vida",
        "priority": 2,
        "objective": "Assegurar que a finalização de chamado preenche a dt_conclusao e notifica o cidadão autor.",
        "preconditions": "Chamado em status 'EM_EXECUCAO'.",
        "inputs": {
            "chamadoId": 101,
            "novoStatus": "CONCLUIDO",
            "observacoes": "Reparo asfáltico executado com sucesso e via desobstruída."
        },
        "expected_output": "HTTP 200 OK; chamado atualizado para 'CONCLUIDO'; coluna dt_conclusao gravada com timestamp atual.",
        "steps": [
            {"action": "Gestor marca chamado como 'CONCLUIDO' e anexa comprovante", "expected": "Chamado é movido para o histórico de resolvidos."},
            {"action": "Consultar chamado no aplicativo", "expected": "Tag verde 'Resolvido' exibida com data de conclusão visível."}
        ]
    },

    # -------------------------------------------------------------------------
    # SUÍTE 6: Sensoriamento IoT & Telemetria Urbana (ESP32/MQTT)
    # -------------------------------------------------------------------------
    {
        "id_code": "TC-16",
        "title": "TC-16 [Positivo]: Emissão de Alerta Automático de Alagamento via Sensor IoT",
        "type": "Positivo",
        "feature_name": "Sensoriamento Urbano e IoT",
        "priority": 2,
        "objective": "Validar a ingestão de telemetria MQTT de bueiro inteligente disparando abertura de ocorrência crítica.",
        "preconditions": "Broker MQTT ativo; sensor ESP32 monitorando nível de água.",
        "inputs": {
            "topico": "citizentech/sensores/bueiro_12",
            "payload": {"distancia_cm": 5.2, "nivel_critico": True, "bairroId": 2}
        },
        "expected_output": "Ingestão bem-sucedida; chamado com categoria 'Alagamento Iminente' gerado automaticamente no sistema.",
        "steps": [
            {"action": "Simular publicação MQTT de sensor com nível de lâmina d'água perigoso", "expected": "Serviço consumidor processa o payload JSON."},
            {"action": "Verificar painel de chamados municipais", "expected": "Alerta vermelho de urgência emitido aos agentes da Defesa Civil."}
        ]
    },

    # -------------------------------------------------------------------------
    # SUÍTE 7: IA Generativa & Triagem Inteligente
    # -------------------------------------------------------------------------
    {
        "id_code": "TC-17",
        "title": "TC-17 [Positivo]: Classificação de Severidade de Ocorrência por IA Generativa",
        "type": "Positivo",
        "feature_name": "Inteligência Artificial e Triagem",
        "priority": 2,
        "objective": "Homologar a triagem automática de imagens de chamados via LLM/Visão Computacional para categorização preditiva.",
        "preconditions": "Microsserviço Python FastAPI ativo com endpoint de IA disponível.",
        "inputs": {
            "imagemUrl": "https://storage.citizentech.org/evidencias/fio_eletrico_caido.jpg"
        },
        "expected_output": "HTTP 200 OK; JSON com sugestão de categoria 'Risco Elétrico', nível de urgência 'ALTO' e resumo descritivo.",
        "steps": [
            {"action": "Cidadão anexa foto de fio de alta tensão rompido", "expected": "Preview carregado no app."},
            {"action": "IA processa a imagem em background", "expected": "Campo de categoria sugere automaticamente 'Rede Elétrica e Iluminação' com tag de urgência."}
        ]
    },
    {
        "id_code": "TC-18",
        "title": "TC-18 [Negativo]: Rejeição de Imagem Irrelevante / Não-Urbana por IA",
        "type": "Negativo",
        "feature_name": "Inteligência Artificial e Triagem",
        "priority": 3,
        "objective": "Garantir que a IA filtre imagens que não contenham problemas de infraestrutura pública.",
        "preconditions": "Serviço de IA operacional.",
        "inputs": {
            "imagemUrl": "https://storage.citizentech.org/evidencias/meme_internet.jpg"
        },
        "expected_output": "Status de triagem 'REVISAO_NECESSARIA'; mensagem 'A foto anexada não parece retratar um problema de infraestrutura urbana'.",
        "steps": [
            {"action": "Cidadão anexa imagem sem conteúdo de zeladoria", "expected": "IA detecta baixa aderência semântica com o catálogo de zeladoria."},
            {"action": "Sistema alerta o munícipe", "expected": "Solicitação de foto real do local para prosseguimento."}
        ]
    },

    # -------------------------------------------------------------------------
    # SUÍTE 8: Resiliência Mobile & Cache Offline
    # -------------------------------------------------------------------------
    {
        "id_code": "TC-19",
        "title": "TC-19 [Positivo]: Abertura do App em Modo Offline e Exibição de Cache Local",
        "type": "Positivo",
        "feature_name": "Resiliência e Cache Offline",
        "priority": 2,
        "objective": "Garantir que a experiência do munícipe não seja bloqueada por tela em branco ou crash caso esteja sem sinal de internet.",
        "preconditions": "Aplicativo aberto anteriormente com chamados sincronizados no AsyncStorage.",
        "inputs": {
            "estadoRede": "Modo Avião ativado (Sem conectividade)"
        },
        "expected_output": "Aplicativo abre sem travar; exibe banner amarelo 'Modo Offline - Exibindo dados salvos localmente'; chamados previamente salvos são renderizados.",
        "steps": [
            {"action": "Ativar Modo Avião no smartphone e abrir o app CitizenTech", "expected": "App inicializa sem crash."},
            {"action": "Visualizar a aba 'Home / Feed'", "expected": "Chamados em cache são exibidos com indicador visual de dados locais."}
        ]
    },
    {
        "id_code": "TC-20",
        "title": "TC-20 [Positivo]: Sincronização Automática ao Restabelecer Conectividade",
        "type": "Positivo",
        "feature_name": "Resiliência e Cache Offline",
        "priority": 2,
        "objective": "Validar a reconciliação e atualização transparente de dados quando a rede é restaurada.",
        "preconditions": "Aplicativo operando em modo offline.",
        "inputs": {
            "estadoRede": "Conexão Wi-Fi / 4G restabelecida"
        },
        "expected_output": "Banner de offline desaparece; Axios dispara consulta à API Java; listagem é atualizada com dados do servidor em background.",
        "steps": [
            {"action": "Desativar o Modo Avião com o app aberto", "expected": "Detector de rede identifica conexão ativa."},
            {"action": "Observar o feed", "expected": "Atualização reativa de dados sem necessidade de reiniciar a aplicação."}
        ]
    }
]


# =============================================================================
# EXPORTAÇÃO DE ARTEFATOS DOCUMENTAIS EM MARKDOWN
# =============================================================================

def export_test_matrix_md(output_path: str):
    lines = [
        "# 🏛️ Matriz de Casos de Testes Manuais — CitizenTech",
        "> **Projeto:** CitizenTech — Zeladoria Urbana Colaborativa (FIAP Global Solution 2026/2)  ",
        "> **Disciplina:** Compliance, Quality Assurance & Tests (2TDSPG)  ",
        "> **Norma:** Padrão Oficial Azure Boards & Test Plans (Cobertura Caixa-Preta 100%)",
        "",
        "---",
        "",
        "## 📊 Sumário Executivo de Cobertura de Testes",
        "",
        f"- **Total de Casos de Teste Mapeados:** {len(TEST_CASES_DATA)}",
        f"- **Casos Positivos (Caminho Feliz):** {sum(1 for t in TEST_CASES_DATA if t['type'] == 'Positivo')} (65%)",
        f"- **Casos Negativos (Exceções / Borda):** {sum(1 for t in TEST_CASES_DATA if t['type'] == 'Negativo')} (35%)",
        "- **Técnica Aplicada:** Dados de Entrada Controlados (Predefined Inputs)",
        "- **Rastreabilidade:** 100% vinculado aos critérios de aceite das Features no Azure Boards",
        "",
        "---",
        "",
        "## 📋 Tabela Resumo dos Casos de Teste Estruturados por Feature",
        "",
        "| ID | Título do Caso de Teste | Tipo | Feature de Referência | Prioridade |",
        "| :---: | :--- | :---: | :--- | :---: |"
    ]

    for tc in TEST_CASES_DATA:
        badge = "🟢 Positivo" if tc["type"] == "Positivo" else "🔴 Negativo"
        prio_str = "Alta" if tc["priority"] == 1 else "Média"
        lines.append(f"| **{tc['id_code']}** | {tc['title']} | {badge} | {tc['feature_name']} | {prio_str} |")

    lines.extend([
        "",
        "---",
        "",
        "## 🔍 Detalhamento dos Casos de Testes com Dados Controlados e Passos",
        ""
    ])

    for tc in TEST_CASES_DATA:
        badge = "🟢 Positivo" if tc["type"] == "Positivo" else "🔴 Negativo"
        lines.append(f"### 🧪 {tc['id_code']}: {tc['title']}")
        lines.append(f"- **Tipo:** {badge}")
        lines.append(f"- **Feature Vinculada:** {tc['feature_name']}")
        lines.append(f"- **Objetivo:** {tc['objective']}")
        lines.append(f"- **Pré-condições (Preparação):** {tc['preconditions']}")
        lines.append("- **Dados de Entrada Controlados (Inputs):**")
        for k, v in tc["inputs"].items():
            lines.append(f"  - `{k}`: `{v}`")
        lines.append(f"- **Resultado Esperado (Outputs):** {tc['expected_output']}")
        lines.append("")
        lines.append("| Passo | Ação do Testador (Entrada) | Resposta Esperada do Sistema (Saída) |")
        lines.append("| :-: | :--- | :--- |")
        for idx, s in enumerate(tc["steps"], 1):
            act_clean = s['action'].replace("\n", " ")
            exp_clean = s['expected'].replace("\n", " ")
            lines.append(f"| {idx} | `{act_clean}` | {exp_clean} |")
        lines.append("")
        lines.append("---")
        lines.append("")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"✅ Matriz de testes exportada com sucesso em: {output_path}")


def export_test_plan_md(output_path: str):
    lines = [
        "# 📋 Plano de Testes de Software — Azure Boards & Test Plans",
        "## 🏛️ Projeto: CitizenTech — Zeladoria Urbana Colaborativa",
        "> **FIAP Global Solution 2026/2** • Turmas de Fevereiro (2TDSPG)  ",
        "> **Disciplina:** Compliance, Quality Assurance & Tests  ",
        "> **Plataforma Oficial:** Microsoft Azure DevOps (Azure Boards & Test Plans)",
        "",
        "---",
        "",
        "## 👥 Integrantes do Grupo (Ordem Alfabética)",
        "",
        "| Nome Completo | RM | Turma | Papel no Projeto / Governança QA |",
        "| :--- | :---: | :---: | :--- |",
        "| **Enzo Okuizumi** | **561432** | 2TDSPG | Governança Scrum, Gestão Azure DevOps e Automação de Testes |",
        "| **Gustavo Okada** | **563428** | 2TDSPG | Arquitetura .NET, Testes Unitários AAA e Observabilidade |",
        "| **Lucas Barros Gouveia** | **566422** | 2TDSPG | Database Advanced (Oracle PL/SQL, Triggers DML e MongoDB) |",
        "| **Luna de Carvalho Guimarães** | **562290** | 2TDSPG | Mobile Development (React Native, Rotas Protegidas e Cache) |",
        "| **Milton Jakson de Sousa Marcelino** | **564836** | 2TDSPG | DevOps & Cloud (Docker/Azure) e Disruptive IoT/GenAI |",
        "",
        "---",
        "",
        "## 🎯 1. Escopo e Estratégia de Qualidade de Software",
        "",
        "O presente plano formaliza as diretrizes de garantia de qualidade para a solução **CitizenTech**, contemplando:",
        "1. **Governança Ágil no Azure Boards:** Estruturação estrita da hierarquia Scrum (Epics ➔ Features ➔ PBIs ➔ Tasks).",
        "2. **Cobertura Funcional Caixa-Preta:** Homologação com cenários positivos (caminho feliz) e negativos (validação de erros, restrições e limites).",
        "3. **Técnica de Dados de Entrada Controlados:** Uso de parâmetros estáticos previamente acordados para garantir repetibilidade na auditoria da banca examinadora.",
        "4. **Rastreabilidade de Código (Git Commits):** Vínculo formal dos commits dos 7 repositórios aos itens de trabalho do Azure Boards.",
        "5. **Evidências no Azure Test Plans:** Execução de casos com status Passed e Failed controlados para validação de métricas de bug tracking.",
        "",
        "---",
        "",
        "## 📊 2. Resumo da Suíte de Casos de Testes no Azure Test Plans",
        "",
        "| Domínio Funcional / Suíte | Total de Casos | Positivos | Negativos | Foco de Avaliação |",
        "| :--- | :---: | :---: | :---: | :--- |",
        "| **Autenticação e Usuários** | 5 | 3 | 2 | Segurança JWT, cadastro com validação e controle de senhas |",
        "| **Abertura de Chamados** | 3 | 1 | 2 | Inserção de ocorrências, coordenadas GPS e fotos de comprovação |",
        "| **Radar e Consultas** | 2 | 2 | 0 | Filtragem por categoria, busca textual e debounce |",
        "| **Engajamento & Votos** | 2 | 1 | 1 | Voto comunitário em chamados e bloqueio de votos duplicados |",
        "| **Ciclo de Vida do Chamado** | 3 | 2 | 1 | Transição de status por gestores, auditoria DML e controle RBAC |",
        "| **Sensoriamento IoT** | 1 | 1 | 0 | Telemetria MQTT de bueiro inteligente com alerta de alagamento |",
        "| **IA Generativa & Triagem** | 2 | 1 | 1 | Classificação de fotos de ocorrências e filtragem de conteúdo |",
        "| **Resiliência Mobile & Cache** | 2 | 2 | 0 | Operação offline resiliente e reconciliação com o backend |",
        "| **TOTAL CONSOLIDADO** | **20** | **13 (65%)** | **7 (35%)** | **100% de Cobertura das Features da Solução** |",
        "",
        "---",
        "",
        "## 🛠️ 3. Ferramentas e Procedimentos Operacionais",
        "",
        "- **Azure Boards:** Gerenciamento do Backlog, sprints e rastreabilidade de requisitos.",
        "- **Azure Test Plans:** Execução de casos de testes manuais e emissão de gráficos analíticos.",
        "- **Postman:** Suíte automatizada de testes de integração contra a API Java Spring Boot.",
        "- **Scripts de Automação Python:** Sincronização automatizada e extração de evidências via REST API oficial da Microsoft.",
        "",
        "> 📌 *Consulte a matriz completa e detalhada em [`docs/MATRIZ_CASOS_DE_TESTE_AZURE.md`](./MATRIZ_CASOS_DE_TESTE_AZURE.md).*"
    ]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"✅ Plano de testes exportado com sucesso em: {output_path}")


# =============================================================================
# SINCRONIZAÇÃO COM A API DO AZURE DEVOPS
# =============================================================================

def sync_test_cases_to_azure(org: str, project: str, pat: str, dry_run: bool = False):
    print("\n" + "="*80)
    prefix = "[DRY-RUN] " if dry_run else ""
    print(f"🚀 {prefix}SINCRONIZANDO CASOS DE TESTES NO AZURE BOARDS")
    print(f"🏛️ Organização: {org} | Projeto: {project}")
    print("="*80)

    auth_header = "Basic " + base64.b64encode(f":{pat}".encode("utf-8")).decode("utf-8")
    headers = {
        "Authorization": auth_header,
        "Content-Type": "application/json-patch+json",
        "Accept": "application/json"
    }

    # Busca Features existentes para associar os Test Cases
    features_cache = {}
    if pat and not dry_run:
        url_wiql = f"https://dev.azure.com/{org}/{project}/_apis/wit/wiql?api-version=7.1-preview.2"
        q = {"query": "Select [System.Id], [System.Title] From WorkItems Where [System.TeamProject] = @project And [System.WorkItemType] = 'Feature'"}
        try:
            req_wiql = urllib.request.Request(url_wiql, data=json.dumps(q).encode("utf-8"), headers={
                "Authorization": auth_header,
                "Content-Type": "application/json"
            }, method="POST")
            with urllib.request.urlopen(req_wiql, timeout=20) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                f_ids = [it["id"] for it in data.get("workItems", [])]
                if f_ids:
                    b_url = f"https://dev.azure.com/{org}/{project}/_apis/wit/workitemsbatch?api-version=7.0"
                    b_req = urllib.request.Request(b_url, data=json.dumps({"ids": f_ids, "fields": ["System.Id", "System.Title"]}).encode("utf-8"), headers={
                        "Authorization": auth_header,
                        "Content-Type": "application/json"
                    }, method="POST")
                    with urllib.request.urlopen(b_req, timeout=20) as b_resp:
                        b_data = json.loads(b_resp.read().decode("utf-8"))
                        for item in b_data.get("value", []):
                            fid = item["id"]
                            ftitle = item["fields"]["System.Title"]
                            furl = item["url"]
                            features_cache[fid] = {"title": ftitle, "url": furl}
        except Exception as e:
            print(f"ℹ️ Não foi possível listar features existentes: {e}")

    def get_matched_feature_url(fn: str):
        f_low = fn.lower()
        target_fid = None
        if "offline" in f_low or "resili" in f_low:
            target_fid = 5
        elif "autentica" in f_low:
            target_fid = 5
        elif "zeladoria" in f_low or "crud" in f_low or "consulta" in f_low or "radar" in f_low:
            target_fid = 8
        elif "engajamento" in f_low or "vota" in f_low:
            target_fid = 11
        elif "painel" in f_low or "ciclo" in f_low:
            target_fid = 21
        elif "sensoriamento" in f_low or "iot" in f_low:
            target_fid = 59
        elif "intelig" in f_low or "artificial" in f_low:
            target_fid = 62

        if target_fid and target_fid in features_cache:
            return features_cache[target_fid]["url"], features_cache[target_fid]["title"]

        # Fallback de busca por palavra-chave no cache
        for fid, finfo in features_cache.items():
            t = finfo["title"].lower()
            if any(k in t for k in ["autentica", "crud", "engajamento", "regras", "sensoriamento", "ia"]):
                return finfo["url"], finfo["title"]
        return None, None

    created_count = 0
    simulated_id = 2000

    for idx, tc in enumerate(TEST_CASES_DATA, 1):
        clean_title = f"{tc['id_code']}: {tc['title'].replace(tc['id_code'] + ' ', '')}"
        
        # Constrói XML dos passos no padrão oficial Azure Test Plans
        step_nodes = []
        for s_idx, st in enumerate(tc["steps"], 2):
            act = html.escape(st["action"])
            exp = html.escape(st["expected"])
            step_nodes.append(
                f'<step id="{s_idx}" type="ValidateStep">'
                f'<parameterizedString isformatted="true">{act}</parameterizedString>'
                f'<parameterizedString isformatted="true">{exp}</parameterizedString>'
                f'<description/>'
                f'</step>'
            )
        steps_xml = f'<steps id="0" last="{len(tc["steps"]) + 1}">{"".join(step_nodes)}</steps>'

        # Monta sumário em HTML para o campo System.Description
        inputs_html = "".join(f"<li><b>{k}:</b> {v}</li>" for k, v in tc["inputs"].items())
        summary_html = (
            f"<div><b>Objetivo:</b> {tc['objective']}</div><br/>"
            f"<div><b>Preparação / Pré-condições:</b> {tc['preconditions']}</div><br/>"
            f"<div><b>Dados de Entrada Controlados:</b><ul>{inputs_html}</ul></div><br/>"
            f"<div><b>Resultados Esperados:</b> {tc['expected_output']}</div>"
        )

        tags = ["ZelaFix", "QA", "BlackBox", tc["type"], tc["feature_name"].replace(" ", "")]

        if dry_run:
            simulated_id += 1
            print(f"  🧪 [DRY-RUN] Criaria TC #{simulated_id}: {clean_title} ({tc['type']} | {len(tc['steps'])} passos)")
            created_count += 1
            continue

        url_tc = f"https://dev.azure.com/{org}/{project}/_apis/wit/workitems/$Test%20Case?api-version=7.1-preview.3"
        patch_doc = [
            {"op": "add", "path": "/fields/System.Title", "value": clean_title},
            {"op": "add", "path": "/fields/System.Description", "value": summary_html},
            {"op": "add", "path": "/fields/Microsoft.VSTS.Common.Priority", "value": int(tc["priority"])},
            {"op": "add", "path": "/fields/Microsoft.VSTS.TCM.Steps", "value": steps_xml},
            {"op": "add", "path": "/fields/System.Tags", "value": "; ".join(tags)}
        ]

        f_url, f_title = get_matched_feature_url(tc["feature_name"])
        if f_url:
            patch_doc.append({
                "op": "add",
                "path": "/relations/-",
                "value": {
                    "rel": "Microsoft.VSTS.Common.TestedBy-Reverse",
                    "url": f_url,
                    "attributes": {
                        "comment": f"Vinculado à {f_title}"
                    }
                }
            })

        try:
            req = urllib.request.Request(url_tc, data=json.dumps(patch_doc).encode("utf-8"), headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=30) as resp:
                res_data = json.loads(resp.read().decode("utf-8"))
                new_id = res_data.get("id")
                print(f"  ✅ Caso de Teste #{new_id} criado: {clean_title}")
                created_count += 1
        except Exception as e:
            print(f"  ❌ Falha ao criar caso de teste '{clean_title}': {e}")

    print("\n" + "="*80)
    print(f"✨ Sincronização concluída! Total de Casos de Teste processados: {created_count}")
    print("="*80 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="CitizenTech - Gestão e Sincronização de Casos de Testes no Azure Boards",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--sync-azure", "-s", action="store_true", help="Cria os casos de teste na nuvem do Azure Boards")
    parser.add_argument("--dry-run", "-d", action="store_true", help="Simula sem enviar nada à API do Azure DevOps")
    parser.add_argument("--export-all", "-e", action="store_true", help="Gera os arquivos Markdown da Matriz e do Plano de Testes")
    parser.add_argument("--org", type=str, default=None, help="Organização no Azure DevOps")
    parser.add_argument("--project", type=str, default=None, help="Projeto no Azure DevOps")
    parser.add_argument("--pat", type=str, default=None, help="Personal Access Token")

    args = parser.parse_args()

    env_vars = load_env_file()
    org = args.org or os.getenv("AZURE_DEVOPS_ORG") or env_vars.get("AZURE_DEVOPS_ORG", "ZelaFixGS")
    project = args.project or os.getenv("AZURE_DEVOPS_PROJECT") or env_vars.get("AZURE_DEVOPS_PROJECT", "ZelaFix")
    pat = args.pat or os.getenv("AZURE_DEVOPS_PAT") or env_vars.get("AZURE_DEVOPS_PAT", "")

    # Base dos docs
    script_dir = os.path.dirname(os.path.abspath(__file__))
    compliance_root = os.path.dirname(script_dir)
    matrix_path = os.path.join(compliance_root, "docs", "MATRIZ_CASOS_DE_TESTE_AZURE.md")
    plan_path = os.path.join(compliance_root, "docs", "PLANO_DE_TESTES_AZURE_BOARDS.md")

    if args.export_all or (not args.sync_azure and not args.dry_run):
        export_test_matrix_md(matrix_path)
        export_test_plan_md(plan_path)

    if args.sync_azure or args.dry_run:
        sync_test_cases_to_azure(org=org, project=project, pat=pat, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
