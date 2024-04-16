class Persona:  # Creamos una clase

    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  # Se lo llama metodo Init Dunder, inicia la clase
        # *args argumento variables para tuplas, **kwargs argumento variables para diccionarios
        self.nombre = nombre  # atributos (de metodo) - Variables
        self.apellido = apellido
        self._dni = dni  # este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):  # la variable self se encuentra dentro de los metodos. En java se usa como THIS
        print(
            f"La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la dirección es: {self.args}, los datos importantes son: {self.kwargs}")


persona1 = Persona("Ariel", "Betancud", 24845739,
                   40)  # Objeto, Constructor que apunta a init (se debe colocar argumento)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona("Osvaldo", "Giordanini", 32498934, 45)
print(f"El objeto2 de la clase persona: {persona2.nombre}, {persona2.apellido}, su edad es {persona2.edad}")

# TAREA: HACER PRINT CON LAS VARIABLES DEL OBJETO PERSONA1
print(f"El objeto1 de la clase persona es: {persona1.nombre}, {persona1.apellido}, y su edad es {persona1.edad}")

persona1.nombre = "Liliana"
persona1.apellido = "Buccella"
persona1.edad = 40
print(
    f"El objeto1 modificado de la clase persona es: {persona1.nombre}, {persona1.apellido}, y su edad es {persona1.edad}")

# Los atributos son: caracteristicas
# Los metodos son: el comportamiento que van a tener los objetos (acciones)

persona1.mostrar_detalle()  # La referiencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1)  #Debemos pasarle una referencia para el self o derá error, es ineficiente, ya no se usa
persona1.telefono = "44445555289"
print(f"Este es el telefono: {persona1.nombre} {persona1.telefono}")

# print(persona2.telefono)   El objeto persona2 no tiene este atributo, da error
persona3 = Persona("Rogelio", "Romero", 93728334, 22, "Teléfono", "20292939", "Calle Lopez", 823, "Manzana", 77, "Casa",
                   18,
                   Altura=1.83, peso=105, CFavorito="Azul", Auto="Citroen", Modelo=2021)
persona3.mostrar_detalle()
# print(persona3._dni)     esto no se debe utilizar (esta encapsulado), esto dice que lo desconocemos python
# print(persona3.__nombre)    #esta totalmente encapsulado, no se puede usar
