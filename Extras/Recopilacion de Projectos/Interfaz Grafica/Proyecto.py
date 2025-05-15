# Funcion de Errores
def errores(error):
    global panel_abajo_derecha
    for elemento in panel_abajo_derecha.winfo_children():
        elemento.destroy()

    etiqueta_titulo_principal2 = Label(panel_abajo_derecha,
                                       text=f"{error}",
                                       fg=COLOR_TITULO,
                                       font=("NotoSansCJKTC", 15),
                                       width=100,
                                       bg=COLOR_PANEL)

    etiqueta_titulo_principal2.pack(side="bottom")


# Flujo de errores
try:

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
                       "Desarrolla un código en Python que pida a tu amigo\n"
                       "responder dos preguntas con una sola palabra cada una,\n"
                       "y luego combine esas palabras para crear una marca única.",
                       "#Python, #Input, #String", "19/03/2025", "Día 1", "1")

    Data_2 = Proyectos("Calculador de Comisiones",
                       "Trabajas en una empresa donde los vendedores reciben\n"
                       "comisiones del 13%. Crea un programa que pida su nombre\n"
                       "y cuánto han vendido este mes, y muestre la comisión total.",
                       "#Python, #Input, #Float, #Format", "20/03/2025", "Día 2", "2")

    Data_3 = Proyectos("Analizador de Textos",
                       "Solicita un texto y tres letras al usuario.\n"
                       "El programa hará cinco análisis sobre el texto,\n"
                       "usando las letras proporcionadas como base de comparación.",
                       "#Python, #String, #Input, #TextAnalysis", "22/03/2025", "Día 3", "3")

    Data_4 = Proyectos("Adivina el Número",
                       "El jugador debe adivinar un número entre 1 y 100\n"
                       "en un máximo de cinco intentos. El programa da pistas\n"
                       "según el número ingresado en cada intento para ayudarlo.",
                       "#Python, #Random, #While, #Game", "27/03/2025", "Día 4", "4")

    Data_5 = Proyectos("El Ahorcado",
                       "El programa elige una palabra secreta y muestra guiones.\n"
                       "El jugador intenta adivinar las letras. Si acierta, se\n"
                       "revelan; si falla, pierde una vida. Gana al completar la palabra.",
                       "#Python, #Game, #Loops, #Conditions", "02/04/2025", "Día 5", "5")

    Data_6 = Proyectos("Recetario",
                       "El programa da la bienvenida, muestra cuántas recetas\n"
                       "existen y en qué carpeta están. Luego permite elegir\n"
                       "diferentes opciones para ver o gestionar recetas disponibles.",
                       "#Python, #Os, #Filesystem", "04/04/2025", "Día 6", "6")

    Data_7 = Proyectos("Cuenta Bancaria",
                       "Crea una clase Cliente con métodos para imprimir datos,\n"
                       "depositar dinero y retirar fondos. Simula una cuenta\n"
                       "bancaria con operaciones básicas de manejo de dinero.",
                       "#Python, #POO, #Métodos, #Clases", "10/04/2025", "Día 7", "7")

    Data_8 = Proyectos("Consola de Turnos",
                       "Simula un sistema de turnos para perfumería, farmacia\n"
                       "y cosméticos. El cliente elige el área y recibe un turno\n"
                       "como P-01, F-32, etc. Este proceso se repite para nuevos clientes.",
                       "#Python, #Condicionales, #Simulación, #Interacción", "13/04/2025", "Día 8", "8")

    Data_9 = Proyectos("Buscador de Números en Serie",
                       "Busca números de serie con formato específico en archivos\n"
                       ".txt. Usa expresiones regulares para recorrer carpetas,\n"
                       "muestra los hallazgos en consola y calcula el tiempo total de búsqueda.",
                       "#Python, #Regex, #Os, #Datetime, #Automatización", "14/02/2025", "Día 9", "9")

    Data_10 = Proyectos("Invasión Espacial",
                        "Juego estilo Space Invaders con Pygame. Controla una nave,\n"
                        "dispara a enemigos, evita que lleguen al fondo. Incluye\n"
                        "efectos de sonido y un sistema de puntaje con retroalimentación.",
                        "#Python, #Pygame, #Juego2D, #Animaciones, #Colisiones", "17/04/2025", "Día 10", "10")

    Data_11 = Proyectos("Scraping de Libros",
                        "Realiza scraping de 'Books to Scrape' con requests y\n"
                        "BeautifulSoup. Extrae títulos de libros con 4 o 5 estrellas,\n"
                        "recorriendo las 50 páginas del sitio y mostrando los resultados.",
                        "#Python, #WebScraping, #BeautifulSoup, #Requests", "21/04/2025", "Día 11", "11")

    Data_12 = Proyectos("Gestor de Restaurantes",
                        "Sistema de facturación con interfaz gráfica (Tkinter).\n"
                        "Permite seleccionar productos, calcular totales e impuestos,\n"
                        "guardar recibos y usar una calculadora integrada para las operaciones.",
                        "#Python, #Tkinter, #InterfazGráfica, #Facturación, #GUI", "22/04/2025", "Día 12", "12")

    Data_13 = Proyectos("Asistente Personal",
                        "Asistente virtual por voz que entiende comandos y responde\n"
                        "con voz. Puede decir la hora, abrir páginas, buscar en Wikipedia,\n"
                        "y realizar varias tareas usando librerías como pyttsx3 y speech_recognition.",
                        "#Python, #AsistenteVirtual, #ReconocimientoVoz, #pyttsx3, #speechrecognition", "02/05/2025",
                        "Día 13", "13")

    Data_14 = Proyectos("Reconocimiento Facial",
                        "Captura imágenes con la webcam, compara rostros con una\n"
                        "base de empleados y registra nombre y hora si hay coincidencia.\n"
                        "Usa OpenCV y face_recognition para la identificación precisa.",
                        "#Python, #ReconocimientoFacial, #OpenCV, #face_recognition", "02/05/2025", "Día 14", "14")

    Data_15 = Proyectos("Machine Learning - Titanic",
                        "Analiza el dataset del Titanic usando árboles de decisión.\n"
                        "Predice la supervivencia según variables como sexo, edad y clase.\n"
                        "Incluye limpieza de datos, métricas, visualización y análisis.",
                        "#Python, #MachineLearning, #ÁrbolDeDecisión, #Titanic, #ScikitLearn", "03/05/2025", "Día 15",
                        "15")

    Data_16 = Proyectos("Aplicación Web de Tareas",
                        "Desarrolla una app web para gestionar tareas personales con\n"
                        "Django. Incluye login, CRUD, filtro de tareas y contador. El\n"
                        "diseño usa HTML y CSS, asegurando que cada usuario solo vea sus tareas.",
                        "#Python, #Django, #ToDoApp, #CRUD, #Login, #HTML, #CSS", "04/05/2025", "Día 16", "16")


    # Importar Interfaz Gráfica
    from tkinter import *
    from pathlib import Path
    import Recopilacion

    # Colores Modernos
    COLOR_FONDO = "#F8F9FA"
    COLOR_PANEL = "#FFFFFF"
    COLOR_TITULO = "#343A40"
    COLOR_BOTON = "#168ae2"
    COLOR_BOTON_PULSADO = "#0f6db5"
    COLOR_SELECCION = "#E9ECEF"
    COLOR_TEXTO = "#343A40"


    # Ruta
    ruta = Path(Path.home(), "Proyectos", "Interfaz_Grafica")


    # Iniciar tkinter
    aplicacion = Tk()


    # Dimensiones de la aplicación
    aplicacion.geometry("1000x600+0+0")


    # No Maximizar
    aplicacion.resizable(False, False)


    # Título / Fondo / Icono
    aplicacion.title("Recopilación de Proyectos - Rubén Blasco Armengod")
    aplicacion.config(bg=COLOR_FONDO)
    aplicacion.iconbitmap(Path(ruta, "icono.ico"))


    # Paneles
    panel_arriba = Frame(aplicacion, bd=1, relief="raised", bg=COLOR_PANEL)
    panel_arriba.pack(side="top")

    panel_abajo = Frame(aplicacion, bd=1, relief="raised", bg=COLOR_PANEL)
    panel_abajo.pack(side="bottom")

    panel_abajo_derecha = Frame(panel_abajo, bd=0, relief="raised", bg=COLOR_PANEL)
    panel_abajo_derecha.pack(side="right")

    panel_izquierdo = Frame(aplicacion, bd=0, relief="raised", bg=COLOR_FONDO)
    panel_izquierdo.pack(side="left", fill="x")

    panel_derecho = Frame(aplicacion, bd=1, relief="raised", bg=COLOR_PANEL)
    panel_derecho.pack(side="right", padx=48)

    panel_texto = Frame(panel_izquierdo, bd=0, relief="raised", bg=COLOR_FONDO)
    panel_texto.pack(side="top")

    panel_scrollbar = Frame(panel_izquierdo, bd=0, relief="raised", bg=COLOR_FONDO)
    panel_scrollbar.pack(fill="both")

    panel_boton = Frame(panel_izquierdo, bd=0, relief="raised", bg=COLOR_FONDO)
    panel_boton.pack(side="bottom")


    # Etiquetas
    etiqueta_titulo_principal = Label(panel_arriba,
                                      text="Recopilación de Proyectos - Python Total",
                                      fg=COLOR_TITULO,
                                      font=("NotoSansCJKTC", 15),
                                      width=100,
                                      bg=COLOR_PANEL)

    etiqueta_titulo_principal.pack(side="top")

    etiqueta_titulo_principal2 = Label(panel_abajo_derecha,
                                       text="",
                                       fg=COLOR_TITULO,
                                       font=("NotoSansCJKTC", 15),
                                       width=130,
                                       bg=COLOR_PANEL)

    etiqueta_titulo_principal2.pack(side="bottom")

    etiqueta_titulo = Label(panel_texto,
                            text="¡Bienvenido de Nuevo!",
                            fg=COLOR_TEXTO,
                            font=("NotoSansCJKTC", 20),
                            width=20,
                            bg=COLOR_FONDO)

    etiqueta_titulo.grid(row=3, column=0)

    etiqueta_descripcion = Label(panel_texto,
                                 text='Elige un proyecto para ejecutar',
                                 fg=COLOR_TEXTO,
                                 font=("NotoSansCJKTC", 13),
                                 width=30,
                                 bg=COLOR_FONDO)

    etiqueta_descripcion.grid(row=6, column=0)

    # Listbox
    listbox = Listbox(panel_izquierdo,
                      width=22,
                      height=16,
                      selectbackground= COLOR_SELECCION,
                      selectforeground= COLOR_TITULO,
                      font=("NotoSansCJKTC", 10),
                      bg= COLOR_PANEL,
                      fg= COLOR_TEXTO,
                      bd=1,
                      relief="flat")

    listbox.pack(padx=5, pady=5)

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

    listbox.pack(fill= "both", pady= 20, padx= 48)


    # Selelecion
    selecciones = listbox.curselection()

    for selecion in selecciones:
        nombre = listbox.get(selecion)


    # Borrar Panel
    def borrar_panel_derecho():
        if panel_derecho.winfo_children():
            for label in panel_derecho.winfo_children():
                label.destroy()


    # Descipciones
    def descripciones(dia, fecha, titulo, descripcion, etiqueta, informacion):

        proyecto_titulo = Label(panel_derecho,
                                text= f"{dia}: {titulo}",
                                fg="black",
                                font=("NotoSansCJKTC", 13, "bold"),
                                width=30,
                                bg= COLOR_PANEL)

        proyecto_titulo.grid(row=0, column=0, padx=5, pady=10)

        proyecto_fecha = Label(panel_derecho,
                                text= f"Fecha: {fecha}",
                                fg="black",
                                font=("NotoSansCJKTC", 11),
                                width=30,
                                bg= COLOR_PANEL)

        proyecto_fecha.grid(row=1, column=0, padx=5, pady=5)

        proyecto_descripcion = Label(panel_derecho,
                                     text= f"{descripcion}",
                                     fg="black",
                                     font=("NotoSansCJKTC", 11),
                                     width=60,
                                     bg = COLOR_PANEL)

        proyecto_descripcion.grid(row=2, column=0, padx=5, pady=5)

        proyecto_etiquetas = Label(panel_derecho,
                                   text= f"{etiqueta}",
                                   fg="black",
                                   font=("NotoSansCJKTC", 11),
                                   width=60,
                                   bg=COLOR_PANEL)

        proyecto_etiquetas.grid(row=3, column=0, padx=5, pady=5)

        texto_demonstracion = Text(panel_derecho,
                                   fg= "white",
                                   font=("NotoSansCJKTC", 10, "bold"),
                                   bd=2,
                                   width=65,
                                   height=10,
                                   bg="#181c18")

        texto_demonstracion.grid(row=4, column=0, padx=5, pady=10)
        texto_demonstracion.delete(0.1, END)
        texto_demonstracion.insert(END, f"{informacion}")
        texto_demonstracion.config(state= "disabled")

    """ boton_demonstracion = Button(panel_boton_derecha,
                                text="Demostración",
                                fg="#FFFFFF",
                                bg=COLOR_BOTON,
                                bd=3,
                                font=("NotoSansCJKTC", 10),
                                width=10,
                                activebackground=COLOR_BOTON_PULSADO)

        boton_demonstracion.grid(row=5, column=0)"""



    # Funcion Boton
    def boton():

        # Capturar la selección actual del Listbox
        selecciones = listbox.curselection()

        # Verificar si hay al menos un elemento seleccionado
        if selecciones:
            nombre = listbox.get(selecciones[0])  # Solo tomamos el primer seleccionado

            if Data_1.titulo in nombre:
                borrar_panel_derecho()
                descripciones(Data_1.dia, Data_1.fecha ,Data_1.titulo, Data_1.descripcion, Data_1.etiqueta, Recopilacion.Nombre_Cerveza())

            elif Data_2.titulo in nombre:
                borrar_panel_derecho()
                descripciones(Data_2.dia, Data_2.fecha, Data_2.titulo, Data_2.descripcion, Data_2.etiqueta, Recopilacion.Calculador_impuestos())

            elif Data_3.titulo in nombre:
                borrar_panel_derecho()
                descripciones(Data_3.dia,  Data_3.fecha, Data_3.titulo, Data_3.descripcion, Data_3.etiqueta, Recopilacion.analizador_textos())

            elif Data_4.titulo in nombre:
                borrar_panel_derecho()
                descripciones(Data_4.dia, Data_4.fecha, Data_4.titulo, Data_4.descripcion, Data_4.etiqueta, Recopilacion.numero_aleatorio())

            elif Data_5.titulo in nombre:
                borrar_panel_derecho()
                descripciones(Data_5.dia, Data_5.fecha, Data_5.titulo, Data_5.descripcion, Data_5.etiqueta, Recopilacion.elegir_palabra())

            elif Data_6.titulo in nombre:
                borrar_panel_derecho()
                descripciones(Data_6.dia, Data_6.fecha, Data_6.titulo, Data_6.descripcion, Data_6.etiqueta, Recopilacion.recetario())

            elif Data_7.titulo in nombre:
                borrar_panel_derecho()
                descripciones(Data_7.dia, Data_7.fecha, Data_7.titulo, Data_7.descripcion, Data_7.etiqueta, Recopilacion.cuenta_banco())

            elif Data_8.titulo in nombre:
                borrar_panel_derecho()
                descripciones(Data_8.dia, Data_8.fecha, Data_8.titulo, Data_8.descripcion, Data_8.etiqueta, Recopilacion.elegir_turno())

            elif Data_9.titulo in nombre:
                borrar_panel_derecho()
                descripciones(Data_9.dia, Data_9.fecha, Data_9.titulo, Data_9.descripcion, Data_9.etiqueta, Recopilacion.buscar_numeros())

            elif Data_10.titulo in nombre:
                borrar_panel_derecho()
                descripciones(Data_10.dia, Data_10.fecha, Data_10.titulo, Data_10.descripcion, Data_10.etiqueta, Recopilacion.juego())

            elif Data_11.titulo in nombre:
                borrar_panel_derecho()
                descripciones(Data_11.dia, Data_11.fecha, Data_11.titulo, Data_11.descripcion, Data_11.etiqueta, Recopilacion.web_scraping())

            elif Data_12.titulo in nombre:
                borrar_panel_derecho()
                descripciones(Data_12.dia, Data_12.fecha, Data_12.titulo, Data_12.descripcion, Data_12.etiqueta, Recopilacion.mi_restaurante())

            elif Data_13.titulo in nombre:
                borrar_panel_derecho()
                descripciones(Data_13.dia, Data_13.fecha, Data_13.titulo, Data_13.descripcion, Data_13.etiqueta)

            elif Data_14.titulo in nombre:
                borrar_panel_derecho()
                descripciones(Data_14.dia, Data_14.fecha, Data_14.titulo, Data_14.descripcion, Data_14.etiqueta)

            elif Data_15.titulo in nombre:
                borrar_panel_derecho()
                descripciones(Data_15.dia, Data_15.fecha, Data_15.titulo, Data_15.descripcion, Data_15.etiqueta)

            elif Data_16.titulo in nombre:
                borrar_panel_derecho()
                descripciones(Data_16.dia, Data_16.fecha, Data_16.titulo, Data_16.descripcion, Data_16.etiqueta)


    # Funcion Infomacion
    def informacion():
        borrar_panel_derecho()

        proyecto_titulo = Label(panel_derecho,
                                text= "Información sobre la Recopilación de Proyectos",
                                fg="black",
                                font=("NotoSansCJKTC", 13, "bold"),
                                width=50,
                                bg= COLOR_PANEL)

        proyecto_titulo.grid(row=0, column=0, padx=5, pady=5)



        proyecto_descripcion = Label(panel_derecho,
                                     text= f'Esta interfaz grafica es una recopilación de los proyectos de\nRubén Blasco Armengod durante su formación en "Python Total",\nimpartido por Federico Garay.\n\nEn esta formación realizo 16 proyectos que son mencionados\nen la parte izquierda de su pantalla incluyendo una demostración.\n\n Enlace del Repositorio: https://github.com/Rubenba5/Curso-Python',
                                     fg="black",
                                     font=("NotoSansCJKTC", 11),
                                     width=60,
                                     bg = COLOR_PANEL)
        proyecto_descripcion.grid(row=1, column=0, padx=5, pady=5)

    # Botón de Ejecutar
    boton_ejecutar = Button(panel_boton,
                            text="Ejecutar",
                            fg="#FFFFFF",
                            bg=COLOR_BOTON,
                            bd=3,
                            font=("NotoSansCJKTC", 10),
                            width=10,
                            activebackground=COLOR_BOTON_PULSADO)

    boton_ejecutar.grid(row=9, column=1, padx= 10)
    boton_ejecutar.config(command= boton)

    # Botón de Información
    boton_informacion = Button(panel_boton,
                            text="Información",
                            fg="#FFFFFF",
                            bg= "#c2c3c2",
                            bd=3,
                            font=("NotoSansCJKTC", 10),
                            width=10,
                            activebackground= "#969996")

    boton_informacion.grid(row=9, column=0)
    boton_informacion.config(command= informacion)

    # Iniciar la aplicación
    aplicacion.mainloop()


