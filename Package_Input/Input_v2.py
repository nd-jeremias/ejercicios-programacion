from Package_Input.Validate import * # Trae las funciones de validacion.
maximo = 15

def get_int()-> int | None:
    """ La fucion obtiene un numero entero y llama a la funcion validate_number() para validarlo.
    En el caso de que el numero sea valido, lo devuelve.
    Caso contrario devuelve None """
    retorno = None
    numero = int(input("Ingrese un numero entero: "))
    if validate_number(numero):
        retorno = numero
    return retorno

def get_float()-> float | None:
    """ La fucion obtiene un numero flotante y llama a la funcion validate_number() para validarlo.
    En el caso de que el numero sea valido, lo devuelve.
    Caso contrario devuelve None """
    retorno = None
    numero = float(input("Ingrese un numero: "))
    if validate_number(numero):
        retorno = numero
    return retorno

def get_string()-> str | None:
    """ La funcion obtiene una cadena ingresada por el usuario.
    Luego llama a la funcion validate_lenght() para verificar el largo.
    Se devuelve el String validado, o None en caso de ser demasiado larga """
    retorno = None
    print(f"Ingrese una cadena menor a {maximo} caracteres")
    cadena = input()
    longitud = len(cadena)
    if validate_lenght(longitud):
        retorno = cadena
    return retorno