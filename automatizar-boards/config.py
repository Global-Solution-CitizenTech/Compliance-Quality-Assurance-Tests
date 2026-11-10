#!/usr/bin/env python3
"""
ZelaFix - Configurações Centrais e Metadados do Projeto
Centraliza configurações do Azure DevOps, integrantes da equipe e as 7 disciplinas.
"""

import os
from typing import Dict, Any
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
        "iteration": "Release 1 - Global Solution\\Semana 1",
        "owner_email": TEAM_MEMBERS["luna"]["email"],
        "owner_name": TEAM_MEMBERS["luna"]["name"],
        "file": "BACKLOG_MOBILE.md",
        "repo": "Mobile-Application-Development"
    },
    "java": {
        "key": "java",
        "name": "Java Advanced",
        "tag": "JavaAdvanced",
        "iteration": "Release 1 - Global Solution\\Semana 1",
        "owner_email": TEAM_MEMBERS["enzo"]["email"],
        "owner_name": TEAM_MEMBERS["enzo"]["name"],
        "file": "BACKLOG_JAVA_ADVANCED.md",
        "repo": "Java-Advanced"
    },
    "database": {
        "key": "database",
        "name": "Database Advanced",
        "tag": "Database",
        "iteration": "Release 1 - Global Solution\\Semana 1",
        "owner_email": TEAM_MEMBERS["lucas"]["email"],
        "owner_name": TEAM_MEMBERS["lucas"]["name"],
        "file": "BACKLOG_DATABASE_ADVANCED.md",
        "repo": "Database-Advanced"
    },
    "dotnet": {
        "key": "dotnet",
        "name": "Advanced Business Development with .NET",
        "tag": "DotNet",
        "iteration": "Release 1 - Global Solution\\Semana 2",
        "owner_email": TEAM_MEMBERS["gustavo"]["email"],
        "owner_name": TEAM_MEMBERS["gustavo"]["name"],
        "file": "BACKLOG_DOT_NET.md",
        "repo": "Advanced-Business-Development-with-Dot-Net"
    },
    "devops": {
        "key": "devops",
        "name": "DevOps Tools & Cloud Computing",
        "tag": "DevOps",
        "iteration": "Release 1 - Global Solution\\Semana 2",
        "owner_email": TEAM_MEMBERS["milton"]["email"],
        "owner_name": TEAM_MEMBERS["milton"]["name"],
        "file": "BACKLOG_DEVOPS.md",
        "repo": "DevOps-Tools-Cloud-Computing"
    },
    "iot": {
        "key": "iot",
        "name": "Disruptive Architectures (IoT, IoB & IA)",
        "tag": "DisruptiveArchitectures",
        "iteration": "Release 1 - Global Solution\\Semana 2",
        "owner_email": TEAM_MEMBERS["enzo"]["email"],
        "owner_name": TEAM_MEMBERS["enzo"]["name"],
        "file": "BACKLOG_DISRUPTIVE_ARCHITECTURES.md",
        "repo": "Disruptive-Architectures-IoT-IoB-IA"
    },
    "compliance": {
        "key": "compliance",
        "name": "Compliance, Quality Assurance & Tests",
        "tag": "Compliance",
        "iteration": "Release 1 - Global Solution\\Semana 2",
        "owner_email": TEAM_MEMBERS["enzo"]["email"],
        "owner_name": TEAM_MEMBERS["enzo"]["name"],
        "file": "BACKLOG_COMPLIANCE.md",
        "repo": "Compliance-Quality-Assurance-Tests"
    }
}
