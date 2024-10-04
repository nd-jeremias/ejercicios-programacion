from os import system
from Package_Input.Validate import validate_range
from Menu_listas_anidadas.utilidades import *

def menu() -> int:
    system("cls")
    opcion = int(input('''
        1 - Alta de productos (producto nuevo)
        2 - Baja de productos (producto existente)
        3 - Modificar productos (cantidad, ubicación)
        4 - Listar productos
        5 - Lista de productos ordenado por nombre
        6 - Salir
        '''))
    if validate_range(opcion, 1, 6):
        retorno = opcion
    else:
        retorno = menu()

    return retorno

def opcion_uno() -> bool:
    retorno = False
    producto = pedir_producto()
    if producto:
        imprimir_producto(producto)
        submit = input("Esta informacion es correcta? si / no ").lower()
        while submit != "si":
            producto = pedir_producto()
            imprimir_producto(producto)
            submit = input("Esta informacion es correcta? si / no ").lower()
        print(Gondola)
        alta_producto(producto)
        print(Gondola)
        retorno = True
    return retorno

def opcion_dos():
    
    opcion = int(input(""" 
        Va a dar de baja un producto.
        Seleccione el metodo:
                            1. Nombre
                            2. Ubicacion
                            """))
    while validate_range(opcion,1,2) == False:
        opcion = int(input(""" 
        Va a dar de baja un producto.
        Seleccione el metodo:
                            1. Nombre
                            2. Ubicacion
                            """))
    if opcion == 1:
        nombre = input("Ingrese el nombre del producto. ").capitalize()
        index = buscar_producto_nombre(nombre)
        imprimir_producto(Gondola[index[0]][index[1]])
        submit = input("Va a eliminar el siguiente producto. Esta seguro si / no ").lower()
        while submit != "si":
            nombre = input("Ingrese el nombre del producto. ").capitalize()
            index = buscar_producto_nombre(nombre)
            imprimir_producto(Gondola[index[0]][index[1]])
            submit = input("Va a eliminar el siguiente producto. Esta seguro si / no ").lower()
        eliminar_producto(Gondola[index[0]][index[1]])
    else:
        pass

def opcion_tres():
    pass

def opcion_cuatro():
    pass

def opcion_cinco():
    pass