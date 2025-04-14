# Importar Librerias y Ruta de Recursos.
import pygame
import random
Recursos = "C:\\Users\\Ruben\\Desktop\\Python\\Curso-Python\\Dia 10\\Recursos\\"

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

# Variables del Jugador
img_Jugador = pygame.image.load(f"{Recursos}cohete.png")
Jugador_x = 368 # Eje X
Jugador_y = 500 # Eje Y
Jugador_x_cambio = 0

# Variables del Enemigo
img_Enemigo = pygame.image.load(f"{Recursos}enemigo.png")
Enemigo_x = random.randint(0, 736) # Eje X
Enemigo_y = random.randint(50,200) # Eje Y
Enemigo_x_cambio = 0.3
Enemigo_y_cambio = 50

# Función del Jugador
def Jugador(eje_x, eje_y):
    Pantalla.blit(img_Jugador,(eje_x, eje_y)) # .blit() es el metodo arrojar en la pantalla.

# Función del Enemigo
def Enemigo(eje_x, eje_y):
    Pantalla.blit(img_Enemigo,(eje_x, eje_y)) # .blit() es el metodo arrojar en la pantalla.

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

    # Modificar la ubicacion del Enemigo
    Enemigo_x += Enemigo_x_cambio

    # Mantener dentro de los Bordes al Enemigo
    if Enemigo_x <= 0:
        Enemigo_x_cambio = 0.3
        Enemigo_y += Enemigo_y_cambio
    elif Enemigo_x >= 736:
        Enemigo_x_cambio = -0.3
        Enemigo_y += Enemigo_y_cambio

    # Invocación de variable Jugador
    Jugador(Jugador_x, Jugador_y)

    # Invocación de variable Enemigo
    Enemigo(Enemigo_x, Enemigo_y)

    # Actualizar
    pygame.display.update()

