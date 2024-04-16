class Persona2:
    def __init__(self, nombre, apellido, edad):  # Esta encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}")

    @property  # decorador
    def nombre(self):  # Método Getter
        print("Estamos usando el método get")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Método setter
        print("Estamos usando el método set")
        self._nombre = nombre

    @property  # decorador
    def apellido(self):  # Método Getter
        print("Estamos usando el método get")
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # Método setter (necesita incluir un parametro, apellido)
        print("Estamos usando el método set")
        self._apellido = apellido

    @property  # decorador
    def edad(self):  # Método Getter
        print("Estamos usando el método get")
        return self._edad

    @edad.setter
    def edad(self, edad):  # Método setter
        print("Estamos usando el método set")
        self._edad = edad


if __name__ == "__main__":
    persona1 = Persona2("Ariel", "Betancud", 41)
print(persona1.nombre)  # o   print(persona1.nombre())    Llamamos al método getter

persona1 = Persona2("Ariel", "Betancud", 41)
print(persona1.apellido)

persona1 = Persona2("Ariel", "Betancud", 41)
print(persona1.edad)

persona1.nombre = "Juan Pedro"
print(persona1.nombre)
print(persona1.nombre)  # otra vez con el metodo getter
print(persona1.mostrar_detalles())  # Llamamos el método mostrar_detalles
# Atributo read-only seria la edad porque no tiene el método setter
print(persona1.edad)

# EJERCICIO:
# Crear 3 objetos más, utilizandolos métodos getter and setter para modificar, y mostrar los cambios con
# el método mostrar_detalles
persona2 = Persona2("Flor", "Romero", 23)
persona2.nombre = "Florencia"
persona2.apellido = "Romery"
persona2.edad = 22
print(persona2.mostrar_detalles())

persona3 = Persona2("Caro", "Felisa", 21)
persona3.nombre = "Carolina"
persona3.apellido = "Romery"
persona3.edad = 31
print(persona3.nombre)
print(persona3.apellido)
print(persona3.edad)
print(persona3.mostrar_detalles())

persona4 = Persona2("Naty", "Lucer", 35)
persona4.nombre = "Natalia"
persona4.apellido = "Lucero"
persona4.edad = 33
print(persona4.nombre)
print(persona4.apellido)
print(persona4.edad)
print(persona4.mostrar_detalles())

print(__name__)
