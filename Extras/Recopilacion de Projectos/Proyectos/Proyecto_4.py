# Librerias
from random import *

# Variables
Nombre = input("¿Cómo te llamas?")
Numero_Generado = int(randint(1, 100))
Intentos = 8
Numero_Intentos = 0

# Bucle While
while Intentos != 0:
    print(" ")
    print(f"Bueno, {Nombre}, piensa otro numero entre 1 y 100. Te quedan {Intentos} intentos!")
    Numero_Introducido = int(input("¿Cuál es el número? "))
    Numero_Intentos += 1

    if Numero_Introducido < 0 or Numero_Introducido > 100:
        print("⮕ El número introducido no es valido.")

    elif Numero_Introducido > Numero_Generado:
        print("⮕ El número es menor.")
        Intentos -= 1

    elif Numero_Introducido < Numero_Generado:
        print("⮕ El número es mayor.")
        Intentos -= 1

    elif Numero_Introducido == Numero_Generado:
        print(f"✱ Has acertado el número en {Numero_Intentos} intento. ¡Felicitaciones!")
        quit()

    if Intentos == 0:
        print(" ")
        print(f"✱ Te has quedado sin intentos (el número era {Numero_Generado}). ¡Vuelve a Intentarlo!")



