import pygame
from candyutn.package.constants import *
import sys

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
ANCHO, ALTO = 1280, 720
pantalla = pygame.display.set_mode((ANCHO, ALTO))

ABECEDARIO = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z Enter Espacio"    
ABECEDARIO = ABECEDARIO.split(" ")
print(ABECEDARIO)

miFuente = pygame.font.Font(None, 30)
#miTexto = miFuente.render(button_text, 0, (80, 60, 200))

def make_grid() -> list:
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

# Dibujar las grageas
def draw_grid(grid:list,abc:list) -> None:
    cont = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            miTexto = miFuente.render(abc[cont], 0, (80, 60, 200))
            pantalla.blit(miTexto,grid[i][j])
            cont += 1

running = True
grilla = make_grid()
while running:
    
    # Verificador de eventos
    for event in pygame.event.get():

        # Se verifica si el usuario cerro la ventana
        if event.type == pygame.QUIT:
            running = False
            
    pos_mouse = pygame.mouse.get_pos()
    for fila in range(ROW):
        for columna in range(COL):
            rect = grilla[fila][columna]
            if rect.collidepoint(pos_mouse):
                pygame.draw.rect(pantalla, COLOR_HOVER, rect)
            else:
                pygame.draw.rect(pantalla, (0,0,0), rect)
                pygame.draw.rect(pantalla, COLOR_LINEA, rect, 1)
    
    draw_grid(grilla, ABECEDARIO)
    pygame.display.flip()