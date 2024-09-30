from Paquete.opciones import *
import time
from os import system

import_flag = False

while 1:
    system("cls")
    opcion = menu()
    if opcion < 0 or opcion > 8:
        print('''
            ********************************************
            |                                          |
            |    Error - Ingrese una opcion valida:    |
            |                                          |
            ********************************************
            ''')
        time.sleep(1.5)
    elif opcion == 1:
        listado = list_import()
        import_flag = True
        print('''
            ***************************
            |                         |
            |    Listado importado    |
            |                         |
            ***************************
            ''')
        time.sleep(1.5)
    elif opcion == 2:
        if import_flag:
            opcion_dos(listado)
            input("Presione enter para volver al menu.") #Buscar alternativa
        else:
            falta_listado()
    elif opcion == 3:
        if import_flag:
            opcion_tres(listado)
            input("Presione enter para volver al menu.") #Buscar alternativa
        else:
            falta_listado()
    elif opcion == 4:
        if import_flag:
            opcion_cuatro(listado)
            input("Presione enter para volver al menu.") #Buscar alternativa
        else:
            falta_listado()
    elif opcion == 5:
        if import_flag:
            opcion_cinco(listado)
            input("Presione enter para volver al menu.") #Buscar alternativa
        else:
            falta_listado()
    elif opcion == 6:
        if import_flag:
            opcion_seis(listado)
            input("Presione enter para volver al menu.") #Buscar alternativa
        else:
            falta_listado()
    elif opcion == 7:
        if import_flag:
            opcion_siete(listado)
            input("Presione enter para volver al menu.") #Buscar alternativa
        else:
            falta_listado()
    elif opcion == 8:
        if import_flag:
            opcion_ocho(listado)
            input("Presione enter para volver al menu.") #Buscar alternativa
        else:
            falta_listado()
    elif opcion == 0:
        break