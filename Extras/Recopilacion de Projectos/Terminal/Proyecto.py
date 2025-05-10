# Indicaciones:
# Los recursos comprimidos, hay que descomprimirlos en la ruta base de tu ordenador, en mi caso: "C:\Users\Ruben".
# Los archivos "Proyecto.py" y "Recopilacion.py" tienen que estar en el mismo directorio.
# Debes activar en este archivo la cualidad llamada "Emulate Terminal In Output Console".


# Importar Días
import Recopilacion


# Librerias
import datetime
from os import system

# Dia de hoy
Fecha = datetime.datetime.now()
Dia_Hoy = f"{Fecha.day}/{Fecha.month}/{Fecha.year}"


# Función de Pedir
def Presentacion():
    print(f"¡Bienvenido/a de Nuevo! ({Dia_Hoy})")
    print(f'Este Proyecto es una recopilación de los proyectos de {negrita_y_subrayado("Rubén Blasco Armengod")} durante su formación en "Python Total".')
    print("Durante su desarrollo en este curso, realizó 16 proyectos, que son mencionados a continuación:")
    print("")
    print(f"Día 1: {Data_1.titulo}")
    print(f"Día 2: {Data_2.titulo}")
    print(f"Día 3: {Data_3.titulo}")
    print(f"Día 4: {Data_4.titulo}")
    print(f"Día 5: {Data_5.titulo}")
    print(f"Día 6: {Data_6.titulo}")
    print(f"Día 7: {Data_7.titulo}")
    print(f"Día 8: {Data_8.titulo}")
    print(f"Día 9: {Data_9.titulo}")
    print(f"Día 10: {Data_10.titulo}")
    print(f"Día 11: {Data_11.titulo}")
    print(f"Día 12: {Data_12.titulo}")
    print(f"Día 13: {Data_13.titulo}")
    print(f"Día 14: {Data_14.titulo}")
    print(f"Día 15: {Data_15.titulo}")
    print(f"Día 16: {Data_16.titulo}")
    print("")
    Pregunta = input(f"{negrita("¿Que projecto deseas ejecutar?")} ")

    while Pregunta not in Lista_de_Verificacion:
        print("")
        print("🚨⏐ Por favor, introduzca el Nombre del Proyecto / El Día con su nº / Nº del Proyecto correctamente.")
        print("")
        Pregunta = input(f"{negrita("¿Que projecto deseas ejecutar?")} ")
    return Pregunta


# Funcion Limpiar Pantalla
def Limpiar_pantalla():
    system("cls")


# Función Negrita + Subrayado [\033[1m → Negrita, \033[3m → Cursiva, \033[4m → Subrayado, \033[0m → Reset (vuelve al estilo normal]
def negrita_y_subrayado(texto):
    return f"\033\033[4m{texto}\033[0m"


# Función Subrayado [\033[1m → Negrita, \033[3m → Cursiva, \033[4m → Subrayado, \033[0m → Reset (vuelve al estilo normal]
def negrita(texto):
    return f"\033[1m{texto}\033[0m"


# Descripcion
def Descripcion(dia, fecha, descripcion, etiqueta):
    print(negrita(f"Este es el Proyecto del {dia}:"))
    print("")
    print(f"{negrita("Fecha:")} {fecha}")
    print("")
    print(negrita("Este proyecto trata sobre:"))
    print(f"{descripcion}")
    print("")
    print(f"{negrita("Las etiquetas de este projecto son:")} {etiqueta}")
    print("")
    print(f"{negrita("Demonstración:")}")
    print("")


# Descripcion Día 10
def Descripcion_Modf(dia, fecha, descripcion, etiqueta):
    print(negrita(f"Este es el Proyecto del {dia}:"))
    print("")
    print(f"{negrita("Fecha:")} {fecha}")
    print("")
    print(negrita("Este proyecto trata sobre:"))
    print(f"{descripcion}")
    print("")
    print(f"{negrita("Las etiquetas de este projecto son:")} {etiqueta}")
    print("")
    print(f"{negrita("Demonstración:")}")
    print("Este proyecto se ejecuta en una pestaña diferente.")
    print("")


