from Paquete.Validate import *
from Paquete.utilidades import *
from os import system

def menu() -> int:
    system("cls")
    print("Seleccione una opcion: ")
    opcion = int(input(""" 
         01 - Importar listas 
         02 - Listar los datos de los usuarios de México 
         03 - Listar los nombres, mails y teléfonos de los usuarios de Brasil 
         04 - Listar los datos del/los usuario/s más joven/es 
         05 - Obtener un promedio de edad de los usuarios
         06 - De los usuarios de Brasil, listar los datos del usuario de mayor edad 
         07 - Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 
         08 - Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años
         09 - Listar los datos de los usuarios de México ordenados por nombre 
         10 - Listar los datos del/los usuario/s más joven/es ordenados por edad de manera ascendente
                (Si la edad se repite, ordenar por nombre de manera ascendente) 
         11 - Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
            (ordenado por nombre y edad de manera descendente)
          0 - Salir 
          """))
    if validate_range(opcion, 0, 11):
        retorno = opcion
    else:
        retorno = menu()
    return retorno

def opcion_dos(listado) -> None:
    
    """ Opcion 2:
        La funcion fitra los paises con la funcion filtrar_pais() y luego imprime los resultados """
    
    paises = listado.country
    posiciones = filtrar_pais(paises, "Mexico")
    for i in range (len(posiciones)):
        print_all(listado, posiciones[i])

def opcion_tres(listado) -> None:
    paises = listado.country
    posiciones = filtrar_pais(paises, "Brazil")
    for i in range (len(posiciones)):
        print_partial(listado, posiciones[i])

def opcion_cuatro(listado) -> None:
    
    edades = listado.ages
    posiciones = filtrar_edad_mayor(edades)
    for p in posiciones:
        print_all(listado, p)

def opcion_cinco(listado) -> None:
    edades = listado.ages
    print(f'''
        *****************************************************

           El promedio de edades de los usuarios es: {calc_promedio(edades)} 

        *****************************************************
        ''')
    
def opcion_seis(listado) -> None:
    edades = []
    paises = listado.country
    posiciones = filtrar_pais(paises, "Brazil")
    for p in posiciones:
        edades.append(listado.ages[p])
    pos_mayores = filtrar_edad_mayor(edades)
    for p in pos_mayores:
        print_all(listado, posiciones[p])

def opcion_siete(listado) -> None:
    paises = listado.country
    posiciones = filtrar_pais(paises, "Brazil")
    posiciones += filtrar_pais(paises, "Mexico")
    for i in range(len(posiciones)):
        if listado.postalZip[posiciones[i]] > 8000:
            print_all(listado, posiciones[i])

def opcion_ocho(listado) -> None:
    paises = listado.country
    edades = listado.ages
    posiciones = filtrar_pais(paises, "Italy")
    for i in range(len(posiciones)):
        if edades[posiciones[i]] > 40:
            print_partial(listado, posiciones[i])

def opcion_nueve(listado) -> None:
    
    paises = listado.country
    nombres = listado.names
    posiciones = filtrar_pais(paises, "Mexico")
    ordenar_asc(posiciones, nombres)
    for posicion in posiciones:
        print_all(listado, posicion)

def opcion_diez(listado) -> None:
    menores = filtrar_edad_menor(listado.ages)
    ordenar_asc(menores, listado.names)
    for p in menores:
        print_all(listado, p)

def opcion_once(listado) -> None:
    paises = listado.country
    posiciones = filtrar_pais(paises, "Brazil")
    posiciones += filtrar_pais(paises, "Mexico")
    ordenar_descendente(listado.ages, posiciones)
    ordenar_descendente(listado.names, posiciones)
    for p in posiciones:
        print_all(listado, p)