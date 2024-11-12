from package_stark.opciones import *

while 1:
    opcion = menu()
    if opcion == "1":
        opcion_uno()
    elif opcion == "2":
        opcion_dos()
    elif opcion == "3":
        opcion_tres()
    elif opcion == "4":
        opcion_cuatro()
    elif opcion == "5":
        opcion_cinco()
    elif opcion == "6":
        opcion_seis()
    elif opcion == "7":
        opcion_siete()
    elif opcion == "8":
        print("Hasta luego!")
        break
    else:
        print("Opcion fuera de rango")
    input("\nPresione enter para continuar.")