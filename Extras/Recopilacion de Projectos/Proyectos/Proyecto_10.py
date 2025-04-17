def Proyecto_10():
    # Importar Librerias y Ruta de Recursos.
    import pygame
    import random
    import math
    import io
    from pygame import mixer # Importar sonidos
    Recursos = "C:\\Users\\Ruben\\Desktop\\Python\\Curso-Python\\Extras\\Recopilacion de Projectos\\Proyectos\\Recursos_10\\"

    # Inicializar el juego
    pygame.init()

    # Crear la pantalla y indicar sus dimensiones.
    Pantalla = pygame.display.set_mode((800, 600))

    # Titulo
    pygame.display.set_caption("Invasión Espacial")

    # Icono
    Icono = pygame.image.load(f"{Recursos}ovni.png")
    pygame.display.set_icon(Icono)

    # Fondo
    Fondo = pygame.image.load(f"{Recursos}fondo.jpg")

    # Musica
    mixer.music.load(f"{Recursos}MusicaFondo.mp3") # Cargar Musica
    mixer.music.set_volume(0.2) # Controlar el volumen (0-1)
    mixer.music.play(-1) # Reproducirlo en bucle

    # Variables del Jugador
    img_Jugador = pygame.image.load(f"{Recursos}cohete.png")
    Jugador_x = 368 # Eje X
    Jugador_y = 500 # Eje Y
    Jugador_x_cambio = 0

    # Variables del Enemigo
    img_Enemigo = []
    Enemigo_x = []
    Enemigo_y = []
    Enemigo_x_cambio = []
    Enemigo_y_cambio = []
    Cantidad_enemigos = 5

    for enemigo in range(Cantidad_enemigos):
        img_Enemigo.append(pygame.image.load(f"{Recursos}enemigo.png"))
        Enemigo_x .append(random.randint(0, 736))  # Eje X
        Enemigo_y.append(random.randint(50,200))  # Eje Y
        Enemigo_x_cambio.append(0.3)
        Enemigo_y_cambio.append(50)

    # Transformar el Nombre de la Fuente a Bytes
    def fuente_bytes(fuente):
        with open(fuente, "rb") as f:
            ttf_bytes = f.read()
        return io.BytesIO(ttf_bytes)

    # Variables de la Bala
    Balas = []
    img_bala = pygame.image.load(f"{Recursos}bala.png")
    Bala_x = 0 # Eje X
    Bala_y = 500 # Eje Y
    Bala_x_cambio = 0
    Bala_y_cambio = 1
    Bala_visible = False

    # Variable Puntaje
    Puntaje = 0
    Fuente_como_Bytes = fuente_bytes(f"{Recursos}SpecialElite.ttf")
    Fuente = pygame.font.Font(f"{Recursos}SpecialElite.ttf", 32) # Tipo de fuente que aparece en pantalla
    Texto_x = 10
    Texto_y = 10

    # Variable Fin
    Fuente_Fin = pygame.font.Font(f"{Recursos}SpecialElite.ttf", 40) # Tipo de fuente que aparece en pantalla
    Texto_Fin_x = 400
    Texto_Fin_y = 300

    # Función Monstrar Puntaje
    def Monstrar_puntaje(eje_x, eje_y):
        Texto = Fuente.render(f"Puntaje: {Puntaje}", True, (255,255,255)) # Renderizar puntaje
        Pantalla.blit(Texto, (eje_x ,eje_y)) # Monstrar Puntaje

    # Función Fin del Juego
    def Monstrar_Fin():
        Texto = Fuente.render(f"Juego Terminado", True, (255,255,255)) # Renderizar puntaje
        Pantalla.blit(Texto, (60, 200)) # Monstrar Puntaje

    # Función del Jugador
    def Jugador(eje_x, eje_y):
        Pantalla.blit(img_Jugador,(eje_x, eje_y)) # .blit() es el metodo arrojar en la pantalla.

    # Función del Enemigo
    def Enemigo(eje_x, eje_y, ene):
        Pantalla.blit(img_Enemigo[ene],(eje_x, eje_y)) # .blit() es el metodo arrojar en la pantalla.

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
    se_ejecuta = True # Variable que mantiene el juego ejecutandose.
    while se_ejecuta:

        # Imagen de Fondo.
        Pantalla.blit(Fondo,(0,0))

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
                    Sonido_bala = mixer.Sound(f"{Recursos}disparo.mp3") # Cargar la música
                    Sonido_bala.play() # Reproducirla
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
                colision_bala_enemigo = Detectar_colisiones(Enemigo_x[enemigo], Enemigo_y[enemigo], bala["x"], bala["y"])
                if colision_bala_enemigo:
                    sonido_colision = mixer.Sound(f"{Recursos}Golpe.mp3")
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

Proyecto_10()