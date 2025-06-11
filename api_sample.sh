AUTH_HEADER="Authorization: Basic OjljVGN1THFZMlppckx3ZUR2Y2xIdVlWYUg2eENvQnMyQ2RJeFlGTGltOXlDMFpPWjRRQ09KUVFKOTlCREFDQUFBQUFBQUFBQUFBQVNBWkRPNGFpUw=="
ORG="takurou76"
PRJ="az-learn"

# Upload picture
IMAGE_URL=$( \ 
  curl -X POST \
    -H "$AUTH_HEADER" \
    -H "Content-Type: application/octet-stream" \
    --data-binary @"./57DB2109-BF44-4FCE-844D-1DB4245C831E_4_5005_c.jpeg" \
    "https://dev.azure.com/$ORG/$PRJ/_apis/wit/attachments?fileName=your-image.png&api-version=7.0" | jq -r '.url')

# Create workItem =========================================================================================
  JSON_DATA=$(cat <<EOF
[
  {
    "op": "add",
    "path": "/fields/System.Title",
    "value": "NEW TASK-1001"
  },
  {
    "op": "add",
    "path": "/fields/System.Description",
    "value": "<p>以下に画像を添付します。</p><p><img src=\"$IMAGE_URL\" alt=\"参考画像\" /></p>"
  },
  {
    "op": "add",
    "path": "/fields/System.AssignedTo",
    "value": "takurou76@icloud.com"
  },
  {
    "op": "add",
    "path": "/fields/System.Tags",
    "value": "Batch1"
  }
]
EOF
)

curl -X POST \
  -H "Content-Type: application/json-patch+json" \
  -H "$AUTH_HEADER" \
  -d "$JSON_DATA" \
  "https://dev.azure.com/$ORG/$PRJ/_apis/wit/workitems/%24Task?api-version=7.0"

# Get workItems =========================================================================================
curl -X POST \
  -H "$AUTH_HEADER" \
  -H "Content-Type: application/json" \
  -d '{"query": "SELECT [System.Id], [System.Title], [System.State] FROM WorkItems WHERE [System.TeamProject] = \"az-learn\" ORDER BY [System.ChangedDate] DESC"}' \
  "https://dev.azure.com/$ORG/$PRJ/_apis/wit/wiql?api-version=7.0" | jq

# Get workItems for NG =========================================================================================
# only NG
IDS=$(curl -X POST \
  -H "$AUTH_HEADER" \
  -H "Content-Type: application/json" \
  -d '{"query": "SELECT [System.Id] FROM WorkItems WHERE [System.Tags] CONTAINS \"NG\""}' \
  "https://dev.azure.com/$ORG/$PRJ/_apis/wit/wiql?api-version=7.0" | jq '.workItems[].id')

# NG and Bathc1
IDS=$(curl -X POST \
  -H "$AUTH_HEADER" \
  -H "Content-Type: application/json" \
  -d '{"query": "SELECT [System.Id] FROM WorkItems WHERE [System.Tags] CONTAINS \"NG\" AND [System.Tags] CONTAINS \"Batch1\""}' \
  "https://dev.azure.com/$ORG/$PRJ/_apis/wit/wiql?api-version=7.0" | jq '.workItems[].id')


for ID in $IDS; do
  curl -X GET \
    -H "$AUTH_HEADER" \
    -H "Content-Type: application/json" \
    "https://dev.azure.com/$ORG/$PRJ/_apis/wit/workItems/$ID/comments?api-version=7.0-preview" | jq '.comments[] | {createdDate, text}'
done



