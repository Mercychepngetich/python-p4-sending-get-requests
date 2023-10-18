import requests
import json

url = "https://learn-co-curriculum.github.io/json-site-example/"

response = requests.get(url)



# print(json.dumps(json_content, indent=4))
# print(response.text)

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"

response = requests.get(url)
json_content= json.loads(response.content)

print(json.dumps(json_content, indent=4, sort_keys=True))
