# Abrir un archivo y manipular su contenido:
# open("nombre archivo", "modo de apertura" (r)) sirve para abrir un archivo
# El modo de apertura puede ser: r (SOLO leectura), w (SOLO escritura, crear), a (SOLO escritura al final del archivo, crear)

# open("nombre archivo", "modo de apertura") sirve para abrir un archivo
# .close() sirve para cerrar el archivo. MUY IMPORTANTE
# .write("texto") sirve para escribir en el archivo, eliminando el contenido anterior (w) no con (a). No deja espacio al escribir, usar: """texto""" o \n
# .writelines(["palabra",]) sirve para escribir en el archivo, usando una lista. No deja espacio al escribir
# .read() sirve para leer el contenido del archivo
# .readline() lee la primera línea del archivo. Lee la siguiente línea donde se quedó anteriormente.
# .readlines() lee todas las líneas del archivo y las guarda en una lista
# .rstrip sirve para eliminar los espacios en blanco al final de la línea

# -------------------------------------------------------------------------------------------------------------------- #

# Directorios:
# Para definir un directorio usar \\ en vez de \

# Import os
# os.remove() sirve para eliminar un archivo
# os.getcwd() sirve para obtener el directorio actual
# os.chdir("directorio") sirve para cambiar el directorio actual
# os.mkdir("nombre carpeta") sirve para crear una carpeta
# os.path.basename("directorio") sirve para obtener el nombre del archivo
# os.path.dirname("directorio") sirve para obtener el nombre del directorio
# os.path.split("directorio") sirve para obtener el nombre del archivo y el nombre del directorio
# os.rmdir("directorio") sirve para eliminar una carpeta
# os.parents[] sirve para ascender a las rutas superiores del directorio como diga el número

# From pathlib import Path, PureWindowsPath
# Path es usado para que cualquier distribucion pueda leer el archivo sin importar el sistema operativo
# PureWindowsPath es usado para definir un directorio en Windows en vez de usar el general
# Cuando se usa Path se puede usar / en vez de \\ para definir un directorio
# Para definir un archivo se una por ejemplo: archivo = "directorio / archivo.txt"
# Usando PathLib no hace falta cerrar el archivo.
# Además, si le das una lista de palabras, te crea un directorio en ese orden.
# .read_text() sirve para leer el contenido del archivo
# .name() sirve para obtener el nombre del archivo con la terminacion
# .stem() sirve para obtener el nombre del archivo sin la terminacion
# .exist() sirve para verificar si el archivo existe
# .suffix() sirve para obtener la terminacion del archivo
# .home() sirve para obtener el directorio general de tu ordenador
# .with_name() sirve para cambiar el nombre del archivo
# .parent() sirve para obtener el directorio antes del archivo
# .glob() sirve para obtener todos los archivos de un directorio ("*.txt") sirve para obtener todos los archivos.txt
# Usando glob para obtener todos los archivos de un directorio, se puede usar ("**/*.txt") para obtener todos los archivos.txt de todos los subdirectorios
# .relative_to(Path()) sirve para obtener el directorio relativo al archivo

# -------------------------------------------------------------------------------------------------------------------- #

# Limpiar la terminal:
# from os import system
# system("cls") sirve para limpiar la terminal en Windows