# Función Preguntar de Volver
def Volver_preguntar():
    print("")
    print("Volver al Menu ⏐ Salir")
    Volver_Preguntar = input(negrita("¿Qué deseas hacer a continuación? "))

    while Volver_Preguntar not in Lista_de_Verificacion_Volver_A_Preguntar:
        print("")
        print('🚨⏐ Por favor, introduzca salir o volver al menu correctamente.')
        print("")
        Volver_Preguntar = input(f"{negrita("¿Qué deseas hacer a continuación? ")} ")

    return Volver_Preguntar


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
Data_1 = Proyectos("Creador de Nombres", "Vas a crear un código en Python que le pida a tu amigo que responda\ndos preguntas que requieran una sola palabra cada una y que luego\nle muestre en pantalla esas palabras combinadas para formar una marca creativa.", "#Python, #Input, #String", "19/03/2025", "Día 1", "1")

Data_2 = Proyectos("Calculador de Comisiones", "La situación es esta: tú trabajas en una empresa donde los vendedores reciben comisiones\ndel 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus\ncomisiones creando un programa que les pregunte su nombre y cuánto han vendido en este\nmes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le\ncorresponde por las comisiones.", "#Python, #Input, #Float, #Format", "20/03/2025", "Día 2", "2")

Data_3 = Proyectos("Analizador de Textos", "La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que\ningrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un\npoema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres\nletras a su elección y a partir de ese momento nuestro código va a procesar esa información\npara hacer cinco tipos de análisis.", "#Python, #String, #Input, #TextAnalysis", "22/03/2025", "Día 3", "3")

Data_4 = Proyectos("Adivina el Número", "el programa le va a preguntar al usuario su nombre, y luego le va a decir\nalgo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos\npara adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un\nnúmero y el programa puede responder cuatro cosas distintas", "#Python, #Random, #While, #Game", "27/03/2025", "Día 4", "4")

Data_5 = Proyectos("El Ahorcado", "El programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una serie\nde guiones que representa la cantidad de letras que tiene la palabra. El jugador en cada turno\ndeberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a\nmostrar en qué lugares se encuentra. Pero si el jugador dice una letra que no se encuentra en\nla palabra oculta, pierde una vida.", "#Python, #Game, #Loops, #Conditions", "02/04/2025", "Día 5", "5")

Data_6 = Proyectos("Recetario", "Este código le va a dar primero la bienvenida al usuario, le va a informar\nla ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas, le va a informar\ncuántas recetas hay en total dentro de esa carpeta, y luego le va a pedir que elija una de\nestas opciones que tenemos aquí.", "#Python, #Os, #Filesystem", "04/04/2025", "Día 6", "6")

Data_7 = Proyectos("Cuenta Bancaria", "El cliente también va a tener tres métodos. El primero va a ser uno de los\nmétodos especiales y es el que permite que podamos imprimir a nuestro cliente. Este método\nva a permitir que cuando el código pida imprimir Cliente, se muestren todos sus datos,\nincluyendo el balance de su cuenta. Luego, un método llamado Depositar, que le va a permitir\ndecidir cuánto dinero quiere agregar a su cuenta. Y finalmente, un tercer método llamado\nRetirar, que le permita decidir cuánto dinero quiere sacar de su cuenta.", "#Python, #POO, #Métodos, #Clases", "10/04/2025", "Día 7", "7")

