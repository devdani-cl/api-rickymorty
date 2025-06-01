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
#print(status_personaje)

# 3.- Un método capaz de obtener TODOS los episodios. Gu´ardelos en una lista llamada episodios dentro de la clase.
episodios = []
for e in characters["results"]:
    capitulos = e["episode"]
    for i in capitulos:
        info = requests.get(i).json() #['id', 'name', 'air_date', 'episode', 'characters', 'url', 'created']
        episodio = info["episode"]
        episodios.append(episodio)
#print(episodios)
#4.- crear una lista de diccionario que muestre: "[{temporada 1: 12 episodios}]" algo así.


#5.- Un método capaz de obtener todos los planetas y estaciones espaciales que se muestran en el endpoint location.


#6.- El hilo principal, en donde usted llamar´a a la clase RAMExtractor, debe iterar sobre las páginas de resultados.


#7.- Imprima los índices que ocupan los personajes que en su nombre lleven ”Rick” y ”Morty”.

#8.- Si en el ítem anterior usted es capaz de hacer que la impresión en pantalla
#muestre el índice y además el nombre de los personajes de manera “bonita”, obtiene 10
#puntos más. Por otro lado, si es capaz de dejar en listas separadas a estos personajes
#e imprimir de manera “bonita” cada lista, obtiene 10 puntos adicionales.

