
#1
""" def invertir(cadena:str) -> str:

    retorno = ""
    aux = []
    
    for c in range(len(cadena)):
        aux.append(cadena[len(cadena)-c-1])
    retorno = retorno.join(aux)
    
    return retorno

print(invertir("Hola")) """

#2
""" def contar_palabras(cadena:str):
    lenght = cadena.split(' ')
    print(len(lenght))

contar_palabras("LLendo a casa") """

#3
""" def reemplazar(cadena:str, palabra_vieja:str, palabra_nueva:str):
    
    retorno = cadena.replace(palabra_vieja, palabra_nueva)
    return retorno

print(reemplazar("Hola jamaica","jamaica","mundo")) """

#4
""" lista_peli = [["Matrix", "El Padrino", "Titanic"],
              ["Forrest Gump", "Pulp Fiction", "Gladiador"],
              ["Blade Runner", "El Rey León", "Volver al Futuro"],
              ["La La Land", "El Gran Lebowski", "Blade Runner"],
              ["Jurassic Park", "Avatar", "El Resplandor", "El Sexto Sentido"],
              ["Harry Potter", "Forrest Gump", "Pulp Fiction"],
              ["Titanic", "Star Wars", "El Señor de los Anillos"],
              ["The Truman Show", "The Shape of Water", "The Big Lebowski"],
              ["Forrest Gump", "The Godfather", "Goodfellas"],
              ["The Terminator", "The Sixth Sense", "The Great Gatsby"]]

def convertir(lista:list) -> None:
    
    separador = ", "
    
    for i in range(len(lista)):
        cadena = "Se recomienda ver "
        cadena += separador.join(lista[i])
        print(cadena)
    
convertir(lista_peli) """

#6
""" def palindromo(cadena:str) -> bool:
    
    retorno = False
    
    if invertir(cadena) == cadena:
        retorno = True
        
    return retorno """

#print(palindromo("malvavisco"))

#7
""" def ordenar_desc(cadena:str) -> str:
    retorno = cadena.lower().split()
    for i in range(len(retorno)-1):
        for j in range(i+1, len(retorno)):
            if retorno[j] > retorno[i]:
                aux = retorno[j]
                retorno[j] = retorno[i]
                retorno[i] = aux
    retorno = "".join(retorno)
    
    return retorno

def ordenar_asc(cadena:str) -> str:
    retorno = cadena.lower().split()
    for i in range(len(retorno)-1):
        for j in range(i+1, len(retorno)):
            if retorno[j] < retorno[i]:
                aux = retorno[j]
                retorno[j] = retorno[i]
                retorno[i] = aux
    retorno = "".join(retorno)
    
    return retorno
                
def ordenar(cadena:str, orden=1) -> str:

    ''' Se recibe una cadena por parametro y un numero
    Si se recibe 1 se ordena la cadena de forma ascendente
    Si se recibe -1, la cadena se va a ordenar descendentemente
    Si se recibe otro numero imprime un error.
    Por defecto se ordena ascendente '''
    
    if orden == 1:
        retorno = ordenar_asc(cadena)
    elif orden == -1:
        retorno = ordenar_desc(cadena)
    else:
        print("Se ingreso una opcion invalida")

    return retorno """
