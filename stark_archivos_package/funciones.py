import json

archivo = "data_stark.json"
with open(archivo) as file:
    data = json.load(file)
    diccionario = data["heroes"]


cabecera = str(diccionario[0].keys())
for e in diccionario:
    print(e.values())
#print(data)