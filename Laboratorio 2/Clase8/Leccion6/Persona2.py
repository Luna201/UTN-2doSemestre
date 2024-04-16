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
    def apellido(self, apellido):  # Método setter
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


persona1 = Persona2("Ariel", "Betancud", 41)
print(persona1.nombre)  # o   print(persona1.nombre())    Llamamos al método getter

persona1 = Persona2("Ariel", "Betancud", 41)
print(persona1.apellido)

persona1 = Persona2("Ariel", "Betancud", 41)
print(persona1.edad)

persona1.nombre= "Juan Pedro"
print(persona1.nombre)