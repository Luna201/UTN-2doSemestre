#Comenzamos con Funciones
#Definimos una función
# mi_funcion()      No se puede llamar antes de definir una función
def mi_funcion():   #snake_case o camelCase
    print("Saludos a todos los alumnos de la Tecnicatura")

mi_funcion()    #Llamamos la función
mi_funcion()


# CLASE 6
#DEsempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+" "+lastName)
person = ["Ariel", "Betancud"]
show(person[0], person[1])  #Pasamos uno por uno  los datos de la lista a la funcion
show(*person)   # con el asterisco muestra todo
person2 = ("Ovaldo", "Giordanini")  #desampaquetamos atraves de una TUPLA
show(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}
show(**person3)

numbers =[1, 2, 3, 4, 5] # se ejecuta aunque este vacio  el else a menos que este el break
for n in numbers:
    print(n)
    if n == 3:
        break   #Esta es la unica manera para que no se ejecute el else
else:
    print("Esto se termina")


# List comprehesion, lista de compresion. NO modifica la lista, SOLO extrae
names = ["Paolo","Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0]  == "P" ] #Genera una nueva lista
print(alongP)

bottleC = [{"name": "Quilmes", "country": "Arg"},
           {"name": "Corona", "country": "Mex"},
           {"name": "Stella Artois", "country": "Belgium"},
            ]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)


# Paso de Argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos lo que ven a través del canal de YouTube")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2("Jorge", "Lucero")
mi_funcion2("Ariel", "Betancud")
mi_funcion2("Analia", "Pedrosa")


# La palabra Return en funciones
# Creamos una funcion para sumar
def sumar(a, b):
    return a + b
"""resultado = sumar(78, 22)
print(f"El resultado de la suma es: {resultado}")   """
print(f"El resultado de la suma es: {sumar(55, 45)}")   #opcion reducida


#Valores por Defaul
def sumar2(a = 0, b= 0) :    #Le damos un valor por default
    return a + b
resultado = sumar2()
print(f"Resultado de la suma: {resultado}")
print(f"Resultado de la suma: {sumar2(22, 66)}")


# Argumentos variables en funciones
def listarNombres(*nombres):    #Es la forma cuando no se conoce el nro de argumentos: *args
    for nombre in nombres:  #Se convierte en tupla
        print(nombre)
listarNombres("Lucas", "Jose", "Claudia", "Rosa")
listarNombres("Marcos", "Daniel", "Romina", "Carlos")