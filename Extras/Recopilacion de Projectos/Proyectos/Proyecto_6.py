# Librerias
import os
from os import system
from pathlib import *
import shutil

# Cosas Necesarias
ruta = Path("C:/Users/Ruben/Desktop/Python/Curso-Python/Extras/Recopilacion de Projectos/Proyectos/Recursos_6") #Si quieres probarlo cambia la ruta
Numero_Recetas = 0
Bucle = 0
recetas = ruta.glob("**/*.txt")

for archivo in recetas:
    Numero_Recetas += 1

# Bienvenida
def bienvenida(ruta1, numero_recetas):

    print("¡Bienvenido de nuevo!")
    print(f"Las recetas estan en: {ruta1}")
    print(f"Tienes {numero_recetas} recetas en tu recetario.")
    print("")

# Menu Despliegue
def menu_despligue():

    print("[1] Leer receta\n[2] Crear Receta\n[3] Crear Categoria\n[4] Eliminar Receta\n[5] Eliminar Categoria\n[6] Finalizar Programa")
    print("")

# Seleccion
def menu_seleccion():

    Seleccion = input("Elije una opción para continuar: ")
    while Seleccion not in "123456":
        Seleccion = input("Elije una opción para continuar: ")

    return Seleccion

# [1] Leer receta
def opcion_1(ruta1):

    Categorias = input("Introduce la Categoria deseada: ")
    Categorias_Ruta = Path(ruta1, Categorias)
    Receta = input("Que receta quiere leer: ")
    Ruta_Final = Path(ruta1, Categorias_Ruta, Receta+".txt")
    Archivo_a_Leer = open(Ruta_Final, "r")
    print("")
    print(Archivo_a_Leer.readlines())

# [2] Crear Receta
def opcion_2(ruta1):

    Categorias = input("Introduce la Categoria deseada: ")
    Categorias_Ruta = Path(ruta1, Categorias)

    Receta = input("Que receta quiere crear: ")
    Ruta_Final = Path(ruta1, Categorias_Ruta, Receta+".txt")

    Archivo_a_Crear = open(Ruta_Final, "w")
    Texto = input(f"Que desea escribir en esta receta ({Receta}): ")
    Archivo_a_Crear.write(Texto)

# [3] Crear Categoria
def opcion_3(ruta1):

    Categorias = input("Introduce el nombre de la nueva categoria:  ")
    Categorias_Ruta = Path(ruta1, Categorias)
    os.mkdir(Categorias_Ruta)

# [4] Eliminar Receta
def opcion_4(ruta1):

    Categorias = input("Introduce la Categoria deseada: ")
    Categorias_Ruta = Path(ruta1, Categorias)
    Receta = input("Que receta quiere leer: ")
    Ruta_Final = Path(ruta1, Categorias_Ruta, Receta+".txt")
    os.remove(Ruta_Final)

# [5] Eliminar Categoria
def opcion_5(ruta1):

    Categorias = input("Introduce la Categoria deseada: ")
    Categorias_Ruta = Path(ruta1, Categorias)
    shutil.rmtree(Categorias_Ruta)

# [5] Eliminar Categoria
def opcion_6():
    quit()



# Ejecucion
while Bucle == 0:
    print("")
    bienvenida(ruta, Numero_Recetas)
    menu_despligue()
    Seleccion_Definitiva = menu_seleccion()
    if Seleccion_Definitiva == "1":
        opcion_1(ruta)

    elif Seleccion_Definitiva == "2":
        opcion_2(ruta)

    elif Seleccion_Definitiva == "3":
        opcion_3(ruta)

    elif Seleccion_Definitiva == "4":
        opcion_4(ruta)

    elif Seleccion_Definitiva == "5":
        opcion_5(ruta)

    elif Seleccion_Definitiva == "6":
        opcion_6()
        Bucle = 1

    system("cls")



