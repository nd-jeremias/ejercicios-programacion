""" def ordenar(lista_uno:list):
    
    ''' Ordenamiento de lista metodo: burbuja '''
    
    for i in range(len(lista_uno)-1):
        for j in range(i+1, len(lista_uno)):
            if lista_uno[j] > lista_uno[i]:
                aux = lista_uno[j]
                lista_uno[j] = lista_uno[i]
                lista_uno[i] = aux
                
    return lista_uno """

def swaper(lista_uno:list, i:int, j:int):
    aux = lista_uno[j]
    lista_uno[j] = lista_uno[i]
    lista_uno[i] = aux


#1
""" Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

def ordenar_datos(lista_uno:list, lista_dos:list):

    for i in range(len(lista_uno)-1):
        for j in range(i+1, len(lista_uno)):
            if lista_uno[j] < lista_uno[i]:
                swaper(lista_uno,i,j)
                swaper(lista_dos,i,j)

ordenar_datos(Nombres, Edades)
print("Nombres:                 |   Edades:    ")
print("-------------------------------------")
for i in range(len(Nombres)):
    print(f"{Nombres[i]:<{25}}|    {Edades[i]:<{5}}")  """

#2
""" Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

def ordenar_datos(lista_uno:list, lista_dos:list):
    
    for i in range(len(lista_uno)-1):
        for j in range(i+1, len(lista_uno)):
            if lista_uno[j] < lista_uno[i]:
                swaper(lista_uno,i,j)
                swaper(lista_dos,i,j)
            if lista_uno[j] == lista_uno[i]:
                if lista_dos[j] > lista_dos[i]:
                    swaper(lista_uno,i,j)
                    swaper(lista_dos,i,j)
    
ordenar_datos(Nombres, Puntos)
print("Materia:                 |   Puntos:    ")
print("-------------------------------------")
for i in range(len(Nombres)):
    print(f"{Nombres[i]:<{25}}|    {Puntos[i]:<{5}}") """


#3
""" Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

def ordenar_datos(lista_uno:list, lista_dos:list, lista_tres:list):
    
    for i in range(len(lista_uno)-1):
        for j in range(i+1, len(lista_uno)):
            if lista_uno[j] < lista_uno[i]:
                swaper(lista_uno,i,j)
                swaper(lista_dos,i,j)
                swaper(lista_tres,i,j)
            if lista_uno[j] == lista_uno[i]:
                if lista_dos[j] < lista_dos[i]:
                    swaper(lista_uno,i,j)
                    swaper(lista_dos,i,j)
                    swaper(lista_tres,i,j)
                if lista_dos[j] == lista_dos[i]:
                    if lista_tres[j] > lista_tres[i]:
                        swaper(lista_uno,i,j)
                        swaper(lista_dos,i,j)
                        swaper(lista_tres,i,j)
    
ordenar_datos(Apellidos, Estudiantes, Nota)
print('''   
        ***************************************************
        |   Apellido        |   Nombre          |   Nota  |
        ***************************************************
        ---------------------------------------------------
        ''')
for i in range(len(Apellidos)):
    print(f'''
        |   {Apellidos[i]:<{15}} |   {Estudiantes[i]:<{15}} |   {Nota[i]:<{5}} |
        ''')
    print("        ---------------------------------------------------") """