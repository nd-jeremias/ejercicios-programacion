from Menu_listas_anidadas.gondola import Gondola
from Package_Input.Input import *

max_filas = len(Gondola)
max_columnas = len(Gondola[0])
max_cantidad = 100

def pedir_producto() -> list:
    
    """ Pide con una serie de preguntas los datos que se deberan ingresar por el usuario.
        Devuelve una lista del producto """
    producto = []
    nombre = get_string("Que producto va a dar de alta? ", "El nombre no puede ser tan largo. Max 15 car.", 15, 3).capitalize()
    if nombre != None:
        fila = get_int(f"Ingrese la fila donde va a colocar el producto: min: 1 - max: {max_filas} ", "Error - Ingrese una opcion dentro del rango", 1, max_filas, 3)
        if fila != None:
            columna = get_int(f"Ingrese la columna: min: 1 - max: {max_columnas} ", "Error - Ingrese una opcion dentro del rango", 1, max_columnas, 3)
            if columna != None:
                cantidad = get_int(f"Que cantidad va a ingresar? maximo {max_cantidad}u. por producto ", "Error - Ingrese una opcion dentro del rango", 0, max_cantidad, 3)
                if cantidad != None:
                    producto = [nombre, cantidad, [fila,columna]]
                else:
                    input("Error al ingresar la cantidad. Se excedio el maximo de intentos permitidos")
            else:
                input("Error al ingresar la columna. Se excedio el maximo de intentos permitidos")
        else:
            input("Error al ingresar la fila. Se excedio el maximo de intentos permitidos")
    else:
        input("Error al ingresar el nombre. Se excedio el maximo de intentos permitidos")

    return producto

def alta_producto(producto:list) -> None:
    
    """ Recibe el producto a dar de alta en formato lista
    Utiliza la informacion recibida para guardarlo en la matriz de datos"""
    
    fila = producto[2][0] - 1
    columna = producto[2][1] - 1
    Gondola[fila][columna] = producto
    
def buscar_producto_nombre(nombre:str) -> list | None :
    
    """ Busca en la matriz de datos, el producto que coincida con el nombre pasado por parametro.
    Devuelve una lista con la ubicacion del producto en la matriz o None si no la encuentra.
    Donde la posicion [0] es la fila, y la posicion [1] la columna"""
    
    for i in range(len(Gondola)):
        for j in range(len(Gondola[i])):
            if Gondola[i][j]:
                if Gondola[i][j][0] == nombre:
                    retorno = [i,j]
                else:
                    retorno = None
    
    return retorno

def imprimir_producto(producto:list) -> None:
    
    """ Impresion detallada de un producto determinado
        El cual se pasa por parametro"""
    
    print(f"""
          Nombre:        {producto[0]}
          Cantidad:      {producto[1]}
          Ubicacion:
             Fila:       {producto[2][0]}
             Columna:    {producto[2][1]}""")
    
def eliminar_producto(producto:list) -> None:
    fila = producto[2][0] - 1
    columna = producto[2][1] - 1
    Gondola[fila][columna] = []
    
def error_alta() -> None:
    
    """ Impresion de carte de error al no dar de alta un producto """
    
    print('''
            *************************************************
            |                                               |
            |                    Error -                    |
            |    Primero se debe dar de alta al producto    |
            |                                               |
            *************************************************
            ''')
    time.sleep(1.5)