Data_8 = Proyectos("Consola de Turnos", "Vas a crear el tunero para una farmacia que tiene tres áreas de atención:\nperfumería, farmacia (que es donde venden los medicamentos), y cosméticos. Tu programa le\ntiene que preguntar al cliente a cuál de las áreas desea dirigirse, y le va a dar un número de\nturno según a qué área se dirija. Por ejemplo, si elige cosmética le va a dar el número C-54\n(“C” de cosmética). Luego de eso, nos va a preguntar si queremos sacar otro turno. Esto, en\nrealidad, es para simular si viene un nuevo cliente. Y repetirá todo el proceso.", "#Python, #Condicionales, #Simulación, #Interacción", "13/04/2025", "Día 8", "8")

Data_9 = Proyectos("Buscador de Números en Serie", "Un programa diseñado para buscar números de serie con un formato específico dentro de un árbol de carpetas y archivos .txt.\nEl usuario descomprime una carpeta que contiene subcarpetas y múltiples archivos de texto. Aunque la mayoría del contenido es irrelevante, algunos archivos contienen números de serie válidos.\nEl formato de número de serie buscado es: una letra 'N' seguida de tres caracteres alfabéticos, un guion y cinco números. Ejemplo: Nryu-12365.\nEl programa recorre todas las carpetas y archivos utilizando el módulo os (especialmente el método walk()), y emplea expresiones regulares para detectar los patrones válidos.\nCada hallazgo se muestra en una tabla en consola con la fecha actual, los nombres de los archivos y los números de serie encontrados.\nAdemás, se indica cuántos números se encontraron y cuánto tiempo tomó la búsqueda, redondeando este tiempo hacia arriba.\nSe utilizan los módulos datetime para obtener la fecha en formato dd/mm/aa, y time para calcular la duración.\nEl programa está pensado como un ejercicio práctico para afianzar conocimientos sobre manejo de archivos, estructuras de carpetas, regex y presentación de resultados en consola.", "#Python, #Regex, #Os, #Datetime, #Automatización", "14/02/2025", "Día 9", "9")

Data_10 = Proyectos("Invasión Espacial", "Un juego en Pygame que es una versión del clásico 'Space Invaders'.\nEl jugador controla una nave espacial que puede moverse lateralmente y disparar balas para eliminar enemigos.\nLos enemigos se desplazan horizontalmente y descienden al tocar los bordes de la pantalla.\nSi alguno de ellos llega a la parte inferior, el juego termina.\nSe incluyen efectos de sonido para los disparos y las colisiones, lo cual mejora la experiencia de juego.\nAdemás, se incorpora un sistema de puntaje que se muestra en todo momento, y un mensaje en pantalla indica cuando el juego ha finalizado.", "#Python, #Pygame, #Juego2D, #Animaciones, #Colisiones", "17/04/2025", "Día 10", "10")

Data_11 = Proyectos("Scraping de Libros", "Un proyecto en Python que realiza web scraping en la página 'Books to Scrape'.\nUtiliza las librerías `requests` y `BeautifulSoup` para recorrer automáticamente las 50 páginas del sitio web.\nExtrae e imprime en consola los títulos de los libros que tienen una calificación de 4 o 5 estrellas.\nEste proyecto muestra cómo automatizar la recopilación de datos relevantes desde páginas web estructuradas.\nEs ideal para aprender sobre el análisis de HTML, la navegación por múltiples páginas y el filtrado de información específica.", "#Python, #WebScraping, #BeautifulSoup, #Requests", "21/04/2025", "Día 11", "11")

Data_12 = Proyectos("Gestor de Restaurantes", "Un sistema de facturación completo desarrollado en Python con la librería `tkinter`.\nIncluye una interfaz gráfica que permite seleccionar productos (comidas, bebidas y postres), calcular costos, aplicar impuestos y generar un recibo detallado.\nTambién incorpora una calculadora básica integrada y opciones para guardar el recibo en un archivo de texto.\nSe destacan conceptos como la gestión de estados en widgets, control de eventos con `Checkbutton` y `Entry`, y el uso de `StringVar` para enlazar datos entre la interfaz y la lógica del programa.", "#Python, #Tkinter, #InterfazGráfica, #Facturación, #GUI", "22/04/2025", "Día 12", "12")

