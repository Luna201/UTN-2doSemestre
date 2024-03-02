"""Ejercicio 5: Convertidor de temperaturas
Realizar dos funciones para convertir de grados celcius a fahrenheit y viceversa.
Formula: (0 °C × 9/5) + 32 = 32 °F"""


#Función que convierte de celcius a fahrenheit
def celcius_fahrenheit(celcius):
    return celcius * 9 / 5 + 32     #Lapresedencia: multiplicación, división y suma

#Función que convierte de fahrenheit a celcius
def fahrenheit_celcius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


celcius = float(input("Digite el valor de celcius: "))
resultado = celcius_fahrenheit(celcius)
print(f"{celcius} C a F -> {resultado:.2f}")    #.2f es para reducir los nros

fahrenheit = float(input("Digite el valor de fahrenheit: "))
resultado = fahrenheit_celcius(fahrenheit)
print(f"{fahrenheit} F a C -> {resultado: .2f}")



