# Librerias
import pygame
from pygame import mixer
import os
from os import system
from pathlib import *
import shutil
from random import *
import re
import datetime
import time
import math
import io
import random
import bs4
import requests

# Dia 1
def Nombre_Cerveza():
    print("\nEl nombre de tu cerveza\n"+ "es '"+ (input("¿Qué serie te gusta? ")+" "+input("Qué animal es tu favorito? "))+ "'\n"+"¡Felicitaciones!")


# Dia 2
def Calculador_impuestos():
    Nombre = input("¿Cómo te llamas? ")
    Vendido = input("¿Cuánto has vendido? ")
    Vendido = int(Vendido)
    Vendido = round(Vendido*13/100,2)
    print("")
    print (f"Ok {Nombre}. Este mes has pagado {Vendido} euros de comisiones.")


# Dia 3
def analizador_textos():
    Texto = input("Añade un texto:")
    Texto_Minusculas = Texto.lower()

    #Letras
    Letras = []
    Letras.append(input("Dime la primera letra:").lower())
    Letras.append(input("Dime la segunda letra:").lower())
    Letras.append(input("Dime la tercera letra:").lower())
    Cantidad_palabras1 = Texto_Minusculas.count(Letras[0])
    Cantidad_palabras2 = Texto_Minusculas.count(Letras[1])
    Cantidad_palabras3 = Texto_Minusculas.count(Letras[2])
    Letras_Total = (Cantidad_palabras1+Cantidad_palabras2+Cantidad_palabras3)

    #Contar palabras
    Palabras = Texto.split()
    Contar = len(Palabras)

    #Primera y ultima letra
    Primera_Letra = Texto[0]
    Ultima_Letra = Texto[-1]

    #Palabras en orden inverso
    Palabras.reverse()
    Texto_Inveritido = " ".join(Palabras)


    #Aparicion de la palabra python
    Python = bool("python" in Texto_Minusculas)
    Expresar = ""

    if (Python == True):
        Expresar = "aparece"

    else:
        Expresar = "no aparece"

    #Final
    print(" ")
    print("Este texto contiene:")
    print(f"-Aparecen {Contar} palabra en este texto.")
    print(f"-Las letras {Letras[0]}, {Letras[1]}, {Letras[2]} añadidas aparecen {Letras_Total} veces.")
    print(f"-La primera letra y la ultima son: {Primera_Letra} y {Ultima_Letra}.")
    print(f"-El texto al reves sería asi: {Texto_Inveritido}.")
    print(f'-La palabra "python" {Expresar} en el texto.')


# Dia 4
def numero_aleatorio():

    # Variables
    Nombre = input("¿Cómo te llamas? ")
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


# Dia 5
def elegir_palabra():
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


# Dia 6
def recetario():
    # Cosas Necesarias
    ruta_base = Path.home()
    ruta = Path(ruta_base, "Proyectos", "Recursos_6") #Si quieres probarlo cambia la ruta
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


# Dia 7
def cuenta_banco():
    # Clase Persona Información
    class Persona:
        def __init__(self, nombre, apellido):
            self.nombre = nombre
            self.apelllido = apellido

    # Clase Cliente del Banco
    class Cliente(Persona):

        def __init__(self, nombre, apellido, numero_cuenta, balance):
            super().__init__(nombre, apellido)
            self.numero_cuenta = numero_cuenta
            self.balance = balance

        def __str__(self):
            return f"Usted se llama {self.nombre} {self.apelllido}, su número de cuenta es {self.numero_cuenta} con un balance de {self.balance}€."

        def depositar(self):
            Cantidad = int(input("Cuánto desea depositar en su cuenta: "))
            self.balance += Cantidad
            print(f"Su cuenta ahora tiene un saldo de {self.balance}€")

        def retirar(self):

            Cantidad = int(input("Cuánto desea retirar en su cuenta: "))
            if self.balance > Cantidad:
                self.balance -= Cantidad
                print(f"Su cuenta ahora tiene un saldo de {self.balance}€")

            else:
                print("No tienes suficiente saldo para poder retirar dicha cantidad.")

    # Funciones
    def crear_cliente():
        Nombre = input("Introduce tu nombre: ")
        Apellido = input("Introduce tu apellido: ")
        Numero_Cuenta = input("Introduce el número de cuenta deseado: ")
        Cliente_Nuevo = Cliente(Nombre, Apellido, Numero_Cuenta, 0)
        return Cliente_Nuevo

    def inicio(cliente):
        Bucle = 0
        while Bucle == 0:
            print("")
            print(f"Bienvenido, {cliente.nombre} ({cliente.numero_cuenta})")
            print(f"Su saldo es de {cliente.balance}€")
            print("Puede Depositar(1), Retirar(2) o Salir(3)")
            Accion = input("Que desea hacer: ")

            if Accion == "1":
                cliente.depositar()

            elif Accion == "2":
                cliente.retirar()

            elif Accion == "3":
                Bucle = 1
                quit()

    # Ejecucion
    cliente_nuevo = crear_cliente()
    inicio(cliente_nuevo)


