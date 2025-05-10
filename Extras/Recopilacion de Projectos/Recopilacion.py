# Librerias
from tkinter import *  # Importar TKINTER (interfaz grafica)


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
    from random import randint

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
            Vidas = 0

    if "-" not in lista_guiones:
        print("¡Felicidades! Has adivinado la palabra.")


# Dia 6
def recetario():
    import os
    from pathlib import Path
    import shutil

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
    from pathlib import Path
    import time
    import os
    import re
    import datetime
    import math

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
    import pygame
    from pygame import mixer
    import random
    import io
    import math
    from pathlib import Path

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
    import requests
    import bs4

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


# Dia 12
def mi_restaurante():
    from platform import release
    import random
    import datetime
    from tkinter import filedialog, messagebox  # Guardar

    # Funciones de Calculadora
    operador = ""
    def click_boton(numero):
        global operador
        operador = operador + numero
        visor_calculadora.delete(0, END)
        visor_calculadora.insert(END, operador)

    def borrar():
        global operador
        operador = ""
        visor_calculadora.delete(0, END)

    def obtener_resultado():
        global operador
        resultado = str(eval(operador))
        visor_calculadora.delete(0, END)
        visor_calculadora.insert(0, resultado)
        operador = ""

    # Funcion de CheckButtoms
    def revisar_check():
        x = 0
        for c in cuadros_comida:
            if variables_comida[x].get() == 1:
                cuadros_comida[x].config(state= NORMAL)
                if cuadros_comida[x].get() == "0":
                    cuadros_comida[x].delete(0, END)
                cuadros_comida[x].focus() # Poner el cursor enfocado

            else:
                cuadros_comida[x].config(state= DISABLED)
                texto_comida[x].set("0")

            x += 1

        x = 0
        for c in cuadros_bebida:
            if variables_bebida[x].get() == 1:
                cuadros_bebida[x].config(state= NORMAL)
                if cuadros_bebida[x].get() == "0":
                    cuadros_bebida[x].delete(0, END)
                cuadros_bebida[x].focus() # Poner el cursor enfocado

            else:
                cuadros_bebida[x].config(state= DISABLED)
                texto_bebida[x].set("0")

            x += 1

        x = 0
        for c in cuadros_postres:
            if variables_postres[x].get() == 1:
                cuadros_postres[x].config(state= NORMAL)
                if cuadros_postres[x].get() == "0":
                    cuadros_postres[x].delete(0, END)
                cuadros_postres[x].focus() # Poner el cursor enfocado

            else:
                cuadros_postres[x].config(state= DISABLED)
                texto_postres[x].set("0")

            x += 1

    # Funcion de Calcular Total / Precios
    precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
    precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
    precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

    def total():
        # Comida
        sub_total_comida = 0
        indice = 0
        for cantidad in texto_comida:
            if cantidad.get() != "0":
                sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[indice])
            indice += 1


        # Bebida
        sub_total_bebidas = 0
        indice = 0
        for cantidad in texto_comida:
            if cantidad.get() != "0":
                sub_total_bebidas = sub_total_bebidas + (float(cantidad.get()) * precios_bebida[indice])
            indice += 1

        # Postres
        sub_total_postres = 0
        indice = 0
        for cantidad in texto_comida:
            if cantidad.get() != "0":
                sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[indice])
            indice += 1

        # Calcular Subtotal
        subtotal = sub_total_comida + sub_total_bebidas + sub_total_postres
        impuestos = subtotal * 0.07
        total = subtotal + impuestos

        # Insertar texto en variables de los textos
        var_costo_comida.set(f"{round(sub_total_comida, 2)} €")
        var_costo_bebida.set(f"{round(sub_total_bebidas, 2)} €")
        var_costo_postres.set(f"{round(sub_total_postres, 2)} €")
        var_subtotal.set(f"{round(subtotal, 2)} €")
        var_impuestos.set(f"{round(impuestos, 2)} €")
        var_total.set(f"{round(total, 2)} €")


    # Funcion de Recibo
    def recibo():
        texto_recibo.delete(1.0, END)
        num_recibo = f"N# - {random.randint(1000, 9999)}"
        fecha = datetime.datetime.now()
        fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.hour}"
        texto_recibo.insert(END, f"Datos:\t{num_recibo}\t\t\t{fecha_recibo}\n")
        texto_recibo.insert(END, f"*" * 75 + "\n")
        texto_recibo.insert(END, "Items\t\tCant.\t\tCosto Items\n")
        texto_recibo.insert(END, f"-" * 90 + "\n")

        x = 0
        for comida in texto_comida:
            if comida.get() != "0":
                texto_recibo.insert(END, f"{lista_comidas[x]}\t\t{comida.get()}\t\t{int(comida.get()) * precios_comida[x]} €\n")
            x += 1

        x = 0
        for bebida in texto_bebida:
            if bebida.get() != "0":
                texto_recibo.insert(END, f"{lista_bebidas[x]}\t\t{bebida.get()}\t\t{int(bebida.get()) * precios_bebida[x]} €\n")
            x += 1

        x = 0
        for postres in texto_postres:
            if postres.get() != "0":
                texto_recibo.insert(END, f"{lista_postres[x]}\t\t{postres.get()}\t\t{int(postres.get()) * precios_postres[x]} €\n")
            x += 1

        texto_recibo.insert(END, f"-" * 90 + "\n")
        texto_recibo.insert(END, f"Costo de la Comida:\t\t\t{var_costo_comida.get()}\n")
        texto_recibo.insert(END, f"Costo de la Bebida:\t\t\t{var_costo_bebida.get()}\n")
        texto_recibo.insert(END, f"Costo de los Postres:\t\t\t{var_costo_postres.get()}\n")
        texto_recibo.insert(END, f"-" * 90 + "\n")
        texto_recibo.insert(END, f"Sub-Total:\t\t{var_subtotal.get()}\n")
        texto_recibo.insert(END, f"Impuestos:\t\t{var_impuestos.get()}\n")
        texto_recibo.insert(END, f"Total:\t\t{var_total.get()}\n")
        texto_recibo.insert(END, f"*" * 75 + "\n")
        texto_recibo.insert(END, "Lo esperamos pronto.")


    # Funcion Guardar
    def guardar():
        info_recibo = texto_recibo.get(1.0, END)
        archivo = filedialog.asksaveasfile(mode= "w", defaultextension=".txt") # Crear Archivo
        archivo.write(info_recibo)
        archivo.close()
        messagebox.showinfo("Información", "Su recibo ha sido guardado")


    # Funcion Resetear
    def resetear():
        texto_recibo.delete(0.1, END)

        for texto in texto_comida:
            texto.set("0")

        for texto in texto_bebida:
            texto.set("0")

        for texto in texto_postres:
            texto.set("0")

        for cuadro in cuadros_comida:
            cuadro.config(state= DISABLED)

        for cuadro in cuadros_bebida:
            cuadro.config(state= DISABLED)

        for cuadro in cuadros_postres:
            cuadro.config(state= DISABLED)

        for v in variables_comida:
            v.set(0)

        for v in variables_bebida:
            v.set(0)

        for v in variables_postres:
            v.set(0)

        var_costo_comida.set("")
        var_costo_bebida.set("")
        var_costo_postres.set("")
        var_subtotal.set("")
        var_impuestos.set("")
        var_total.set("")


    # Incializar a Tkinter
    aplicacion = Tk()


    # Tamaño de la Ventana
    aplicacion.geometry("1350x725+0+0") # Resolucion + x + y de la aparición en pantalla.


    # Evitar Maximizar
    aplicacion.resizable(False, False)


    # Título de la Ventana
    aplicacion.title("Mi Restaurante - Sitema de Factruración")


    # Color de fondo de la Ventana
    # Lista de nombres: https://es.wikibooks.org/wiki/Python/Interfaz_gr%C3%A1fica_con_Tkinter/Los_nombres_de_los_colores
    aplicacion.config(bg="burlywood") # bg = Background / Se puede usar rgb o lista de nombres.


    # Panel Superior
    # 1. Donde lo quieres ubicar, 2. Su borde (bd), 3. Relieve: "flat", "raised", "sunken", "groove", "ridge".
    panel_superior = Frame(aplicacion, bd= 1, relief= "flat")
    panel_superior.pack(side= "top") # Añadirlo a la ventana (side = sitio)


    # Etiqueta Título
    # 1. En que panel va la etiqueta, 2. Texto, 3. Color del texto (lo mismo que el color de fondo), 4. Font (tipo de letra) + Tamaño, 5. Color de Fondo, 5. Ancho.
    etiqueta_titulo = Label(panel_superior, text="Sistema de Facturación", fg="azure4",
                            font=("Dosis", 48), bg="burlywood", width= 28)

    etiqueta_titulo.grid(row=0, column=0) # Añadirlo a al ventana / Orden = Fila, Columna


    # Panel Izquierdo
    panel_izquierdo = Frame(aplicacion, bd= 1, relief= "flat")
    panel_izquierdo.pack(side= "left")


    # Panel Costos
    panel_costos = Frame(panel_izquierdo, bd= 1, relief= "flat", bg= "azure4", padx= 80)
    panel_costos.pack(side = "bottom")


    # Panel Comidas
    # LabelFrame es un panel que contiene integrada una etiqueta.
    panel_comidas = LabelFrame(panel_izquierdo, text="Comida", font=("Dosis", 19, "bold"),
                               bd = 1, relief= "flat", fg="azure4")

    panel_comidas.pack(side= "left")

    # Panel Bebidas
    # LabelFrame es un panel que contiene integrada una etiqueta.
    panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", font=("Dosis", 19, "bold"),
                               bd = 1, relief= "flat", fg="azure4")

    panel_bebidas.pack(side= "left")

    # Panel Postres
    # LabelFrame es un panel que contiene integrada una etiqueta.
    panel_postres = LabelFrame(panel_izquierdo, text="Postres", font=("Dosis", 19, "bold"),
                               bd = 1, relief= "flat", fg="azure4")

    panel_postres.pack(side= "left")


    # Panel Derecha
    panel_derecha = Frame(aplicacion, bd= 1, relief= "flat")
    panel_derecha.pack(side= "right")

    # Panel Calculadora
    panel_calculadora = Frame(panel_derecha, bd=1, relief="flat", bg="burlywood")
    panel_calculadora.pack(side= "top")

    # Panel Recibo
    panel_recibo = Frame(panel_derecha, bd=1, relief="flat", bg="burlywood")
    panel_recibo.pack() # Por defecto, se situa en la parte superior.

    # Panel Botones
    panel_botones = Frame(panel_derecha, bd=1, relief="flat", bg="burlywood")
    panel_botones.pack(side="bottom")

    # Lista de Productos
    lista_comidas = ['pollo', 'coredero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
    lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
    lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']
    variables_comida = []
    variables_bebida = []
    variables_postres = []
    cuadros_comida = []
    texto_comida = []
    cuadros_bebida = []
    texto_bebida = []
    cuadros_postres = []
    texto_postres = []


    # Generar Items Comida
    # Onvalue = Activado / Offvalue = Desactivado
    Contador = 0
    for comida in lista_comidas:
        # crear checkbutton
        variables_comida.append('')
        variables_comida[Contador] = IntVar()
        comida = Checkbutton(panel_comidas,
                             text=comida.title(),
                             font=('Dosis', 19, 'bold',),
                             onvalue=1,
                             offvalue=0,
                             variable=variables_comida[Contador],
                             command=revisar_check)

        comida.grid(row=Contador,
                    column=0,
                    sticky=W)

        # crear los cuadros de entrada
        cuadros_comida.append("")
        texto_comida.append("")
        texto_comida[Contador] = StringVar()
        texto_comida[Contador].set(0)
        cuadros_comida[Contador] = Entry(panel_comidas,
                                         font=('Dosis', 18, 'bold'),
                                         bd=1,
                                         width=6,
                                         state="disabled",
                                         textvariable=texto_comida[Contador])
        cuadros_comida[Contador].grid(row=Contador,
                                      column=1)
        Contador += 1


    # Generar Items Bebida
    # Onvalue = Activado / Offvalue = Desactivado
    Contador = 0
    for bebida in lista_bebidas:
        variables_bebida.append("")
        variables_bebida[Contador] = IntVar() # Pone el valor del CheckButton
        bebida = Checkbutton(panel_bebidas,
                             text=bebida.title(),
                             font=("Dosis", 19, "bold"),
                             onvalue= 1,
                             offvalue= 0,
                             variable= variables_bebida[Contador],
                             command=revisar_check)

        bebida.grid(row= Contador,
                    column= 0,
                    sticky= W)

        # crear los cuadros de entrada
        cuadros_bebida.append("")
        texto_bebida.append("")
        texto_bebida[Contador] = StringVar()
        texto_bebida[Contador].set(0)
        cuadros_bebida[Contador] = Entry(panel_bebidas,
                                         font=('Dosis', 18, 'bold'),
                                         bd=1,
                                         width=6,
                                         state="disabled",
                                         textvariable=texto_bebida[Contador])

        cuadros_bebida[Contador].grid(row=Contador,
                                      column=1)
        Contador += 1


    # Generar Items Postres
    # Onvalue = Activado / Offvalue = Desactivado
    Contador = 0
    for postres in lista_postres:
        variables_postres.append("")
        variables_postres[Contador] = IntVar() # Pone el valor del CheckButton
        postres = Checkbutton(panel_postres,
                              text=postres.title(),
                              font=("Dosis", 19, "bold"),
                              onvalue= 1,
                              offvalue= 0,
                              variable= variables_postres[Contador],
                              command=revisar_check)

        postres.grid(row= Contador,
                     column= 0,
                     sticky= W)

        # crear los cuadros de entrada
        cuadros_postres.append("")
        texto_postres.append("")
        texto_postres[Contador] = StringVar()
        texto_postres[Contador].set(0)
        cuadros_postres[Contador] = Entry(panel_postres,
                                         font=('Dosis', 18, 'bold'),
                                         bd=1,
                                         width=6,
                                         state="disabled",
                                         textvariable=texto_postres[Contador])

        cuadros_postres[Contador].grid(row=Contador,
                                      column=1)
        Contador += 1


    # Variables
    var_costo_comida = StringVar()
    var_costo_bebida = StringVar()
    var_costo_postres = StringVar()
    var_subtotal = StringVar()
    var_impuestos = StringVar()
    var_total = StringVar()


    # Etiquetas de Costo y Campos de Entrada
    # Comida
    etiqueta_costo_comida = Label(panel_costos,
                                  text= "Costo Comida",
                                  font= ("Dosis", 12, "bold"),
                                  bg= "azure4",
                                  fg= "white")

    etiqueta_costo_comida.grid(row= 0, column= 0)

    texto_costo_comida = Entry(panel_costos,
                               font=("Dosis", 12, "bold"),
                               bd= 1,
                               width= 10,
                               state= "readonly",
                               textvariable= var_costo_comida)

    texto_costo_comida.grid(row = 0, column= 1)

    # Bebida
    etiqueta_costo_bebida = Label(panel_costos,
                                  text= "Costo Bebida",
                                  font= ("Dosis", 12, "bold"),
                                  bg= "azure4",
                                  fg= "white")

    etiqueta_costo_bebida.grid(row= 1, column= 0)

    texto_costo_bebida = Entry(panel_costos,
                               font=("Dosis", 12, "bold"),
                               bd= 1,
                               width= 10,
                               state= "readonly",
                               textvariable= var_costo_bebida)

    texto_costo_bebida.grid(row = 1, column= 1)

    # Postres
    etiqueta_costo_postres = Label(panel_costos,
                                  text= "Costo Postres",
                                  font= ("Dosis", 12, "bold"),
                                  bg= "azure4",
                                  fg= "white")

    etiqueta_costo_postres.grid(row= 2, column= 0, padx= 41)

    texto_costo_postres = Entry(panel_costos,
                               font=("Dosis", 12, "bold"),
                               bd= 1,
                               width= 10,
                               state= "readonly",
                               textvariable= var_costo_postres)

    texto_costo_postres.grid(row = 2, column= 1, padx= 41)

    # Subtotal
    etiqueta_subtotal = Label(panel_costos,
                                  text= "Subtotal",
                                  font= ("Dosis", 12, "bold"),
                                  bg= "azure4",
                                  fg= "white")

    etiqueta_subtotal.grid(row= 0, column= 2, padx= 41)

    texto_subtotal = Entry(panel_costos,
                               font=("Dosis", 12, "bold"),
                               bd= 1,
                               width= 10,
                               state= "readonly",
                               textvariable= var_subtotal)

    texto_subtotal.grid(row = 0, column= 3, padx= 41)

    # Impuestos
    etiqueta_impuestos = Label(panel_costos,
                                  text= "Impuestos",
                                  font= ("Dosis", 12, "bold"),
                                  bg= "azure4",
                                  fg= "white")

    etiqueta_impuestos.grid(row= 1, column= 2, padx= 41)

    texto_impuestos = Entry(panel_costos,
                               font=("Dosis", 12, "bold"),
                               bd= 1,
                               width= 10,
                               state= "readonly",
                               textvariable= var_impuestos)

    texto_impuestos.grid(row = 1, column= 3, padx= 41)

    # Total
    etiqueta_total = Label(panel_costos,
                                  text= "Costo Total",
                                  font= ("Dosis", 12, "bold"),
                                  bg= "azure4",
                                  fg= "white")

    etiqueta_total.grid(row= 2, column= 2, padx= 41)

    texto_total = Entry(panel_costos,
                               font=("Dosis", 12, "bold"),
                               bd= 1,
                               width= 10,
                               state= "readonly",
                               textvariable= var_total)

    texto_total.grid(row = 2, column= 3, padx= 41)


    # Botones
    botones = ["total", "recibo", "guardar", "resetear"]
    botones_creados = []
    columnas = 0

    for boton in botones:
        boton = Button(panel_botones,
                       text= boton.title(),
                       font=("Dosis", 14, "bold"),
                       fg = "white",
                       bg = "azure4",
                       bd = 1,
                       width = 9)

        botones_creados.append(boton)

        boton.grid(row = 0, column = columnas)

        columnas += 1

    botones_creados[0].config(command= total)
    botones_creados[1].config(command= recibo)
    botones_creados[2].config(command= guardar)
    botones_creados[3].config(command= resetear)

    # Area de Recibo
    texto_recibo = Text(panel_recibo,
                        font=("Dosis", 12, "bold"),
                        bd= 1,
                        width= 50,
                        height= 10)

    texto_recibo.grid(row = 0, column= 0, columnspan=20)


    # Calculadora
    visor_calculadora = Entry(panel_calculadora,
                              font=('Dosis', 16, 'bold'),
                              width=38,
                              bd=1)

    visor_calculadora.grid(row=0, column=0, columnspan=40)

    # Calculadora Botones
    botones_calculadora = ["7", "8", "9", "+", "4", "5", "6", "-",
                           "1", "2", "3", "x","R", "B", "0", "/"]
    botones_guardados = []

    fila = 1
    columna = 0
    for texto in botones_calculadora:
        boton = Button(panel_calculadora,
                       text=texto,
                       font=('Dosis', 16, 'bold'),
                       fg='white',
                       bg='azure4',
                       bd=1,
                       width=8)

        boton.grid(row=fila, column=columna, padx=1, pady=1)
        botones_guardados.append(boton)

        columna += 1
        if columna == 4:
            columna = 0
            fila += 1


    botones_guardados[0].config(command=lambda : click_boton("7"))
    botones_guardados[1].config(command=lambda : click_boton("8"))
    botones_guardados[2].config(command=lambda : click_boton("9"))
    botones_guardados[3].config(command=lambda : click_boton("+"))
    botones_guardados[4].config(command=lambda : click_boton("4"))
    botones_guardados[5].config(command=lambda : click_boton("5"))
    botones_guardados[6].config(command=lambda : click_boton("6"))
    botones_guardados[7].config(command=lambda : click_boton("-"))
    botones_guardados[8].config(command=lambda : click_boton("1"))
    botones_guardados[9].config(command=lambda : click_boton("2"))
    botones_guardados[10].config(command=lambda : click_boton("3"))
    botones_guardados[11].config(command=lambda : click_boton("*"))
    botones_guardados[12].config(command=obtener_resultado)
    botones_guardados[13].config(command=borrar)
    botones_guardados[14].config(command=lambda : click_boton("0"))
    botones_guardados[15].config(command=lambda : click_boton("/"))


    # Evitar que la pantalla se cierre
    aplicacion.mainloop()


# Dia 13
def asistente_personal():
    import datetime
    import pyttsx3  # Texto a Voz
    import speech_recognition as sr  # Voz a Texto
    import pywhatkit  # Buscar en internet
    import yfinance as yf  # Consultar la Bolsa
    import pyjokes  # Chistes
    import webbrowser  # Navegar en Internet
    import wikipedia  # Wikipedia

    # Escuchar nuestro microfono y devolver el audio como texto.
    def transformar_audio_en_texto():

        # Almacenar recognizer en variable
        r = sr.Recognizer()

        # Configurar el microfono
        with sr.Microphone() as origen:

            # Tiempo de espera
            r.pause_threshold = 0.8

            # Informar que comenzo la grabacion
            print("")
            print("🗣️⏐ Ya puedes hablar.")

            # Guardar lo que escuche como audio
            audio = r.listen(origen)

            try:
                # Buscar en google
                pedido = r.recognize_google(audio, language="es-ES")

                # Prueba de que pudo ingresar
                print(f"🎤⏐ Se ha grabado: {pedido}")

                # Devolver pedido
                return pedido

            # En caso de que no comprenda el audio
            except sr.UnknownValueError:

                # Prueba de que no comprendio el

                # Devolver error
                return "Sigo esperando"

            except sr.RequestError:

                # Prueba de que no comprendio el audio
                print("🚨⏐ No hay servicio de internet.")

                # Devolver error
                return "Sigo esperando"

            # Eror inesperado
            except:
                # Prueba de que no comprendio el audio
                print("🚨⏐ Algo ha salido mal.")

                # Devolver error
                return "Sigo esperando"

    # Funcion para que el asistente pueda ser escuchado
    # Descargar voces externas: https://support.microsoft.com/es-es/topic/descargar-idiomas-y-voces-para-lector-inmersivo-el-modo-lectura-y-lectura-en-voz-alta-4c83a8d8-7486-42f7-8e46-2b0fdf753130
    def hablar(mensaje):

        # Encender el motor de pyttsx3
        engine = pyttsx3.init()
        # engine.setProperty("voices", "id de la voz") (Setear las voces)

        # Pronunciar el mensaje
        engine.say(mensaje)
        engine.runAndWait()

    # Informar el dia de la semana
    def pedir_dia():

        # Crear varible con datos de hoy
        dia = datetime.datetime.today()

        # Crear una variable para el día de semana
        dia_semana = dia.weekday()

        # Diccionario con nombres de días
        calendario = {0: "Lunes",
                      1: "Martes",
                      2: "Miércoles",
                      3: "Jueves",
                      4: "Viernes",
                      5: "Sábado",
                      6: "Domingo"}

        # Decir el día de la semana
        hablar(f"Hoy es {calendario[dia_semana]}")

    # Informar de que hora es
    def pedir_hora():

        # Crear varible con datos de la hora
        hora = datetime.datetime.now()
        hora = f"En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos."

        # Decir la hora
        hablar(hora)

    # Funcion Saludo Incial
    def saludo_inicial():

        # Crear Variable con datos de hora
        hora = datetime.datetime.now()
        if hora.hour < 6 or hora.hour > 20:
            momento = "Buenas noches"

        elif 6 <= hora.hour < 13:
            momento = "Buen día"

        else:
            momento = "Buenas tardes"

        # Decir el saludo
        hablar(f"{momento}, soy tu asistente personal. Por favor, dime en qué te puedo ayudar.")

    # Funcion central del asistente
    def pedir_cosas():

        # Acticar saludo inicial
        saludo_inicial()

        # Variable de corte
        comenzar = True

        # Loop central
        while comenzar:

            # Activar el micro y guardar el pedido en un string
            pedido = transformar_audio_en_texto().lower()

            if "abre youtube" in pedido:
                hablar("Con gusto, estoy abriendo youTube,")
                webbrowser.open("https://www.youtube.com")
                continue

            elif "abre navegador" in pedido:
                hablar("Claro, estoy en ello.")
                webbrowser.open("https://www.google.com")
                continue

            elif "qué día es hoy" in pedido:
                pedir_dia()
                continue

            elif "qué hora es" in pedido:
                pedir_hora()
                continue

            elif "busca en wikipedia" in pedido:
                hablar("Buscando eso en wikipedia")
                pedido = pedido.replace("busca en wikipedia", "")
                wikipedia.set_lang("es")
                resultado = wikipedia.summary(pedido, sentences=1)
                hablar(f"Wikpedia dice lo siguiente:{resultado}")
                continue

            elif "busca en internet" in pedido:
                hablar("Ya mismo estoy en buscando")
                pedido = pedido.replace("busca en internet", "")
                pywhatkit.search(pedido)
                hablar("Esto es lo que he encontrado")
                continue

            elif "reproduce" in pedido:
                hablar("Buena idea, ya comienzo a reproducirlo.")
                pywhatkit.playonyt(pedido)
                continue

            elif "broma" in pedido:
                hablar(pyjokes.get_joke("es"))
                continue

            elif "precio de las acciones" in pedido:
                accion = pedido.split("de")[-1].strip()
                cartera = {"apple": "APPL",
                           "amazon": "AMZN",
                           "google": "GOOGL"}
                try:
                    accion_buscada = cartera[accion]
                    accion_buscada = yf.Ticker(accion_buscada)
                    precio_actual = accion_buscada.info["regularMarketPrice"]
                    hablar(f"La he encontrado, el precio de {accion} es {precio_actual}.")
                    continue

                except:
                    hablar("Perdón pero no la he encontrado.")
                    continue

            elif "adiós" in pedido or "chao" in pedido:
                hablar("Me voy a descansar, cualquier cosa me avisas.")
                comenzar = False

            elif "funcionalidades" in pedido or "qué puedes hacer" in pedido:
                hablar("Estoy programada para poder contarte chistes, buscar acciones en la bolsa, reproducir videos en youTube, buscar diferentes cosas en wikipedia, decirte qué día o hora es, abrir el navegador y youtube")

    pedir_cosas()


# Dia 14
def reconocimiento_facial():

    # Librerias / Bibliotecas
    import cv2
    import face_recognition as fr
    import os
    from pathlib import Path
    import numpy
    from datetime import datetime

    # Ruta de Archivos.
    ruta = Path(Path.home(), "Proyectos", "Recursos_14", "Empleados")

    # Crear base de datos
    mis_imagenes = []
    nombres_empleados = []
    lista_empleados = os.listdir(ruta)

    for nombre in lista_empleados:
        imagen_actual = cv2.imread(Path(ruta, nombre))
        mis_imagenes.append(imagen_actual)
        nombres_empleados.append(os.path.splitext(nombre)[0])

    # Codificar imagenes
    def codificar(imagenes):

        # Crear una lista nueva
        lista_codificada = []

        # Pasar todas las imagenes a rgb
        for imagen in imagenes:
            imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

            # Codificar
            codificado = fr.face_encodings(imagen)[0]

            # Agregar a la lista
            lista_codificada.append(codificado)

        # Devolver lista codificada
        return lista_codificada

    # Registrar los ingresos:
    def registrar_ingresos(persona):

        # Abrir hoja de calculo
        f = open(Path(ruta, "Registro.csv"), "r+")  # R+ (abrir y escribir)
        lista_datos = f.readlines()
        nombres_registro = []

        for linea in lista_datos:
            ingreso = linea.split(",")
            nombres_registro.append(ingreso[0])

        if persona not in nombres_registro:
            hora = datetime.now()
            string_ahora = hora.strftime("%H:%M:%S")
            f.writelines(f"\n{persona}, {string_ahora}")

    lista_empleados_codificado = codificar(mis_imagenes)


    # Tomar una imagen de camara web
    captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Capturar imagen

    # Leer imagen de la camara
    exito, imagen = captura.read()  # Devuelve si se ha podido tomar la imagen y la imagen.

    if not exito:
        print("No se ha podido tomar la captura.")

    else:
        # Reconocer cara en captura
        cara_captura = fr.face_locations(imagen)

        # Codificar cara capturada
        cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

        # Buscar coincidencias
        for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
            coincidencias = fr.compare_faces(lista_empleados_codificado, caracodif)
            distancias = fr.face_distance(lista_empleados_codificado, caracodif)

            print(distancias)

            indice_coincidencia = numpy.argmin(distancias)  # Da el numero menor

            # Mostrar coincidencias si las hay
            if distancias[indice_coincidencia] > 0.6:
                print("No coincide con ninguno de nuestros empleados.")

            else:

                # Buscar el nombre del empleado encontrado
                nombre = nombres_empleados[indice_coincidencia]

                # Mostrar rectangulo
                y1, x2, y2, x1 = caraubic
                cv2.rectangle(imagen,
                              (x1, y1),
                              (x2, y2),
                              (0, 255, 0),
                              2)
                cv2.rectangle(imagen,
                              (x1, y2 - 35),
                              (x2, y2),
                              (0, 255, 0),
                              cv2.FILLED)
                cv2.putText(imagen,
                            nombre,
                            (x1 + 6, y2 - 6),
                            cv2.FONT_HERSHEY_COMPLEX,
                            1,
                            (255, 255, 255),
                            2)

                # Registrar ingresos
                registrar_ingresos(nombre)

                # Mostrar la imagen optenida
                cv2.imshow("Imagen Web", imagen)

                # Mantener ventana abierta
                cv2.waitKey(0)


# Dia 15
def machine_learning():
    pass


# Dia 16
def pagina_web():
    import subprocess
    from pathlib import Path
    import os

    ruta = Path(Path.home(), "Proyectos", "Recursos_16", "Pagina_Web")
    comando = "python manage.py runserver"

    os.chdir(ruta)
    inciar_app = subprocess.run(comando, shell= True, capture_output= True, text= True)



