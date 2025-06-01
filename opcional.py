import json
import requests


url = 'https://rickandmortyapi.com/api'
 # {'characters': 'url', 'locations': 'url', 'episodes': 'url'}
response = requests.get(url) 
api_json = json.loads(response.text)

characters = requests.get(api_json["characters"]).json() # ['info', 'results']
#characters["results"] = ['id', 'name', 'status', 'species', 'type', 'gender', 'origin', 'location', 'image', 'episode', 'url', 'created']

'''
mi duda al usar list-comprehesion es, 
¿puedo usar la lista creada para acceder a otras llaves? ejemplo: 'status', 'species', 'origin', etc
'''

personajes = [n["name"] for n in characters["results"]]
status = [s["status"] for s in characters["results"]]

status_personaje = []
for n in personajes:
    name = n 
    for s in status:
        estado = s
        status_personaje.append((name,estado))

print(status_personaje)

