class Aritmetica:
    """
    El nombre de ste tipo de comentario es: DocString, esto es documentación de la clase en python
    Vamos a hacer en esta clase algunas operaciones de: suma, resta, moltiplicación y mas
    """

    def __init__(self, operandoA, operandoB):  # metodo iniciador de atributos
        self.operandoA = operandoA
        self.operandoB = operandoB

    # Método para sumar
    def sumar(self):
        return self.operandoA + self.operandoB

    def resta(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB


aritmetica1 = Aritmetica(7, 9)  # Le pasamos los argumentos para los operandos
print(aritmetica1.sumar())
print(f"La resta de los números es: {aritmetica1.resta()}")
print(f"La multiplicación de los números es: {aritmetica1.multiplicar()}")
print(f"La división de los números es: {aritmetica1.dividir():.2f}")  # .2f redondea en 2
