#1
def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int)-> int | None:
    # La funcion valida el numero ingresado por el usuario entre el minimo y el maximo pasados por parametros. Ej: 
    # MINIMO = 0
    # MAXIMO = 100
    # MENSAJE = 'Ingrese un numero entre {minimo} y {maximo}' -> Reemplazar por los numeros deseados
    # MENSAJE_ERROR = "Ha ingresado un dato invalido, vuelva a intentarlo!"
    # REINTENTOS = 3
    # Se devuelve el numero validado, o None en caso de exceder los intentos
    print(mensaje)
    numero = int(input())
    if numero < minimo or numero > maximo:
        reintentos -= 1
        if reintentos > 0:
            return get_int(mensaje, mensaje_error, minimo, maximo, reintentos)
        else:
            print("Ha alcanzado el maximo de intentos")
            return None
    return numero

def get_float(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int)-> float | None:
    # La funcion valida el numero ingresado por el usuario entre el minimo y el maximo pasados por parametros. Ej: 
    # MINIMO = 0
    # MAXIMO = 100
    # MENSAJE = 'Ingrese un numero entre {minimo} y {maximo}' -> Reemplazar por los numeros deseados
    # MENSAJE_ERROR = "Ha ingresado un dato invalido, vuelva a intentarlo!"
    # REINTENTOS = 3
    # Se devuelve el numero validado, o None en caso de exceder los intentos
    print(mensaje)
    numero = float(input())
    if numero < minimo or numero > maximo:
        reintentos -= 1
        if reintentos > 0:
            return get_float(mensaje, mensaje_error, minimo, maximo, reintentos)
        else:
            print("Ha alcanzado el maximo de intentos")
            return None
    return numero

#2
def get_string(mensaje:str, mensaje_error:str, maximo:int, reintentos:int)-> str | None:
    # La funcion valida el largo de la cadena ingresada por el usuario
    # El limite maximos se pasa por parametro. Ej: 
    # MAXIMO = 10
    # MENSAJE = 'Ingrese un numero cadena menor a 10 caracteres'
    # MENSAJE_ERROR = "Ha ingresado un dato invalido, vuelva a intentarlo!"
    # REINTENTOS = 3
    # Se devuelve el String validado, o None en caso de exceder los intentos
    print(mensaje)
    cadena = input()
    longitud = len(cadena)
    if longitud > maximo:
        reintentos -= 1
        if reintentos > 0:
            print(mensaje_error)
            return get_string(mensaje, mensaje_error, maximo, reintentos)
        else:
            print("Ha alcanzado el maximo de intentos")
            return None
    return cadena

