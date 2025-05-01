# Librerias
from platform import release
from tkinter import * # Importar TKINTER (interfaz grafica)
import random
import datetime
from tkinter import filedialog, messagebox # Guardar


# Funciones de Calculadora
operador = ""
def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ""
    visor_calculadora.delete(0, END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ""

# Funcion de CheckButtoms
def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state= NORMAL)
            if cuadros_comida[x].get() == "0":
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus() # Poner el cursor enfocado

        else:
            cuadros_comida[x].config(state= DISABLED)
            texto_comida[x].set("0")

        x += 1

    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state= NORMAL)
            if cuadros_bebida[x].get() == "0":
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus() # Poner el cursor enfocado

        else:
            cuadros_bebida[x].config(state= DISABLED)
            texto_bebida[x].set("0")

        x += 1

    x = 0
    for c in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state= NORMAL)
            if cuadros_postres[x].get() == "0":
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus() # Poner el cursor enfocado

        else:
            cuadros_postres[x].config(state= DISABLED)
            texto_postres[x].set("0")

        x += 1

# Funcion de Calcular Total / Precios
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def total():
    # Comida
    sub_total_comida = 0
    indice = 0
    for cantidad in texto_comida:
        if cantidad.get() != "0":
            sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[indice])
        indice += 1


    # Bebida
    sub_total_bebidas = 0
    indice = 0
    for cantidad in texto_comida:
        if cantidad.get() != "0":
            sub_total_bebidas = sub_total_bebidas + (float(cantidad.get()) * precios_bebida[indice])
        indice += 1

    # Postres
    sub_total_postres = 0
    indice = 0
    for cantidad in texto_comida:
        if cantidad.get() != "0":
            sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[indice])
        indice += 1

    # Calcular Subtotal
    subtotal = sub_total_comida + sub_total_bebidas + sub_total_postres
    impuestos = subtotal * 0.07
    total = subtotal + impuestos

    # Insertar texto en variables de los textos
    var_costo_comida.set(f"{round(sub_total_comida, 2)} €")
    var_costo_bebida.set(f"{round(sub_total_bebidas, 2)} €")
    var_costo_postres.set(f"{round(sub_total_postres, 2)} €")
    var_subtotal.set(f"{round(subtotal, 2)} €")
    var_impuestos.set(f"{round(impuestos, 2)} €")
    var_total.set(f"{round(total, 2)} €")


# Funcion de Recibo
def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f"N# - {random.randint(1000, 9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.hour}"
    texto_recibo.insert(END, f"Datos:\t{num_recibo}\t\t\t{fecha_recibo}\n")
    texto_recibo.insert(END, f"*" * 75 + "\n")
    texto_recibo.insert(END, "Items\t\tCant.\t\tCosto Items\n")
    texto_recibo.insert(END, f"-" * 90 + "\n")

    x = 0
    for comida in texto_comida:
        if comida.get() != "0":
            texto_recibo.insert(END, f"{lista_comidas[x]}\t\t{comida.get()}\t\t{int(comida.get()) * precios_comida[x]} €\n")
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != "0":
            texto_recibo.insert(END, f"{lista_bebidas[x]}\t\t{bebida.get()}\t\t{int(bebida.get()) * precios_bebida[x]} €\n")
        x += 1

    x = 0
    for postres in texto_postres:
        if postres.get() != "0":
            texto_recibo.insert(END, f"{lista_postres[x]}\t\t{postres.get()}\t\t{int(postres.get()) * precios_postres[x]} €\n")
        x += 1

    texto_recibo.insert(END, f"-" * 90 + "\n")
    texto_recibo.insert(END, f"Costo de la Comida:\t\t\t{var_costo_comida.get()}\n")
    texto_recibo.insert(END, f"Costo de la Bebida:\t\t\t{var_costo_bebida.get()}\n")
    texto_recibo.insert(END, f"Costo de los Postres:\t\t\t{var_costo_postres.get()}\n")
    texto_recibo.insert(END, f"-" * 90 + "\n")
    texto_recibo.insert(END, f"Sub-Total:\t\t{var_subtotal.get()}\n")
    texto_recibo.insert(END, f"Impuestos:\t\t{var_impuestos.get()}\n")
    texto_recibo.insert(END, f"Total:\t\t{var_total.get()}\n")
    texto_recibo.insert(END, f"*" * 75 + "\n")
    texto_recibo.insert(END, "Lo esperamos pronto.")


# Funcion Guardar
def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode= "w", defaultextension=".txt") # Crear Archivo
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo("Información", "Su recibo ha sido guardado")


