from package.colores import GRAY79

# Tamaño de pantalla
SCREEN_H = 720
SCREEN_W = 1280

# Ubicaciones
BACKGROUDN_LOC = "./candyutn/img/background.jpg"
DRAGEE_BLUE_LOC = "./candyutn/img/dragee_blue.png"
DRAGEE_GREEN_LOC = "./candyutn/img/dragee_green.png"
DRAGEE_RED_LOC = "./candyutn/img/dragee_red.png"
GET_RESULTS_LOC = "./candyutn/img/get_results_btn.png"
SUBMIT_BTN_LOC = "./candyutn/img/submit_btn.png"
RESTART_BTN_LOC = "./candyutn/img/restart_btn.png"
FONT_LOC = "./candyutn/font/candy_crush.ttf"

# Celdas
COL = 7
ROW = 4
CELL_SIZE = 100

# Cartel de puntos
LEADERBOARD_SIZE = (375, 600)
LEADERBOARD_POS = (450, 30)

# Botones
BUTTON_SIZE = (153, 47)
BUTTON_POS = (563, 630)

COLOR_LINEA = GRAY79 # BORRAR SI NO SE USA
COLOR_HOVER = (150, 230, 255)

ORIGEN_X = (SCREEN_W - (CELL_SIZE * COL)) / 2
ORIGEN_Y = (SCREEN_H - (CELL_SIZE * ROW)) / 2

K_COL = 10
K_ROW = 3
ORIGEN_KX = (SCREEN_W - (CELL_SIZE * K_COL)) / 2
ORIGEN_KY = (SCREEN_H - (CELL_SIZE * K_ROW)) / 2

LATIN_KEYBOARD = [
        ["Q","W","E","R","T","Y","U","I","O","P"],
        ["A","S","D","F","G","H","J","K","L","Ñ"],
        ["-","Z","X","C","V","B","N","M","ENTER", "-"]]

