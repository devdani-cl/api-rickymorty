import json
import requests

url = 'https://rickandmortyapi.com/api'
 # {'characters': 'url', 'locations': 'url', 'episodes': 'url'}
response = requests.get(url) 
api_json = json.loads(response.text)

characters = requests.get(api_json["characters"]).json() # ['info', 'results']
#characters["results"] = ['id', 'name', 'status', 'species', 'type', 'gender', 'origin', 'location', 'image', 'episode', 'url', 'created']

status_personaje = []
for n in characters["results"]:
    name = n["name"]
    status = n["status"]
    status_personaje.append((name,status))

print(status_personaje)
