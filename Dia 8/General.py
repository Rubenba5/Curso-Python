# Instalar Paquetes
# Para instalar paquetes en Python, se utiliza el comando pip install nombre_paquete en la terminal de windows.
# Buscar paquetes en https://pypi.org/

# Para importar el parquete entrar en la interfaz de python primero.
# Para importar el paquete en Python para utilizarlo, se usa el comando from nombre_paquete import nombre_funcion.

# -------------------------------------------------------------------------------------------------------------------- #

# Modulos y Paquetes
# Un módulo es un archivo que contiene código Python y puede contener funciones, clases y variables.
# Un módulo se puede importar en otro módulo con el comando from nombre_modulo_a_importar import variables, *, etc.

# Un paquete es una colección de módulos organizados en un directorio.
# En todos los parquetes debe haber un archivo __init__.py, que indica que el directorio es un paquete.
# Un paquete se puede importar en otro módulo con el comando from nombre_paquete import nombre_modulo.
# Una vez importado para usar el módulo, hay que usar el comando nombre_modulo.nombre_funcion.
# Para importar subpaquetes, hay que usar el comando from nombre_paquete.nombre_subpaquete import nombre_modulo.

# -------------------------------------------------------------------------------------------------------------------- #

# Manejo de Errores
# El manejo de errores en Python se hace con los comandos try, except, else y finally.
# El bloque try contiene el código que puede generar un error.
# El bloque else contiene el código que se ejecuta si no se produce un error.
# El bloque finally contiene el código que se ejecuta siempre, haya o no habido un error.
# El bloque except contiene el código que se ejecuta si se produce un error. Se puede especificar el tipo de error que se quiere manejar.
# Por ejemplo, si se quiere manejar un error de tipo TypeError, se usa el comando except TypeError.

# -------------------------------------------------------------------------------------------------------------------- #

# Busca Errores con Pylint:
# Pylint es una herramienta para analizar el código Python y detectar problemas de errores o estilo.
# Se puede instalar con el comando pip install pylint.
# Para usar pylint, se usa el comando pylint nombre_archivo.py -r y en terminal.

# -------------------------------------------------------------------------------------------------------------------- #

# Probar codigo con Unitest:
# Unitest es un módulo de Python que permite hacer pruebas unitarias.
# Se puede importar con el comando import unittest y el archivo, import archivo.
# Para crear una prueba unitaria, se crea una clase que hereda de unittest.TestCase.
# Las funciones dentro de las clases se tienen que llamar "text_loquesea"
# Se puede usar self.assertEqual(devuelve, yo creo) para comparar dos resultados.
# Hay que pones el comando if __name__ == "__main__": unittest.main() para que se ejecute la prueba.

# -------------------------------------------------------------------------------------------------------------------- #
# Decoradores:
# Un decorador es una función que toma otra función como argumento y devuelve una nueva función.








