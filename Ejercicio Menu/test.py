from Paquete import listas_personas
from Paquete.opciones import *
from os import system

system("cls")

def opcion_siete(listado) -> None:
    paises = listado.country
    posiciones = filtrar_pais(paises, "Brazil")
    print(posiciones)
    posiciones += filtrar_pais(paises, "Mexico")
    print(posiciones)
            
opcion_siete(listas_personas)