# Dia 8
def elegir_turno():
    def Perfumeria(funcion):
        print("")
        print(f"Su turno es: P-{funcion}")
        print("Aguarde y espere a ser atendido")

    def Farmacia(funcion):
        print("")
        print(f"Su turno es: F-{funcion}")
        print("Aguarde y espere a ser atendido")

    def Cosmetica(funcion):
        print("")
        print(f"Su turno es: C-{funcion}")
        print("Aguarde y espere a ser atendido")

    def Perfumeria_Cuenta():
        num = 1
        while True:
            yield num
            num += 1

    def Farmacia_Cuenta():
        num = 1
        while True:
            yield num
            num += 1

    def Cosmetica_Cuenta():
        num = 1
        while True:
            yield num
            num += 1

    def Preguntar():
        print("Las secciones disponibles son: Perfumeria, Cosmetica y Farmacia. ")
        Eleccion = input("Ha que sección se quiere derigir: ")
        return Eleccion

    def Preguntar_De_Nuevo():
        print("")
        Pregunta = input("¿Desea sacar otro ticket?: ")
        return Pregunta

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
            if Eleccion == "Si" or Eleccion == "si":
                print("Las secciones disponibles son: Perfumeria, Cosmetica y Farmacia. ")
                Preguntar()

            elif Eleccion == "No" or Eleccion == "no":
                print("")
                print("¡Hasta Pronto!")
                Bucle = 1

        elif Eleccion == "Farmacia":
            Farmacia(next(Numero_F))
            Eleccion = Preguntar_De_Nuevo()
            if Eleccion == "Si" or Eleccion == "si":
                print("Las secciones disponibles son: Perfumeria, Cosmetica y Farmacia. ")
                Preguntar()

            elif Eleccion == "No" or Eleccion == "no":
                print("")
                print("¡Hasta Pronto!")
                Bucle = 1

        elif Eleccion == "Cosmetica":
            Cosmetica(next(Numero_C))
            Eleccion = Preguntar_De_Nuevo()
            if Eleccion == "Si" or Eleccion == "si":
                print("Las secciones disponibles son: Perfumeria, Cosmetica y Farmacia. ")
                Preguntar()

            elif Eleccion == "No" or Eleccion == "no":
                print("")
                print("¡Hasta Pronto!")
                Bucle = 1


# Dia 9
def buscar_numeros():
    # Ruta del Directorio
    ruta_base = Path.home()
    ruta = Path(ruta_base,"Proyectos", "Recursos_9","Mi_Gran_Directorio")

    # Buscar Archivos
    def buscar_archivos(ruta):
        Dic = {}

        for Directorio, Subdirectorio, Archivo in os.walk(ruta):
            for archivo in Archivo:
                Dic[archivo] = Directorio

        return Dic

    # Comprobar
    def comprobar_archivo(dic):
        Patron = r"N\w{3}-\d{5}"
        Dic = {}

        for archivo in dic:
            Ruta_Nueva = Path(dic[archivo], archivo)
            Archivo_Abrir = open(Ruta_Nueva, "r")
            Lineas = Archivo_Abrir.readlines()
            Unir = "".join(Lineas)

            Coincidencia = re.search(Patron, Unir)
            if Coincidencia is None:
                Dic[archivo] = "No encontrado"
            else:
                Dic[archivo] = Coincidencia.group()

            Archivo_Abrir.close()

        return Dic

    # Imprimir
    def monstrar(dic, duracion):
        Contador = 0
        Fecha = datetime.date.today()
        Fecha_Ordenada = f"{Fecha.day}/{Fecha.month}/{Fecha.year}"

        print(f"Fecha de búsqueda: {Fecha_Ordenada}")
        print("")
        print("Archivo\t   |    Número de Serie")
        print("-------------------------------")

        for archivo, coincidencia in dic.items():
            if coincidencia == "No encontrado":
                pass

            else:
                print(f"{archivo}\t{coincidencia}")
                Contador += 1

        print("")
        print(f"Números encontrados: {Contador}")
        print(f"Duración de la busqueda: {math.ceil(duracion)} segundos.")

    # Ejecución
    Inicio = time.time()
    Lista = buscar_archivos(ruta)
    Dic = comprobar_archivo(Lista)
    Fin = time.time()
    Duracion = Fin - Inicio
    monstrar(Dic, Duracion)


