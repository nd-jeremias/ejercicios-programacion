from package.utilidades import *
from os import system

def menu() -> str:
    system("cls")
    opcion = input(''' 
                1 - Listar los alumnos por orden ascendente (apellido) y mostrar legajo, nombre, apellido y edad
                2 - Obtener el promedio de notas para cada estudiante 
                3 - Listar legajo, nombre, apellido y edad de los estudiantes que cursan el programa de “Ingenieria en Informatica” 
                4 - Obtener un promedio de edad de los estudiantes.
                5 - Informar el alumno con mayor pomedio de notas. Mostrar nombre y apellido 
                6 - Listar nombre y apellido de los alumnos que forman el grupo “Club de Informática” con sus respectivos promedios
                7 - Listar legajo, nombre, apellido y programas que cursan los alumnos más jóvenes.
                8 - Salir
                Ingrese el numero de la opcion solicitada: 
                ''')
    return opcion

def opcion_uno(data:list) -> None:
    ordenar_asc(data)
    imprimir_cabecera()
    for e in range(len(data)):
        imprimir(data[e])

def opcion_dos(data:list) -> None:
    print(f'''
            {"Legajo".center(7)} - {"Nombre".center(15)} - {"Apellido".center(15)} - {"Promedio".center(6)}
            ''')
    for e in range(len(data)):
        prom = promedio(data[e]["notas"])
        print(f'''
            {str(data[e]["legajo"]).center(7)} - {data[e]["nombre"].center(15)} - {data[e]["apellido"].center(15)} - {str('%.2f' % prom).center(6)}
            ''')

def opcion_tres(data:list) -> None:
    imprimir_cabecera()
    for e in range(len(data)):
        if data[e]["programa"]["nombre"] == "Ingenieria en Informatica":
            imprimir(data[e])
            
def opcion_cuatro(data:list):
    edades = []
    for i in range(len(data)):
        edades.append(data[i]["edad"])
    prom_edad = promedio(edades)
    print(f'''
        El promedio de dedades es: {prom_edad:.2f}
        ''')

def opcion_cinco(data:list):
    mayor = [data[0]]
    mayor_prom = promedio(data[0]["notas"])
    
    for e in range(len(data)):
        prom = promedio(data[e]["notas"])
        if prom > mayor_prom:
            mayor_prom = prom
            mayor = [data[e]]
        elif prom == mayor_prom and e != 0:
            mayor.append(data[e])
            
    cabecera_promedio()
    for e in range(len(mayor)):
        print(f'''
        {mayor[e]['nombre'].center(15)} - {mayor[e]['apellido'].center(15)} - {str('%.2f' % mayor_prom).center(8)}
            ''')

def opcion_seis(data:list) -> None:
    alumnos = obtener_grupo(data, "Club de Informatica")
    cabecera_promedio()
    for a in alumnos:
        prom = promedio(a["notas"])
        print(f'''
        {a['nombre'].center(15)} - {a['apellido'].center(15)} - {str('%.2f' % prom).center(8)}
            ''')
        
def opcion_siete(data:list) -> None:
    jovenes = buscar_jovenes(data)
    cabecera_menores()
    for e in jovenes:
        imprimir_menores(e)