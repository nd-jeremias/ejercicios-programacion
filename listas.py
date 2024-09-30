from Package_Input.Validate import validate_number

#1
""" def get_list(lista:list, mensaje:str) -> list:
    for i in range(len(lista)):
        lista[i] = input(mensaje)
    return lista
        
lista_nombres = [" "] * 3

print(get_list(lista_nombres, "Ingrese su nombre: ")) """

#2
""" def get_random_list() -> list:
    control = 's'
    lista = [0] * 10
    while control == 's':
        numero = int(input("Ingrese un numero: "))
        index = int(input("Ingrese la posicion del numero: (1-10) "))
        lista [index-1] = numero
        control = input("Desea seguir guardando numeros? s/n").lower()
        while control != 's' and control != 'n':
            control = input("Ingrese una opcion valida: s/n").lower()

    return lista

print(get_random_list()) """

#3
""" def get_lista_numeros(minimo = 0, maximo = 100) -> list:

    largo_lista = 5
    lista = [0] * largo_lista
    
    for i in range(largo_lista):
        lista[i] = int(input(f"Ingrese un numero entre {minimo} y {maximo}: "))
        while validate_number(lista[i], minimo, maximo) == False:
            print("Numero fuera de rango. Ingreselo nuevamente: ")
            lista [i] = int(input(f"El numero tiene que estar entre {minimo} y {maximo}: "))
            validate_number(lista[i], minimo, maximo)

    return lista

print(get_lista_numeros(5, 10)) """

#4
""" def search_list(lista:list, numero:int) -> bool:
    retorno = False
    for i in range(len(lista)):
        if numero == lista[i]:
            retorno = True
    return retorno """

#5
def search_age(nombres:list, edades:list, limite) -> list:
    
    retorno = []
    for i in range(len(edades)):
        if edades[i] <= limite:
            #print(f"{nombres[i]} tiene {edades[i]}. Es menor de {limite} años")
            retorno.append([nombres[i],edades[i]])
        #print("Vuelta: ", i, "Retorno: ", retorno)
    return retorno

nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [32, 45, 34, 22, 46, 23, 45, 67, 37, 68, 25, 55, 45, 27, 43]

lista_filtrada = search_age(nombres, edades, 24)

for i in range(len(lista_filtrada)):
    for j in range(len(lista_filtrada[i])):
        print(lista_filtrada[i][j])