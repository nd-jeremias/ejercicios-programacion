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
    
    """La funcion recibe la longitud de la cadena a validar y lo compara con el maximo. Devuelve Verdadero o Falso segun corresponda """
    
    if longitud <= maximo:
        retorno = True
    else:
        retorno = False
        
    return retorno
