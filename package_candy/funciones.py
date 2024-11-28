from random import randint
from colorama import Fore

def generar_matriz(lista:list, cant_col) -> list:
    
    """ Genera una matriz de numeros aleatoria entre 1 y 3 """
    
    for e in lista:
        for i in range(cant_col):
            e["piezas"].append(randint(1,3))
    return lista

def print_matriz(matriz:list, atributo:str) -> None:
    
    """ Imprime la matriz recibida en consola """
    
    print(Fore.BLUE+"    |1||2||3||4||5||6||7|")
    for i in range(len(matriz)):
        print(Fore.BLUE+f"|{i+1}|",end="")
        print(Fore.WHITE,matriz[i][atributo])
        
        
def get_col(max_col:int) -> int:
    
    """ Obtiene la columna seleccionada por usuario.
    Recibe el tamaño maximo de las columnas a validar
    Una vez validada la devuelve por retorno """
    
    input_flag = False
    while not input_flag:
        col_select = (input(f"Seleccione columna: (1-{max_col}) "))
        if col_select.isnumeric():
            col_select = int(col_select)
            if col_select >= 1 and col_select <= max_col:
                input_flag = True
            else:
                print(f"Debe ingresar un nuermo dentro del rango: (1-{max_col}) ")
        else:
            print("El ingreso debe ser numerico!")
    return col_select

def get_row(max_row:int) -> int:
    
    """ Obtiene la fila seleccionada por usuario.
    Recibe el tamaño maximo de filas a validar
    Una vez validada la devuelve por retorno """
    
    input_flag = False
    while not input_flag:
        row_select = (input(f"Seleccione fila: (1-{max_row}) "))
        if row_select.isnumeric():
            row_select = int(row_select)
            if row_select >= 1 and row_select <= max_row:
                input_flag = True
            else:
                print(f"Debe ingresar un nuermo dentro del rango: (1-{max_row}) ")
        else:
            print("El ingreso debe ser numerico!")
    return row_select

def get_pos(max_row:int, max_col:int) -> list:
    
    """ Obtiene la columna y la fila que ingresa el usuario
    Devuelve una lista, con el indice seleccionado [fila, columna]
    (Es decir, se resta uno a lo que ingreso el usuario)"""
    
    col = get_col(max_col)-1
    row = get_row(max_row)-1
    return [row, col]

def check(matriz:list, posicion:list, dir=1, check=0) -> bool:
    
    """ Verifica que haya 3 numeros iguales, consecutivos de forma vertical """
    
    retorno = False
    for i in range(1,3):
        if dir == 1:
            new_pos = posicion[0] + i
        elif dir == -1:
            new_pos = posicion[0] - i
        if matriz[posicion[0]]["piezas"][posicion[1]] == matriz[new_pos]["piezas"][posicion[1]]:
            check += 1
    if check == 2:
        retorno = True
    return retorno

def print_header():
    
    """ Imprime cabecera """
    
    print(f'''
        |-------------------------------------------------------------------|
        | {"Posicion:".ljust(10)}| {"Nombre:".ljust(20)}| {"Apellido:".ljust(20)}| {"Puntos:".ljust(10)}|
        |-------------------------------------------------------------------|
    ''')