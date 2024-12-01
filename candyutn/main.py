import pygame
from package.constants import *
from package.functions import *
from package.initializers import *
from package.colores import GREEN1, WHITESMOKE
from os import system

system("cls") # Limpia la pantalla

# Inicializacion de pygame:
pygame.init()

# Escalar imagenes:
fondo = pygame.transform.scale(fondo,(SCREEN_W, SCREEN_H))
dragee_red = pygame.transform.scale(dragee_red,(CELL_SIZE,CELL_SIZE))
dragee_blue = pygame.transform.scale(dragee_blue,(CELL_SIZE,CELL_SIZE))
dragee_green = pygame.transform.scale(dragee_green,(CELL_SIZE,CELL_SIZE))
get_results_btn = pygame.transform.scale(get_results_btn,BUTTON_SIZE)

leaderboard = pygame.image.load("./candyutn/img/leaderboard.png")
leaderboard = pygame.transform.scale(leaderboard,LEADERBOARD_SIZE)

# Fuente
# font = pygame.font.Font(FONT_LOC, 30)
# text = font.render(user, 1, WHITESMOKE)

while running:

    # Verificador de eventos
    for event in pygame.event.get():

        # Se verifica si el usuario cerro la ventana
        if event.type == pygame.QUIT:
            running = False
        
        # Se verifica si fue pulsado el boton restart
        if leaderboard_show:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_restart_btn.collidepoint(event.pos):
                    print("RESTART")
                    leaderboard_show = False
                    user_input = True
        
        # Ingreso de username
        if user_input: # Se verifica si ya se ingreso el usuario
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                for i in range(len(keyboard_grid)):
                        for j in range(len(keyboard_grid[i])):
                            if keyboard_grid[i][j].collidepoint(pos[0], pos[1]):
                                if LATIN_KEYBOARD[i][j] != "-":
                                    user += (LATIN_KEYBOARD[i][j])
                                print(user)#BORRAR
            
            # Verifica boton submit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_submit_btn.collidepoint(event.pos):
                    print("SUBMIT")
                    user_input = False
                    game = True
                        
        #Obtengo la posicion del mouse y verifico que colisione con la gragea
        if game:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                for i in range(len(dragee_grid)):
                    for j in range(len(dragee_grid[i])):
                        if dragee_grid[i][j].collidepoint(pos[0], pos[1]):

                            if i < 2:
                                validate = (check(matrix,[i,j]))
                            elif i >= 2:
                                validate = (check(matrix,[i,j], -1))

                            if validate:
                                print("SE GANO 10 PUNTOS")
                                points += 10
                                validate = False
                                #miTexto = miFuente.render(str(points), 0, (80, 60, 200))
                            else:
                                print("VUELVA A INTENTARLO")
                            matrix = make_matrix(ROW,COL)
#VERIFICAR POR QUE ACCIONAN LOS DOS BOTONES A LA VEZ
asde
            # Se verifica si fue pulsado el boton leaderboard
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_get_results_btn.collidepoint(event.pos):
                    print("LEADERBOARD")
                    leaderboard_show = True
                    game = False
                    

    # Se pinta el fondo de la ventana:
    screen.fill(GREEN1)
    # Se carga la imagen de fondo:
    screen.blit(fondo, (0,0))
    
    if user_input:
        
        screen.blit(submit_btn, rect_submit_btn)
        # Dibujar teclado
        draw_keyboard(screen,keyboard_grid,keyboard)
        
    if game:    
        
        # Dibujar grilla
        draw_grid(screen, dragee_grid, matrix, dragee_list)
        # Dibujar boton para ver leaderboard
        screen.blit(get_results_btn, rect_get_results_btn)
        
    if leaderboard_show:
        
        screen.blit(fondo, (0,0)) #ESTO PISA LA GRILLA ANTERIOR
        screen.blit(leaderboard,LEADERBOARD_POS)
        # Dibujar boton para volver a empezar
        screen.blit(restart_btn, rect_restart_btn)
    
    # Actualiza la pantalla
    pygame.display.flip()
    
pygame.quit() # Fin