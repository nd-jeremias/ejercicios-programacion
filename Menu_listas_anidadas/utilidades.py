from Menu_listas_anidadas.gondola import Gondola
from Package_Input.Input import *
    
max_filas = len(Gondola)
max_columnas = len(Gondola[0])
max_cantidad = 100

def pedir_producto() -> list | None:
    
    """ Pide con una serie de preguntas los datos que se deberan ingresar por el usuario.
        Devuelve una lista del producto """

    producto = None
    nombre = get_string("Que producto va a dar de alta? ", "El nombre no puede ser tan largo. Max 15 car.", 15, 3)
    if nombre != None:
        nombre = nombre.capitalize()
        fila = get_int(f"Ingrese la fila donde va a colocar el producto: min: 1 - max: {max_filas} ", "Error - Ingrese una opcion dentro del rango", 1, max_filas, 3)
        if fila != None:
            columna = get_int(f"Ingrese la columna: min: 1 - max: {max_columnas} ", "Error - Ingrese una opcion dentro del rango", 1, max_columnas, 3)
            if columna != None:
                cantidad = get_int(f"Que cantidad va a ingresar? maximo {max_cantidad}u. por producto ", "Error - Ingrese una opcion dentro del rango", 0, max_cantidad, 3)
                if cantidad != None:
                    producto = [nombre, cantidad, [fila,columna]]
                else:
                    print("Error al ingresar la cantidad. Se excedio el maximo de intentos permitidos")
                    input("Presione enter para volver al menu")
            else:
                print("Error al ingresar la columna. Se excedio el maximo de intentos permitidos")
                input("Presione enter para volver al menu")
        else:
            print("Error al ingresar la fila. Se excedio el maximo de intentos permitidos")
            input("Presione enter para volver al menu")
    else:
        print("Error al ingresar el nombre. Se excedio el maximo de intentos permitidos")
        input("Presione enter para volver al menu")

    return producto

def alta_producto(matriz:list, producto:list) -> None:
    
    """ Recibe el producto a dar de alta en formato lista
    Utiliza la informacion recibida para guardarlo en la matriz de datos"""
    
    # Se saca 1 a la fila y la columna porque el usuario ve la matriz desde el 1
    fila = producto[2][0] - 1 
    columna = producto[2][1] - 1
    matriz[fila][columna] = producto
    
def buscar_producto_nombre(nombre:str, matriz:list) -> list | None :
    
    """ Busca en la matriz de datos, el producto que coincida con el nombre pasado por parametro.
    Devuelve una lista con la ubicacion del producto en la matriz o None si no la encuentra.
    Donde la posicion [0] es la fila, y la posicion [1] la columna"""
    
    retorno = None
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]:
                if matriz[i][j][0] == nombre:
                    retorno = [i,j]
    
    return retorno

def baja_nombre(matriz:list) -> None:
    
    """ Pide el nombre del producto para darle la baja.
    Lo busca llamando a la funcion buscar_producto_nombre()
    Si lo encuentra lo elimina, sino avisa y termina la funcion."""
    
    nombre = get_string("Que producto va a dar de baja? ", "El nombre no puede ser tan largo. Max 15 car.", 15, 3).capitalize()
    if nombre != None:
        index = buscar_producto_nombre(nombre, matriz)
        if index:
            imprimir_producto(matriz[index[0]][index[1]])
            submit = input("Va a eliminar el siguiente producto. Esta seguro si / no ").lower()
            if submit == "si":
                eliminar_producto(matriz, matriz[index[0]][index[1]])
                print('''
                     **************************
                    |                          |
                    |    Producto eliminado    |
                    |                          |
                     **************************
                    ''')
                time.sleep(1.5)
        else:
            print('''
                     **********************************
                    |                                  |
                    |    No se encontro el producto    |
                    |                                  |
                     **********************************
                    ''')
            time.sleep(1.5)
    else:
        input("Error al ingresar el nombre. Se excedio el maximo de intentos permitidos")

