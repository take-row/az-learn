import requests
import json
import os

org = os.environ["ORG_NAME"]
project = os.environ["PROJECT_NAME"]
pat = os.environ["AZURE_DEVOPS_PAT"]

def main():
    for i in range(4):
        count = 1 + i
        batch_number = "batch1"
        add_tags = [batch_number]
        is_3 = True if (count % 3 == 0) else False
        is_4 = True if (count % 4 == 0) else False

        # NG
        if is_4:
            add_tags.append("NG")

        payload = [
            {
                "op": "add",
                "path": "/fields/System.Title",
                "value": f"task-{count}"
            },
            {
                "op": "replace",
                "path": "/fields/System.Tags",
                "value": "; ".join(add_tags)
            },
        ]
            
        # Done
        if not is_4 and is_3:
            doing_dict = {
                "op": "add",
                "path": "/fields/System.State",
                "value": "Doing"
            }
            payload.append(doing_dict)

        exec_post_api(payload)

def exec_post_api(payload):
    url = f"https://dev.azure.com/{org}/{project}/_apis/wit/workitems/$Task?api-version=7.0"
    headers = {
        "Content-Type": "application/json-patch+json",
        "Authorization": f"Basic {pat}",
    }

    count = 0
    while True:
        response = requests.post(
            url,
            headers=headers,
            data=json.dumps(payload)
        )

        if response.status_code == 200:
            break

        print("Status Code:", response.status_code)
        print("Response:", response.json())
        count += 1
        if count > 10:
            raise Exception

main()