from Persona2 import Persona2
print("Creación de objetos".center(50, "-"))
if __name__ == "__main__":
    persona5 = Persona2("Lionel", "Messi", 35)
    persona5.mostrar_detalles()
    print(__name__)     #dice en que parte del codigo estamos


print("Eliminación de objetos".center(50, "-"))
del persona5