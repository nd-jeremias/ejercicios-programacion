def ordenar_asc(lista:list, atributo:str) -> None:
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[j][atributo] > lista[i][atributo]:
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux

def print_one(elemento:dict):
    print(f'''
        |-------------------------------------------------|      
        |    {"Nombre:".ljust(14)} {elemento["nombre"].ljust(30)}|
        |    {"Identidad:".ljust(14)} {elemento["identidad"].ljust(30)}|
        |    {"Altura:".ljust(14)} {str(elemento["altura"]).ljust(30)}|
        |    {"Peso:".ljust(14)} {str(elemento["peso"]).ljust(30)}|
        |    {"Fuerza:".ljust(14)} {str(elemento["fuerza"]).ljust(30)}|
        |    {"Inteligencia:".ljust(14)} {elemento["inteligencia"].ljust(30)}|
        |-------------------------------------------------|''')

def print_all(lista:list) -> None:
    for e in lista:
        print_one(e)
        
def filtrar(lista:list, atributo:str, filtro) -> list:
    
    retorno = []
    for e in lista:
        if e[atributo] == filtro:
            retorno.append(e)
    
    return retorno

def promedio(lista:list, atributo:str, acum=0) -> float:
    
    if len(lista) > 0:
        for e in lista:
            acum += float(e[atributo])
        prom = acum / len(lista)
    return prom

def calcular_imc(peso:float,altura:float) -> float:
    imc = peso / (altura ** 2)
    return imc

def convertir_cm_a_m(distancia:float) -> float:
    retorno = distancia * 100
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