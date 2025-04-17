# Importar Días
from Proyectos import Proyecto_1
"""from Proyectos import Proyecto_2
from Proyectos import Proyecto_3
from Proyectos import Proyecto_4
from Proyectos import Proyecto_5
from Proyectos import Proyecto_6
from Proyectos import Proyecto_7
from Proyectos import Principal_8
from Proyectos import Numeros_8
from Proyectos import Proyecto_9
from Proyectos import Proyecto_10
from Proyectos import Proyecto_11"""

# Librerias
import datetime
from os import system

# Dia de hoy
Fecha = datetime.date.today()
Dia_Hoy = f"{Fecha.day}/{Fecha.month}/{Fecha.year}"


# Función de Pedir
def Presentacion(negrita, subrayado):
    print(f"¡Bienvenido/a de Nuevo! ({Dia_Hoy})")
    print(f'Este Proyecto es una recopilación de los proyectos de {negrita} durante su formación en "Python Total".')
    print("Durante su desarrollo en este curso, realizó 16 proyectos, que seran mencionados a continuación:")
    print("")
    print(f"Día 1: {Data_1.titulo}")
    print(f"Día 2: {Data_2.titulo}")
    print(f"Día 3: {Data_3.titulo}")
    print(f"Día 4: ")
    print(f"Día 5: ")
    print(f"Día 6: ")
    print(f"Día 7: ")
    print(f"Día 8: ")
    print(f"Día 9: ")
    print(f"Día 10: ")
    print(f"Día 11: ")
    print(f"Día 12: ")
    print(f"Día 13: ")
    print(f"Día 14: ")
    print(f"Día 15: ")
    print(f"Día 16: ")
    print("")
    Pregunta = input(f"{subrayado} ")
    while Pregunta not in Lista_de_Verificacion:
        print("")
        print("🚨⏐ Por favor, introduzca el Nombre del Proyecto Correctamente.")
        print("")
        Pregunta = input(f"{negrita} ")
    return Pregunta


# Función Preguntar de Volver
def Volver_preguntar():
    pass

# Funcion Limpiar Pantalla
def Limpiar_pantalla():
    system("cls")

# Función Negrita [\033[1m → Negrita, \033[3m → Cursiva, \033[4m → Subrayado, \033[0m → Reset (vuelve al estilo normal]
def negrita_y_subrayado(texto):
    return f"\033\033[4m{texto}\033[0m"


# Función Subrayado [\033[1m → Negrita, \033[3m → Cursiva, \033[4m → Subrayado, \033[0m → Reset (vuelve al estilo normal]
def negrita(texto):
    return f"\033[1m{texto}\033[0m"


# Descripcion
def Descripcion(dia, fecha, descripcion, etiqueta):
    print(f"Este es el projecto del {dia}:")
    print("")
    print(f"Descripcion: {fecha}")
    print("")
    print(f"Este projecto trata sobre: {descripcion}")
    print("")
    print(f"Las etiquetas de este projecto son: {etiqueta}")
    print("")


# Clase del Proyecto
class Proyectos:
    def __init__(self, titulo, descripcion, etiqueta, fecha, dia):
        self.titulo = titulo
        self.descripcion = descripcion
        self.etiqueta = etiqueta
        self.fecha = fecha
        self.dia = dia


# Data de Proyectos
Data_1 = Proyectos("Creador de Nombres","Vas a crear un código en Python que le pida a tu amigo que responda\ndos preguntas que requieran una sola palabra cada una y que luego\nle muestre en pantalla esas palabras combinadas para formar una marca creativa.", "#Python", "19/03/2025", "Día 1")
Data_2 = Proyectos("Calculador de Comisiones","La situación es esta: tú trabajas en una empresa donde los vendedores reciben comisiones\ndel 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus\ncomisiones creando un programa que les pregunte su nombre y cuánto han vendido en este\nmes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le\ncorresponde por las comisiones.", "#Python", "20/03/2025", "Día 2")
Data_3 = Proyectos("Analizador de Textos", "La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que\ningrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un\npoema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres\nletras a su elección y a partir de ese momento nuestro código va a procesar esa información\n para hacer cinco tipos de análisis.", "#Python", "22/03/2025", "Día 3")


# Variables / Listas
Lista_de_Verificacion = [Data_1.titulo]
Bucle = True


# Ejecucion del Codigo
Respuesta = Presentacion(negrita_y_subrayado("Rubén Blasco Armengod"), negrita("¿Que projecto desea ejecutar?"))

if Respuesta == "Creador de Nombres":
    Limpiar_pantalla()
    Descripcion(Data_1.dia, Data_1.fecha, Data_1.descripcion, Data_1.etiqueta)
    Proyecto_1.Nombre_Cerveza()
    Volver_preguntar()

