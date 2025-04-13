# Módulo Collections:
# El módulo collections proporciona alternativas a los tipos de datos integrados de Python.
# from collections import *

# Hay varias clases dentro de este módulo, pero las más importantes son:
# 1. Counter(): sirve para contar elementos en una lista. Lo organiza en un diccionario. Los counter tienen métodos como most_common().
# 2. defaultdict(lambda: ""): es un diccionario que devuelve un valor por defecto si la clave no existe.
# 3. namedtuple(): es una tupla con nombre. Permite acceder a los elementos por nombre en lugar de por índice. Se aceede usando, por ejemplo, "tupla.nombre".
# 4. deque(): es una lista que permite añadir y quitar elementos por ambos lados. Es más eficiente que una lista normal.

# -------------------------------------------------------------------------------------------------------------------- #
# Módulo OS:
# El módulo os proporciona una forma de interactuar con el sistema operativo.
# Es bastante util para trabajar con rutas de archivos y directorios.

# Algunas funciones útiles son:
# 1. os.getcwd(): devuelve el directorio de trabajo actual.
# 2. os.listdir(): devuelve una lista de los archivos y directorios en un directorio dado.
# 3. os.unlink(): elimina un archivo o enlace simbólico.
# 4. os.rmdir(): eliminar un directorio.
# 5. os.walk("ruta"): devuelve una lista de tuplas que contienen el nombre del directorio, una lista de subdirectorios y una lista de archivos en un directorio dado.
# Ejemplo: For: for dir, subdir, archivo in os.walk("ruta"):...

# -------------------------------------------------------------------------------------------------------------------- #
# Módulo Shutil:
# El módulo shutil proporciona funciones para trabajar con archivos y directorios.
# Es bastante útil para copiar, mover y eliminar archivos y directorios.

# Algunas funciones útiles son:
# 1. shutil.move("archivo", "ruta"): mueve un archivo o directorio a una nueva ubicación.
# 2. shutil.rmtree("directorio"): elimina un directorio y su contenido de forma recursiva.

# -------------------------------------------------------------------------------------------------------------------- #
# Módulo Send to Trash:
# El módulo send2trash proporciona una forma de enviar archivos y directorios a la papelera de reciclaje.
# Para usarlo, primero debes instalarlo con el siguiente comando: pip install send2trash
# Para ejecutar el comando, debes importar el módulo con: from send2trash import send2trash
# Finalmente: send2trash.send2trash("archivo, dir"): envía un archivo o directorio a la papelera de reciclaje.

# -------------------------------------------------------------------------------------------------------------------- #
# Módulo Datetime:
# El módulo datetime proporciona clases para trabajar con fechas y horas.
# Para poder usar este módulo, debes importarlo con: import datetime.
# Para obtener la fecha y hora actual, puedes usar: datetime.datetime.now() o el atributo .today().

# Algunas funciones útiles son:
# 1. datetime.time(hora, mins, seg): devuelve la hora deseada. El formato es de 24 horas.
# 2. datetime.date(año, mes, día): devuelve la fecha deeseada. Tiene un atributo llaamado .cttime() que devuelve la fecha en formato de cadena.
# 3. datetime(dia, mes, año): devuelve la fecha deseada. Para usarlo, from datetime import datetime.
# 4. date(año, mes, día): devuelve la fecha deseada. Para usarlo, from datetime import date.
# 5. datetime.now(): devuelve la fecha y hora actual. Para usarlo, from datetime import datetime.

# -------------------------------------------------------------------------------------------------------------------- #
# Modulos Time:
# El módulo time proporciona funciones para trabajar con el tiempo.
# Para usarlo, debes importarlo con: import time.

# Algunas funciones útiles son:
# 1. time.time(): devuelve el tiempo transcurrido desde dos putos de la ejecución del programa. Por ejemplo, puedes usarlo para medir el tiempo de ejecución de un fragmento de código.
# 2. time.sleep(segundos): pausa la ejecución del programa durante el número de segundos especificado.

# -------------------------------------------------------------------------------------------------------------------- #
# Módulo Timeit:
# El modulo "timeit" proporciona una forma de medir el tiempo de ejecución de un fragmento de código.
# Para usarlo, debes importar el módulo con: import timeit.

# Algunas funciones útiles son:
# 1. timeit.timeit("declaración(prueba_fun(10))", "código", number=1): mide el tiempo de ejecución del código especificado.
# Menos el número, lo demás va comentando con """ """.

# -------------------------------------------------------------------------------------------------------------------- #
# Módulo Math:
# El módulo math proporciona funciones matemáticas.
# Para usarlo, debes importarlo con: import math.

# Algunas funciones útiles son:
# 1. math.floor(x): devuelve el redondeandolo al número entero más bajo de x.
# 2. math.ceil(x): devuelve el redondeandolo al número entero más alto de x.
# 3. math.pi: devuelve el valor de pi.
# 4. math.log(n.º expuesto, al que lo vas a exponer): devuelve el logaritmo natural del numero a exponer.
# 5. math.tan(x): devuelve la tangente de x.
# 6. math.cos(x): devuelve el coseno de x.