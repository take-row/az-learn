# Fetch Task
```sh
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Basic OjljVGN1THFZMlppckx3ZUR2Y2xIdVlWYUg2eENvQnMyQ2RJeFlGTGltOXlDMFpPWjRRQ09KUVFKOTlCREFDQUFBQUFBQUFBQUFBQVNBWkRPNGFpUw==" \
  --data '{
    "query": "SELECT [System.Id], [System.Title], [System.State] FROM WorkItems WHERE [System.TeamProject] = \"az-learn\" ORDER BY [System.ChangedDate] DESC"
  }' \
  "https://dev.azure.com/takurou76/az-learn/_apis/wit/wiql?api-version=7.0"
```
```json
{
    "queryType":"flat",
    "queryResultType":"workItem",
    "asOf":"2025-04-26T03:26:59.513Z",
    "columns":[
        {
            "referenceName":"System.Id",
            "name":"ID",
            "url":"https://dev.azure.com/takurou76/_apis/wit/fields/System.Id"
        },
        {
            "referenceName":"System.Title",
            "name":"Title",
            "url":"https://dev.azure.com/takurou76/_apis/wit/fields/System.Title"
        },
        {
            "referenceName":"System.State",
            "name":"State",
            "url":"https://dev.azure.com/takurou76/_apis/wit/fields/System.State"
        }
    ],
    "sortColumns":[
        {
            "field":
            {
                "referenceName":"System.ChangedDate",
                "name":"Changed Date",
                "url":"https://dev.azure.com/takurou76/_apis/wit/fields/System.ChangedDate"
            },
            "descending":true
        }
    ],
    "workItems":[
        {
            "id":9,
            "url":"https://dev.azure.com/takurou76/7400eb47-8ae1-409c-bd3f-b53bc4d5e6c8/_apis/wit/workItems/9"
        },
        {
            "id":8,
            "url":"https://dev.azure.com/takurou76/7400eb47-8ae1-409c-bd3f-b53bc4d5e6c8/_apis/wit/workItems/8"
        },
        {
            "id":7,
            "url":"https://dev.azure.com/takurou76/7400eb47-8ae1-409c-bd3f-b53bc4d5e6c8/_apis/wit/workItems/7"
        }
    ]
}
```

# Add Task
```sh
curl -X POST \
  -H "Content-Type: application/json-patch+json" \
  -H "Authorization: Basic OjljVGN1THFZMlppckx3ZUR2Y2xIdVlWYUg2eENvQnMyQ2RJeFlGTGltOXlDMFpPWjRRQ09KUVFKOTlCREFDQUFBQUFBQUFBQUFBQVNBWkRPNGFpUw==" \
  --data '[
    {
      "op": "add",
      "path": "/fields/System.Title",
      "value": "NEW TASK"
    },
    {
      "op": "add",
      "path": "/fields/System.Description",
      "value": "このタスクはAPI経由で追加されました。"
    }
  ]' \
  "https://dev.azure.com/takurou76/az-learn/_apis/wit/workitems/%24Task?api-version=7.0"


```

```
curl -X GET \
  -H "Authorization: Basic OjljVGN1THFZMlppckx3ZUR2Y2xIdVlWYUg2eENvQnMyQ2RJeFlGTGltOXlDMFpPWjRRQ09KUVFKOTlCREFDQUFBQUFBQUFBQUFBQVNBWkRPNGFpUw==" \
  "https://dev.azure.com/takurou76/az-learn/_apis/wit/workitemtypes/Task?api-version=7.0"
```