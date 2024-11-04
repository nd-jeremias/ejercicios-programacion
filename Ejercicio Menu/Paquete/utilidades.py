import time

def list_import():
    
    """ Se importa el modulo donde se encuentran las listas con datos
        Se devuelve el modulo. """
    
    from Paquete import listas_personas
    
    return listas_personas

def filtrar_pais(lista:list, pais:str) -> list:
    
    """ Funcion que devuelve la posicion donde se encuentra en el listado, el pais ingresado. """
    
    retorno = []
    for i in range(len(lista)):
        if pais == lista [i]:
            retorno.append(i)
    return retorno

# Posible alternativa a las dos funciones q filtran edad:
# def filtrar_rango(lista:list, minimo=0, maximo=100) -> list:
#     retorno = []
#     for i in range(len(lista)):
#         if lista [i] >= minimo and lista[i] <= maximo:
#             retorno.append(i)
#     return retorno

def filtrar_edad_menor(edades:list) -> list:
    
    """ Funcion que devuelve las posiciones de las personas con menor edad. """
    
    minimo = int(edades[0])
    posiciones = [0]
    for i in range (len(edades)):
        if edades[i] < minimo:
            minimo = edades[i]
            posiciones = [i]
        elif edades[i] == minimo and i > 0:
            posiciones.append(i)
    
    return posiciones

def filtrar_edad_mayor(edades:list,) -> list:
    
    """ Funcion que devuelve las posiciones de las personas de mayor edad. """
    
    maximo = int(edades[0])
    posiciones = [0]
    for i in range (len(edades)):
        if edades[i] > maximo:
            maximo = edades[i]
            posiciones = [i]
        elif edades[i] == maximo and i > 0:
            posiciones.append(i)
    
    return posiciones

def calc_promedio(lista:list, suma = 0) -> float:
    
    """ La funcion debe recibir una lista con numeros y calcula el promedio de los mismos
        Devuelve el resultado"""
    
    for i in range(len(lista)):
        suma += lista[i]
    promedio = suma / (len(lista))
    return promedio

def falta_listado():
    print('''
            **********************************************
            |                                            |
            |    Primero se deben importar las listas    |
            |                                            |
            **********************************************
            ''')
    time.sleep(1.5)
    
def print_all(listado, posicion):
    print(f""" 
            -------------------------------------
            
             ->  Nombre:    {listado.names[posicion]}
             ->  Telefono:  {listado.phones[posicion]}
             ->  Mail:      {listado.mails[posicion]}
             ->  Direccion: {listado.address[posicion]}
             ->  CP:        {listado.postalZip[posicion]}
             ->  Provincia: {listado.region[posicion]}
             ->  Pais:      {listado.country[posicion]}
             ->  Edad:      {listado.ages[posicion]}
            """)
    
def print_partial(listado, posicion):
    print(f""" 
            -------------------------------------
            
             ->  Nombre:    {listado.names[posicion]}
             ->  Telefono:  {listado.phones[posicion]}
             ->  Mail:      {listado.mails[posicion]}
            """)
    
def ordenar_descendente(lista:list, posiciones:list) -> list:
    for i in range(len(posiciones)-1):
        for j in range(i+1, len(posiciones)):
            if lista[posiciones[j]] > lista[posiciones[i]]:
                aux = posiciones[j]
                posiciones[j] = posiciones[i]
                posiciones[i] = aux
                

def ordenar_asc(posiciones:list, lista:list) -> None:
    for i in range(len(posiciones)-1):
        for j in range(i+1, len(posiciones)):
            if lista[posiciones[j]] < lista[posiciones[i]]:
                aux = posiciones[j]
                posiciones[j] = posiciones[i]
                posiciones[i] = aux