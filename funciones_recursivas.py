from Package_Input import Input

#Ejercicio en clase "Numeros primos"
""" def primo(numero:int, i = 2, cont = 0) -> bool:
    ''' La funcion regresa:
           True si el numero es primo
           False si el numero NO es primo '''
    retorno = True
    if i < numero:
        resultado = numero % i
        if resultado == 0:
            retorno = False
        else:
            primo(numero, i + 1)
    return retorno

number = int(input("Ingrese un numero mayor que 1 que desee saber si es primo. "))
while number < 2:
    number = int(input("Numero invalido. Ingrese un numero mayor que 1. "))

if primo(number):
    print("El numero es primo.")
else:
    print("El numero no es primo.") """
    
#1

""" def sumar_naturales(numero:int, suma=0) -> int:
    ''' La funcion suma los numeros desde el 1 hasta el numero ingresado por parametro
     Devuelve el resultado de la suma '''

    suma += numero
    if numero == 0:
        return suma
    else:
        numero -= 1
        return sumar_naturales(numero, suma)

numero = int(input("Ingrese un numero natural para calcular. "))
while numero <= 0:
    numero = int(input("Numero invalido, debe ser mayor a 0"))
print("La suma de los numeros naturales hasta el numero ingresado es: ", sumar_naturales(numero)) """

#2

""" def calcular_potencia(base:int, exponente:int)->int:
    if exponente == 0:
        return 1
    else:
        return base * calcular_potencia(base, exponente - 1)

base = int(input("Ingrese la base del numero a elevar: "))
exponente = int(input("Ingrese el exponente del numero ingresado: (Solamente positivos)"))
while exponente <= 0:
    exponente = int(input("Error, el exponente debe ser positivo: "))
print(calcular_potencia(base, exponente)) """

#3

""" def sumar_digitos(numero:str, digitos:int, suma=0)->int:
    digitos -= 1
    suma += int(numero[digitos])
    if digitos == 0:
        return suma
    else:
        return sumar_digitos(numero, digitos, suma)

numero = input("Ingrese un numero para sumar sus digitos: ")
digitos = len(numero)
print("La suma de los digitos es: ", sumar_digitos(numero, digitos)) """

#4

def calcular_fibonacci(numero:int):
    
    if numero == 0:
        retorno = 0
    elif numero == 1:
        retorno = 1
    else:
        retorno = calcular_fibonacci(numero-1) + calcular_fibonacci(numero-2)
    
    return retorno

numero = Input.get_int("Ingrese un numero mayor a cero y menor a 100 para calcular el Fibonacci", "El numero tiene que ser positivo", 1, 100, 3)

if type(numero) == int:
    print(calcular_fibonacci(numero))
else: 
    print("Cerrando programa - No se ingreso un numero correcto")