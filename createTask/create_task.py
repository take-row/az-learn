import requests
from requests.auth import HTTPBasicAuth
import json
import os

org = os.environ["ORG_NAME"]
project = os.environ["PROJECT_NAME"]
pat = os.environ["AZURE_DEVOPS_PAT"]

url = f"https://dev.azure.com/{org}/{project}/_apis/wit/workitems/$Task?api-version=7.0"

headers = {
    "Content-Type": "application/json-patch+json",
    "Authorization": "Basic OjljVGN1THFZMlppckx3ZUR2Y2xIdVlWYUg2eENvQnMyQ2RJeFlGTGltOXlDMFpPWjRRQ09KUVFKOTlCREFDQUFBQUFBQUFBQUFBQVNBWkRPNGFpUw=="
}

payload = [
    {
        "op": "add",
        "path": "/fields/System.Title",
        "value": "Python経由で作成された作業項目"
    },
    {
        "op": "add",
        "path": "/fields/System.Description",
        "value": "この作業項目はPythonスクリプトから生成されました。"
    }
]

response = requests.post(
    url,
    # auth=HTTPBasicAuth('', pat),
    headers=headers,
    data=json.dumps(payload)
)

print("Status Code:", response.status_code)
print("Response:", response.json())
