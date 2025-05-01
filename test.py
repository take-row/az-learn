from azure.storage.blob import ContainerClient

# ストレージアカウントとコンテナの名前
account_name = "prestudystorage"
container_name = "test"

# 事前に取得済みのSASトークン（例: "xxxxx11112222"）
sas_token = "sp=rl&st=2025-05-01T05:03:48Z&se=2025-05-01T13:03:48Z&skoid=9460b971-adfd-48dc-99b4-e9be50a1c92b&sktid=2196ef49-d9ea-4f38-82cf-823230ba5b3b&skt=2025-05-01T05:03:48Z&ske=2025-05-01T13:03:48Z&sks=b&skv=2024-11-04&spr=https&sv=2024-11-04&sr=c&sig=lX7HglWSX4dmG%2F50O2xvSJLWKbGA8RtZg8kEQvkzQEA%3D"

# コンテナURL（末尾にSASトークンを付ける）
container_url = f"https://{account_name}.blob.core.windows.net/{container_name}?{sas_token}"

# コンテナクライアントを作成
container_client = ContainerClient.from_container_url(container_url)

# 仮想フォルダ一覧を取得
print("フォルダ一覧:")
for item in container_client.walk_blobs(delimiter="/"):
    if hasattr(item, 'name'):
        print(item.name)
