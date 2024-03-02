"""Ejercicio 03: Función recursiva
Imprimir números de 5 a 1 de manera descendente usando funciones recursivas. Puede ser cualquier
valor positivo, por ejemplo, si pasamos el nro 5, debe imprimir:
5
4
3
2
1
si se ingresan nros negativos no se imprime nada"""

"""
def imprimirDecreciente(numero):
    if numero >= 1: #caso base
        print(numero)
        imprimirDecreciente(numero-1)   #caso recursivo
imprimirDecreciente(5)

def imprimirDecreciente(numero):
    if numero >= 1: #caso base
        print(numero)
        imprimirDecreciente(numero-1)   #caso recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print("Valor ingresado incorrecto")
imprimirDecreciente(5)
 """


# TAREA, INGRESAR EL NRO MANUAMENTE

def imprimirDecreciente(num):
    if num >= 1:  # caso base
        print(num)
        imprimirDecreciente(num - 1)  # caso recursivo
    elif num == 0:
        return
    elif num <= 0:
        print("Valor ingresado incorrecto")


num = int(input("Digite un número para trabajar: "))
imprimirDecreciente(num)
