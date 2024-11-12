def swap(lista:list, i:int, j:int) -> None:
    
    """ Realiza un swap en la lista recibida """
    
    aux = lista[j]
    lista[j] = lista[i]
    lista[i] = aux

def ordenar(lista:list, atributo:str, orden=1) -> None:
    
    """ Ordena la lista recibida segun el orden definido.
    Si recibe 1 ordena ascendente. Forma predeterminada
    Con -1 se ordena de forma descendente"""
    
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if orden == 1 and lista[j][atributo] < lista[i][atributo]:
                swap(lista, i, j)
            elif orden == -1 and lista[j][atributo] > lista[i][atributo]:
                swap(lista, i, j)

def obtener_min_max(lista:list, atributo:str, opcion=1) -> list:
    
    """ Se obtiene una lista con diccionarios de los personajes
    Si la opcion es 1(por defecto) se devuelven los mayores
    si no (-1) se devuelven los menores.
    La funcion solamente evalua numeros"""
    
    numero = (lista[0][atributo])
    lista_filtrada = [lista[0]]
    if isnumber(numero):
        numero = float(numero)
        for i in range(len(lista)):
            if opcion == 1 and float(lista[i][atributo]) > numero:
                numero = float(lista[i][atributo])
                lista_filtrada = [lista[i]]
            elif opcion == -1 and float(lista[i][atributo]) < numero:
                numero = float(lista[i][atributo])
                lista_filtrada = [lista[i]]
            elif float(lista[i][atributo]) == numero and i > 0:
                lista_filtrada.append(lista[i])
            elif opcion != 1 and opcion != -1:
                print("La opcion de busqueda es incorrecta")
    else:
        print("La lista no posee numeros a evaluar en esa posicion")
   
    return lista_filtrada
def print_header(imc_flag):
    
    """ Imprime cabecera """
    
    print(f'''
        |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|{"-----------|" if imc_flag == True else ""}
        | {"Nombre:".ljust(32)}| {"Identidad:".ljust(32)}| {"Empresa:".ljust(32)}| {"Altura:".ljust(10)}| {"Peso:".ljust(10)}|{"Genero:".center(10)}| {"Ojos:".ljust(25)}| {"Pelo:".ljust(20)}| {"Fuerza:".ljust(10)}| {"Inteligencia:".ljust(20)}| {"IMC".ljust(10) if imc_flag == True else ""}{"|" if imc_flag == True else ""}
        |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|{"-----------|" if imc_flag == True else ""}''',end="")
    
def print_one(elemento:dict):
    
    """ Imprime un superheroe """
    
    print(f'''
        | {elemento["nombre"].ljust(32)}| {elemento["identidad"].ljust(32)}| {elemento["empresa"].ljust(32)}|{str("%.2f" %float(elemento["altura"])).rjust(10)} |{str("%.2f" %float(elemento["peso"])).rjust(10)} |{elemento["genero"].center(10)}| {elemento["color_ojos"].ljust(25)}| {elemento["color_pelo"].ljust(20)}|{elemento["fuerza"].rjust(10)} | {elemento["inteligencia"].ljust(20)}|{elemento["IMC"].rjust(10) if "IMC" in elemento else ""} {"|" if "IMC" in elemento else ""}
        |---------------------------------|---------------------------------|---------------------------------|-----------|-----------|----------|--------------------------|---------------------|-----------|---------------------|{"-----------|" if "IMC" in elemento else ""}''',end="")

def print_all(lista:list, imc_flag) -> None:
    """ Imprime todos los superheroes de la lista """
    print_header(imc_flag)
    for e in lista:
        print_one(e)
        
def filtrar(lista:list, atributo:str, filtro) -> list:
    
    """ Regresa una lista con todos los superheroes que cumplan
    condicion : atributo -> filtro"""
    
    retorno = []
    for e in lista:
        if e[atributo] == filtro:
            retorno.append(e)
    
    return retorno

def promedio(lista:list, atributo:str, acum=0) -> float | None:
    
    """ Saca el promedio de un atributo en la lista recibida"""
    
    if isnumber(lista[0][atributo]):
        if len(lista) > 0:
            for e in lista:
                acum += float(e[atributo])
            prom = acum / len(lista)
    else:
        print("La lista no contiene numeros en ese atributo.")
        prom = None
        
    return prom

def calcular_imc(peso:float,altura:float) -> float:
    
    """ Calcula el IMC segun el peso y altura recibidos """
    
    imc = peso / (altura ** 2)
    return imc

def convertir_cm_a_m(distancia:float) -> float:
    retorno = distancia / 100
    return retorno

################### MODIFICAR USANDO METODOS STRING#############
def obtener_datos(lista:str, atributo:str) -> list:
    datos = []
    for e in lista:
        flag = False
        for d in datos:
            if e[atributo] == d:
                flag = True
        if flag == False:
            datos.append(e[atributo])
    return datos

##############################################################
def isfloat(cadena:str) -> bool:
    """ Recibe una cadena y evalua caracter por caracter
    Si encuentra una letra devuelve False.
    Si encuentra solamente numeros y un solo punto devuelve True """
    retorno = True
    if cadena.count(".") == 1:
        for char in cadena:
            if not char.isdigit() and char != ".":
                retorno = False
    else:
        retorno = False

    return retorno

def isnumber(number:str) -> bool:
    retorno = False
    if isfloat(number): retorno = True 
    if number.isdigit(): retorno = True
    return retorno