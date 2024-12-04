import pygame
from package.constants import *
from package.functions import *
from package.initializers import *
from package.colores import GREEN1, ROYALBLUE4
from os import system
# Inicializacion de pygame:
pygame.init()

# Limpia la pantalla
system("cls")

# Timer
clock = pygame.time.Clock()
# Crea un evento cada 1"
pygame.time.set_timer(pygame.USEREVENT, 1000)
# Fuente
font = pygame.font.Font(FONT_LOC, FONT_SIZE)
display_font = pygame.font.Font(FONT_LOC, DISPLAY_FONT_SIZE)
# Sonidos
success_sfx = pygame.mixer.Sound(SUCCESS_LOC)
mistake_sfx = pygame.mixer.Sound(MISTAKE_LOC)

# Escalar imagenes:
fondo = pygame.transform.scale(fondo,(SCREEN_W, SCREEN_H))
dragee_red = pygame.transform.scale(dragee_red,(CELL_SIZE,CELL_SIZE))
dragee_blue = pygame.transform.scale(dragee_blue,(CELL_SIZE,CELL_SIZE))
dragee_green = pygame.transform.scale(dragee_green,(CELL_SIZE,CELL_SIZE))
get_results_btn = pygame.transform.scale(get_results_btn,BUTTON_SIZE)
leaderboard = pygame.transform.scale(leaderboard,LEADERBOARD_SIZE)
sign = pygame.transform.scale(sign, SIGN_SIZE)
user_sign = pygame.transform.scale(user_sign, USER_SIGN_SIZE)

while running:

    # Verificador de eventos
    for event in pygame.event.get():
        
        # Se verifica si el usuario cerro la ventana
        if event.type == pygame.QUIT:
            running = False
                    
        if screen_flag == "leaderboard":
        # Se verifica si fue pulsado el boton restart
            if event.type == pygame.MOUSEBUTTONDOWN:
                #pos = event.pos
                if rect_restart_btn.collidepoint(event.pos):
                    user_name = "" # BORRAR, PASAR POR PARAMETRO AL ARMAR FUNCIONES // Al reiniciar blanquea
                    points = 0
                    countdown = 10
                    # Delay para que no se presionen varios botones en el click
                    pygame.time.delay(200)
                    screen_flag = "main"

        # Ingreso de username
        if screen_flag == "input":
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                for i in range(len(keyboard_grid)):
                        for j in range(len(keyboard_grid[i])):
                            if keyboard_grid[i][j].collidepoint(pos[0], pos[1]):
                                if LATIN_KEYBOARD[i][j] != "-" and LATIN_KEYBOARD[i][j] != "ENTER" and LATIN_KEYBOARD[i][j] != "DELETE":
                                    if len(user_name) <= USER_NAME_SIZE:
                                        user_name += (LATIN_KEYBOARD[i][j])

                # Verifica boton "Del"(Delete)
                if keyboard_grid[2][9].collidepoint(pos[0], pos[1]):
                    if len(user_name) > 0:
                        user_name = user_name[0:-1]

                # Verifica boton "ENTER"
                if keyboard_grid[2][8].collidepoint(pos[0], pos[1]):
                    # Delay para que no se presionen varios botones en el click
                    pygame.time.delay(200)
                    screen_flag = "game"
            
            # Verifica ingreso por teclado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_name = user_name[0:-1]
                if event.key == pygame.K_RETURN:
                    pygame.time.delay(200)
                    screen_flag = "game"
                else:
                    user_name += event.unicode

        # Obtengo la posicion del mouse y verifico que colisione con la gragea
        if screen_flag == "game":
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                for i in range(len(dragee_grid)):
                    for j in range(len(dragee_grid[i])):
                        if dragee_grid[i][j].collidepoint(pos[0], pos[1]):
                            
                            validate = (check_col(matrix,"piezas", [i,j]))

                            if validate:
                                success_sfx.play()
                                print(f"SE GANO {ADD_POINTS} PUNTOS")
                                points += ADD_POINTS
                                validate = False
                            else:
                                countdown -= 1
                                points -= 1
                                mistake_sfx.play()
                                print("VUELVA A INTENTARLO")
                            lista = [{"piezas":[]},{"piezas":[]},{"piezas":[]},{"piezas":[]}]
                            matrix = make_matrix(lista,COL,"piezas")
                
            if event.type == pygame.USEREVENT:
                if countdown > 0:
                    countdown -= 1
                    print(countdown)
                else:
                    # Creamos un string con los datos de usuario y lo renderizamos
                    user_string = format_user(user_name, points, user_list)
                    last_elements = user_list[-1:-7:-1]
                    print(last_elements)
                    order_user_list(last_elements)
                    # Crea lista de impresion en pantalla
                    user_data = user_list_render(last_elements, font, ROYALBLUE4)
                    
                    # Crea el archivo con los datos de usuario
                    update_userlist_archive(ARCHIVE_LOC, user_list)
                    screen_flag = "leadeboard"
                    
                    print("se acabo el tiempo")
                    screen_flag = "leaderboard"
        
        if screen_flag == "main":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_start_btn.collidepoint(event.pos):
                    # Delay para que no se presionen varios botones en el click
                    pygame.time.delay(200)
                    screen_flag = "input"
                if rect_get_results_btn.collidepoint(event.pos):
                    screen_flag = "leaderboard"
                    
    # Se pinta el fondo de la ventana:
    screen.fill(GREEN1)
    # Se carga la imagen de fondo:
    screen.blit(fondo, (0,0))

    if screen_flag == "main":
        
        # Dibujar boton para ver leaderboard
        screen.blit(get_results_btn, rect_get_results_btn)
        # Dibujar boton para volver a empezar
        screen.blit(start_btn, rect_start_btn)
        
    if screen_flag == "input":
        
        # Dibujar teclado
        draw_keyboard(screen, keyboard_grid, keyboard)
        # Dibujar cartel usuario
        screen.blit(user_sign, rect_user_sign)
        # Renderizar nombre usuario
        render_user = display_font.render(user_name, 1, ROYALBLUE4)
        screen.blit(render_user, USER_NAME_POS)
        
    if screen_flag == "game":
        # Dibujar  cartel
        screen.blit(sign, SIGN_POS)
        # Renderizar y mostrar puntaje
        render_points = display_font.render(str(points), 1, ROYALBLUE4)
        screen.blit(render_points, DISPLAY_POINTS_POS)
        # Renderizar y mostrar temporizador
        render_countdown = display_font.render(str(countdown), 1, ROYALBLUE4)
        screen.blit(render_countdown, (200, 60))
        # Dibujar grilla
        draw_grid(screen, dragee_grid, matrix, "piezas", dragee_list)

    if screen_flag == "leaderboard":
        
        screen.blit(fondo, (0,0)) #ESTO PISA LA GRILLA ANTERIOR
        # Dibujar cartel
        screen.blit(leaderboard,LEADERBOARD_POS)
        # Dibujar posiciones
        print_points(screen, user_data, USER_INIT_POS)
        # Dibujar boton para volver a empezar
        screen.blit(restart_btn, rect_restart_btn)
    
    # Actualiza la pantalla
    pygame.display.flip()
    
pygame.quit() # Fin