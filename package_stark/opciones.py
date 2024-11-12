from package_stark.utilidades import *
from package_stark.data_stark import lista_personajes

from copy import deepcopy
from os import system

heroes = deepcopy(lista_personajes)
imc_flag = False

def menu() -> str:
    system("cls")
    opcion = input('''
            1. Listar ordenado por Nombre.
            2. Listar Masculinos débiles.
            3. Cantidad por color de ojos.
            4. Listar por color de Pelo.
            5. Listar inteligencia.
            6. Listar Promedio.
            7. Asignar IMC.
            8. Salir
            Ingrese una opcion: ''')
            
    return opcion

def opcion_uno() -> None:

    ordenar(heroes, "nombre")
    print_all(heroes, imc_flag)

def opcion_dos() -> None:
    lista_filtrada = obtener_min_max(heroes, "fuerza", -1)
    ordenar(lista_filtrada, "fuerza")
    print(f'''
        |-------------------------------------------------|
        |    {'Los masculinos con menos fuerza son:'.center(44)} |
        |-------------------------------------------------|''')
    print_all(lista_filtrada, imc_flag)

def opcion_tres() -> None:
    lista_color_ojos = obtener_datos(heroes,"color_ojos")
    for o in lista_color_ojos:
        cant = 0
        for h in heroes:
            cant = cant + 1 if h["color_ojos"] == o else cant
        print(f'''
        |--------------------------------------------------------------|
        
            Hay {cant} superheroes 
            con color de ojos {o}   ''')
    print(f'''
        |--------------------------------------------------------------|''')

def opcion_cuatro() -> None:
    lista_color_pelo = obtener_datos(heroes,"color_pelo")
    for e in lista_color_pelo:
        lista_filtrada = filtrar(heroes, "color_pelo", e)
        print(f'''
              
            Color de pelo: {e}''')
        print_all(lista_filtrada, imc_flag)
        
def opcion_cinco() -> None:
    tipo_inteligencia = obtener_datos(heroes,"inteligencia")
    for e in tipo_inteligencia:
        lista_filtrada = filtrar(heroes, "inteligencia", e)
        print(f"Inteligencia: {e}")
        print_all(lista_filtrada, imc_flag)

def opcion_seis() -> None:
    mujeres = filtrar(heroes, "genero", "F")
    prom = promedio(mujeres, "fuerza")
    for h in heroes:
        if int(h["fuerza"]) > prom:
            print(f'''
        |-------------------------------------------------|      
        |    {"Nombre:".ljust(14)} {h["nombre"].ljust(30)}|
        |    {"Peso:".ljust(14)} {str("%.2f" %float(h["peso"])).ljust(30)}|
        |-------------------------------------------------|''')

def opcion_siete() -> None:
    global imc_flag
    imc_flag = True
    print_header(imc_flag)
    for h in heroes:
        imc = calcular_imc(float(h["peso"]), convertir_cm_a_m(float(h["altura"])))
        h["IMC"] = str("%.2f" %imc)
        print_one(h)