# Funcion Resetear
def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set("0")

    for texto in texto_bebida:
        texto.set("0")

    for texto in texto_postres:
        texto.set("0")

    for cuadro in cuadros_comida:
        cuadro.config(state= DISABLED)

    for cuadro in cuadros_bebida:
        cuadro.config(state= DISABLED)

    for cuadro in cuadros_postres:
        cuadro.config(state= DISABLED)

    for v in variables_comida:
        v.set(0)

    for v in variables_bebida:
        v.set(0)

    for v in variables_postres:
        v.set(0)

    var_costo_comida.set("")
    var_costo_bebida.set("")
    var_costo_postres.set("")
    var_subtotal.set("")
    var_impuestos.set("")
    var_total.set("")


# Incializar a Tkinter
aplicacion = Tk()


# Tamaño de la Ventana
aplicacion.geometry("1350x725+0+0") # Resolucion + x + y de la aparición en pantalla.


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
panel_costos = Frame(panel_izquierdo, bd= 1, relief= "flat", bg= "azure4", padx= 80)
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

# Panel Calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief="flat", bg="burlywood")
panel_calculadora.pack(side= "top")

# Panel Recibo
panel_recibo = Frame(panel_derecha, bd=1, relief="flat", bg="burlywood")
panel_recibo.pack() # Por defecto, se situa en la parte superior.

# Panel Botones
panel_botones = Frame(panel_derecha, bd=1, relief="flat", bg="burlywood")
panel_botones.pack(side="bottom")

# Lista de Productos
lista_comidas = ['pollo', 'coredero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']
variables_comida = []
variables_bebida = []
variables_postres = []
cuadros_comida = []
texto_comida = []
cuadros_bebida = []
texto_bebida = []
cuadros_postres = []
texto_postres = []


# Generar Items Comida
# Onvalue = Activado / Offvalue = Desactivado
Contador = 0
for comida in lista_comidas:
    # crear checkbutton
    variables_comida.append('')
    variables_comida[Contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold',),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[Contador],
                         command=revisar_check)

    comida.grid(row=Contador,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadros_comida.append("")
    texto_comida.append("")
    texto_comida[Contador] = StringVar()
    texto_comida[Contador].set(0)
    cuadros_comida[Contador] = Entry(panel_comidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state="disabled",
                                     textvariable=texto_comida[Contador])
    cuadros_comida[Contador].grid(row=Contador,
                                  column=1)
    Contador += 1


# Generar Items Bebida
# Onvalue = Activado / Offvalue = Desactivado
Contador = 0
for bebida in lista_bebidas:
    variables_bebida.append("")
    variables_bebida[Contador] = IntVar() # Pone el valor del CheckButton
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=("Dosis", 19, "bold"),
                         onvalue= 1,
                         offvalue= 0,
                         variable= variables_bebida[Contador],
                         command=revisar_check)

    bebida.grid(row= Contador,
                column= 0,
                sticky= W)

    # crear los cuadros de entrada
    cuadros_bebida.append("")
    texto_bebida.append("")
    texto_bebida[Contador] = StringVar()
    texto_bebida[Contador].set(0)
    cuadros_bebida[Contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state="disabled",
                                     textvariable=texto_bebida[Contador])

    cuadros_bebida[Contador].grid(row=Contador,
                                  column=1)
    Contador += 1


# Generar Items Postres
# Onvalue = Activado / Offvalue = Desactivado
Contador = 0
for postres in lista_postres:
    variables_postres.append("")
    variables_postres[Contador] = IntVar() # Pone el valor del CheckButton
    postres = Checkbutton(panel_postres,
                          text=postres.title(),
                          font=("Dosis", 19, "bold"),
                          onvalue= 1,
                          offvalue= 0,
                          variable= variables_postres[Contador],
                          command=revisar_check)

    postres.grid(row= Contador,
                 column= 0,
                 sticky= W)

    # crear los cuadros de entrada
    cuadros_postres.append("")
    texto_postres.append("")
    texto_postres[Contador] = StringVar()
    texto_postres[Contador].set(0)
    cuadros_postres[Contador] = Entry(panel_postres,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state="disabled",
                                     textvariable=texto_postres[Contador])

    cuadros_postres[Contador].grid(row=Contador,
                                  column=1)
    Contador += 1


# Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()


# Etiquetas de Costo y Campos de Entrada
# Comida
etiqueta_costo_comida = Label(panel_costos,
                              text= "Costo Comida",
                              font= ("Dosis", 12, "bold"),
                              bg= "azure4",
                              fg= "white")

etiqueta_costo_comida.grid(row= 0, column= 0)

texto_costo_comida = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd= 1,
                           width= 10,
                           state= "readonly",
                           textvariable= var_costo_comida)

texto_costo_comida.grid(row = 0, column= 1)

