# 🛡️ Plano de Testes Formais - ZelaFix
> **Disciplina:** Compliance, Quality Assurance & Tests (FIAP 2TDSPG)
> **Projeto Azure DevOps:** [ZelaFix](https://dev.azure.com/ZelaFixGS/ZelaFix)

## 1. Escopo de Testes
O presente plano cobre a validação funcional caixa-preta do ecossistema ZelaFix:
- Autenticação JWT e Sessão Persistente (Mobile/Java)
- CRUD Completo de Ocorrências Urbanas com Foto e GPS
- Votação Coletiva Comunitária em Chamados
- Ciclo de Vida e Permissões Administrativas RBAC
- Telemetria de Sensores IoT via MQTT e Triagem por IA
- Resiliência de Conexão e Suporte a Cache Offline

## 2. Critérios de Aceite e Homologação
- 100% dos fluxos positivos validados com status 'Passed'.
- 100% dos fluxos negativos devidamente tratados com mensagens amigáveis sem stacktrace.
- Rastreabilidade bidirecional entre Casos de Teste, Features e Commits Git.