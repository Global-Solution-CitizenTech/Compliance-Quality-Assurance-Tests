"""
Script de verificação final dos Iteration Paths e Tags de todos os 93 itens no Azure Boards.
"""
import requests
import base64
from config import AZURE_PAT, AZURE_ORG, AZURE_PROJECT

auth_header = "Basic " + base64.b64encode(f":{AZURE_PAT}".encode("utf-8")).decode("utf-8")
headers = {
    "Authorization": auth_header,
    "Content-Type": "application/json"
}

wiql_url = f"https://dev.azure.com/{AZURE_ORG}/{AZURE_PROJECT}/_apis/wit/wiql?api-version=7.1-preview.2"
query = {"query": "SELECT [System.Id], [System.Title], [System.WorkItemType], [System.IterationPath], [System.Tags], [System.AssignedTo] FROM WorkItems WHERE [System.TeamProject] = @project ORDER BY [System.Id]"}

res = requests.post(wiql_url, json=query, headers=headers)
work_items = res.json().get("workItems", [])
ids = [w["id"] for w in work_items]

batch_url = f"https://dev.azure.com/{AZURE_ORG}/{AZURE_PROJECT}/_apis/wit/workitemsbatch?api-version=7.1-preview.1"
batch_res = requests.post(batch_url, json={"ids": ids, "fields": ["System.Id", "System.Title", "System.WorkItemType", "System.IterationPath", "System.Tags", "System.AssignedTo"]}, headers=headers)

items = batch_res.json().get("value", [])

print(f"Total Work Items verificados: {len(items)}")

epics = [i for i in items if i["fields"]["System.WorkItemType"] == "Epic"]
print("\n=== RESUMO DAS EPICS (Conforme Imagem do Usuário) ===")
for epic in epics:
    f = epic["fields"]
    assigned = f.get("System.AssignedTo", {}).get("displayName", "Não Atribuído")
    tags = f.get("System.Tags", "")
    print(f"ID #{f['System.Id']:02d} | {f['System.Title']} | {f['System.IterationPath']} | Tags: {tags} | Responsável: {assigned}")

print("\n=== CONTAGEM POR ITERATION PATH ===")
counts = {}
for i in items:
    path = i["fields"].get("System.IterationPath", "N/A")
    counts[path] = counts.get(path, 0) + 1

for path, count in counts.items():
    print(f"  • {path}: {count} itens")

print("\n=== VERIFICAÇÃO DA TAG 'ZelaFix' ===")
has_zelafix = [i["id"] for i in items if "ZelaFix" in i["fields"].get("System.Tags", "")]
print(f"Itens contendo a tag 'ZelaFix': {len(has_zelafix)}")