Data_13 = Proyectos("Asistente Personal", "Un asistente virtual controlado por voz desarrollado en Python.\nUtiliza `speech_recognition` para interpretar comandos hablados y `pyttsx3` para responder con voz.\nPuede decir la hora y el día, abrir sitios web como YouTube o Google, buscar en Wikipedia, contar chistes, reproducir videos de YouTube, buscar en internet y consultar precios de acciones usando `yfinance`.\nIncluye manejo de errores por voz no reconocida o sin conexión.\nEjemplo de integración de múltiples librerías para crear una experiencia de usuario interactiva por voz.", "#Python, #AsistenteVirtual, #ReconocimientoVoz, #pyttsx3, #speechrecognition", "02/05/2025", "Día 13", "13")

Data_14 = Proyectos("Reconocimiento Facial", "Aplicación en Python que emplea `face_recognition` y `OpenCV` para capturar una imagen desde la cámara web, identificar rostros comparándolos con\nuna base de datos de empleados previamente codificada, y registrar automáticamente el nombre y la hora de ingreso en un archivo CSV\nsi se encuentra una coincidencia confiable, integrando visión por computadora y biometría facial para control de accesos.", "#Python, #ReconocimientoFacial, #OpenCV, #face_recognition, #VisiónComputacional", "02/05/2025", "Día 14", "14")

Data_15 = Proyectos("Machine Learning - Titanic", "Este proyecto en Python que aplica técnicas de aprendizaje automático para analizar el famoso dataset del Titanic, utilizando un modelo de `DecisionTreeClassifier` de `Scikit-Learn`.\nA partir de características como sexo, edad y clase del pasajero, el modelo es entrenado para predecir la probabilidad de supervivencia de cada individuo.\nSe realiza una limpieza y preparación de datos, separación entre atributos predictivos `X` y la variable objetivo `y`, entrenamiento del modelo, y evaluación con métricas como precisión\ny matriz de confusión.\nAdemás, se visualiza el árbol de decisión generado para interpretar las reglas aprendidas y se analiza la importancia de cada atributo en la predicción,\noferciendo una visión clara de cómo factores socioeconómicos y demográficos influyeron en las chances de supervivencia durante el hundimiento del Titanic.", "#Python, #MachineLearning, #ÁrbolDeDecisión, #Titanic, #ScikitLearn, #Visualización", "03/05/2025", "Día 15", "15")

Data_16 = Proyectos("Aplicación de Tareas con Django", "Proyecto web que permite gestionar tareas personales mediante autenticación de usuarios.\nCada usuario puede crear, ver, editar y eliminar sus propias tareas.\nSe implementan vistas genéricas de Django como `ListView`, `CreateView`, `UpdateView` y `DeleteView`.\nEl modelo `Tarea` se asocia al usuario que la crea.\nIncluye un buscador para filtrar tareas por título y contador de tareas incompletas.\nEl registro y login se gestionan con `UserCreationForm` y `LoginView`, redirigiendo al panel principal tras autenticarse.\nLa plantilla `principal.html` estructura la interfaz con estilos básicos en CSS y elementos visuales como íconos de estado.\nEste proyecto demuestra el uso de CRUD con Django, separación por usuario y diseño web funcional.", "#Python, #Django, #ToDoApp, #CRUD, #Login, #HTML, #CSS", "04/05/2025", "Día 16", "16")


