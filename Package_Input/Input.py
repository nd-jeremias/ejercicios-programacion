from Package_Input.Validate import *

def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int)-> int | None:
    
    """ Funcion que le pide al usuario un numero entero y valida el rango llamando a la funcion validate_number()
    Devuelve el numero en caso que sea correcto y None en caso incorrecto si se exceden los reintentos"""
    
    retorno = None
    if reintentos > 0:
        numero = int(input(mensaje))
        if validate_range(numero, minimo, maximo):
            retorno = numero
        else:
            print(mensaje_error)
            retorno = get_int(mensaje,mensaje_error, minimo, maximo, reintentos-1)
    return retorno

def get_float(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int)-> int | None:
    
    """ Funcion que le pide al usuario un numero flotante y valida el rango llamando a la funcion validate_number()
    Devuelve el numero en caso que sea correcto y None en caso incorrecto si se exceden los reintentos"""
    
    retorno = None
    if reintentos >= 0:
        numero = float(input(mensaje))
        if validate_range(numero, minimo, maximo):
            retorno = numero
        else:
            print(mensaje_error)
            retorno = get_float(mensaje,mensaje_error, minimo, maximo, reintentos-1)
    return retorno

def get_string(mensaje:str, mensaje_error:str, maximo:int, reintentos:int)-> str | None:
    
    """ Funcion que pide una cadena y valida la longitud llamando a la funcion validate_lenght()
    Devuelve la cadena si es correcto, y None en caso de que exceda el limite"""
    
    retorno = None
    if reintentos > 0:
        cadena = input(mensaje)
        longitud = len(cadena)
        if validate_lenght(longitud, maximo):
            retorno = cadena
        else:
            print(mensaje_error)
            retorno = get_string(mensaje,mensaje_error, maximo, reintentos-1)
    
    return retorno
    
    
    
    
    