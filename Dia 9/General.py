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
# 4. os.rmdir(): eliminar un nuevo directorio.

# -------------------------------------------------------------------------------------------------------------------- #
# Módulo Shutil:
# El módulo shutil proporciona funciones para trabajar con archivos y directorios.
# Es bastante útil para copiar, mover y eliminar archivos y directorios.

# Algunas funciones útiles son:
# 1. shutil.move("archivo", "ruta"): mueve un archivo o directorio a una nueva ubicación.
# 2. shutil.rmtree("directorio"): elimina un directorio y su contenido de forma recursiva.
