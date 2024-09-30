from Paquete.utilidades import *

def menu() -> int:
    print("Seleccione una opcion: ")
    opcion = int(input(""" 
          1 - Importar listas 
          2 - Listar los datos de los usuarios de México 
          3 - Listar los nombres, mails y teléfonos de los usuarios de Brasil 
          4 - Listar los datos del/los usuario/s más joven/es 
          5 - Obtener un promedio de edad de los usuarios
          6 - De los usuarios de Brasil, listar los datos del usuario de mayor edad 
          7 - Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 
          8 - Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años 
          0 - Salir 
          """))
    return opcion

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
    maximo = calc_promedio(edades)
    posiciones = filtrar_edad_menor(edades, maximo)
    for i in range (len(posiciones)):
        print_all(listado, posiciones[i])

def opcion_cinco(listado) -> None:
    edades = listado.ages
    print(f'''
        *****************************************************

           El promedio de edades de los usuarios es: {calc_promedio(edades)} 

        *****************************************************
        ''')
    
def opcion_seis(listado) -> None:
    edades = listado.ages
    paises = listado.country
    posiciones = filtrar_pais(paises, "Brazil")
    promedio = calc_promedio(edades)
    for i in range(len(posiciones)):
        if promedio < edades[posiciones[i]]:
            print_all(listado, posiciones[i])

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