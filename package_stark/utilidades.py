def ordenar_asc(lista:list, atributo:str) -> None:
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[j][atributo] > lista[i][atributo]:
                aux = lista[j]
                lista[j] = lista[i]
                lista[i] = aux

def print_one(elemento:dict):
    print(f'''
        |-----------------------------------------------|      
        |    {"Nombre:".ljust(14)} {elemento["nombre"].ljust(28)}|
        |    {"Identidad:".ljust(14)} {elemento["identidad"].ljust(28)}|
        |    {"Altura:".ljust(14)} {str(elemento["altura"]).ljust(28)}|
        |    {"Peso:".ljust(14)} {str(elemento["peso"]).ljust(28)}|
        |    {"Fuerza:".ljust(14)} {str(elemento["fuerza"]).ljust(28)}|
        |    {"Inteligencia:".ljust(14)} {elemento["inteligencia"].ljust(28)}|
        |-----------------------------------------------|''')

def print_all(lista:list) -> None:
    for e in lista:
        print_one(e)
        
def filtrar(lista:list, atributo:str, filtro) -> list:
    
    retorno = []
    for e in lista:
        if e[atributo] == filtro:
            retorno.append(e)
    
    return retorno