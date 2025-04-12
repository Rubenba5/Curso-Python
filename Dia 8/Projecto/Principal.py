# Importar Numeros.py
from Numeros import *

# Preguntar
def Preguntar():
    print("Las secciones disponibles son: Perfumeria, Cosmetica y Farmacia. ")
    Eleccion = input("Ha que sección se quiere derigir: ")
    return Eleccion


def Preguntar_De_Nuevo():
    print("")
    Pregunta = input("¿Desea sacar otro ticket?: ")
    if Pregunta == "Si" or Pregunta == "si":
        print("Las secciones disponibles son: Perfumeria, Cosmetica y Farmacia. ")
        Eleccion = input("Ha que sección se quiere derigir: ")
        return Eleccion

    elif Pregunta == "No" or Pregunta == "no":
        print("")
        print("¡Hasta Pronto!")
        quit()

# Ejecución
Numero_P = Perfumeria_Cuenta()
Numero_F = Farmacia_Cuenta()
Numero_C = Cosmetica_Cuenta()
Bucle = 0
Eleccion = Preguntar()
while Bucle == 0:
    if Eleccion == "Perfumeria":
        Perfumeria(next(Numero_P))
        Eleccion = Preguntar_De_Nuevo()

    elif Eleccion == "Farmacia":
        Farmacia(next(Numero_F))
        Eleccion = Preguntar_De_Nuevo()

    elif Eleccion == "Cosmetica":
        Cosmetica(next(Numero_C))
        Eleccion = Preguntar_De_Nuevo()










