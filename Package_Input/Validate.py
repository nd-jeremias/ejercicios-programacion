import time

def validate_range(numero:int|float, minimo:int, maximo:int) -> bool:
    
    """ Funcion para validar un numero en determinado rango.
    Una vez validado el numero devuelve Verdadero o Falso segun corresponda """
    
    if numero >= minimo and numero <= maximo:
        retorno = True
    else:
        retorno = False
    
    return retorno

def validate_lenght(longitud:int, maximo:int) -> bool:
    
    """La funcion recibe la longitud de la cadena a validar y lo compara con el maximo.
    Devuelve Verdadero o Falso segun corresponda """
    
    if longitud <= maximo:
        retorno = True
    else:
        retorno = False
        
    return retorno

def isfloat(cadena:str) -> bool:
    """ Recibe una cadena y evalua caracter por caracter
    Si encuentra una letra devuelve False.
    Si encuentra solamente numeros y un solo punto devuelve True """
    retorno = True
    if cadena.count(".") == 1:
        for char in cadena:
            if not char.isdigit() and char != ".":
                retorno = False
    else:
        retorno = False

    return retorno

def isnumber(number:str) -> bool:
    retorno = False
    if isfloat(number): retorno = True 
    if number.isdigit(): retorno = True
    return retorno

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