import json

def leer_json(ubicacion:str, nombre:str) -> list | bool:
    
    """ Se recibe por parametro la ruta del archivo a leer(ej: archivo.json)
    y como segundo parametro el nombre de la clave a buscar dentro.
    Si existe, se lee el archivo y se devuelve la lista obtenida
    sino, se retorna False"""
    ubicacion += ".json"
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
    nombre_archivo += ".csv"
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
def generar_csv_gpt_v2(nombre:str, lista:list) -> None | bool:
    
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
        guardar_archivo(nombre, cadena)
    else:
        print("Error - La lista esta vacia")
        return False

def swap(lista:list, i:int, j:int) -> None:
    
    """ Realiza un swap en la lista recibida """
    
    aux = lista[j]
    lista[j] = lista[i]
    lista[i] = aux

def ordenar(lista:list, atributo:str, orden=1) -> None:
    
    """ Ordena la lista recibida segun el orden definido.
    Si recibe 1 ordena ascendente. Forma predeterminada
    Con -1 se ordena de forma descendente"""
    
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if orden == 1 and lista[j][atributo] < lista[i][atributo]:
                swap(lista, i, j)
            elif orden == -1 and lista[j][atributo] > lista[i][atributo]:
                swap(lista, i, j)