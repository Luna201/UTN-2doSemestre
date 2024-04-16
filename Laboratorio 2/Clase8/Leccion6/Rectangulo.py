"""
Crear una clase llamada Rectangulo, debe tener 2 atributos: altura y base, el nombre del metodo sera
clacular_area utilizando la formula: area = base*altura. Pero la base y la altura deben ser ingresados
por el usuario y los objetos debes ser 3
"""
class Rectangulo:

    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.altura * self.base


base = int(input("Digite el número para la base del retangulo: "))
altura = int(input("Digite el número para la altura del retangulo: "))
rectangulo1 = Rectangulo(base, altura)
print(f"El area del rectangulo es: {rectangulo1.calcular_area()}")