def baja_ubicacion(matriz:list) -> None:
    
    """ Pide la ubicacion del producto en la gondola para darle la baja.
    Si lo encuentra lo elimina, sino avisa y termina la funcion."""
    
    fila = get_int(f"Ingrese la fila donde va a colocar el producto: min: 1 - max: {max_filas} ", "Error - Ingrese una opcion dentro del rango", 1, max_filas, 3)
    if fila != None:
        columna = get_int(f"Ingrese la columna: min: 1 - max: {max_columnas} ", "Error - Ingrese una opcion dentro del rango", 1, max_columnas, 3)
        if columna != None:
            if matriz[fila-1][columna-1]:
                eliminar_producto(matriz[fila-1][columna-1])
            else:
                print('''
                 ******************************************
                |                                          |
                |    No existe un producto en ese lugar    |
                |                                          |
                 ******************************************
                ''')
                time.sleep(1.5)
        else:
            input("Error al ingresar la columna. Se excedio el maximo de intentos permitidos")
    else:
        input("Error al ingresar la fila. Se excedio el maximo de intentos permitidos")

def mod_cant_nombre(matriz:list) -> None:
    
    """ Pide el nombre del producto, lo busca en la matriz.
    Si lo encuentra, pide la cantidad que se va a modificar, sino muestra un cartel de error."""
    
    nombre = get_string("Como se llama el producto? ", "El nombre no puede ser tan largo. Max 15 car.", 15, 3).capitalize()
    if nombre != None:
        index = buscar_producto_nombre(nombre, matriz)
        if index != None:
            imprimir_producto(matriz[index[0]][index[1]])
            cantidad = get_int(f"Ingrese la cantidad nueva: maximo {max_cantidad}u. por producto ", "Error - Ingrese una opcion dentro del rango", 0, max_cantidad, 3)
            if cantidad != None:
                matriz[index[0]][index[1]][1] = cantidad
                print('''
                         ****************************
                        |                            |
                        |    Cantidad actualizada    |
                        |                            |
                         ****************************
                        ''')
                time.sleep(1.5)
            else:
                input("Error al ingresar la cantidad. Se excedio el maximo de intentos permitidos")
        else:
            print('''
                     **********************************
                    |                                  |
                    |    No se encontro el producto    |
                    |                                  |
                     **********************************
                    ''')
            time.sleep(1.5)
    else:
        input("Error al ingresar el nombre. Se excedio el maximo de intentos permitidos")

def mod_cant_ubi(matriz:list) -> None:
    
    """ Pide la ubicacion del producto a modificar.
    Si se encuentra el producto, pide la cantidad para modificar.
    Sino, muestra un cartel de error"""
    
    fila = get_int(f"Ingrese la fila donde se encuentra el producto: min: 1 - max: {max_filas} ", "Error - Ingrese una opcion dentro del rango", 1, max_filas, 3)
    if fila != None:
        columna = get_int(f"Ingrese la columna: min: 1 - max: {max_columnas} ", "Error - Ingrese una opcion dentro del rango", 1, max_columnas, 3)
        if columna != None:
            fila -= 1
            columna -= 1
            if matriz[fila][columna]:
                imprimir_producto(matriz[fila][columna])
                cantidad = get_int(f"Ingrese la cantidad nueva: maximo {max_cantidad}u. por producto ", "Error - Ingrese una opcion dentro del rango", 0, max_cantidad, 3)
                if cantidad != None:
                    matriz[fila][columna][1] = cantidad
                    print('''
                             ****************************
                            |                            |
                            |    Cantidad actualizada    |
                            |                            |
                             ****************************
                            ''')
                    time.sleep(1.5)
                else:
                    input("Error al ingresar la cantidad. Se excedio el maximo de intentos permitidos")
            else:
                print('''
                         ******************************************
                        |                                          |
                        |    No existe un producto en ese lugar    |
                        |                                          |
                         ******************************************
                        ''')
                time.sleep(1.5)
        else:
            input("Error al ingresar la columna. Se excedio el maximo de intentos permitidos")
    else:
        input("Error al ingresar la fila. Se excedio el maximo de intentos permitidos")

