# Principios de Web Scraping:
# Los principios de web scraping son: html, css y javascript.
# 1. HTML: Lenguaje de marcado utilizado para estructurar el contenido de una página web, usando etiquetas . En python, se busca entre los tags, por ejemplo: <h1>, <p>, <div>, etc.
# 2. CSS: Lenguaje de estilo utilizado para dar formato y diseño a una página web. En python, se busca entre los selectores, por ejemplo: <link>, #id, .class, etc.
# 3. JavaScript: Lenguaje de programación utilizado para agregar interactividad y dinamismo a una página web. En python, se busca entre los scripts, por ejemplo: <script>, <json>, etc.
# Para buscar encontrar información en una página web, se busca apuntando a una etiqueta.

# -------------------------------------------------------------------------------------------------------------------- #
# Reglas del Web Scraping:
# 1. Respeta el archivo robots.txt: Verifica si el sitio web permite el scraping y sigue las reglas establecidas.
# 2. No sobrecargues el servidor: Realiza solicitudes de manera responsable y evita hacer demasiadas solicitudes en poco tiempo.

# -------------------------------------------------------------------------------------------------------------------- #
# Limitaciones de Web Scraping:
# 1. Cambios en la estructura del sitio web: Si el sitio web cambia su diseño o estructura, el scraper puede dejar de funcionar.
# 2. Bloqueo por parte del servidor: Algunos sitios web implementan medidas para bloquear el scraping, como restricciones de IP.
# 3. Legalidad: El scraping puede ser ilegal en algunos países o violar los términos de servicio de un sitio web.

# -------------------------------------------------------------------------------------------------------------------- #
# Librerias de Web Scraping para Python:
# 1. BeautifulSoup: Biblioteca para analizar documentos HTML y XML, facilitando la extracción de datos. Instalar: pip install beautifulsoup4.
# 2. Requests: Biblioteca para realizar solicitudes HTTP de manera sencilla. Instalar: pip install requests.
# 3. 1xml: Biblioteca para analizar y manipular documentos XML. Instalar: pip install lxml.

# -------------------------------------------------------------------------------------------------------------------- #
# Ejemplo de Web Scraping con BeautifulSoup y Requests:
# Se utiliza la libreria requests para hacer una solicitud HTTP a una página web y obtener su contenido HTML. Luego, se utiliza BeautifulSoup para analizar el HTML y extraer información específica.
# Importar: import requests (realizar solicitud) y import bs4 (analizar codigo fuente).

# Algunas funciones utiles de Requests:
# 1. requests.get("url"): Realiza una solicitud GET a la URL especificada y devuelve la respuesta.
# 3. variable.txt: Devuelve el codigo fuente como texto.

# Algunas funciones utiles de BeautifulSoup:
# 1. bs4.BeautifulSoup(variable.txt, "lxml"): Analiza el contenido HTML y crea un objeto BeautifulSoup para poder utilizarlo.
# 2. variable.selector("etiqueta"): Analiza en el codigo y imprime quienes tienen esa etiqueta en una lista.
# 3. variable.get_text(): Devuelve el texto dentro de la etiqueta seleccionada, pero sí la etiqueta.



