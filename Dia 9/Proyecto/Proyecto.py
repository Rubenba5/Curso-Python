# Importar Librerias
import os
import re
from pathlib import Path
import datetime
import time
import math

# Ruta del Directorio
ruta = Path("C:\\Users\\Ruben\\Desktop\\Python\\Curso-Python\\Dia 9\\Proyecto\\Comprimido\\Descomprimido\\Mi_Gran_Directorio")


# Buscar Archivos
def buscar_archivos(ruta):
    Dic = {}

    for Directorio, Subdirectorio, Archivo in os.walk(ruta):
        for archivo in Archivo:
                Dic[archivo] = Directorio

    return Dic


# Comprobar
def comprobar_archivo(lista):
    Patron = r"N\w{3}-\d{5}"
    Dic = {}

    for archivo in lista:
        Ruta_Nueva = Path(lista[archivo], archivo)
        Archivo_Abrir = open(Ruta_Nueva, "r")
        Lineas = Archivo_Abrir.readlines()
        Unir = "".join(Lineas)

        Coincidencia = re.search(Patron, Unir)
        if Coincidencia is None:
            Dic[archivo] = "No encontrado"
        else:
            Dic[archivo] = Coincidencia.group()

        Archivo_Abrir.close()

    return Dic

# Imprimir
def monstrar(dic, duracion):
    Contador = 0
    Fecha = datetime.date.today()
    Fecha_Ordenada = f"{Fecha.day}/{Fecha.month}/{Fecha.year}"

    print(f"Fecha de búsqueda: {Fecha_Ordenada}")
    print("")
    print("Archivo\t   |    Número de Serie")
    print("-------------------------------")

    for archivo, coincidencia in dic.items():
        print(f"{archivo}\t{coincidencia}")
        if coincidencia == "No encontrado":
            pass

        else:
            Contador += 1

    print("")
    print(f"Números encontrados: {Contador}")
    print(f"Duración de la busqueda: {math.ceil(duracion)} segundos.")


# Ejecución
Inicio = time.time()
Lista = buscar_archivos(ruta)
Dic = comprobar_archivo(Lista)
Fin = time.time()
Duracion = Fin - Inicio
monstrar(Dic, Duracion)