def mod_cantidad(matriz:list) -> None:
    
    """ Muestra las opciones por la cual se va a buscar el producto para modificar """
    
    opcion = get_int(""" 
        Seleccione como buscar el producto:
        
                            1. Nombre
                            2. Ubicacion
                            """,
        "Debe seleccionar una opcion de la lista. ", 1, 2, 3)
    if opcion == 1:
        mod_cant_nombre(matriz)
    if opcion == 2:
        mod_cant_ubi(matriz)
    # else:
    #     input("Se excedio el maximo de intentos permitidos")

def mod_ubi_nombre(matriz:list) -> None:
    
    """ Pide el nombre del producto, lo busca en la matriz.
    Si lo encuentra pide la nueva ubicacion, sino muestra un cartel de error."""
    
    nombre = get_string("Como se llama el producto? ", "El nombre no puede ser tan largo. Max 15 car.", 15, 3).capitalize()
    if nombre != None:
        index = buscar_producto_nombre(nombre, matriz)
        if index != None:
            imprimir_producto(matriz[index[0]][index[1]])
            fila = get_int(f"Ingrese la nueva fila donde va a colocar el producto: min: 1 - max: {max_filas} ", "Error - Ingrese una opcion dentro del rango", 1, max_filas, 3)
            if fila != None:
                columna = get_int(f"Ingrese la nueva columna: min: 1 - max: {max_columnas} ", "Error - Ingrese una opcion dentro del rango", 1, max_columnas, 3)
                if columna != None:
                    if matriz[index[0]][index[1]][2][0] == fila and matriz[index[0]][index[1]][2][1] == columna:
                        input("El objeto quedo en el mismo lugar")
                    else:
                        # Primero se modifica la informacion del producto
                        matriz[index[0]][index[1]][2][0] = fila
                        matriz[index[0]][index[1]][2][1] = columna
                        # Restamos 1 a fila/columna porque el usuario ingresa la posicion +1
                        # Copiamos el producto a la nueva posicion
                        matriz[fila-1][columna-1] = matriz[index[0]][index[1]]
                        # Eliminamos el producto de la posicion anterior
                        # No se puede llamar a la funcion eliminar_producto() porque copia la lista original.
                        matriz[index[0]][index[1]] = []
                        print('''
                                 *****************************
                                |                             |
                                |    Ubicacion actualizada    |
                                |                             |
                                 *****************************
                                ''')
                        time.sleep(1.5)
                else:
                    input("Error al ingresar la columna. Se excedio el maximo de intentos permitidos")
            else:
                input("Error al ingresar la fila. Se excedio el maximo de intentos permitidos")
        else:
            print('''
                     **********************************
                    |                                  |
                    |    No se encontro el producto    |
                    |                                  |
                     **********************************
                    ''')
            time.sleep(1.5)
    else:
        input("Error al ingresar el nombre. Se excedio el maximo de intentos permitidos")