# Dia 10
def juego():
    ruta_base = Path.home()
    Recursos = Path(ruta_base, "Proyectos", "Recursos_10")
    print(Recursos)
    # Inicializar el juego
    pygame.init()

    # Crear la pantalla y indicar sus dimensiones.
    Pantalla = pygame.display.set_mode((800, 600))

    # Titulo
    pygame.display.set_caption("Invasión Espacial")

    # Icono
    Icono = pygame.image.load(f"{Recursos}\\ovni.png")
    pygame.display.set_icon(Icono)

    # Fondo
    Fondo = pygame.image.load(f"{Recursos}\\fondo.jpg")

    # Musica
    mixer.music.load(f"{Recursos}\\MusicaFondo.mp3")  # Cargar Musica
    mixer.music.set_volume(0.2)  # Controlar el volumen (0-1)
    mixer.music.play(-1)  # Reproducirlo en bucle

    # Variables del Jugador
    img_Jugador = pygame.image.load(f"{Recursos}\\cohete.png")
    Jugador_x = 368  # Eje X
    Jugador_y = 500  # Eje Y
    Jugador_x_cambio = 0

    # Variables del Enemigo
    img_Enemigo = []
    Enemigo_x = []
    Enemigo_y = []
    Enemigo_x_cambio = []
    Enemigo_y_cambio = []
    Cantidad_enemigos = 5

    for enemigo in range(Cantidad_enemigos):
        img_Enemigo.append(pygame.image.load(f"{Recursos}\\enemigo.png"))
        Enemigo_x.append(random.randint(0, 736))  # Eje X
        Enemigo_y.append(random.randint(50, 200))  # Eje Y
        Enemigo_x_cambio.append(0.3)
        Enemigo_y_cambio.append(50)

    # Transformar el Nombre de la Fuente a Bytes
    def fuente_bytes(fuente):
        with open(fuente, "rb") as f:
            ttf_bytes = f.read()
        return io.BytesIO(ttf_bytes)

    # Variables de la Bala
    Balas = []
    img_bala = pygame.image.load(f"{Recursos}\\bala.png")
    Bala_x = 0  # Eje X
    Bala_y = 500  # Eje Y
    Bala_x_cambio = 0
    Bala_y_cambio = 1
    Bala_visible = False

    # Variable Puntaje
    Puntaje = 0
    Fuente_como_Bytes = fuente_bytes(f"{Recursos}\\SpecialElite.ttf")
    Fuente = pygame.font.Font(f"{Recursos}\\SpecialElite.ttf", 32)  # Tipo de fuente que aparece en pantalla
    Texto_x = 10
    Texto_y = 10

    # Variable Fin
    Fuente_Fin = pygame.font.Font(f"{Recursos}\\SpecialElite.ttf", 40)  # Tipo de fuente que aparece en pantalla
    Texto_Fin_x = 400
    Texto_Fin_y = 300

    # Función Monstrar Puntaje
    def Monstrar_puntaje(eje_x, eje_y):
        Texto = Fuente.render(f"Puntaje: {Puntaje}", True, (255, 255, 255))  # Renderizar puntaje
        Pantalla.blit(Texto, (eje_x, eje_y))  # Monstrar Puntaje

    # Función Fin del Juego
    def Monstrar_Fin():
        Texto = Fuente.render(f"Juego Terminado", True, (255, 255, 255))  # Renderizar puntaje
        Pantalla.blit(Texto, (60, 200))  # Monstrar Puntaje

    # Función del Jugador
    def Jugador(eje_x, eje_y):
        Pantalla.blit(img_Jugador, (eje_x, eje_y))  # .blit() es el metodo arrojar en la pantalla.

    # Función del Enemigo
    def Enemigo(eje_x, eje_y, ene):
        Pantalla.blit(img_Enemigo[ene], (eje_x, eje_y))  # .blit() es el metodo arrojar en la pantalla.

    # Función Disparar Bala
    def Disparar_bala(eje_x, eje_y):
        global Bala_visible
        Bala_visible = True
        Pantalla.blit(img_bala, (eje_x + 16, eje_y + 10))

    # Función Detectar Colisiones
    def Detectar_colisiones(x_1, y_1, x_2, y_2):
        Distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
        if Distancia < 27:
            return True
        else:
            return False

    # Loop del Juego
    se_ejecuta = True  # Variable que mantiene el juego ejecutandose.
    while se_ejecuta:

        # Imagen de Fondo.
        Pantalla.blit(Fondo, (0, 0))

        # Iterar Eventos
        for evento in pygame.event.get():

            # Evento Cerrar
            if evento.type == pygame.QUIT:
                se_ejecuta = False

            # Evento Presionar Teclas
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    Jugador_x_cambio = -0.8

                if evento.key == pygame.K_RIGHT:
                    Jugador_x_cambio = 0.8

                if evento.key == pygame.K_SPACE:
                    Sonido_bala = mixer.Sound(f"{Recursos}\\disparo.mp3")  # Cargar la música
                    Sonido_bala.play()  # Reproducirla
                    nueva_bala = {
                        "x": Jugador_x,
                        "y": Jugador_y,
                        "velocidad": -5
                    }
                    Balas.append(nueva_bala)

            # Evento Soltar Teclas
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    Jugador_x_cambio = 0

        # Modificar la ubicacion del Jugador
        Jugador_x += Jugador_x_cambio

        # Mantener dentro de los Bordes al Jugador
        if Jugador_x <= 0:
            Jugador_x = 0

        elif Jugador_x >= 736:
            Jugador_x = 736

        # Modificar los Enemigos
        for enemigo in range(Cantidad_enemigos):

            # Fin del Juego
            if Enemigo_y[enemigo] >= 500:
                for cada_enemigo in range(Cantidad_enemigos):
                    Enemigo_y[cada_enemigo] = 1000
                Monstrar_Fin()
                break

            Enemigo_x[enemigo] += Enemigo_x_cambio[enemigo]

            # Mantener dentro de los Bordes al Enemigo
            if Enemigo_x[enemigo] <= 0:
                Enemigo_x_cambio[enemigo] = 0.3
                Enemigo_y[enemigo] += Enemigo_y_cambio[enemigo]

            elif Enemigo_x[enemigo] >= 736:
                Enemigo_x_cambio[enemigo] = -0.3
                Enemigo_y[enemigo] += Enemigo_y_cambio[enemigo]

            # Invocacion de la función Colision
            for bala in Balas:
                colision_bala_enemigo = Detectar_colisiones(Enemigo_x[enemigo], Enemigo_y[enemigo], bala["x"],
                                                            bala["y"])
                if colision_bala_enemigo:
                    sonido_colision = mixer.Sound(f"{Recursos}\\Golpe.mp3")
                    sonido_colision.play()
                    Balas.remove(bala)
                    Puntaje += 1
                    Enemigo_x[enemigo] = random.randint(0, 736)
                    Enemigo_y[enemigo] = random.randint(20, 200)
                    break

            # Invocación de función Enemigo
            Enemigo(Enemigo_x[enemigo], Enemigo_y[enemigo], enemigo)

        # Movimiento Bala
        for bala in Balas:
            bala["y"] += bala["velocidad"]
            Pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
            if bala["y"] < 0:
                Balas.remove(bala)

        if Bala_visible:
            Disparar_bala(Bala_x, Bala_y)
            Bala_y -= Bala_y_cambio

        # Invocación de la función Jugador
        Jugador(Jugador_x, Jugador_y)

        # Invocación de la función Puntaje
        Monstrar_puntaje(Texto_x, Texto_y)

        # Actualizar
        pygame.display.update()


# Dia 11
def web_scraping():

    # Url Base de la Página Web
    url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

    # Lista de Titulos con 4 o 5 estrellas
    titulos_rating_alto = []

    # Iterar Paginas
    for pagina in range(1, 51):

        # Crear sopa en cada página
        url_pagina = url_base.format(pagina)

        # Request a la Pagina
        resultado = requests.get(url_pagina)
        sopa = bs4.BeautifulSoup(resultado.text, "lxml")

        # Seleccionar datos de los Libros
        libros = sopa.select(".product_pod")

        # Iterar en los libros
        for libro in libros:

            # Verificar que el libro tenga 4 o 5 estrellas
            if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:
                # Titulo del Libro (variable)
                titulo_libro = libro.select("a")[1]["title"]

                # Agregar libro a la lista
                titulos_rating_alto.append(titulo_libro)

    # Ver libros de 4 y 5 estrellas en consola
    for libro in titulos_rating_alto:
        print(libro)