# Variables / Listas
Bucle = True
Lista_de_Verificacion = [Data_1.dia, Data_1.titulo, Data_1.numero,
                         Data_2.dia, Data_2.titulo, Data_2.numero,
                         Data_3.dia, Data_3.titulo, Data_3.numero,
                         Data_4.dia, Data_4.titulo, Data_4.numero,
                         Data_5.dia, Data_5.titulo, Data_5.numero,
                         Data_6.dia, Data_6.titulo, Data_6.numero,
                         Data_7.dia, Data_7.titulo, Data_7.numero,
                         Data_8.dia, Data_8.titulo, Data_8.numero,
                         Data_9.dia, Data_9.titulo, Data_9.numero,
                         Data_10.dia, Data_10.titulo, Data_10.numero,
                         Data_11.dia, Data_11.titulo, Data_11.numero,
                         Data_12.dia, Data_12.titulo, Data_12.numero,
                         Data_13.dia, Data_13.titulo, Data_13.numero,
                         Data_14.dia, Data_14.titulo, Data_14.numero,
                         Data_15.dia, Data_15.titulo, Data_15.numero,
                         Data_16.dia, Data_16.titulo, Data_16.numero,

                         ]

Lista_de_Verificacion_Salir = ["Salir", "salir", "SALIR"]
Lista_de_Verificacion_Volver = ["VOLVER", "volver", "Volver", "Volver al Menu", "volver al menu", "Volver al menu", "VOLVER AL MENU"]
Lista_de_Verificacion_Volver_A_Preguntar = Lista_de_Verificacion_Salir + Lista_de_Verificacion_Volver


