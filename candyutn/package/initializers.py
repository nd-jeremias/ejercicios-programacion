from package.constants import *
from package.functions import *
from package.keyboard import keyboard

# Icono: pygame.display.set_icon(icono) (donde ícono es una superficie de Pygame)
# Modo a pantalla completa: pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
# Ventana redimensionable: pygame.display.set_mode((800, 600), pygame.RESIZABLE)

# Título:
pygame.display.set_caption("Candy-UTN")

# Seteo de pantalla:
screen = pygame.display.set_mode([SCREEN_W, SCREEN_H])

# Seteo juego corriendo
running = True

# Fondo
fondo = pygame.image.load(BACKGROUDN_LOC)

# Grageas
dragee_red = pygame.image.load(DRAGEE_RED_LOC)
dragee_blue = pygame.image.load(DRAGEE_BLUE_LOC)
dragee_green = pygame.image.load(DRAGEE_GREEN_LOC)

dragee_list = [dragee_red, dragee_blue, dragee_green]
# Grilla donde se colocan las grageas
dragee_grid = make_grid(ROW,COL,CELL_SIZE,ORIGEN_X,ORIGEN_Y)

# Boton leaderboard
get_results_btn = pygame.image.load(GET_RESULTS_LOC)
rect_get_results_btn = pygame.Rect((563, 630), BUTTON_SIZE)
# Carter leaderboard
leaderboard = pygame.image.load(LEADERBOARD_LOC)

# Boton restart
restart_btn = pygame.image.load(RESTART_BTN_LOC)
rect_restart_btn = pygame.Rect((563, 630), BUTTON_SIZE)
#(363, 630) #BORRAR
#(763, 630) #BORRAR

# Teclado
key_row = len(keyboard)
key_col = len(keyboard[0])
keyboard_grid = make_grid(key_row,key_col,CELL_SIZE,ORIGEN_KX,ORIGEN_KY)

# Inicializa la matriz aleatoria.
matrix = make_matrix(ROW, COL)

# Variable que valida si la columna es verdadera
validate = False

# Inicializa puntaje en cero.
points = 0

# Inicializa el user vacio
user_name = ""
user_list = get_userlist_archive(ARCHIVE_LOC)
user_data = []

# Flag que muestra el leaderboard
leaderboard_show = False
# Flag que se utiliza para mostrar grilla
game = False
# Flag el ingreso de usuario al comienzo
user_input = True