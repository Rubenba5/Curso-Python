# Clase del Proyecto
class Proyectos:
    def __init__(self, titulo, descripcion, etiqueta, fecha, dia, numero):
        self.titulo = titulo
        self.descripcion = descripcion
        self.etiqueta = etiqueta
        self.fecha = fecha
        self.dia = dia
        self.numero = numero


# Data de Proyectos
Data_1 = Proyectos("Creador de Nombres",
    "Vas a crear un código en Python que le pida a tu amigo\n"
    "que responda dos preguntas con una sola palabra cada una,\n"
    "y luego le muestre esas palabras combinadas como una marca creativa.",
    "#Python, #Input, #String", "19/03/2025", "Día 1", "1")

Data_2 = Proyectos("Calculador de Comisiones",
    "Trabajas en una empresa donde los vendedores reciben\n"
    "comisiones del 13%. Crea un programa que les pida su nombre\n"
    "y cuánto han vendido este mes, y que muestre el monto de su comisión.",
    "#Python, #Input, #Float, #Format", "20/03/2025", "Día 2", "2")

Data_3 = Proyectos("Analizador de Textos",
    "Pide al usuario un texto cualquiera y tres letras.\n"
    "El programa hará cinco análisis diferentes sobre ese texto\n"
    "usando las letras proporcionadas como base.",
    "#Python, #String, #Input, #TextAnalysis", "22/03/2025", "Día 3", "3")

Data_4 = Proyectos("Adivina el Número",
    "El jugador debe adivinar un número entre 1 y 100\n"
    "en un máximo de ocho intentos. Se le dan pistas\n"
    "según el número que ingrese en cada intento.",
    "#Python, #Random, #While, #Game", "27/03/2025", "Día 4", "4")

Data_5 = Proyectos("El Ahorcado",
    "El programa elige una palabra secreta y muestra guiones.\n"
    "El jugador intenta adivinar letras. Si acierta, se revelan;\n"
    "si falla, pierde una vida. Gana si adivina toda la palabra.",
    "#Python, #Game, #Loops, #Conditions", "02/04/2025", "Día 5", "5")

Data_6 = Proyectos("Recetario",
    "El programa da la bienvenida, muestra cuántas recetas hay\n"
    "y en qué carpeta están. Luego permite elegir entre distintas\n"
    "opciones para ver o gestionar recetas.",
    "#Python, #Os, #Filesystem", "04/04/2025", "Día 6", "6")

Data_7 = Proyectos("Cuenta Bancaria",
    "Crea una clase Cliente con métodos para imprimir sus datos,\n"
    "depositar dinero y retirar fondos. Simula una cuenta bancaria\n"
    "con operaciones básicas.",
    "#Python, #POO, #Métodos, #Clases", "10/04/2025", "Día 7", "7")

Data_8 = Proyectos("Consola de Turnos",
    "Simula un sistema de turnos para perfumería, farmacia y cosméticos.\n"
    "El cliente elige el área y se le asigna un turno como P-01, F-32, etc.\n"
    "El proceso se repite para nuevos clientes.",
    "#Python, #Condicionales, #Simulación, #Interacción", "13/04/2025", "Día 8", "8")

Data_9 = Proyectos("Buscador de Números en Serie",
    "Busca números de serie con formato específico en archivos .txt.\n"
    "Usa expresiones regulares, recorre carpetas, muestra hallazgos\n"
    "en consola y calcula el tiempo total de búsqueda.",
    "#Python, #Regex, #Os, #Datetime, #Automatización", "14/02/2025", "Día 9", "9")

Data_10 = Proyectos("Invasión Espacial",
    "Juego al estilo Space Invaders con Pygame.\n"
    "Controla una nave, dispara a enemigos, evita que lleguen al fondo.\n"
    "Incluye efectos de sonido y sistema de puntaje.",
    "#Python, #Pygame, #Juego2D, #Animaciones, #Colisiones", "17/04/2025", "Día 10", "10")