# Detección de Errores
except SyntaxError:
    print("")
    print("🚨⏐ ¡Error detectado! (SyntaxError)")
    errores("🚨⏐ ¡Error detectado! (SyntaxError)")

except NameError:
    print("")
    print("🚨⏐ ¡Error detectado! (NameError)")
    errores("🚨⏐ ¡Error detectado! (NameError)")

except TypeError:
    print("")
    print("🚨⏐ ¡Error detectado! (TypeError)")
    errores("🚨⏐ ¡Error detectado! (TypeError)")

except ValueError:
    print("")
    print("🚨⏐ ¡Error detectado! (ValueError)")
    errores("🚨⏐ ¡Error detectado! (ValueError)")

except KeyError:
    print("")
    print("🚨⏐ ¡Error detectado! (KeyError)")
    errores("🚨⏐ ¡Error detectado! (KeyError)")

except AttributeError:
    print("")
    print("🚨⏐ ¡Error detectado! (AttributeError)")
    errores("🚨⏐ ¡Error detectado! (AttributeError)")

except ZeroDivisionError:
    print("")
    print("🚨⏐ ¡Error detectado! (ZeroDivisionError)")
    errores("🚨⏐ ¡Error detectado! (ZeroDivisionError)")

except (ModuleNotFoundError, ImportError):
    print("")
    print("🚨⏐ ¡Error detectado! (ImportError / ModuleNotFoundError)")
    errores("🚨⏐ ¡Error detectado! (ImportError / ModuleNotFoundError)")

except FileNotFoundError:
    print("")
    print("🚨⏐ ¡Error detectado! (FileNotFoundError)")
    errores("🚨⏐ ¡Error detectado! (FileNotFoundError)")

except PermissionError:
    print("")
    print("🚨⏐ ¡Error detectado! (PermissionError)")
    errores("🚨⏐ ¡Error detectado! (PermissionError)")

except IOError:
    print("")
    print("🚨⏐ ¡Error detectado! (IOError)")
    errores("🚨⏐ ¡Error detectado! (IOError)")

except RuntimeError:
    print("")
    print("🚨⏐ ¡Error detectado! (RuntimeError)")
    errores("🚨⏐ ¡Error detectado! (RuntimeError)")

# Errores específicos de Tkinter
except tkinter.TclError:
    print("")
    print("🚨⏐ ¡Error detectado! (Tkinter TclError)")
    errores("🚨⏐ ¡Error detectado! (Tkinter TclError)")

