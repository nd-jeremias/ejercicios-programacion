from package_candy.funciones import *
from os import system

# Variables/Constantes
points = 0
seguir = 's'
vidas = 3
COLUMNAS = 7
CREDITO = 1 # Esto es la cantidad de intentos por ronda. Dejar en cero para que sea ilimitado

# Abrir archivo leaderboard si existe, sino avisa y pide confirmacion.
try:
    file = open('./package_candy/leaderboard.csv', 'r')
    # Cerramos el archivo
except FileNotFoundError:
    leaderboard = []
    print("No existen partidas guardadas")
    input("Presione enter para continuar...")
except:
    print("Error - No identificado")
else:
    leaderboard = file.readlines() # Esto lee el archivo como una lista
    file.close()

while seguir == 's':
    lista = [
    {"piezas":[]},
    {"piezas":[]},
    {"piezas":[]},
    {"piezas":[]}]
    
    system("cls") # Limpia la pantalla
    if CREDITO: print(f"Vidas restantes: {vidas}") # Muestra la cant de vidas restantes si no son ilimitadas

    # Generar la matriz aleatoria
    matriz = generar_matriz(lista, COLUMNAS)
    # Imprimir matriz en consola
    print_matriz(matriz, "piezas")
    
    # Obtener posicion seleccionada por el usuario
    pos = get_pos(len(lista),COLUMNAS)

    # Verifica la columna
    if pos[0] < 2:
        validacion = check(matriz, pos, 1)
    elif pos[0] >= 2:
        validacion = check(matriz, pos, -1)

    if validacion == True:
        print("Ha GANADO 10 PUNTOS")
        points += 10
    else:
        vidas -= CREDITO
        if vidas > 0: print("SEGUI PARTICIPANDO")
    
    if vidas <= 0:
        print("No tiene mas vidas!")
        seguir = 'n'
    else:
        seguir = input("Desea seguir jugando: s/n ").lower()
        while seguir != 's' and seguir != 'n':
            seguir = input("Ingrese 's' para continuar y 'n' para salir ").lower()

##### NOTA: Se puede acomodar la lista de manera descendente pero hay q transformar el string en una lista primero para realizar el ordenamiento

# Ingresar datos
user_name = input("Ingrese su usuario: ")
points = str(points)
time = get_time()
to_add = ";".join([user_name, points, time])  + "\n"

# Agrega el usuario al leadearboard
leaderboard.append(to_add)
# Imprime el leaderboard en consola
print_leaderboard(leaderboard)

# Creacion del archivo leaderboard
try:
    file = open('./package_candy/leaderboard.csv', 'w')
except:
    print("Error al escribir el archivo")
else:
    file.writelines(leaderboard)
finally:
    file.close()