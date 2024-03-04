class Persona:  #Creamos una clase
    
    def __init__(self, nombre, apellido, edad): #Se define un método dentro de la clase
        self.nombre = nombre   #atributos (de metodo) - Variables
        self.apellido = apellido
        self.edad = edad

persona1 = Persona("Ariel", "Betancud", 40)    #Objeto, Constructor que apunta a init (se debe colocar argumento)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona("Osvaldo", "Giordanini", 45)
print(f"El objeto2 de la clase persona: {persona2.nombre}, {persona2.apellido}, su edad es {persona2.edad}")

#TAREA: HACER PRINT CON LAS VARIABLES DEL OBJETO PERSONA1
print(f"El objeto1 de la clase persona es: {persona1.nombre}, {persona1.apellido}, y su edad es {persona1.edad}")