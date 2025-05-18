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