Data_11 = Proyectos("Scraping de Libros",
    "Hace scraping de 'Books to Scrape' usando requests y BeautifulSoup.\n"
    "Extrae títulos de libros con 4 o 5 estrellas recorriendo las 50 páginas.\n"
    "Filtra, analiza HTML y muestra resultados por consola.",
    "#Python, #WebScraping, #BeautifulSoup, #Requests", "21/04/2025", "Día 11", "11")

Data_12 = Proyectos("Gestor de Restaurantes",
    "Sistema de facturación con interfaz gráfica (Tkinter).\n"
    "Permite seleccionar productos, calcular totales e impuestos,\n"
    "guardar recibos y usar una calculadora integrada.",
    "#Python, #Tkinter, #InterfazGráfica, #Facturación, #GUI", "22/04/2025", "Día 12", "12")

Data_13 = Proyectos("Asistente Personal",
    "Asistente virtual por voz que entiende comandos y responde con voz.\n"
    "Puede decir la hora, abrir páginas, buscar en Wikipedia y más.\n"
    "Usa speech_recognition, pyttsx3, y otras librerías útiles.",
    "#Python, #AsistenteVirtual, #ReconocimientoVoz, #pyttsx3, #speechrecognition", "02/05/2025", "Día 13", "13")

Data_14 = Proyectos("Reconocimiento Facial",
    "Captura imagen con webcam, compara rostros con base de empleados,\n"
    "y registra nombre y hora si hay coincidencia. Usa OpenCV y face_recognition.",
    "#Python, #ReconocimientoFacial, #OpenCV, #face_recognition","02/05/2025", "Día 14", "14")

Data_15 = Proyectos("Machine Learning - Titanic",
    "Analiza el dataset del Titanic usando árboles de decisión.\n"
    "Predice supervivencia según sexo, edad y clase.\n"
    "Incluye limpieza de datos, métricas, visualización y análisis.",
    "#Python, #MachineLearning, #ÁrbolDeDecisión, #Titanic, #ScikitLearn", "03/05/2025", "Día 15", "15")

Data_16 = Proyectos("Aplicación Web de Tareas",
    "App web para gestionar tareas personales con Django.\n"
    "Incluye login, CRUD, filtro de tareas, contador y diseño con HTML y CSS.\n"
    "Cada usuario solo ve y modifica sus propias tareas.",
    "#Python, #Django, #ToDoApp, #CRUD, #Login, #HTML, #CSS", "04/05/2025", "Día 16", "16")


# Importar Interfaz Gráfica
from tkinter import *

# Iniciar tkinter
aplicacion = Tk()

# Dimensiones de la aplicación
aplicacion.geometry("1025x700+0+0")

# No Maximizar
aplicacion.resizable(False, False)

# Título / Fondo
aplicacion.title("Recopilación de Proyectos - Rubén Blasco Armengod")

# Panel Arriba
panel_arriba = Frame(aplicacion, bd= 0, relief= "raised")

# Frame Izquierdo
panel_izquierdo = Frame(aplicacion, bd=0, relief="raised")
panel_izquierdo.pack(side="left", fill= "x")

# Frame Derecho
panel_derecho = Frame(aplicacion, bd= 1, relief="raised")
panel_derecho.pack(side="right", padx=48)

# Panel Texto
panel_texto = Frame(panel_izquierdo, bd= 0, relief="raised")
panel_texto.pack(side= "top")

# Panel Scrollbar
panel_scrollbar = Frame(panel_izquierdo, bd= 0, relief= "raised")
panel_scrollbar.pack(fill= "both")

# Panel Boton
panel_boton = Frame(panel_izquierdo, bd= 0, relief= "raised")
panel_boton.pack(side= "bottom")

# Título
etiqueta_titulo = Label(panel_texto,
                        text="¡Bienvenido de Nuevo!",
                        fg="black",
                        font=("NotoSansCJKTC", 20),
                        width=20)

etiqueta_titulo.grid(row=3, column=0)

# Descripción
etiqueta_descripcion = Label(panel_texto,
                             text='Elige un proyecto para ejecutar',
                             fg="black",
                             font=("NotoSansCJKTC", 13),
                             width=30)

