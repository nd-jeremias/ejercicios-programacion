""" def ordenar(lista_uno:list):
    
    ''' Ordenamiento de lista metodo: burbuja '''
    
    for i in range(len(lista_uno)):
        for j in range(len(lista_uno)-1):
            if lista_uno[j] > lista_uno[i]:
                aux = lista_uno[j]
                lista_uno[j] = lista_uno[i]
                lista_uno[i] = aux
                
    return lista_uno """

#1
Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

def ordenar_datos(lista_uno:list, lista_dos:list):
    
    for i in range(len(lista_uno)):
        for j in range(len(lista_uno)-1):
            if lista_uno[j] > lista_uno[i]:
                aux = lista_uno[j]
                lista_uno[j] = lista_uno[i]
                lista_uno[i] = aux
                aux = lista_dos[j]
                lista_dos[j] = lista_dos[i]
                lista_dos[i] = aux
    print(lista_uno,"\n", lista_dos)
    
ordenar_datos(Nombres, Edades)

#2
""" Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

def ordenar_datos(lista_uno:list, lista_dos:list):
    
    for i in range(len(lista_uno)):
        for j in range(len(lista_uno)-1):
            if lista_uno[j] > lista_uno[i]:
                if lista_uno[j][0] == lista_uno[i][0]:
                    if lista_dos[j] < lista_dos[i]:
                        aux = lista_uno[j]
                        lista_uno[j] = lista_uno[i]
                        lista_uno[i] = aux
                        aux = lista_dos[j]
                        lista_dos[j] = lista_dos[i]
                        lista_dos[i] = aux
                else:
                    aux = lista_uno[j]
                    lista_uno[j] = lista_uno[i]
                    lista_uno[i] = aux
                    aux = lista_dos[j]
                    lista_dos[j] = lista_dos[i]
                    lista_dos[i] = aux

    print(lista_uno,"\n", lista_dos)
    
ordenar_datos(Nombres, Puntos) """
