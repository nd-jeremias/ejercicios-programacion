import pygame
from random import randint

# Armar cuadrícula
def make_grid(row:int, col:int, cell_size:int, origen_x:int, origen_y:int) -> list:
    
    """ Crea una cuadricula de rectangulos """
    
    grid = []
    for r in range(row):
        fila = []
        for c in range(col):
            y = r * cell_size
            x = c * cell_size
            cell = pygame.Rect(x+origen_x, y+origen_y, cell_size*0.8, cell_size*0.8)
            fila.append(cell)
        grid.append(fila)
    return grid

def make_matrix(base_list:list, col:int, attr:str) -> list:
    
    """ Genera una matriz de numeros aleatoria entre 1 y 3 """
    
    for e in base_list:
        for i in range(col):
            e[attr].append(randint(1,3))
    return base_list

""" def check(matriz:list, posicion:list, attr:str, origin=1, check=0) -> bool:
    
    ''' Verifica que haya 3 numeros iguales, consecutivos de forma vertical.
    origin, indica desde donde va verifica
    hacia "abajo"(aumenta las posicion en filas)
    hacia "arriba"(disminuye las posicion en filas) '''
    
    retorno = False
    for i in range(1,3):
        if origin < 2:
            new_pos = posicion[0] + i
        elif origin >= 2:
            new_pos = posicion[0] - i
        if matriz[posicion[0]][attr][posicion[1]] == matriz[new_pos][attr][posicion[1]]:
            check += 1
    if check == 2:
        retorno = True
    return retorno """
    
def check(matrix:list, attr:str, pos_one:list, pos_two:list) -> int:
    
    retorno = 0
    if matrix[pos_one[0]][attr][pos_one[1]] == matrix[pos_two[0]][attr][pos_two[1]]:
        retorno = 1
        
    return retorno

def check_col(matrix:list, attr:str, pos:list) -> bool:
    validate = 0
    retorno = False
    for i in range(1, 3):
        if pos[0] == 0:
            new_pos = (pos[0] + i, pos[1])
            validate += check(matrix, attr, pos, new_pos)
        elif pos[0] >= 1 and pos[0] <= 2:
            if i == 1:
                new_pos = (pos[0] - i, pos[1])
            else:
                new_pos = (pos[0] + i, pos[1])
            validate += check(matrix, attr, pos, new_pos)
            if validate == 0:
                new_pos = (pos[0] + 2, pos[1])
                validate += check(matrix, attr, pos, new_pos)
        elif pos[0] > 2:
            new_pos = (pos[0] - i, pos[1])
            validate += check(matrix, attr, pos, new_pos)
        if validate == 2:
            retorno = True
        return retorno
    
def draw_grid(surface, grid:list,matrix:list, attr:str, dragee_list:list) -> None:
    
    """ Dibuja las grageas en la grilla establecida """
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if matrix[i][attr][j] == 1: surface.blit(dragee_list[0],grid[i][j])
            if matrix[i][attr][j] == 2: surface.blit(dragee_list[1],grid[i][j])
            if matrix[i][attr][j] == 3: surface.blit(dragee_list[2],grid[i][j])

def draw_keyboard(surface, grid:list, keyboard:list) -> None:
    
    """ Dibuja las teclas en los rect asignados """
    
    for i in range(len(keyboard)):
        for j in range(len(keyboard[i])):
            surface.blit(keyboard[i][j],grid[i][j])

def order_user_list(user_list:list):
    
    for i in range(len(user_list)-1):
        for j in range(i+1, len(user_list)):
            if user_list[j] < user_list[i]:
                aux = user_list[j]
                user_list[j] = user_list[i]
                user_list[i] = aux

def get_userlist_archive(archive_loc, file_list=[]) -> list:
    
    """ Lee el archivo de usuarios/puntos y,
    si existe lo devuelve en forma de lista
    sino devuelve una lista vacia """
    
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

def format_user(user_name:str, points:int, user_list:list) -> str:
    
    user_string = user_name + ";" + str(points) + '\n'
    user_list.append(user_string)
    
    return user_string

def print_points(surface, user_data, user_init_pos) -> None:
    keep_pos = user_init_pos[0]
    new_pos = user_init_pos[1]
    for user in user_data:
        surface.blit(user, user_init_pos)
        new_pos += 65
        user_init_pos = (keep_pos, new_pos) # 70 al 140(pos[1]) <=es una tupla

def user_list_render(user_list:list, font, color, data=[]):
    
    """ Carga los ultimos 6 elementos para mostrar en el leaderboard """
    
    last_elements = user_list[-1:-7:-1]
    for element in reversed(last_elements):
        data.append(font.render(element, 1, color))
    
    return data