etiqueta_descripcion.grid(row=6, column=0)

# Listbox
listbox = Listbox(panel_izquierdo,
                  width=20,
                  selectbackground= "GhostWhite",
                  selectforeground= "black",
                  font=("NotoSansCJKTC", 10),
                  height= 17)


# Agregar elementos al Listbox
listbox.insert(END, f"{Data_1.dia}: {Data_1.titulo}")
listbox.insert(END, f"{Data_2.dia}: {Data_2.titulo}")
listbox.insert(END, f"{Data_3.dia}: {Data_3.titulo}")
listbox.insert(END, f"{Data_4.dia}: {Data_4.titulo}")
listbox.insert(END, f"{Data_5.dia}: {Data_5.titulo}")
listbox.insert(END, f"{Data_6.dia}: {Data_6.titulo}")
listbox.insert(END, f"{Data_7.dia}: {Data_7.titulo}")
listbox.insert(END, f"{Data_8.dia}: {Data_8.titulo}")
listbox.insert(END, f"{Data_9.dia}: {Data_9.titulo}")
listbox.insert(END, f"{Data_10.dia}: {Data_10.titulo}")
listbox.insert(END, f"{Data_11.dia}: {Data_11.titulo}")
listbox.insert(END, f"{Data_12.dia}: {Data_12.titulo}")
listbox.insert(END, f"{Data_13.dia}: {Data_13.titulo}")
listbox.insert(END, f"{Data_14.dia}: {Data_14.titulo}")
listbox.insert(END, f"{Data_15.dia}: {Data_15.titulo}")
listbox.insert(END, f"{Data_16.dia}: {Data_16.titulo}")
listbox.insert(END, f"⮞ Información sobre el curso")


listbox.pack(fill= "both", pady= 20, padx= 48)



# Selelecion
selecciones = listbox.curselection()

for selecion in selecciones:
    nombre = listbox.get(selecion)

def borrar_panel_derecho():
    if panel_derecho.winfo_children():
        for label in panel_derecho.winfo_children():
            label.destroy()

