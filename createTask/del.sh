#!/bin/bash

# === 設定値（必要に応じて書き換えてください） ===
ORG="takurou76"        # Azure DevOps Organization
PROJECT="az-learn"         # プロジェクト名
ENCODED_PAT="OjljVGN1THFZMlppckx3ZUR2Y2xIdVlWYUg2eENvQnMyQ2RJeFlGTGltOXlDMFpPWjRRQ09KUVFKOTlCREFDQUFBQUFBQUFBQUFBQVNBWkRPNGFpUw=="  # パーソナルアクセストークン（安全な保管推奨）
API_VERSION="7.0"


# === 1. 全 Work Item ID を取得 ===
echo "🔍 すべての Work Item ID を取得中..."
WIQL_QUERY='{"query": "SELECT [System.Id] FROM WorkItems"}'
WIQL_URL="https://dev.azure.com/takurou76/az-learn/_apis/wit/wiql?api-version=7.0"

RESPONSE=$(curl -s -X POST "https://dev.azure.com/takurou76/az-learn/_apis/wit/wiql?api-version=7.0" \
  -H "Content-Type: application/json" \
  -H "Authorization: Basic OjljVGN1THFZMlppckx3ZUR2Y2xIdVlWYUg2eENvQnMyQ2RJeFlGTGltOXlDMFpPWjRRQ09KUVFKOTlCREFDQUFBQUFBQUFBQUFBQVNBWkRPNGFpUw==" \
  -d "$WIQL_QUERY")

IDS=$(echo "$RESPONSE" | jq '.workItems[].id')

if [ -z "$IDS" ]; then
  echo "✅ Work Item は存在しません。"
  exit 0
fi

echo "🗑️ 削除対象の Work Item ID:"
echo "$IDS"

# === 2. 各 Work Item を削除（Recycle Binへ） ===
for ID in $IDS; do
  echo "🚨 Work Item $ID を削除中..."
  DELETE_URL="https://dev.azure.com/${ORG}/${PROJECT}/_apis/wit/workitems/${ID}?api-version=${API_VERSION}"
  curl -s -X DELETE "$DELETE_URL" \
    -H "Authorization: Basic $ENCODED_PAT" > /dev/null
done

# === 3. Recycle Bin から完全削除 ===
echo "♻️ Recycle Bin から完全削除中..."
for ID in $IDS; do
  echo "❌ 完全削除 Work Item $ID..."
  PURGE_URL="https://dev.azure.com/${ORG}/${PROJECT}/_apis/wit/recyclebin/${ID}?api-version=7.1-preview.1"
  curl -s -X DELETE "$PURGE_URL" \
    -H "Authorization: Basic $ENCODED_PAT" > /dev/null
done

echo "✅ すべての Work Item を削除しました！"
