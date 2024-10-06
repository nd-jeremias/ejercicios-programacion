#1
""" Productos = [["Botellas", 3, [1,2]],["Frascos", 8, [1,4]],["Fideos", 4, [2,3]],["Leche", 6, [3,4]]]
 """
#2
import time
#from Menu_listas_anidadas.gondola import Gondola
from Menu_listas_anidadas.opciones import *

import_flag = False

while 1:
    opcion = menu()
    if opcion == 1:
        if opcion_uno(Gondola):
            import_flag = True
            print('''
                *******************************
                |                             |
                |    Producto dado de alta    |
                |                             |
                *******************************
                ''')
            time.sleep(1.5)
    elif opcion == 2:
        if import_flag:
            opcion_dos(Gondola)
        else:
            error_alta()
    elif opcion == 3:
        if import_flag:
            opcion_tres(Gondola)
        else:
            error_alta()
    elif opcion == 4:
        if import_flag:
            opcion_cuatro(Gondola)
        else:
            error_alta()
    elif opcion == 5:
        if import_flag:
            opcion_cinco(Gondola)
        else:
            error_alta()
    elif opcion == 6:
        break