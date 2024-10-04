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

def filtrar_edad_menor(lista:list, edad_maxima:int) -> list:
    
    """ Funcion que devuelve las posiciones de las personas dentro del limite de edad. """
    
    retorno = []
    for i in range(len(lista)):
        if lista [i] <= edad_maxima:
            retorno.append(i)
    return retorno

def filtrar_edad_mayor(lista:list, edad_minima:int) -> list:
    
    """ Funcion que devuelve las posiciones de las personas que pasan la edad minima. """
    
    retorno = []
    for i in range(len(lista)):
        if lista [i] >= edad_minima:
            retorno.append(i)
    return retorno

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
    
def ordenar_descendente(lista:list, posicion:list) -> list:
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[j] > lista[i]:
                aux = posicion[j]
                posicion[j] = posicion[i]
                posicion[i] = aux

    return lista