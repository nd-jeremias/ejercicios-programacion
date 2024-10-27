#1
""" def cant_char(character:str, string:str, cont=0) -> int:
    for char in range(len(string)):
        if character == string[char]:
            cont +=1
    return cont


print(cant_char("e", "arboleda")) """

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
        char = "n"
    return char

print(char_at("superheroe", 4)) # Se espera 'r' """