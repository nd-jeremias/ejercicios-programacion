from package_candy.funciones import *
from os import system

points = 0
seguir = 's'
vidas = 3

COLUMNAS = 7

try:
    file = open('./package_candy/leaderboard.csv', 'r')
    #for linea in lista_lineas:
    #   print(lista_lineas) => 
# ['id,first_name,last_name,points\n', '1,Ernest,Reville,97\n', '2,Briano,Blare,45\n', "3,Gigi,O'Gavin,91\n", '4,Gabi,Shickle,75\n', '5,Bram,Cray,54\n', '6,Harcourt,Hultberg,43\n', '7,Ramsay,MacKey,62\n', '8,Dorree,Raywood,68\n', '9,Dorise,Uman,78\n', '10,Maurie,Whitehair,73\n', '23,Nico,Jere,100']
    #   print(linea, end="")
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
    
    #system("cls")
    print(f"Vidas restantes: {vidas}")
    matriz = generar_matriz(lista, COLUMNAS)

    print_matriz(matriz, "piezas")
    pos = get_pos(len(lista),COLUMNAS)
    numero = matriz[pos[0]]["piezas"][pos[1]]

    if pos[0] < 2:
        validacion = check(matriz, pos, 1)
    elif pos[0] >= 2:
        validacion = check(matriz, pos, -1)

    if validacion == True:
        print("Ha GANADO 10 PUNTOS")
        points += 10
    else:
        print("SEGUI PARTICIPANDO")
        vidas -= 1
    
    if vidas == 0:
        print("No tiene mas vidas!")
        seguir = 'n'
    else:
        seguir = input("Desea seguir jugando: s/n ").lower()
        while seguir != 's' and seguir != 'n':
            seguir = input("Ingrese 's' para continuar y 'n' para salir ").lower()

# Ingresar datos
user_name = input("Ingrese su usuario: ")
points = str(points)
to_add = ";".join([user_name, points])

##### NOTA: Se puede acomodar la lista de manera descendente pero hay q transformar el string en una lista primero para realizar el ordenamiento
print(f"Usted ha acumulado: {points} points")#BORRAR

leaderboard.append(to_add)
print(leaderboard)#BORRAR

try:
    file = open('./package_candy/leaderboard.csv', 'w')
except:
    print("Error al escribir el archivo")
else:
    file.writelines(leaderboard)
finally:
    file.close()