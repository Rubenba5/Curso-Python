# Librerias
import bs4
import requests


# Url Base de la Página Web
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'


# Lista de Titulos con 4 o 5 estrellas
titulos_rating_alto = []


# Iterar Paginas
for pagina in range(1, 51):

    # Crear sopa en cada página
    url_pagina = url_base.format(pagina)

    # Request a la Pagina
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")

    # Seleccionar datos de los Libros
    libros = sopa.select(".product_pod")

    # Iterar en los libros
    for libro in libros:

        # Verificar que el libro tenga 4 o 5 estrellas
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:

            # Titulo del Libro (variable)
            titulo_libro = libro.select("a")[1]["title"]

            # Agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)


# Ver libros de 4 y 5 estrellas en consola
for libro in titulos_rating_alto:
    print(libro)
