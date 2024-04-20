class Persona():
    def __init__(self, nombre, edad):  # Esta clase hereda de la clase Objet
        self.nombre = nombre
        self.edad = edad


class Empleado(Persona):  # Esta clase es hija de la clase persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo


empleado1 = Empleado("Ariel", 40, 75000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)