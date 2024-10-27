from Package_Input.Input import *

#1
""" def get_list(lista:list) -> list:
    
    ''' Funcion que recibe una lista vacia y la completa con nombres '''
    
    for i in range(len(lista)):
        lista[i] = get_string("Ingrese un nombre de maximo 15 caracteres: ", "Se ha excedido en la cantidad de caracteres. Vuelva a intentarlo", 15, 3)
        
    return lista

cant = 10
lista_nombres = [" "] * cant

print(get_list(lista_nombres)) """

#2
""" def get_random_list() -> list:
    
    ''' Se inicializa una lista de 10 elementos en 0. 
    Luego se pide al usuario que ingrese los numeros que desea guardar y en que ubicacion. '''
    
    control = 's'
    lista = [0] * 10
    while control == 's':
        numero = int(input("Ingrese un numero: "))
        index = get_int("Ingrese la posicion del numero: (1-10) ", "Error- Fuera de rango", 1, 10, 3)
        if type(index) == int:
            lista [index-1] = numero
        else:
            print("Se excedio en el limite de intentos. Vuelva a comenzar.")
            lista = []
            break
        control = input("Desea seguir guardando numeros? s/n").lower()
        while control != 's' and control != 'n':
            control = input("Ingrese una opcion valida: s/n").lower()

    return lista

print(get_random_list()) """

#3
""" def get_lista_numeros() -> list:

    ''' Se piden 10 numeros dentro de un rango y se guardan en una lista.
    El rango se valida dentro de la funcion get_int()'''
    
    largo_lista = 10
    lista = [0] * largo_lista
    
    for i in range(len(lista)):
        
        lista[i] = get_int("Ingrese un numero entre 0 y 100", "Error- el numero esta fuera de rango. Vuelva a intentarlo.", 0, 100, 3)
        if type(lista[i]) != int:
            lista = []
            print("Se excedio en el limite de intentos. Vuelva a comenzar.")
            break
        
    return lista

print(get_lista_numeros()) """

#4
""" def search_list(lista:list, numero:int) -> bool:

    ''' Se recibe una lista de numeros y un numero especifico por parametros.
    Se busca dicho numero en la lista y se retorna True al encontrarlo. False si no se encuentra.'''

    retorno = False
    for i in range(len(lista)):
        if numero == lista[i]:
            retorno = True
    return retorno """

#5
""" def search_age(edades:list) -> list:
    
    ''' Se busca dentro de la lista pasada por paremtro las personas de menor edad '''
    
    menor = edades[0]
    lista = []
    for i in range(len(edades)):
        if edades[i] <= menor:
            menor = edades[i]
    for i in range(len(edades)):
        if edades[i] == menor:
            lista.append(i)
    
    return lista

nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23, 45, 34, 25, 46, 23, 45, 67, 37, 68, 25, 55, 45, 27, 43]

index = search_age(edades)
print("Los mas jovenes son: ")
for i in range(len(index)):
    print(f"        {nombres[index[i]]} con {edades[index[i]]}") """
    
#6
from listas_personas import names

def mostrar_lista(lista:list) -> None:
    for i in range(0, len(lista), 2):
        posicion = str(i+1)
        print(f"{posicion.rjust(2)}: {lista[i].ljust(20)}       -    {i+2}: {lista[i+1].ljust(20)}")
    
nombres = names

mostrar_lista(nombres)