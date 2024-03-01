"""Ejercicio 02: Función con *args para multiplicar.
Crear una función para multiplicar los valores recibidos de tipo numéricos, utilizando
argumentos variables *args como parámetro de la función y regresar como resultado la
multiplicación de todos los valores pasados com argumentos"""


#Definimos la función para multiplicar
def multiplicar_valores(*numeros):  #La variable mas utilizado es " *args "
    resultado = 1   #se le asigna 1 porque con 0 no se puede multiplicar
    for numero in numeros:
        resultado *= numero
    return resultado

#llamamos la función
print(multiplicar_valores(3, 5, 15, 3))    #le pasamos los argumentos