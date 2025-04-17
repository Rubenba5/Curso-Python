# Librerias


# Importar Días
from Proyectos import *


# Función de Pedir
def iniciarlizar_codigo():
    print()



# Clase del Proyecto (titulo, descripcion, etiqueta, lenguaje usado con # y fecha)
class Proyectos:

    def __init__(self, titulo, descripcion, etiqueta, fecha):
        self.titulo = titulo
        self.descripcion = descripcion
        self.etiqueta = etiqueta
        self.fecha = fecha

# Data de Proyectos
Proyecto_1 = Proyectos("Día 1","Vas a crear un código en Python que le pida a tu amigo que responda\ndos preguntas que requieran una sola palabra cada una y que luego\nle muestre en pantalla esas palabras combinadas para formar una marca creativa.", "#Python", "19/03/2025")


# Ejecucion del Codigo
Proyectos.