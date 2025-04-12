# Programacion orientada a objetos (POO):
# Es un paradigma de programacion que utiliza objetos y sus interacciones para diseñar aplicaciones y programas informaticos.
# Definicion de la clase que contienen atributos (caractersticas) y metodos (funciones)
# El concepto de clase es una plantilla para crear objetos con sus atributos y metodos
# La Programacion orientada a objetos tiene unos pilares fundamentales: herencia, polimorfismo, abstracción, encapsulacion y abstraccion.

# -------------------------------------------------------------------------------------------------------------------- #

# Clases:
# Una clase es una plantilla para crear objetos. Define un conjunto de atributos y métodos que los objetos creados a partir de la clase tendrán.
# En Python, se define una clase utilizando la palabra clave `class`, seguida del nombre de la clase y dos puntos.
# Al escribir una clase, si está formada por varias palabras, la primera letra de cada palabra debe ser mayúscula. Por ejemplo: `class MiClase:`.
# Igual que las funciones, las clases se pueden invocar en cualquier parte del código, siempre y cuando se haya definido previamente.
# Para crear un objeto a partir de una clase, se utiliza el nombre de la clase seguido de paréntesis. Por ejemplo: `mi_objeto = MiClase()`.

# -------------------------------------------------------------------------------------------------------------------- #

# Atributos:
# Los atributos son las variables que pertenecen a una clase. Se definen dentro de la clase y se accede a ellos utilizando la notación de punto.
# Existen dos tipos de atributos: atributos de instancia y atributos de clase.

# Atributos de Estancia / Clase:
# Para definir atributos de clase, hay que poner def __init__(self, atributo1, ...): self.atributo1 = atributo1
# Para definir atributos de instancia, se utiliza el atributo definido.
# Clase.color sirve para acceder a los atributos de clase. Self.color (es un artributo de instancia) = color (parametro)

# Atributos de Clase:
# Son atributos que pertenecen a la clase en sí y son compartidos por todas las instancias de la clase.
# Se definen directamente dentro de la clase, fuera de cualquier metodo. Por ejemplo: `class MiClase: atributo_clase = valor`.
# Para acceder a un atributo de clase, se utiliza el nombre de la clase seguido del nombre del atributo. Por ejemplo: `MiClase.atributo_clase`.

# -------------------------------------------------------------------------------------------------------------------- #

# Métodos:
# Los métodos son funciones que pertenecen a una clase. Se definen dentro de la clase y se accede a ellos utilizando la notación de punto.
# Los métodos pueden tomar parámetros y devolver valores, al igual que las funciones normales.
# La diferencia es que los métodos de instancia tienen acceso a los atributos de la instancia a través del parámetro `self`.
# Cuando ivocamos a un atributo, si queremos acceder al atributo de otro, def hay que usar .format(self.atributo)

# Tipos de Métodos:
# 1. Métodos de Instancia:
# Se define como def mi_metodo(self, parametro1, ...): print("Hola, soy un metodo de instanca")
# Pueden acceder y modificar los atributos de la instancia a través del parámetro `self`.

# 2. Métodos de Clase:
# Al usar hay que usar @classmethod
# Se definen utilizando el decorador `@classmethod` y el primer parámetro es `cls`, que representa la clase misma.
# Pueden acceder y modificar los atributos de clase, pero no pueden acceder a los atributos de instancia directamente.

# 3. Métodos Estáticos:
# Al usar hay que usar @staticmethod
# Se definen utilizando el decorador `@staticmethod` y no tienen acceso a la instancia o la clase.
# Son métodos independientes que no dependen de la clase o la instancia.

# -------------------------------------------------------------------------------------------------------------------- #

# Herencia:
# La herencia es un mecanismo que permite crear una nueva clase a partir de una clase existente. La nueva clase hereda los atributos y métodos de la clase base.
# La clase base se llama superclase y la nueva clase se llama subclase.
# Para definir una subclase, se utiliza la siguiente sintaxis: `class SubClase(SuperClase):`.
# Para saber de quién hereda, hay que usar el metodo __bases__.
# Para saber las subclases de una clase, hay que usar el metodo __subclasses__.

# Herencia Extendida:
# La herencia extendida es un tipo de herencia en la que una subclase hereda de otra subclase.
# Para definir nuevos atributos en la subclase, en vez de repetir se puede usar el metodo super().__init__(atributos)  de la superclase.
# Existe un orden de busqueda a la hora de ejecutar los atributos. Por ejemplo class Hijo(Hermano, Padre) ejecutara primero los atributos/acciones de Hermano
# Para saber el orden de busqueda, hay que usar el metodo __mro__.

# -------------------------------------------------------------------------------------------------------------------- #

# Polimorfismo:
# El polimorfismo es la capacidad de un objeto de tomar muchas formas. En POO, se refiere a la capacidad de diferentes clases de responder a la misma llamada de metodo.
# Esto se basa en ejecutar lo mismo en diferentes clases, pero con diferentes implementaciones.
# Por ejemplo, si tenemos una clase `Animal` y dos subclases `Perro` y `Gato`, ambas pueden tener un metodo `hacer_sonido()`, pero cada una implementa el sonido de manera diferente.

# -------------------------------------------------------------------------------------------------------------------- #

# Encapsulamiento:
# Consiste en ocultar los detalles internos de un objeto y exponer solo lo necesario.
# Se usa para proteger los datos y controlar su acceso mediante modificadores (public, private, etc.).

# -------------------------------------------------------------------------------------------------------------------- #

# Abstracción:
# Permite trabajar con objetos mostrando solo lo esencial y ocultando lo complejo.
# Se enfoca en lo que hace un objeto, no en cómo lo hace. Se logra con interfaces o clases abstractas.

# -------------------------------------------------------------------------------------------------------------------- #

# Acoplamiento:
# Mide la dependencia entre clases o módulos.
# Se busca un bajo acoplamiento para que las clases sean independientes y fáciles de mantener o modificar.

# -------------------------------------------------------------------------------------------------------------------- #

# Cohesión:
# Mide cuánto están relacionadas las funciones dentro de una clase.
# Se busca una alta cohesión, donde la clase tenga una única responsabilidad y esté bien organizada.

# -------------------------------------------------------------------------------------------------------------------- #

# Metodos Especiales:
# Son métodos que permiten definir el comportamiento de los objetos en ciertas situaciones.
# Se definen con dos guiones bajos al principio y al final del nombre del metodo.

# Algunos de los métodos especiales más comunes son:
# 1. `__init__(self, ...)`: Constructor de la clase. Se llama al crear una instancia de la clase.
# 2. `__mro__(self)`: Devuelve el orden de búsqueda de la clase.
# 3. ` __bases__(self)`: Devuelve la clase base de la clase.
# 4. `__subclasses__(self)`: Devuelve las subclases de la clase.
# 5. `__str__(self)`: Devuelve una representación en cadena de la instancia.
# 6. `__len__(self)`: Devuelve la longitud de la instancia.
# 7. `__del__(self)`: Destructor de la clase. Se llama al eliminar una instancia de la clase.


# -------------------------------------------------------------------------------------------------------------------- #

# Delete:
# Delele es una palabra clave en Python que se utiliza para eliminar objetos, variables o atributos.
# Se usa como "del objeto.atributo o del objeto"
