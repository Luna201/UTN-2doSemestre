# Tipo Set: no tiene orden ni se puede modificar, PERO, se puede agregar o eliminar
# es semi-inmutable. El orden es aleatorio

planetas = {"Marte","Jupiter","Venus"}
print(len(planetas))    #Len muestra la cantidad len =length= largo



print (" # Revisar si un elemento existe dentro de set:")
print("Marte" in planetas)  # T o F
print("Venus" not in planetas)



print("# Agregar un elemento: ")
planetas.add("Tierra")
print(planetas)



print("# Eliminar elementos, puede arrojar error si el elemento no exite:")
planetas.remove("Jupiter")
print(planetas)
planetas.discard("Tierra")
print(planetas)



print ("# Limpiar Set:")
planetas.clear()
print(planetas)


"""
print ("# Eliminar Set o conjunto:")
del planetas
print(planetas)
"""


#   DICCIONARIO
print("# DICCIONARIO:")
#"Maradona":10      todo eso seria un diccionario, consta de una llave y un valor. dict(key, value)
diccionario = {
    "IDE":"Integrated Development Enviroment",
    "POO":"Programa Orientada a objetos",
    "SABD":"Sistema de Administración de Base de Datos"
}
print(len(diccionario))     #VERIFICA LA CANTIDAD DE ELEMENTOS
print(diccionario)



print("# Acceder a un diccionario con la llaver=key:")
print(diccionario["IDE"])


#otra manera de recuperar un elemento
print(diccionario.get("POO"))
print(diccionario.get("SABD"))



print("# Modificamos elementos:")
diccionario["IDE"]= "Entorno de Desarrollo Integrado"
print(diccionario)



print(" # Como recorrer los elementos: ")
for termino in diccionario:
    print(termino)

#Necesitamos una funcion para recorrer el diccionario
for termino, valor in diccionario.items():
    print(termino, valor)


print( "# Otras maneras de acceder a un diccionario: ")
for termino in diccionario.keys():  #Estamos usando una funcion
    print(termino)      #muestra solo las llaves


for valor in diccionario.values():  #usamos una funcion para acceder a un valor
    print(valor)


print(" # Comprobar la existencia de algun elemento: ")
print("IDE" in diccionario) # Devuelve un booleano


print(" #Agregar un elemento: ")
diccionario["PK"] = "Primary key"
print(diccionario)


print(" # Eliminar un elemento: ")
diccionario.pop("SABD")
print(diccionario)


print(" # Vaciar un diccionario: ")
diccionario.clear()
print(diccionario)


"""
print(" # Eliminar diccionario: ")
del diccionario
print(diccionario)

"""

print(" # concatenamos listas: ")
lista1 = [1,2,1]
lista2 = [4,5,6]
lista3 = lista1 + lista2
print(lista3)


lista3.extend([7,8,9]) #Una funcion para agregar varios elementos a la lista
print(lista3)


print(lista3.index(5))      #Funcion para ubicar en que indice esta el valor ingresado
#print(lista3.index(0))     #esto da error por no ser parte de la lista


print(" # Com osaber cuantos valores repetidos hay dentro de una lista: ")
print(lista3.count(1))      #cuenta cuantos valores iguales hay dentro de la lista



print(" # Para poner la lista al reves: ")
lista3.reverse()
print(lista3)


print(" #Para que una lista se multiplique: ")
lista3 = lista3 * 2
print(lista3)


print(" #Metodo de ordenamiento: ")
lista3.sort()   #funcion que ordena de manera ascendente
print(lista3)


lista3.sort(reverse=True)   #ordena descendentemente
print(lista3)


# REPASO DE TUPLAS
tupla = (4, "Hola", 6.78, [1,2,78],4, "Hola")
print(tupla)


print(4 in tupla)   #Accion booleana, su respuesta es de tipo booleana
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla