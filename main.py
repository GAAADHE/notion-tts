import requests, json

# load token from json
f_token = open("token.json") 
token = json.load(f_token)['token']
f_token.close()

databaseId = "fcebfe34146d42be8e63f33afb2675a6"

headers = {
  "Authorization": f"Bearer {token}",
  "Notion-Version": "2021-08-16",
  "Content-Type": "application/json"
}

def readDatabase(databaseId, headers):
  readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"
  res = requests.request('POST',readUrl, headers=headers)
  data = res.json()
  with open('./db.json','w', encoding='utf8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

def createPage(databaseId, headers):
  createUrl = 'https://api.notion.com/v1/pages' 
  new_page_data = {
    "parent": {"database_id":databaseId},
    "properties": {
      "Name": {
        "title": [
         {
           "type": "text",
            "text": {
            "content": "The title"
            }
          }
        ]
      }, 
      "Descrição": {
        "rich_text": [
          {  
            "text": {
              "content": "texte of exemple"  
            }
          }
        ]
      } 
    }
  }
  data = json.dumps(new_page_data)
  # print(str(data))
  res = requests.request("POST", createUrl, headers=headers, data=data)  
  print(str(res.status_code))

def updateaPage():
  pass


#readDatabase(databaseId, headers)
#createPage(databaseId, headers)

