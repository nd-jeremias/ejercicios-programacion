import pygame
from random import randint

# Armar cuadrícula
def make_grid(row:int, col:int, cell_size:int, origen_x:int, origen_y:int) -> list:
    grid = []
    for r in range(row):
        fila = []
        for c in range(col):
            y = r * cell_size
            x = c * cell_size
            cell = pygame.Rect(x+origen_x, y+origen_y, cell_size, cell_size)
            fila.append(cell)
        grid.append(fila)
    return grid

# Armar matriz aleatoria
def make_matrix(row:int, col:int) -> list:
    matrix = []
    for r in range(row):
        row = []
        for c in range(col):
            row.append(randint(1,3))
        matrix.append(row)
    return matrix

# Verificar posiciones
def check(matriz:list, posicion:list, dir=1, check=0) -> bool:
    
    """ Verifica que haya 3 numeros iguales, consecutivos de forma vertical.
    dir=1 verifica hacia "abajo"(aumenta las posicion en filas)
    dir=-1 verifica hacia "arriba"(disminuye las posicion en filas)"""
    
    retorno = False
    for i in range(1,3):
        if dir == 1:
            new_pos = posicion[0] + i
        elif dir == -1:
            new_pos = posicion[0] - i
        if matriz[posicion[0]][posicion[1]] == matriz[new_pos][posicion[1]]:
            check += 1
    if check == 2:
        retorno = True
    return retorno

# Dibujar las grageas
def draw_grid(screen, grid:list,matrix:list, dragee_list:list) -> None:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if matrix[i][j] == 1: screen.blit(dragee_list[0],grid[i][j])
            if matrix[i][j] == 2: screen.blit(dragee_list[1],grid[i][j])
            if matrix[i][j] == 3: screen.blit(dragee_list[2],grid[i][j])

# Dibujar las teclas
def draw_keyboard(screen, grid:list, keyboard:list) -> None:
    for i in range(len(keyboard)):
        for j in range(len(keyboard[i])):
            screen.blit(keyboard[i][j],grid[i][j])

# Obtener lista de usuarios desde archivo
def get_userlist_archive(archive_loc) -> list:
    
    """ Lee el archivo de usuarios/puntos y,
    si existe lo devuelve en forma de lista
    sino devuelve False """
    
    file_list = []
    try:
        file = open(archive_loc, 'r')
    except FileNotFoundError:
        file_list = []
        print("No existen partidas guardadas")
    except:
        print("Error - No identificado")
    else:
        file_list = file.readlines() # Esto lee el archivo como una lista
        file.close()
    
    return file_list

def update_userlist_archive(archive_loc, file_list) -> None:
    # Creacion del archivo leaderboard
    try:
        file = open(archive_loc, 'w')
    except:
        print("Error al escribir el archivo")
    else:
        file.writelines(file_list)
    finally:
        file.close()