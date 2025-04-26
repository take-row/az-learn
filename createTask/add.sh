#!/bin/bash

# 認証ヘッダー（必要に応じて変更）
AUTH_HEADER="Authorization: Basic OjljVGN1THFZMlppckx3ZUR2Y2xIdVlWYUg2eENvQnMyQ2RJeFlGTGltOXlDMFpPWjRRQ09KUVFKOTlCREFDQUFBQUFBQUFBQUFBQVNBWkRPNGFpUw=="

# ターゲットURL
URL="https://dev.azure.com/takurou76/az-learn/_apis/wit/workitems/%24Task?api-version=7.0"

# 1から10000までループ
for i in $(seq 2441 10000); do
  echo "Creating task $i..."
  sleep 0.001

  # タイトル付きJSON生成
  JSON_DATA=$(cat <<EOF
[
  {
    "op": "add",
    "path": "/fields/System.Title",
    "value": "NEW TASK-$i"
  },
  {
    "op": "add",
    "path": "/fields/System.Description",
    "value": "このタスクはAPI経由で追加されました。"
  }
]
EOF
)

  # curl実行
  curl -s -X POST \
    -H "Content-Type: application/json-patch+json" \
    -H "$AUTH_HEADER" \
    --data "$JSON_DATA" \
    "$URL"

  echo ""  # 改行用

done
