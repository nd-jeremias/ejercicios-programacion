import json

def leer_json(ubicacion:str, nombre:str) -> list | bool:
    
    """ Se recibe por parametro la ruta del archivo a leer(ej: archivo.json)
    y como segundo parametro el nombre de la clave a buscar dentro.
    Si existe, se lee el archivo y se devuelve la lista obtenida
    sino, se retorna False"""
    
    retorno = False
    try:
        with open(ubicacion) as file:
            data = json.load(file)
            if data[nombre]:
                retorno = data[nombre]
    except:
        print("Hubo un error al abrir el archivo")
    return retorno

def guardar_archivo(nombre_archivo:str, contenido:str) -> None:
    
    """ Se recive por parametro el nombre que va a tener el archivo a guardar
    y un string que contenga la informacion formateada para csv
    Se retorna True si fue exitosa la operacion, sino False y se imprime un error"""
    
    try:
        archivo = open(nombre_archivo, 'w+')
        archivo.write(contenido)
        archivo.close()
        print(f"Se creó el archivo: {nombre_archivo}.")
        retorno = True
    except:
        print(f"Error al crear el archivo: {nombre_archivo}.")
        retorno = False
    return retorno

#CHATGPT SOLUTION
def generar_csv_gpt_v2(ubicacion:str, lista:list) -> None | bool:
    
    """ Se recibe la ruta del archivo a escribir,
    y como segundo parametro la lista de informacion.
    si la lista no esta vacia, se vuelva en un csv,
    sino se retorna False"""
    if lista:
        cadena = ";".join(map(str, (lista[0].keys()))) + "\n"
        for e in lista:
            values = list(e.values())
            item = ";".join(map(str, values)) + "\n"
            cadena += "".join(item)
        guardar_archivo(ubicacion, cadena)
    else:
        print("Error - La lista esta vacia")
        return False

lista_heroes = leer_json('data_stark.json', 'heroes')
generar_csv_gpt_v2("archivo.csv", lista_heroes)