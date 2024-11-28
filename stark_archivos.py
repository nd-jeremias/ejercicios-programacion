from stark_archivos_package import opciones
from stark_archivos_package import funciones #BORRAR
flag = False

while 1:
    opcion = opciones.menu()
    if opcion == "A":
        json_r = opciones.opcion_a()
        if json_r:
            print("JSON Importado")
            flag = True
    elif opcion == "B":
        if flag == True:
            opciones.opcion_b(json_r)
        else:
            print("Primero debe leer el JSON")
    elif opcion == "C":
        if flag == True:
            opciones.opcion_c(json_r)
        else:
            print("Primero debe leer el JSON")
    elif opcion == "D":
        print("Hasta luego!")
        break
    else:
        print("Opcion fuera de rango")
    input("\nPresione enter para continuar.")