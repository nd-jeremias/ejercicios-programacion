#1
""" Productos = [["Botellas", 3, [1,2]],["Frascos", 8, [1,4]],["Fideos", 4, [2,3]],["Leche", 6, [3,4]]]
 """
#2
import time
from Menu_listas_anidadas.opciones import *

import_flag = True

while 1:
    opcion = menu()
    if opcion == 1:
        if opcion_uno():
            import_flag = True
            print('''
                *******************************
                |                             |
                |    Producto dado de alta    |
                |                             |
                *******************************
                ''')
            input("Presione enter para continuar.")
    elif opcion == 2:
        if import_flag:
            opcion_dos()
        else:
            error_alta()
            """ Pedir nombre del producto, o ubicacion y chequear en la matriz si existe, borrarlo y sino avisar """
        input("Presione enter para volver al menu.")
        pass
    elif opcion == 3:
        """ Lo mismo que el anterior pero pide los datos a modificar
        crear una funcion de busqueda de producto"""
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    elif opcion == 6:
        break