from os import system
from Menu_listas_anidadas.utilidades import *

def menu() -> int:
    system("cls")
    opcion = get_int('''
        1 - Alta de productos (producto nuevo)
        2 - Baja de productos (producto existente)
        3 - Modificar productos (cantidad, ubicación)
        4 - Listar productos
        5 - Lista de productos ordenado por nombre
        6 - Salir
        
        Seleccione una opcion de la lista:''',
        "Opcion fuera de rango. Intente nuevamente", 1, 6, -1)
    return opcion

def opcion_uno(matriz:list) -> bool:
    
    retorno = False
    producto = pedir_producto()
    if producto:
        imprimir_producto(producto)
        submit = input("Esta informacion es correcta? si / no ").lower()
        if submit == "si":
            alta_producto(matriz, producto)
            retorno = True
        else:
            input("Proceso cancelado por el usuario - Presione enter para volver al menu ")
    return retorno

def opcion_dos(matriz):
    
    opcion = get_int(""" 
        Va a dar de baja un producto.
        Seleccione el metodo:
        
                            1. Nombre
                            2. Ubicacion
                            """,
        "Debe seleccionar una opcion de la lista. ", 1, 2, 3)
    if opcion == 1:
        baja_nombre(matriz)
    elif opcion == 2:
        baja_ubicacion(matriz)
    else:
        input("Se excedio el maximo de intentos permitidos")

def opcion_tres(matriz:list):
    
    opcion = get_int(""" 
        Va a modificar un producto.
        Seleccione lo que desea modificar:
        
                            1. Cantidad
                            2. Ubicacion
                            """,
        "Debe seleccionar una opcion de la lista. ", 1, 2, 3)
    if opcion == 1:
        mod_cantidad(matriz)
    elif opcion == 2:
        mod_ubicacion(matriz)
    else:
        input("Se excedio el maximo de intentos permitidos")

def opcion_cuatro(matriz):
    
    imprimir_cabecera()
    imprimir_listado(matriz)
    input("Presione enter para volver al menu. ")

def opcion_cinco(matriz):
    
    lista_ordenada = [[]]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
             if matriz[i][j]:
                 lista_ordenada[0].append(matriz[i][j])
                 
    for i in range(len(lista_ordenada[0])-1):
        for j in range(i+1, len(lista_ordenada[0])):
            if lista_ordenada[0][j][0] < lista_ordenada[0][i][0]:
                lista_aux = lista_ordenada[0][j]
                lista_ordenada[0][j] = lista_ordenada[0][i]
                lista_ordenada[0][i] = lista_aux
    
    opcion_cuatro(lista_ordenada)