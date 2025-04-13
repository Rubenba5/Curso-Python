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
# 4. math.log"base"(del numero a exponer): devuelve el logaritmo natural del numero a exponer.
# 5. math.tan(x): devuelve la tangente de x.
# 6. math.cos(x): devuelve el coseno de x.
# 7. math.sqrt(x): devuelve la raíz cuadrada de x.
# 8. factorial(x): devuelve el factorial de x. Para usar esta función, debes importar el módulo con: from math import factorial.

# -------------------------------------------------------------------------------------------------------------------- #
# Módulo RE:
# El módulo re proporciona funciones para trabajar con expresiones regulares.
# Las expresiones regulares son una forma de buscar y manipular cadenas de texto.
# Para usarlo, debes importarlo con: import re.
# Para usarlo, hay que poner el prefijo r"\d" antes de la cadena y completarla con \d que significan digitos.
# Por ejemplo, r"\d{3}" busca tres dígitos consecutivos.

#Hay tres tipos de caracteres especiales:
# 1. \d: digito numerico. Ejemplo: r"\d{3}" busca tres dígitos consecutivos.
# 2. \w: caracter alfanumerico. Ejemplo: r"\w{3}" busca tres letras consecutivas.
# 3. \s: espacio en blanco. Ejemplo: r"\s{3}" busca tres espacios consecutivos.
# 4. \D: no digito numerico. Ejemplo: r"\D{3}" busca tres caracteres que no son dígitos consecutivos.
# 5. \W: no caracter alfanumerico. Ejemplo: r"\W{3}" busca tres caracteres que no son alfanuméricos consecutivos.
# 6. \S: no espacio en blanco. Ejemplo: r"\S{3}" busca tres caracteres que no son espacios consecutivos.

# Hay tres tipos de cuantificadores:
# 1. +: uno o más. Ejemplo: r"\d+" busca uno o más dígitos consecutivos.
# 2. {n}: se repiten exactamente un n.º de n. Ejemplo: r"\d{3}" busca exactamente tres dígitos consecutivos.
# 3. {n, m}: se repide de n a m vecees. Ejemplo: r"\d{3, 5}" busca entre tres y cinco dígitos consecutivos.
# 4. {n, }: desde n hacia arriba. Ejemplo: r"\d{3, }" busca tres dígitos o más consecutivos.
# 5. *: cero o más. Ejemplo: r"\d*" busca cero o más dígitos consecutivos.
# 6. ?: cero o uno. Ejemplo: "casas?", busca "casa" o "casas".

# Hay seis tipos de letras comodin:
# 1. ".": cualquier caracter. Ejemplo: r".{3}" busca cualquier caracter tres veces.
# 2. "|": o. Ejemplo: r"casa|perro" busca "casa" o "perro".
# 3. "^": inicio de la cadena. Ejemplo: r"^casa" busca "casa" al inicio de la cadena.
# 4. "$": final de la cadena. Ejemplo: r"casa$" busca "casa" al final de la cadena.
# 5. "[]": conjunto de caracteres. Ejemplo: r"[abc]" busca "a", "b" o "c".
# 6. "+": uno o más. Ejemplo: r"[abc]+" busca "a", "b" o "c" una o más veces.

# Algunos métodos útiles son:
# 1. re.search("palabra", "texto"): busca la expresión regular en la cadena y devuelve un objeto Match. Se puede utilizar .group() para obtener la palabra.
# 2. re.findall("palabra", "texto"): busca todas las coincidencias de la expresión regular en la cadena y devuelve una lista de objetos Match. Se puede utilizar .span() para obtener la ubicación.
# 3. re.finditer("palabra", "texto"): busca todas las coincidencias de la expresión regular en la cadena y devuelve un iterador de objetos Match. Se puede utilizar .span() para obtener la ubicación.
# 4. re.compile(r"expre. regular"): compila la expresión regular en un objeto Pattern. Por ejemplo, patron = re.compile(r"(\d{3})-(\d{3})-(\d{3})"). Se puede usar .group(1) para obtener primera parte.
# 5. re.search(r"expre. regular", "texto"): busca la expresión regular en la cadena y devuelve un objeto Match. Para buscar, se pudede usar r"palabra|palabra2" para buscar dos palabras a la vez.
# 6. re.findall(r"expre. regular", "texto"): busca todas las coincidencias de la expresión regular en la cadena y devuelve una lista excluyendolos.
