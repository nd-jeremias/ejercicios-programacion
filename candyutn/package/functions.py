import pygame
from random import randint

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

def check_extr_col(matriz:list, attr:str, pos:list, order=1) -> bool:
    
    ''' Verifica que haya 3 numeros iguales, consecutivos de forma vertical.
    order, indica hacia donde va verifica
    1 hacia "abajo"(aumenta las posicion en filas)
    -1 hacia "arriba"(disminuye las posicion en filas) '''
    check = 0
    retorno = False
    for i in range(1,3):
        if order == 1:
            new_pos = pos[0] + i
        elif order == -1:
            new_pos = pos[0] - i
        if matriz[pos[0]][attr][pos[1]] == matriz[new_pos][attr][pos[1]]:
            check += 1
    if check == 2:
        retorno = True
    return retorno
    
def check_mid_col(matrix:list, attr:str, pos:list, order=1) -> bool:
    
    ''' Verifica que haya 3 numeros iguales, consecutivos de forma vertical.
    Si no encuentra hacia abajo/arriba, verifica 1 hacia el otro lado
    order, indica hacia donde va verifica
    1 hacia "abajo"(aumenta las posicion en filas)
    -1 hacia "arriba"(disminuye las posicion en filas) '''
    
    cont = 0
    if order == 1:
        new_pos = pos[0] + 1
    elif order == -1:
        new_pos = pos[0] - 1
    retorno = False
    if matrix[pos[0]][attr][pos[1]] == matrix[new_pos][attr][pos[1]]:
        cont += 1
        if order == 1:
            new_pos += 1
        elif order == -1:
            new_pos -= 1
        if matrix[pos[0]][attr][pos[1]] == matrix[new_pos][attr][pos[1]]:
            cont += 1
        else:
            if order == 1:
                new_pos -= 2
            elif order == -1:
                new_pos += 2
            if matrix[pos[0]][attr][pos[1]] == matrix[new_pos][attr][pos[1]]:
                cont += 1
    if cont == 2:
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
    
    """ Ordena alfabeticamente la lista que recibe """
    
    for i in range(len(user_list)-1):
        for j in range(i+1, len(user_list)):
            if user_list[j] < user_list[i]:
                aux = user_list[j]
                user_list[j] = user_list[i]
                user_list[i] = aux

def get_userlist_archive(archive_loc:str, file_list=[]) -> list:
    
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

def update_userlist_archive(archive_loc:str, file_list:list) -> None:
    
    """ Creacion del archivo leaderboard """
    
    try:
        file = open(archive_loc, 'w')
    except:
        print("Error al escribir el archivo")
    else:
        file.writelines(file_list)
    finally:
        file.close()

def format_user_csv(user_name:str, points:int, user_list:list) -> str:
    
    """ Da formato al str de un usuario y lo une con los puntos
    para imprimir en archivo. Devuelve un string de usuario
    Tambien ingresa la informacion en user_list"""
    
    user_string_csv = user_name + ";" + str(points) + '\n'
    user_list.append(user_string_csv)
    
    return user_string_csv

def print_points(surface:object, user_data:list, user_init_pos:list) -> None:
    
    """ Imprime listado de puntaje en pantalla """
    
    keep_pos = user_init_pos[0]
    new_pos = user_init_pos[1]
    for user in user_data:
        surface.blit(user, user_init_pos)
        new_pos += 65
        user_init_pos = (keep_pos, new_pos)

def user_list_render(user_list:list, font, color) -> list:
    
    """ Carga los elementos para mostrar en el leaderboard 
    y les da formato. """
    
    data=[]
    for element in user_list:
        user = element.split(";")
        user_string_print = user[0].ljust(10) + " - " + user[1].rjust(5)
        data.append(font.render(user_string_print, 1, color))
    
    return data