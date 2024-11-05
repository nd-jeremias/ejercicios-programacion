from package_stark.utilidades import *
from package_stark.data_stark import data

heroes = data["heroes"]
color_ojos = ["Celestes","Marrones", "Negros","Verdes"]
tipo_inteligencia = ["","average", "good", "high"]

def menu() -> str:
    opcion = input('''
            1. Listar ordenado por Nombre.
            2. Listar Masculinos débiles.
            3. Cantidad por color de ojos.  Determinar cuántos superhéroes tienen cada tipo de color de ojos. 
            4. Listar por color de Pelo.  Listar todos los superhéroes agrupados por color de pelo.
            5. Listar inteligencia.  Listar todos los superhéroes agrupados por tipo de inteligencia.
            6. Listar Promedio.  Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino
            7. Asignar IMC.  Calcular el índice de masa corporal de cada superhéroe y guardarla en un nuevo campo.  Se deberá hacer uso de una función lambda que asignará a cada superhéroe el  IMC calculado. 
            Ingrese una opcion: ''')
    return opcion

def opcion_uno() -> None:

    ordenar_asc(heroes, "nombre")
    print_all(heroes)

def opcion_dos() -> None:
    lista_filtrada = filtrar(heroes, "genero", "M")
    ordenar_asc(lista_filtrada, "fuerza")
    print_one(lista_filtrada[0])
    
def opcion_tres() -> None:
    
    for o in color_ojos:
        cant = 0
        for h in heroes:
            cant = cant + 1 if h["ojos"] == o else cant
        print(f"Hay {cant} superheroes con color de ojos {o}")

def opcion_cinco() -> None:

    for e in tipo_inteligencia:
        lista_filtrada = filtrar(heroes, "inteligencia", e)
        print(f"Inteligencia: {e}")
        print_all(lista_filtrada)