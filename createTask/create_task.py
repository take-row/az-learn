import requests
import json
import os

org = os.environ["ORG_NAME"]
project = os.environ["PROJECT_NAME"]
pat = os.environ["AZURE_DEVOPS_PAT"]

def main():
    for i in range(1000):
        count = 1 + i
        batch_number = "batch1"
        add_tags = [batch_number]
        is_3 = True if (count % 3 == 0) else False
        is_4 = True if (count % 4 == 0) else False
        print(f"count={count}, is_3={is_3} is_4={is_4}")

        # NG
        if is_4:
            add_tags.append("NG")

        payload = [
            {
                "op": "add",
                "path": "/fields/System.Title",
                "value": f"task-{count}",
            },
            {
                "op": "replace",
                "path": "/fields/System.Tags",
                "value": "; ".join(add_tags),
            },
        ]
        
        response = exec_post_api(payload)
            
        # Done
        if not is_4 and is_3:
            work_item_id = response.json()['id']
    
            payload = [
                {
                    "op": "add",
                    "path": "/fields/System.State",
                    "value": "Done",
                }
            ]

            exec_patch_api(work_item_id, payload)



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
    
    return response
    
def exec_patch_api(id, payload):

    url = f"https://dev.azure.com/{org}/{project}/_apis/wit/workitems/{id}?api-version=7.0"
    headers = {
        "Content-Type": "application/json-patch+json",
        "Authorization": f"Basic {pat}",
    }

    count = 0
    while True:
        response = requests.patch(
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
    
    return response

main()