# Funcion Boton
def boton():

    # Capturar la selección actual del Listbox
    selecciones = listbox.curselection()

    # Verificar si hay al menos un elemento seleccionado
    if selecciones:
        nombre = listbox.get(selecciones[0])  # Solo tomamos el primer seleccionado

        if Data_1.titulo in nombre:
            borrar_panel_derecho()

            proyecto_titulo = Label(panel_derecho,
                                    text=nombre,
                                    fg="black",
                                    font=("NotoSansCJKTC", 13),
                                    width=30)
            proyecto_titulo.grid(row=0, column=0)

            proyecto_descripcion = Label(panel_derecho,
                                         text=Data_1.descripcion,
                                         fg="black",
                                         font=("NotoSansCJKTC", 11),
                                         width=60)
            proyecto_descripcion.grid(row=1, column=0, padx=10, pady=20)

            proyecto_etiquetas = Label(panel_derecho,
                                       text=Data_1.etiqueta,
                                       fg="black",
                                       font=("NotoSansCJKTC", 11),
                                       width=60)
            proyecto_etiquetas.grid(row=3, column=0)

        elif Data_2.titulo in nombre:
            borrar_panel_derecho()

            proyecto_titulo = Label(panel_derecho,
                                    text=nombre,
                                    fg="black",
                                    font=("NotoSansCJKTC", 13),
                                    width=30)
            proyecto_titulo.grid(row=0, column=0)

            proyecto_descripcion = Label(panel_derecho,
                                         text=Data_2.descripcion,
                                         fg="black",
                                         font=("NotoSansCJKTC", 11),
                                         width=0)
            proyecto_descripcion.grid(row=1, column=0, padx=10, pady=20)

            proyecto_etiquetas = Label(panel_derecho,
                                       text=Data_2.etiqueta,
                                       fg="black",
                                       font=("NotoSansCJKTC", 11),
                                       width=60)
            proyecto_etiquetas.grid(row=3, column=0)

        elif Data_3.titulo in nombre:
            borrar_panel_derecho()

            proyecto_titulo = Label(panel_derecho,
                                    text=nombre,
                                    fg="black",
                                    font=("NotoSansCJKTC", 13),
                                    width=30)
            proyecto_titulo.grid(row=0, column=0)

            proyecto_descripcion = Label(panel_derecho,
                                         text=Data_3.descripcion,
                                         fg="black",
                                         font=("NotoSansCJKTC", 11),
                                         width=0)
            proyecto_descripcion.grid(row=1, column=0, padx=10, pady=20)

            proyecto_etiquetas = Label(panel_derecho,
                                       text=Data_3.etiqueta,
                                       fg="black",
                                       font=("NotoSansCJKTC", 11),
                                       width=60)
            proyecto_etiquetas.grid(row=3, column=0, padx=10)

        elif Data_4.titulo in nombre:
            borrar_panel_derecho()

            proyecto_titulo = Label(panel_derecho,
                                    text=nombre,
                                    fg="black",
                                    font=("NotoSansCJKTC", 13),
                                    width=30)
            proyecto_titulo.grid(row=0, column=0)

            proyecto_descripcion = Label(panel_derecho,
                                         text=Data_4.descripcion,
                                         fg="black",
                                         font=("NotoSansCJKTC", 11),
                                         width=0)
            proyecto_descripcion.grid(row=1, column=0, padx=10, pady=20)

            proyecto_etiquetas = Label(panel_derecho,
                                       text=Data_4.etiqueta,
                                       fg="black",
                                       font=("NotoSansCJKTC", 11),
                                       width=60)
            proyecto_etiquetas.grid(row=3, column=0, padx=10)

        elif Data_5.titulo in nombre:
            borrar_panel_derecho()

            proyecto_titulo = Label(panel_derecho,
                                    text=nombre,
                                    fg="black",
                                    font=("NotoSansCJKTC", 13),
                                    width=30)
            proyecto_titulo.grid(row=0, column=0)

            proyecto_descripcion = Label(panel_derecho,
                                         text=Data_5.descripcion,
                                         fg="black",
                                         font=("NotoSansCJKTC", 11),
                                         width=0)
            proyecto_descripcion.grid(row=1, column=0, padx=10, pady=20)

            proyecto_etiquetas = Label(panel_derecho,
                                       text=Data_5.etiqueta,
                                       fg="black",
                                       font=("NotoSansCJKTC", 11),
                                       width=60)
            proyecto_etiquetas.grid(row=3, column=0, padx=10)

        elif Data_6.titulo in nombre:
            borrar_panel_derecho()

            proyecto_titulo = Label(panel_derecho,
                                    text=nombre,
                                    fg="black",
                                    font=("NotoSansCJKTC", 13),
                                    width=30)
            proyecto_titulo.grid(row=0, column=0)

            proyecto_descripcion = Label(panel_derecho,
                                         text=Data_6.descripcion,
                                         fg="black",
                                         font=("NotoSansCJKTC", 11),
                                         width=0)
            proyecto_descripcion.grid(row=1, column=0, padx=10, pady=20)

            proyecto_etiquetas = Label(panel_derecho,
                                       text=Data_6.etiqueta,
                                       fg="black",
                                       font=("NotoSansCJKTC", 11),
                                       width=60)
            proyecto_etiquetas.grid(row=3, column=0, padx=10)

        elif Data_7.titulo in nombre:
            borrar_panel_derecho()

            proyecto_titulo = Label(panel_derecho,
                                    text=nombre,
                                    fg="black",
                                    font=("NotoSansCJKTC", 13),
                                    width=30)
            proyecto_titulo.grid(row=0, column=0)

            proyecto_descripcion = Label(panel_derecho,
                                         text=Data_7.descripcion,
                                         fg="black",
                                         font=("NotoSansCJKTC", 11),
                                         width=0)
            proyecto_descripcion.grid(row=1, column=0, padx=10, pady=20)

            proyecto_etiquetas = Label(panel_derecho,
                                       text=Data_7.etiqueta,
                                       fg="black",
                                       font=("NotoSansCJKTC", 11),
                                       width=60)
            proyecto_etiquetas.grid(row=3, column=0, padx=10)

        elif Data_8.titulo in nombre:
            borrar_panel_derecho()

            proyecto_titulo = Label(panel_derecho,
                                    text=nombre,
                                    fg="black",
                                    font=("NotoSansCJKTC", 13),
                                    width=30)
            proyecto_titulo.grid(row=0, column=0)

            proyecto_descripcion = Label(panel_derecho,
                                         text=Data_8.descripcion,
                                         fg="black",
                                         font=("NotoSansCJKTC", 11),
                                         width=0)
            proyecto_descripcion.grid(row=1, column=0, padx=10, pady=20)

            proyecto_etiquetas = Label(panel_derecho,
                                       text=Data_8.etiqueta,
                                       fg="black",
                                       font=("NotoSansCJKTC", 11),
                                       width=60)
            proyecto_etiquetas.grid(row=3, column=0, padx=10)

        elif Data_9.titulo in nombre:
            borrar_panel_derecho()

            proyecto_titulo = Label(panel_derecho,
                                    text=nombre,
                                    fg="black",
                                    font=("NotoSansCJKTC", 13),
                                    width=32)
            proyecto_titulo.grid(row=0, column=0)

            proyecto_descripcion = Label(panel_derecho,
                                         text=Data_9.descripcion,
                                         fg="black",
                                         font=("NotoSansCJKTC", 11),
                                         width=0)
            proyecto_descripcion.grid(row=1, column=0, padx=10, pady=20)

            proyecto_etiquetas = Label(panel_derecho,
                                       text=Data_9.etiqueta,
                                       fg="black",
                                       font=("NotoSansCJKTC", 11),
                                       width=60)
            proyecto_etiquetas.grid(row=3, column=0, padx=10)

        elif Data_10.titulo in nombre:
            borrar_panel_derecho()

            proyecto_titulo = Label(panel_derecho,
                                    text=nombre,
                                    fg="black",
                                    font=("NotoSansCJKTC", 13),
                                    width=30)
            proyecto_titulo.grid(row=0, column=0)

            proyecto_descripcion = Label(panel_derecho,
                                         text=Data_10.descripcion,
                                         fg="black",
                                         font=("NotoSansCJKTC", 11),
                                         width=0)
            proyecto_descripcion.grid(row=1, column=0, padx=10, pady=20)

            proyecto_etiquetas = Label(panel_derecho,
                                       text=Data_10.etiqueta,
                                       fg="black",
                                       font=("NotoSansCJKTC", 11),
                                       width=60)
            proyecto_etiquetas.grid(row=3, column=0, padx=10)

        elif Data_11.titulo in nombre:
            borrar_panel_derecho()

            proyecto_titulo = Label(panel_derecho,
                                    text=nombre,
                                    fg="black",
                                    font=("NotoSansCJKTC", 13),
                                    width=30)
            proyecto_titulo.grid(row=0, column=0)

            proyecto_descripcion = Label(panel_derecho,
                                         text=Data_11.descripcion,
                                         fg="black",
                                         font=("NotoSansCJKTC", 11),
                                         width=0)
            proyecto_descripcion.grid(row=1, column=0, padx=10, pady=20)

            proyecto_etiquetas = Label(panel_derecho,
                                       text=Data_11.etiqueta,
                                       fg="black",
                                       font=("NotoSansCJKTC", 11),
                                       width=60)
            proyecto_etiquetas.grid(row=3, column=0, padx=10)

        elif Data_12.titulo in nombre:
            borrar_panel_derecho()

            proyecto_titulo = Label(panel_derecho,
                                    text=nombre,
                                    fg="black",
                                    font=("NotoSansCJKTC", 13),
                                    width=30)
            proyecto_titulo.grid(row=0, column=0)

            proyecto_descripcion = Label(panel_derecho,
                                         text=Data_12.descripcion,
                                         fg="black",
                                         font=("NotoSansCJKTC", 11),
                                         width=0)
            proyecto_descripcion.grid(row=1, column=0, padx=10, pady=20)

            proyecto_etiquetas = Label(panel_derecho,
                                       text=Data_12.etiqueta,
                                       fg="black",
                                       font=("NotoSansCJKTC", 11),
                                       width=60)
            proyecto_etiquetas.grid(row=3, column=0, padx=10)

        elif Data_13.titulo in nombre:
            borrar_panel_derecho()

            proyecto_titulo = Label(panel_derecho,
                                    text=nombre,
                                    fg="black",
                                    font=("NotoSansCJKTC", 13),
                                    width=30)
            proyecto_titulo.grid(row=0, column=0)

            proyecto_descripcion = Label(panel_derecho,
                                         text=Data_13.descripcion,
                                         fg="black",
                                         font=("NotoSansCJKTC", 11),
                                         width=0)
            proyecto_descripcion.grid(row=1, column=0, padx=10, pady=20)

            proyecto_etiquetas = Label(panel_derecho,
                                       text=Data_13.etiqueta,
                                       fg="black",
                                       font=("NotoSansCJKTC", 11),
                                       width=60)
            proyecto_etiquetas.grid(row=3, column=0, padx=10)

        elif Data_14.titulo in nombre:
            borrar_panel_derecho()

            proyecto_titulo = Label(panel_derecho,
                                    text=nombre,
                                    fg="black",
                                    font=("NotoSansCJKTC", 13),
                                    width=30)
            proyecto_titulo.grid(row=0, column=0)

            proyecto_descripcion = Label(panel_derecho,
                                         text=Data_14.descripcion,
                                         fg="black",
                                         font=("NotoSansCJKTC", 11),
                                         width=0)
            proyecto_descripcion.grid(row=1, column=0, padx=10, pady=20)

            proyecto_etiquetas = Label(panel_derecho,
                                       text=Data_14.etiqueta,
                                       fg="black",
                                       font=("NotoSansCJKTC", 11),
                                       width=60)
            proyecto_etiquetas.grid(row=3, column=0, padx=10)

        elif Data_15.titulo in nombre:
            borrar_panel_derecho()

            proyecto_titulo = Label(panel_derecho,
                                    text=nombre,
                                    fg="black",
                                    font=("NotoSansCJKTC", 13),
                                    width=30)
            proyecto_titulo.grid(row=0, column=0)

            proyecto_descripcion = Label(panel_derecho,
                                         text=Data_15.descripcion,
                                         fg="black",
                                         font=("NotoSansCJKTC", 11),
                                         width=0)
            proyecto_descripcion.grid(row=1, column=0, padx=10, pady=20)

            proyecto_etiquetas = Label(panel_derecho,
                                       text=Data_15.etiqueta,
                                       fg="black",
                                       font=("NotoSansCJKTC", 11),
                                       width=60)
            proyecto_etiquetas.grid(row=3, column=0, padx=10)

        elif Data_16.titulo in nombre:
            borrar_panel_derecho()

            proyecto_titulo = Label(panel_derecho,
                                    text=nombre,
                                    fg="black",
                                    font=("NotoSansCJKTC", 13),
                                    width=30)
            proyecto_titulo.grid(row=0, column=0)

            proyecto_descripcion = Label(panel_derecho,
                                         text=Data_16.descripcion,
                                         fg="black",
                                         font=("NotoSansCJKTC", 11),
                                         width=0)
            proyecto_descripcion.grid(row=1, column=0, padx=10, pady=20)

            proyecto_etiquetas = Label(panel_derecho,
                                       text=Data_16.etiqueta,
                                       fg="black",
                                       font=("NotoSansCJKTC", 11),
                                       width=60)
            proyecto_etiquetas.grid(row=3, column=0, padx=10)


# Boton de Ejecutar
boton_ejecutar = Button(panel_boton,
                        text="Ejecutar",
                        fg="white",
                        bg="azure4",
                        bd= 3,
                        font=("NotoSansCJKTC", 10),
                        width= 10)

boton_ejecutar.grid(row= 9, column= 0)
boton_ejecutar.config(command= boton)


# Iniciar la aplicación
aplicacion.mainloop()