# Bebida
etiqueta_costo_bebida = Label(panel_costos,
                              text= "Costo Bebida",
                              font= ("Dosis", 12, "bold"),
                              bg= "azure4",
                              fg= "white")

etiqueta_costo_bebida.grid(row= 1, column= 0)

texto_costo_bebida = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd= 1,
                           width= 10,
                           state= "readonly",
                           textvariable= var_costo_bebida)

texto_costo_bebida.grid(row = 1, column= 1)

# Postres
etiqueta_costo_postres = Label(panel_costos,
                              text= "Costo Postres",
                              font= ("Dosis", 12, "bold"),
                              bg= "azure4",
                              fg= "white")

etiqueta_costo_postres.grid(row= 2, column= 0, padx= 41)

texto_costo_postres = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd= 1,
                           width= 10,
                           state= "readonly",
                           textvariable= var_costo_postres)

texto_costo_postres.grid(row = 2, column= 1, padx= 41)

# Subtotal
etiqueta_subtotal = Label(panel_costos,
                              text= "Subtotal",
                              font= ("Dosis", 12, "bold"),
                              bg= "azure4",
                              fg= "white")

etiqueta_subtotal.grid(row= 0, column= 2, padx= 41)

texto_subtotal = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd= 1,
                           width= 10,
                           state= "readonly",
                           textvariable= var_subtotal)

texto_subtotal.grid(row = 0, column= 3, padx= 41)

# Impuestos
etiqueta_impuestos = Label(panel_costos,
                              text= "Impuestos",
                              font= ("Dosis", 12, "bold"),
                              bg= "azure4",
                              fg= "white")

etiqueta_impuestos.grid(row= 1, column= 2, padx= 41)

texto_impuestos = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd= 1,
                           width= 10,
                           state= "readonly",
                           textvariable= var_impuestos)

texto_impuestos.grid(row = 1, column= 3, padx= 41)

# Total
etiqueta_total = Label(panel_costos,
                              text= "Costo Total",
                              font= ("Dosis", 12, "bold"),
                              bg= "azure4",
                              fg= "white")

etiqueta_total.grid(row= 2, column= 2, padx= 41)

texto_total = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd= 1,
                           width= 10,
                           state= "readonly",
                           textvariable= var_total)

texto_total.grid(row = 2, column= 3, padx= 41)


# Botones
botones = ["total", "recibo", "guardar", "resetear"]
botones_creados = []
columnas = 0

for boton in botones:
    boton = Button(panel_botones,
                   text= boton.title(),
                   font=("Dosis", 14, "bold"),
                   fg = "white",
                   bg = "azure4",
                   bd = 1,
                   width = 9)

    botones_creados.append(boton)

    boton.grid(row = 0, column = columnas)

    columnas += 1

botones_creados[0].config(command= total)
botones_creados[1].config(command= recibo)
botones_creados[2].config(command= guardar)
botones_creados[3].config(command= resetear)

# Area de Recibo
texto_recibo = Text(panel_recibo,
                    font=("Dosis", 12, "bold"),
                    bd= 1,
                    width= 50,
                    height= 10)

texto_recibo.grid(row = 0, column= 0, columnspan=20)


# Calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=38,
                          bd=1)

visor_calculadora.grid(row=0, column=0, columnspan=40)

# Calculadora Botones
botones_calculadora = ["7", "8", "9", "+", "4", "5", "6", "-",
                       "1", "2", "3", "x","R", "B", "0", "/"]
botones_guardados = []

fila = 1
columna = 0
for texto in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=texto,
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)

    boton.grid(row=fila, column=columna, padx=1, pady=1)
    botones_guardados.append(boton)

    columna += 1
    if columna == 4:
        columna = 0
        fila += 1


botones_guardados[0].config(command=lambda : click_boton("7"))
botones_guardados[1].config(command=lambda : click_boton("8"))
botones_guardados[2].config(command=lambda : click_boton("9"))
botones_guardados[3].config(command=lambda : click_boton("+"))
botones_guardados[4].config(command=lambda : click_boton("4"))
botones_guardados[5].config(command=lambda : click_boton("5"))
botones_guardados[6].config(command=lambda : click_boton("6"))
botones_guardados[7].config(command=lambda : click_boton("-"))
botones_guardados[8].config(command=lambda : click_boton("1"))
botones_guardados[9].config(command=lambda : click_boton("2"))
botones_guardados[10].config(command=lambda : click_boton("3"))
botones_guardados[11].config(command=lambda : click_boton("*"))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton("0"))
botones_guardados[15].config(command=lambda : click_boton("/"))


# Evitar que la pantalla se cierre
aplicacion.mainloop()