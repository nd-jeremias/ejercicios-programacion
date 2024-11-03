from package.funciones import *
from estudiantes import estudiantes


c_estudiantes = estudiantes

opcion = ""

while opcion != "8":
    opcion = menu()
    if opcion == "1":
        opcion_uno(c_estudiantes)
    elif opcion == "2":
        opcion_dos(c_estudiantes)
    elif opcion == "3":
        opcion_tres(c_estudiantes)
    elif opcion == "4":
        opcion_cuatro(c_estudiantes)
    elif opcion == "5":
        opcion_cinco(c_estudiantes)
    elif opcion == "6":
        opcion_seis(c_estudiantes)
    elif opcion == "7":
        opcion_siete(c_estudiantes)
    if int(opcion) > 0 and int(opcion) < 8:
        input("Presione cualquier tecla para continuar")
    elif opcion == "8":
        print("Hasta luego!")
    else:
        input("Ingrese un valor dentro del rango")