"""Ejercicio 11: Agenda telefonica
Hacer un programa que simule una agenda de telefono. Crear un diccionario
donde la clave sea el nombre del ususario y el valor sea el telefono,
el programa tendra el siguiente menu de opciones:
1. Nuevo contacto
2. Borrar contacto
3. Ver contactos existentes
4. Salir"""

agenda = {}
while True
    print("\n .:MENÚ:.")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    opcion = int(input("Digite una opción de menú: "))
    if opcion == 1
        nombre = input("Digite el nombre del contacto: ")
        telefono = input("Digite el número de teefono: ")
        if nombre not in agenda:
            agenda[nombre] = 