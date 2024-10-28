#1
""" def cant_char(character:str, string:str, cont=0) -> int:
    for char in range(len(string)):
        if character == string[char]:
            cont +=1
    return cont
    
def contar(caracter:str, cadena:str) -> int:
    retorno = cadena.count(caracter)
    return retorno

#print(cant_char("e", "arboleda"))
print(contar("a", "kamaleon")) """

#2
""" def string_range(cadena, i, j) -> str:
    if len(cadena) < j:
        retorno = "El indice es mas grande que la cadena"
    else:
        i -= 1
        x = slice(i,j)
        retorno = cadena[x]
    return retorno

print(string_range("arboleda natural", 4,11)) #4-o #11-a  """

#3
""" def char_at(cadena:str, numero:int) -> str:
    
    if numero <= len(cadena):
        char = cadena[numero]
    else:
        char = "Fuera de rango!"
    return char

print(char_at("superheroe", 4)) # Se espera 'r' """

#####################################################################
#                                                                   #
#                   Introduccion a cadenas 2#                       #
#                                                                   #
#####################################################################

#1
""" def cant_vocales(cadena:str, vocales = ['a','e','i','o','u']) -> list:
    
    retorno = [[],[]]
    
    for c in vocales:
        retorno[0].append(c)
        retorno[1].append(cadena.count(c))
    
    return retorno

matriz = cant_vocales("murcielaguito")

for i in range(len(matriz[0])):
    print(f"'{matriz[0][i]}' -  {matriz[1][i]}") """

#2
""" def buscar_indice(cadena:str, caracter:str) -> int:
    
    retorno = -1
    
    for c in range(len(cadena)):
        if cadena[c] == caracter:
            retorno = c
            break
    
    return retorno

print(buscar_indice("jamaica",  "m")) """

#4
""" def eliminar_repetidos(cadena:str) -> str:
    
    retorno = cadena[0]
    
    for i in range(len(cadena)-1):
        for j in range(i+1,len(cadena)):
            if cadena[i] != cadena[j] and retorno.count(cadena[j]) == 0:
                retorno += cadena[j]
            
    return retorno

print(eliminar_repetidos("jamaica")) """