def mod_ubi_ubi(matriz:list) -> None:
    
    """ Pide la ubicacion del producto a modificar.
    Si se encuentra el producto, pide el nuevo lugar en la gondola.
    Sino, muestra un cartel de error"""
    
    index = [0, 0]
    index[0] = get_int(f"Ingrese la fila donde se encuentra el producto: min: 1 - max: {max_filas} ", "Error - Ingrese una opcion dentro del rango", 1, max_filas, 3)
    if index[0] != None:
        index[1] = get_int(f"Ingrese la columna: min: 1 - max: {max_columnas} ", "Error - Ingrese una opcion dentro del rango", 1, max_columnas, 3)
        if index[1] != None:
            index[0] -= 1
            index[1] -= 1
            if matriz[index[0]][index[1]]:
                imprimir_producto(matriz[index[0]][index[1]])
                fila = get_int(f"Ingrese la nueva fila donde va a colocar el producto: min: 1 - max: {max_filas} ", "Error - Ingrese una opcion dentro del rango", 1, max_filas, 3)
                if fila != None:
                    columna = get_int(f"Ingrese la nueva columna: min: 1 - max: {max_columnas} ", "Error - Ingrese una opcion dentro del rango", 1, max_columnas, 3)
                    if columna != None:
                        if matriz[index[0]][index[1]][2][0] == fila and matriz[index[0]][index[1]][2][1] == columna:
                            input("El objeto quedo en el mismo lugar")
                        else:
                            matriz[index[0]][index[1]][2][0] = fila
                            matriz[index[0]][index[1]][2][1] = columna
                            matriz[fila-1][columna-1] = matriz[index[0]][index[1]]
                            matriz[index[0]][index[1]] = []
                            print('''
                                     *****************************
                                    |                             |
                                    |    Ubicacion actualizada    |
                                    |                             |
                                     *****************************
                                    ''')
                            time.sleep(1.5)
                    else:
                        input("Error al ingresar la columna. Se excedio el maximo de intentos permitidos")
                else:
                    input("Error al ingresar la fila. Se excedio el maximo de intentos permitidos")
            else:
                print('''
                         ******************************************
                        |                                          |
                        |    No existe un producto en ese lugar    |
                        |                                          |
                         ******************************************
                        ''')
                time.sleep(1.5)
        else:
            input("Error al ingresar la columna. Se excedio el maximo de intentos permitidos")
    else:
        input("Error al ingresar la fila. Se excedio el maximo de intentos permitidos")

def mod_ubicacion(matriz:list) -> None:
    
    opcion = get_int(""" 
        Seleccione como buscar el producto:
        
                            1. Nombre
                            2. Ubicacion
                            """,
        "Debe seleccionar una opcion de la lista. ", 1, 2, 3)
    if opcion == 1:
        mod_ubi_nombre(matriz)
    if opcion == 2:
        mod_ubi_ubi(matriz)
    # else:
    #     input("Se excedio el maximo de intentos permitidos")

def imprimir_cabecera() -> None:
    print('''   
         **************************************************************
        |                    |                    |                    |
        |      Producto      |      Cantidad      |      Ubicacion     |
        |                    |                    |  Fila  |  Columna  |
        |                    |                    |                    |
         **************************************************************
        ----------------------------------------------------------------''')

def imprimir_listado(matriz) -> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]:
                print(f'''
        |{matriz[i][j][0].center(20)}|{str(matriz[i][j][1]).center(20)}|{str(matriz[i][j][2][0]).center(9)}|{str(matriz[i][j][2][1]).center(10)}|
        ----------------------------------------------------------------''')

def imprimir_producto(producto:list) -> None:
    
    """ Impresion detallada de un producto determinado
        El cual se pasa por parametro en formato lista"""
    matriz = [[producto]]
    imprimir_cabecera()
    print(f'''
        |{matriz[0][0][0].center(20)}|{str(matriz[0][0][1]).center(20)}|{str(matriz[0][0][2][0]).center(9)}|{str(matriz[0][0][2][1]).center(10)}|
        ----------------------------------------------------------------''')
    
def eliminar_producto(matriz:list, producto:list) -> None:
    
    """ Toma el producto que recibe por parametro, y lo blanquea de la matriz recibida """
    
     # Se reta 1 a la fila y la columna porque el usuario ve la matriz desde el 1
    fila = producto[2][0] - 1
    columna = producto[2][1] - 1
    matriz[fila][columna] = []
    
def error_alta() -> None:
    
    """ Impresion de carte de error al no dar de alta un producto """
    
    print('''
             ***********************************************
            |                                               |
            |                    Error -                    |
            |    Primero se debe dar de alta al producto    |
            |                                               |
             ***********************************************
            ''')
    time.sleep(1.5)