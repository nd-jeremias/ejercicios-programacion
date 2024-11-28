from stark_archivos_package.funciones import *
from os import system

def menu() -> str:
    system("cls")
    opcion = input("""
    A. Leer archivo JSON.
    B. Ordenar héroes por alguna de las claves numéricas (altura, peso y fuerza) de manera ascendente.
    C. Guardar el listado ordenado en un CSV. Pedir el nombre del archivo al usuario.
    D. Salir
    Ingrese la opcion deseada: """).upper()
    return opcion

def opcion_a() -> list | None:
    ruta = input("Ingrese el nombre(o ruta relativa) del archivo JSON(sin extension): ").lower()
    nombre = input("Ingrese el nombre de la lista que quiere importar: ").lower()
    return leer_json(ruta, nombre)

def opcion_b(lista) -> None:
    lista_claves = ["altura", "peso", "fuerza"]
    clave = input(f"Ingrese la clave por la cual desea ordenar: {lista_claves} ").lower()
    while clave != lista_claves[0] and clave != lista_claves[1] and clave != lista_claves[2]:
        clave = input(f"Ingrese una clave valida: {lista_claves} ").lower()
    ordenar(lista, clave, 1)
    #ARMAR PRINT
    for e in lista:
        print(e)

def opcion_c(lista):
    nombre = input("Ingrese el nombre del archivo a guardar: ").lower()
    generar_csv_gpt_v2(nombre, lista)