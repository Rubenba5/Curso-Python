from random import choice


# Elegir palabra
def elegir_palabra():
    palabras = ["python", "programacion", "desarrollador", "computadora", "teclado", "pantalla"]
    elegida = choice(palabras)
    return elegida.lower()


# Mostrar guiones
def mostrar_guiones(palabra):
    lista = ["-"] * len(palabra)
    lista_a_imprimir = " ".join(lista)
    print("")
    print(lista_a_imprimir)
    return lista


# Pedir letra al usuario
def pedir_letra():
    letra = ""
    while letra not in "abcdefghijklmnñopqrstuvwxyz" or len(letra) != 1:
        letra = input("Ingresa la letra deseada a continuación: ").lower()
    return letra


# Esta letra en palabra y vidas
def letra_en_palabra(palabra, letra_importada, lista, Vidas, lista_fallos, lista_acietos):

        if letra_importada in palabra and letra_importada not in lista_acietos:
            lista_acietos.append(letra_importada)
            for posicion, letra_investigada in enumerate(palabra):
                if letra_importada == letra_investigada:
                    lista[posicion] = letra_importada
            Cambio_a_imprimir = " ".join(lista)
            print(Cambio_a_imprimir)

        elif letra_importada in palabra and letra_importada in lista_acietos:
            print("¡Ya has adivinado esta letra!")

        else:
            lista_fallos.append(letra_importada)
            Vidas -= 1
            lista_a_ensenar = ", ".join(lista_fallos)
            print(f"Las letras ({lista_a_ensenar}) no están en la palabra. Te quedan {Vidas} intentos.")
        return Vidas


# Ejecución del juego
palabra1 = elegir_palabra()
lista_guiones = mostrar_guiones(palabra1)
Vidas = 8
lista_fallos = []
lista_acietos = []

while "-" in lista_guiones and Vidas > 0:
    letra1 = pedir_letra()
    Vidas = letra_en_palabra(palabra1, letra1, lista_guiones, Vidas, lista_fallos, lista_acietos)

    if Vidas == 0:
        print(f"¡Has perdido! La palabra era: {palabra1}")
        quit()

if "-" not in lista_guiones:
    print("¡Felicidades! Has adivinado la palabra.")






