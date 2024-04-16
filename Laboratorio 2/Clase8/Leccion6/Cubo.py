"""
Crear la clase Cubo con los atributos, ancho, alto y profundidad, con un método calcular_volumen
que tendrá la formula: volumen = ancho * altura * profundidad
El usuario ingresará los datos
"""
class Cubo:

    def __init__(self, ancho, altura, profundidad):
        self.ancho= ancho
        self.altura= altura
        self.profundidad= profundidad

    def calcular_volumen(self):
        return self.ancho * self.altura * self.profundidad

ancho = int(input("Ingrese un número para el ancho del cubo: "))
altura= int(input("Ingrese un número para la altura del cubo: "))
profundidad= int(input("Ingrese un número para la profundidad del cubo: "))
volumen1= Cubo(ancho, altura, profundidad)
print(f"El volumen es: {volumen1.calcular_volumen()}")


