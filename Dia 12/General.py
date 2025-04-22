# Librerias
from platform import release
from tkinter import * # Importar TKINTER (interfaz grafica)


# Incializar a Tkinter
aplicacion = Tk()


# Tamaño de la Ventana
aplicacion.geometry("1020x630+0+0") # Resolucion + x + y de la aparición en pantalla.


# Evitar Maximizar
aplicacion.resizable(False, False)


# Título de la Ventana
aplicacion.title("Mi Restaurante - Sitema de Factruración")


# Color de fondo de la Ventana
# Lista de nombres: https://es.wikibooks.org/wiki/Python/Interfaz_gr%C3%A1fica_con_Tkinter/Los_nombres_de_los_colores
aplicacion.config(bg="burlywood") # bg = Background / Se puede usar rgb o lista de nombres.


# Panel Superior
# 1. Donde lo quieres ubicar, 2. Su borde (bd), 3. Relieve: "flat", "raised", "sunken", "groove", "ridge".
panel_superior = Frame(aplicacion, bd= 1, relief= "flat")
panel_superior.pack(side= "top") # Añadirlo a la ventana (side = sitio)


# Etiqueta Título
# 1. En que panel va la etiqueta, 2. Texto, 3. Color del texto (lo mismo que el color de fondo), 4. Font (tipo de letra) + Tamaño, 5. Color de Fondo, 5. Ancho.
etiqueta_titulo = Label(panel_superior, text="Sistema de Facturación", fg="azure4",
                        font=("Dosis", 48), bg="burlywood", width= 28)

etiqueta_titulo.grid(row=0, column=0) # Añadirlo a al ventana / Orden = Fila, Columna


# Panel Izquierdo
panel_izquierdo = Frame(aplicacion, bd= 1, relief= "flat")
panel_izquierdo.pack(side= "left")


# Panel Costos
panel_costos = Frame(panel_izquierdo, bd= 1, relief= "flat")
panel_costos.pack(side = "bottom")


# Panel Comidas
# LabelFrame es un panel que contiene integrada una etiqueta.
panel_comidas = LabelFrame(panel_izquierdo, text="Comida", font=("Dosis", 19, "bold"),
                           bd = 1, relief= "flat", fg="azure4")

panel_comidas.pack(side= "left")

# Panel Bebidas
# LabelFrame es un panel que contiene integrada una etiqueta.
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", font=("Dosis", 19, "bold"),
                           bd = 1, relief= "flat", fg="azure4")

panel_bebidas.pack(side= "left")

# Panel Postres
# LabelFrame es un panel que contiene integrada una etiqueta.
panel_postres = LabelFrame(panel_izquierdo, text="Postres", font=("Dosis", 19, "bold"),
                           bd = 1, relief= "flat", fg="azure4")

panel_postres.pack(side= "left")


# Panel Derecha
panel_derecha = Frame(aplicacion, bd= 1, relief= "flat")
panel_derecha.pack(side= "right")

# Panel Recibo
panel_recibo = Frame(panel_derecha, bd=1, relief="flat", bg="burlywood")
panel_recibo.pack() # Por defecto, se situa en la parte superior.


# Panel Botones
panel_botones = Frame(panel_derecha, bd=1, relief="flat", bg="burlywood")
panel_botones.pack()


# Panel Calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief="flat", bg="burlywood")
panel_calculadora.pack()


# Lista de Productos
lista_comidas = ["Pollo", "Cordero", "Kebab", "Pizza", "Merluza", "Salmon", "Macarrones", "Salchichas"]
lista_bebidas = ["Agua", "Cocacola", "Zumo", "Fanta Naranja", "Vino Tinto", "Cerveza", "Roncola", "Vodka"]
lista_postres = ["Helado", "Fruta", "Brownies", "Flan", "Mousse", "Pastel", "Tarta de Queso", "Tarta de Chocolate"]
variables_comida = []
variables_bebida = []
variables_postres = []



# Generar Items Comida
# Onvalue = Activado / Offvalue = Desactivado
Contador = 0
for comida in lista_comidas:
    variables_comida.append("")
    variables_comida[Contador] = IntVar() # Pone el valor del CheckButton
    comida = Checkbutton(panel_comidas, text= comida.title(), font=("Dosis", 19, "bold"),
                         onvalue= 1, offvalue= 0, variable= variables_comida[Contador])

    comida.grid(row= Contador, column= 0, sticky= W)
    Contador += 1


# Generar Items Bebida
# Onvalue = Activado / Offvalue = Desactivado
Contador = 0
for bebida in lista_bebidas:
    variables_bebida.append("")
    variables_bebida[Contador] = IntVar() # Pone el valor del CheckButton
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=("Dosis", 19, "bold"),
                         onvalue= 1, offvalue= 0, variable= variables_bebida[Contador])

    bebida.grid(row= Contador, column= 0, sticky= W)
    Contador += 1


# Generar Items Postres
# Onvalue = Activado / Offvalue = Desactivado
Contador = 0
for postres in lista_postres:
    variables_postres.append("")
    variables_postres[Contador] = IntVar() # Pone el valor del CheckButton
    postres = Checkbutton(panel_postres, text=postres.title(), font=("Dosis", 19, "bold"),
                         onvalue= 1, offvalue= 0, variable= variables_postres[Contador])

    postres.grid(row= Contador, column= 0, sticky= W)
    Contador += 1


# Evitar que la pantalla se cierre
aplicacion.mainloop()