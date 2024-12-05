from package.colores import GRAY79

# Tamaño de pantalla
SCREEN_H = 720
SCREEN_W = 1280

# Ubicaciones
BACKGROUDN_LOC = "./img/background.jpg"
DRAGEE_BLUE_LOC = "./img/dragee_blue.png"
DRAGEE_GREEN_LOC = "./img/dragee_green.png"
DRAGEE_RED_LOC = "./img/dragee_red.png"
GET_RESULTS_LOC = "./img/get_results_btn.png"
RESTART_BTN_LOC = "./img/restart_btn.png"
FONT_LOC = "./font/candy_crush.ttf"
LEADERBOARD_LOC = "./img/leaderboard.png"
ARCHIVE_LOC = "./save/score.csv"
SUCCESS_LOC = "./sounds/success.mp3"
MISTAKE_LOC = "./sounds/mistake.mp3"
SIGN_LOC = "./img/sign.png"
USER_SIGN = "./img/cloud.png"

# Fuente
FONT_SIZE = 30
DISPLAY_FONT_SIZE = 50

# Celdas
COL = 7
ROW = 4
CELL_SIZE = 100

ORIGEN_X = (SCREEN_W - (CELL_SIZE * COL)) / 2
ORIGEN_Y = (SCREEN_H - (CELL_SIZE * ROW)) / 2

KEY = "piezas"

# Cartel de puntos
LEADERBOARD_SIZE = (375, 600)
LEADERBOARD_POS = (450, 30)
MAX_LEADERBOARD = 6 # (Tiene que ser uno menos del maximo para dejar lugar al que ingresa)
ADD_POINTS = 10
SIGN_SIZE = (300, 300)
SIGN_POS = (30, 30)
DISPLAY_POINTS_POS = (150,200)

# Botones
BUTTON_SIZE = (154, 48)
BUTTON_POS = (562, 630)
RESTART_BTN_POS = (562, 630)
START_BTN_POS = (786, 336)
GET_RESULTS_POS = (340, 336)

# Usuario
USER_NAME_SIZE = 10
USER_NAME_POS = (520,80)
USER_INIT_POS = (520,144)
USER_SIGN_POS = (240, 10)
USER_SIGN_SIZE = (800, 200)

# Teclado
K_COL = 10
K_ROW = 3
ORIGEN_KX = (SCREEN_W - (CELL_SIZE * K_COL)) / 2
ORIGEN_KY = (SCREEN_H - (CELL_SIZE * K_ROW)) / 2
LATIN_KEYBOARD = [
        ["Q","W","E","R","T","Y","U","I","O","P"],
        ["A","S","D","F","G","H","J","K","L","Ñ"],
        ["-","Z","X","C","V","B","N","M","ENTER", "DELETE"]]
