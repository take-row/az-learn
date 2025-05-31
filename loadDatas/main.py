import json
import os
import pprint
from azure.storage.blob import BlobServiceClient

URL =  "https://tttestblobstorage.blob.core.windows.net"
TOKEN = "sp=rl&st=2025-05-31T08:47:55Z&se=2025-05-31T16:47:55Z&skoid=9460b971-adfd-48dc-99b4-e9be50a1c92b&sktid=2196ef49-d9ea-4f38-82cf-823230ba5b3b&skt=2025-05-31T08:47:55Z&ske=2025-05-31T16:47:55Z&sks=b&skv=2024-11-04&spr=https&sv=2024-11-04&sr=c&sig=BA6OerWjVzWNA54A9W0X6VpJvGkq0DhJtkph3nm5xZU%3D"

blob_service_client = BlobServiceClient(account_url=URL, credential=TOKEN)
container_client = blob_service_client.get_container_client(container="test")

contents = {}
for blob in container_client.list_blobs():
    ext = os.path.splitext(blob.name)[1]
    if ext != ".json":
        continue
    data = container_client.get_blob_client(blob.name).download_blob().readall()
    
    try:
        json_data = json.loads(data)
        contents[blob.name] = json_data
    except json.JSONDecodeError as e:
        contents[blob.name] = "NG"

with open("output.json", "w") as f:
    json.dump(contents, f)
