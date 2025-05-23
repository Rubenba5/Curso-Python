# Librerias
import pyttsx3 # Texto a Voz
import speech_recognition as sr # Voz a Texto
import pywhatkit # Buscar en internet
import yfinance as yf # Consultar la Bolsa
import pyjokes # Chistes
import webbrowser # Navegar en Internet
import wikipedia # Wikipedia
import datetime


# Escuchar nuestro microfono y devolver el audio como texto.
def transformar_audio_en_texto():

    # Almacenar recognizer en variable
    r = sr.Recognizer()

    # Configurar el microfono
    with sr.Microphone() as origen:

        # Tiempo de espera
        r.pause_threshold = 0.8

        # Informar que comenzo la grabacion
        print("Ya puedes hablar.")

        # Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # Buscar en google
            pedido = r.recognize_google(audio, language="es-ES")

            # Prueba de que pudo ingresar
            print(f"Dijiste: {pedido}")

            # Devolver pedido
            return pedido

        # En caso de que no comprenda el audio
        except sr.UnknownValueError:

            # Prueba de que no comprendio el audio
            print("Ups, no entendi")

            # Devolver error
            return "Sigo esperando"

        except sr.RequestError:

            # Prueba de que no comprendio el audio
            print("Ups, no hay servicio")

            # Devolver error
            return "Sigo esperando"

        # Eror inesperado
        except:
            # Prueba de que no comprendio el audio
            print("Ups, algo ha salido mal")

            # Devolver error
            return "Sigo esperando"


# Funcion para que el asistente pueda ser escuchado
# Descargar voces externas: https://support.microsoft.com/es-es/topic/descargar-idiomas-y-voces-para-lector-inmersivo-el-modo-lectura-y-lectura-en-voz-alta-4c83a8d8-7486-42f7-8e46-2b0fdf753130
def hablar(mensaje):

    # Encender el motor de pyttsx3
    engine = pyttsx3.init()
    #engine.setProperty("voices", "id de la voz") (Setear las voces)

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

        if "abrir youtube" in pedido:
            hablar("Con gusto, estoy abriendo youTube,")
            webbrowser.open("https://www.youtube.com")
            continue

        elif "abrir navegador" in pedido:
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
            resultado = wikipedia.summary(pedido, sentences= 1)
            hablar(f"Wikpedia dice lo siguiente:{resultado}")
            continue

        elif "busca en internet" in pedido:
            hablar("Ya mismo estoy en buscando")
            pedido = pedido.replace("busca en internet", "")
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue

        elif "reproducir" in pedido:
            hablar("Buena idea, ya comienzo a reproducirlo.")
            pywhatkit.playonyt(pedido)
            continue

        elif "broma" in pedido:
            hablar(pyjokes.get_joke("es"))
            continue

        elif "precio de las acciones" in pedido:
            accion = pedido.split("de")[-1].strip()
            cartera = {"apple":"APPL",
                       "amazon":"AMZN",
                       "google":"GOOGL"}
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

pedir_cosas()