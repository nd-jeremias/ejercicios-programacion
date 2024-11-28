from random import randint #BORRAR Y MOVER AL OTRO PAQUETE
import pygame
from constantes import *
# Icono: pygame.display.set_icon(icono) (donde ícono es una superficie de Pygame)
# Modo a pantalla completa: pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
# Ventana redimensionable: pygame.display.set_mode((800, 600), pygame.RESIZABLE)

# Título:
pygame.display.set_caption("Candy-UTN")
# Inicializacion:
pygame.init()

# Seteo de pantalla:
screen = pygame.display.set_mode([SCREEN_W, SCREEN_H])
# Obtengo el fondo
fondo = pygame.image.load(IMG_LOC)
# Escalo la imagen recibida
fondo = pygame.transform.scale(fondo,(SCREEN_W, SCREEN_H))
# Obtengo las grageas y las escalo:
dragee_red = pygame.image.load("./candyutn/dragee_red.png")
dragee_red = pygame.transform.scale(dragee_red,(TAM_CELDA,TAM_CELDA))
dragee_blue = pygame.image.load("./candyutn/dragee_blue.png")
dragee_blue = pygame.transform.scale(dragee_blue,(TAM_CELDA,TAM_CELDA))
dragee_green = pygame.image.load("./candyutn/dragee_green.png")
dragee_green = pygame.transform.scale(dragee_green,(TAM_CELDA,TAM_CELDA))
# Seteo juego corriendo
running = True

########Funciones

# Armar cuadrícula
def make_grid():
    grid = []
    for r in range(ROW):
        fila = []
        for c in range(COL):
            y = r * TAM_CELDA
            x = c * TAM_CELDA
            cell = pygame.Rect(x+ORIGEN_X, y+ORIGEN_Y, TAM_CELDA, TAM_CELDA)
            fila.append(cell)
        grid.append(fila)
    return grid

# Armar matriz aleatoria
def make_matrix():
    matrix = []
    for r in range(ROW):
        row = []
        for c in range(COL):
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

def draw_grid(grid:list,matrix:list):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(screen, COLOR_LINEA, grid[i][j], 1)
            if matrix[i][j] == 1: screen.blit(dragee_red,grid[i][j])
            if matrix[i][j] == 2: screen.blit(dragee_blue,grid[i][j])
            if matrix[i][j] == 3: screen.blit(dragee_green,grid[i][j])

#####Variables

grid_list = make_grid()
validate = False
points = 0

# matrix_flag se utiliza para generar la matriz aleatoria, paralela a la grilla. Cuando se hace click en una gragea se vuelve a generar una nueva
matrix_flag = True

while running:
     
    # Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        
        # Evento que cierra el programa
        if event.type == pygame.QUIT:
            running = False
        
        # Obtengo la posicion del mouse y verifico que colisione con la dragee
        if event.type == pygame.MOUSEBUTTONDOWN :
            pos = event.pos
            for i in range(len(grid_list)):
                for j in range(len(grid_list[i])):
                    if grid_list[i][j].collidepoint(pos[0], pos[1]):
                        #ACA EJECUTAR VERIFICACION
                        
                        if i < 2:
                            validate = (check(matrix,[i,j]))
                        elif i >= 2:
                            validate = (check(matrix,[i,j], -1))
                        
                        if validate:
                            print("SE GANO 10 PUNTOS")
                            points += 10
                            validate = False
                        else:
                            print("VUELVA A INTENTARLO")
        
                        matrix_flag = True
                        #print(f"fila:  {i} columna: {j} Objeto: ")#BORRAR
                        #print(f"{cell}")#BORRAR

        
    if matrix_flag:
        matrix = make_matrix()
        matrix_flag = False

    # Se pinta el fondo de la ventana:
    screen.fill((255, 60, 255))
    # Se carga la imagen de fondo:
    screen.blit(fondo, (0,0))

    # Dibujar grilla
    draw_grid(grid_list, matrix)
    
    # Actualiza la pantalla
    pygame.display.flip()
    
pygame.quit() # Fin