# Ejecucion del Codigo
while Bucle:
    try:
        Limpiar_pantalla()
        Respuesta = Presentacion()

        if Respuesta == Data_1.dia or Respuesta == Data_1.titulo or Respuesta == Data_1.numero:
            Limpiar_pantalla()
            Descripcion(Data_1.dia, Data_1.fecha, Data_1.descripcion, Data_1.etiqueta)
            Recopilacion.Nombre_Cerveza()
            Respuesta_Preguntar = Volver_preguntar()

            if Respuesta_Preguntar in Lista_de_Verificacion_Volver:
                pass

            elif Respuesta_Preguntar in Lista_de_Verificacion_Salir:
                Bucle = False

        elif Respuesta == Data_2.dia or Respuesta == Data_2.titulo or Respuesta == Data_2.numero:
            Limpiar_pantalla()
            Descripcion(Data_2.dia, Data_2.fecha, Data_2.descripcion, Data_2.etiqueta)
            Recopilacion.Calculador_impuestos()
            Respuesta_Preguntar = Volver_preguntar()

            if Respuesta_Preguntar in Lista_de_Verificacion_Volver:
                pass

            elif Respuesta_Preguntar in Lista_de_Verificacion_Salir:
                Bucle = False

        elif Respuesta == Data_3.dia or Respuesta == Data_3.titulo or Respuesta == Data_3.numero:
            Limpiar_pantalla()
            Descripcion(Data_3.dia, Data_3.fecha, Data_3.descripcion, Data_3.etiqueta)
            Recopilacion.analizador_textos()
            Respuesta_Preguntar = Volver_preguntar()

            if Respuesta_Preguntar in Lista_de_Verificacion_Volver:
                pass

            elif Respuesta_Preguntar in Lista_de_Verificacion_Salir:
                Bucle = False

        elif Respuesta == Data_4.dia or Respuesta == Data_4.titulo or Respuesta == Data_4.numero:
            Limpiar_pantalla()
            Descripcion(Data_4.dia, Data_4.fecha, Data_4.descripcion, Data_4.etiqueta)
            Recopilacion.numero_aleatorio()
            Respuesta_Preguntar = Volver_preguntar()

            if Respuesta_Preguntar in Lista_de_Verificacion_Volver:
                pass

            elif Respuesta_Preguntar in Lista_de_Verificacion_Salir:
                Bucle = False

        elif Respuesta == Data_5.dia or Respuesta == Data_5.titulo or Respuesta == Data_5.numero:
            Limpiar_pantalla()
            Descripcion(Data_5.dia, Data_5.fecha, Data_5.descripcion, Data_5.etiqueta)
            Recopilacion.elegir_palabra()
            Respuesta_Preguntar = Volver_preguntar()

            if Respuesta_Preguntar in Lista_de_Verificacion_Volver:
                pass

            elif Respuesta_Preguntar in Lista_de_Verificacion_Salir:
                Bucle = False

        elif Respuesta == Data_6.dia or Respuesta == Data_6.titulo or Respuesta == Data_6.numero:
            Limpiar_pantalla()
            Descripcion(Data_6.dia, Data_6.fecha, Data_6.descripcion, Data_6.etiqueta)
            Recopilacion.recetario()
            Respuesta_Preguntar = Volver_preguntar()

            if Respuesta_Preguntar in Lista_de_Verificacion_Volver:
                pass

            elif Respuesta_Preguntar in Lista_de_Verificacion_Salir:
                Bucle = False

        elif Respuesta == Data_7.dia or Respuesta == Data_7.titulo or Respuesta == Data_7.numero:
            Limpiar_pantalla()
            Descripcion(Data_7.dia, Data_7.fecha, Data_7.descripcion, Data_7.etiqueta)
            Recopilacion.cuenta_banco()
            Respuesta_Preguntar = Volver_preguntar()

            if Respuesta_Preguntar in Lista_de_Verificacion_Volver:
                pass

            elif Respuesta_Preguntar in Lista_de_Verificacion_Salir:
                Bucle = False

        elif Respuesta == Data_8.dia or Respuesta == Data_8.titulo or Respuesta == Data_8.numero:
            Limpiar_pantalla()
            Descripcion(Data_8.dia, Data_8.fecha, Data_8.descripcion, Data_8.etiqueta)
            Recopilacion.elegir_turno()
            Respuesta_Preguntar = Volver_preguntar()

            if Respuesta_Preguntar in Lista_de_Verificacion_Volver:
                pass

            elif Respuesta_Preguntar in Lista_de_Verificacion_Salir:
                Bucle = False

        elif Respuesta == Data_9.dia or Respuesta == Data_9.titulo or Respuesta == Data_9.numero:
            Limpiar_pantalla()
            Descripcion(Data_9.dia, Data_9.fecha, Data_9.descripcion, Data_9.etiqueta)
            Recopilacion.buscar_numeros()
            Respuesta_Preguntar = Volver_preguntar()

            if Respuesta_Preguntar in Lista_de_Verificacion_Volver:
                pass

            elif Respuesta_Preguntar in Lista_de_Verificacion_Salir:
                Bucle = False

        elif Respuesta == Data_10.dia or Respuesta == Data_10.titulo or Respuesta == Data_10.numero:
            Limpiar_pantalla()
            Descripcion_Modf(Data_10.dia, Data_10.fecha, Data_10.descripcion, Data_10.etiqueta)
            Recopilacion.juego()
            Bucle = False

        elif Respuesta == Data_11.dia or Respuesta == Data_11.titulo or Respuesta == Data_11.numero:
            Limpiar_pantalla()
            Descripcion(Data_11.dia, Data_11.fecha, Data_11.descripcion, Data_11.etiqueta)
            Recopilacion.web_scraping()
            Respuesta_Preguntar = Volver_preguntar()

            if Respuesta_Preguntar in Lista_de_Verificacion_Volver:
                pass

            elif Respuesta_Preguntar in Lista_de_Verificacion_Salir:
                Bucle = False

        elif Respuesta == Data_12.dia or Respuesta == Data_12.titulo or Respuesta == Data_12.numero:
            Limpiar_pantalla()
            Descripcion_Modf(Data_12.dia, Data_12.fecha, Data_12.descripcion, Data_12.etiqueta)
            Recopilacion.mi_restaurante()
            Bucle = False

        elif Respuesta == Data_13.dia or Respuesta == Data_13.titulo or Respuesta == Data_13.numero:
            Limpiar_pantalla()
            Descripcion(Data_13.dia, Data_13.fecha, Data_13.descripcion, Data_13.etiqueta)
            Recopilacion.asistente_personal()
            Respuesta_Preguntar = Volver_preguntar()

            if Respuesta_Preguntar in Lista_de_Verificacion_Volver:
                pass

            elif Respuesta_Preguntar in Lista_de_Verificacion_Salir:
                Bucle = False

        elif Respuesta == Data_14.dia or Respuesta == Data_14.titulo or Respuesta == Data_14.numero:
            Limpiar_pantalla()
            Descripcion(Data_14.dia, Data_14.fecha, Data_14.descripcion, Data_14.etiqueta)
            Recopilacion.reconocimiento_facial()
            Respuesta_Preguntar = Volver_preguntar()

            if Respuesta_Preguntar in Lista_de_Verificacion_Volver:
                pass

            elif Respuesta_Preguntar in Lista_de_Verificacion_Salir:
                Bucle = False

        elif Respuesta == Data_15.dia or Respuesta == Data_15.titulo or Respuesta == Data_15.numero:
            Limpiar_pantalla()
            Descripcion(Data_15.dia, Data_15.fecha, Data_15.descripcion, Data_15.etiqueta)

            print(f"Este proyecto fue desarrollado en {negrita_y_subrayado("Google Colab")}. Por esta razón, no puedes contemplarlo en esta terminal.")
            print("")
            print(f"Podrás visualizar este proyecto a traves de {negrita("este enlace")}: {negrita_y_subrayado("https://machleaning.zenithmc.es/")}")

            Recopilacion.machine_learning()
            Respuesta_Preguntar = Volver_preguntar()

            if Respuesta_Preguntar in Lista_de_Verificacion_Volver:
                pass

            elif Respuesta_Preguntar in Lista_de_Verificacion_Salir:
                Bucle = False

        elif Respuesta == Data_16.dia or Respuesta == Data_16.titulo or Respuesta == Data_16.numero:
            Limpiar_pantalla()
            Descripcion(Data_16.dia, Data_16.fecha, Data_16.descripcion, Data_16.etiqueta)


            print(f"Este proyecto fue desarrollado junto a {negrita("Django")}. Por esta razón, no puedes contemplarlo en esta terminal.")
            print("")
            print(f"Podrás visualizar este proyecto a traves de {negrita("esta url local")}: {negrita_y_subrayado("http://localhost:8000/")}")

            Recopilacion.pagina_web()
            Bucle = False


    except SyntaxError:
        print("")
        print(negrita("🚨⏐ ¡Error detectado! (SyntaxError)"))
        Bucle = False

    except NameError:
        print("")
        print(negrita("🚨⏐ ¡Error detectado! (NameError)"))
        Bucle = False

    except TypeError:
        print("")
        print(negrita("🚨⏐ ¡Error detectado! (TypeError)"))
        Bucle = False

    except ValueError	:
        print("")
        print(negrita("🚨⏐ ¡Error detectado! (ValueError)"))
        Bucle = False

    except KeyError:
        print("")
        print(negrita("🚨⏐ ¡Error detectado! (KeyError)"))
        Bucle = False

    except AttributeError:
        print("")
        print(negrita("🚨⏐ ¡Error detectado! (AttributeError)"))
        Bucle = False

    except ZeroDivisionError:
        print("")
        print(negrita("🚨⏐ ¡Error detectado! (ZeroDivisionError)"))
        Bucle = False

    except (ModuleNotFoundError, ImportError):
        print("")
        print(negrita("🚨⏐ ¡Error detectado! (ImportError / ModuleNotFoundError)"))
        Bucle = False

    except FileNotFoundError:
        print("")
        print(negrita("🚨⏐ ¡Error detectado! (FileNotFoundError)"))
        Bucle = False

    except PermissionError:
        print("")
        print(negrita("🚨⏐ ¡Error detectado! (PermissionError)"))
        Bucle = False

    except IOError:
        print("")
        print(negrita("🚨⏐ ¡Error detectado! (IOError)"))
        Bucle = False

    except RuntimeError:
        print("")
        print(negrita("🚨⏐ ¡Error detectado! (RuntimeError)"))
        Bucle = False

