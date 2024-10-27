#1
""" class Persona():
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
    
    def presentacion(self) -> None:
        print(f"Hola! Mi nombre es {self.nombre} y tengo {self.edad} años")
        #return 'Hola! Mi nombre es {0} y tengo {1} años'.format(self.nombre, self.edad)
    
persona = Persona("Nicolas", 32)
persona.presentacion()
#print(persona.presentacion()) """

#2
'''class Libro():
    def __init__(self, tittle, author, year,) -> None:
        self.tittle = tittle
        self.author = author
        self.year = year
        
    def info(self) -> None:
        print(f"""
              Nombre:             {self.tittle} 
              Autor:              {self.author}
              Año de publicacion: {self.year}""")
        
libro = Libro("Chances", "Oracio Altuna", 1986)
libro.info()'''

#3
""" class Rectangulo():
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura
    
    def area(self) -> float:
        area = self.base * self.altura
        return area

    def perimetro(self) -> float:
        perimetro = (self.base * 2) + (self.altura * 2)
        return perimetro

rectangulo = Rectangulo(10, 5)
print(f"El area del rectangulo es: {rectangulo.area()}")
print("El perimetro del rectangulo es de: ", rectangulo.perimetro()) """

#4
""" class Calculadora():
    def __init__(self, numero_a, numero_b) -> None:
        self.numero_a = numero_a
        self.numero_b = numero_b
    
    def suma(self) -> float:
        resultado = self.numero_a + self.numero_b
        return resultado
    
    def resta(self) -> float:
        resultado = self.numero_a - self.numero_b
        return resultado
    
    def multiplicacion(self) -> float:
        resultado = self.numero_a * self.numero_b
        return resultado
    
    def division(self) -> float | None:
        resultado = None
        if self.numero_b == 0:
            print("Error, no se puede dividir por cero")
        else:
            resultado = self.numero_a / self.numero_b
        return resultado
    
calculadora = Calculadora(10, 0)
print(calculadora.suma())
print(calculadora.resta())
print(calculadora.multiplicacion())
print(calculadora.division()) """

#5
""" class Animal():
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        
    def sonido_que_hace(self) -> None:
        print(self.sonido)
        
class Perro(Animal):
    def __init__(self, nombre, sonido) -> None:
        super().__init__(nombre)
        self.sonido = sonido

class Gato(Animal):
    def __init__(self, nombre, sonido) -> None:
        super().__init__(nombre)
        self.sonido = sonido


gato = Gato("Desplumado", "Miauuu")
perro = Perro("Sultan", "Guau guau")
gato.sonido_que_hace()
perro.sonido_que_hace() """

#6
""" class CuentaBancaria():
    
    #Constructor Atributos
    def __init__(self, titular, saldo) -> None:
        self.__titular = titular
        self.__saldo = saldo
    
    #Getter & Setter
    def obtener_saldo(self) -> float:
        return self.__saldo
    
    def cargar_saldo(self, saldo_nuevo) -> None:
        self.__saldo += saldo_nuevo
        print("Carga exitosa")
        
    def retirar_saldo(self, saldo_retirar) -> None:
        if self.__saldo < saldo_retirar:
            print("Saldo insuficiente")
        else:
            self.__saldo -= saldo_retirar
            print("Retiro exitoso")
    
cuenta = CuentaBancaria("Nico", 100)
print(cuenta.obtener_saldo())
cuenta.retirar_saldo(50)
print(cuenta.obtener_saldo()) """
