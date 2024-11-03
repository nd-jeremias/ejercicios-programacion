def swaper(lista_uno:list, i:int, j:int):
    aux = lista_uno[j]
    lista_uno[j] = lista_uno[i]
    lista_uno[i] = aux
    
def ordenar_asc(data:list) -> None:
    for e in range(len(data)-1):
        for f in range(e+1, len(data)):
            if data[f]["apellido"] < data[e]["apellido"]:
                swaper(data, e, f)
            elif data[f]["apellido"] == data[e]["apellido"] and data[f]["nombre"] < data[e]["nombre"]:
                swaper(data, e, f)

def imprimir_cabecera() -> None:
    print(f'''
        {"Legajo".center(7)} - {"Nombre".center(15)} - {"Apellido".center(15)} - {"Edad".center(6)}
        ''')
   
def imprimir(data:dict) -> None:
    print(f'''
        {str(data["legajo"]).center(7)} - {data["nombre"].center(15)} - {data["apellido"].center(15)} - {str(data["edad"]).center(6)}
        ''')

def cabecera_menores() -> None:
    print(f'''
        {"Legajo".center(7)} - {"Nombre".center(15)} - {"Apellido".center(15)} - {"Programa".center(15)} - {"Nivel".center(15)}
        ''')
    
def imprimir_menores(data:dict) -> None:
    print(f'''
        {str(data["legajo"]).center(7)} - {data["nombre"].center(15)} - {data["apellido"].center(15)} - {data["programa"]["nombre"].center(15)} - {data["programa"]["nivel"].center(15)}
        ''')

def cabecera_promedio() -> None:
    print(f'''
        {"Nombre".center(15)} - {"Apellido".center(15)} - {"Promedio".center(6)}
        ''')

def promedio(data:list, suma=0) -> float | None:
    
    result = None
    if len(data) > 0:
        for i in range(len(data)):
            suma += data[i]
        result = suma / len(data)
    else:
        print("No existe informacion para calcular el promedio")
    
    return result

def obtener_grupo(data:list, grupo:str) -> list:
    lista = []
    for e in range(len(data)):
        if 'grupos' in data[e]:
            for g in range(len(data[e]["grupos"])):
                if data[e]["grupos"][g]["nombre"] == grupo:
                    lista.append(data[e])
    return lista

def buscar_jovenes(data:list) -> list:
    menores = [data[0]]
    edad_menor = data[0]["edad"]
    for i in range(len(data)):
        if data[i]["edad"] < edad_menor:
            menores = [data[i]]
            edad_menor = data[i]["edad"]
        elif data[i]["edad"] == edad_menor and i > 0:
            menores.append(data[i])
    return(menores)
