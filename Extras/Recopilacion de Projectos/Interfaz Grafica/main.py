# Importar Interfaz Gráfica
import tkinter
from tkinter import *
from CTkListbox import *
import customtkinter as ctk

# Importar Otras Librerias
from pathlib import Path

# Importar Archivos
import models
import functions

# Funcion Errores
def errores(error):
    global panel_abajo_derecha

    if panel_abajo_derecha.winfo_children():
        for elemento in panel_abajo_derecha.winfo_children():
            elemento.destroy()

    etiqueta_titulo_principal = ctk.CTkLabel(panel_abajo_derecha,
                                       text=f"{error}",
                                       text_color="#343A40",
                                       font=("NotoSansCJKTC", 15),
                                       width=1000,
                                       fg_color="#FFFFFF")

    etiqueta_titulo_principal.pack(side="bottom")


# Flujo de errores
try:

    # Colores Modernos
    COLOR_FONDO = "#F8F9FA"
    COLOR_PANEL = "#FFFFFF"
    COLOR_TITULO = "#343A40"
    COLOR_BOTON = "#168ae2"
    COLOR_BOTON_PULSADO = "#0f6db5"
    COLOR_SELECCION = "#E9ECEF"
    COLOR_TEXTO = "#343A40"


    # Ruta
    ruta = Path(Path.home(), "Proyectos", "Interfaz_Grafica")

    # Iniciar tkinter
    aplicacion = ctk.CTk()


    # Dimensiones de la aplicación
    aplicacion.geometry("1000x600+460+240")


    # No Maximizar
    aplicacion.resizable(False, False)


    # Título / Fondo / Icono
    aplicacion.title("Recopilación de Proyectos - Rubén Blasco Armengod")
    aplicacion.config(bg= COLOR_FONDO)
    aplicacion.iconbitmap(Path(ruta, "icono.ico"))


    # Paneles
    panel_arriba = ctk.CTkFrame(aplicacion, border_width=1, fg_color=COLOR_PANEL)
    panel_arriba.pack(side="top")

    panel_abajo = ctk.CTkFrame(aplicacion, border_width=0,  fg_color=COLOR_PANEL)
    panel_abajo.pack(side="bottom")

    panel_abajo_derecha = ctk.CTkFrame(panel_abajo, border_width=1, fg_color=COLOR_PANEL)
    panel_abajo_derecha.pack(side="right")

    panel_izquierdo = Frame(aplicacion, bg=COLOR_FONDO)
    panel_izquierdo.pack(side="left", padx= 10)

    panel_derecho = ctk.CTkFrame(aplicacion, border_width=1, fg_color=COLOR_PANEL, corner_radius=10)
    panel_derecho.pack_forget()

    panel_texto = ctk.CTkFrame(panel_izquierdo, border_width=0, fg_color=COLOR_FONDO)
    panel_texto.pack(side="top")

    panel_boton = Frame(panel_izquierdo, bd=0, bg=COLOR_FONDO)
    panel_boton.pack(side="bottom")


    # Etiquetas
    etiqueta_titulo_principal = ctk.CTkLabel(panel_arriba,
                                      text="Recopilación de Proyectos - Python Total",
                                      text_color= "#000000",
                                      font=("NotoSansCJKTC", 15),
                                      width=1000,
                                      bg_color= COLOR_PANEL)

    etiqueta_titulo_principal.pack(side="top")

    errores("")


    etiqueta_titulo = Label(panel_texto,
                            text="¡Bienvenido de Nuevo!",
                            fg=COLOR_TEXTO,
                            font=("NotoSansCJKTC", 20),
                            width=20,
                            bg=COLOR_FONDO)

    etiqueta_titulo.grid(row=3, column=0)

    etiqueta_descripcion = Label(panel_texto,
                                 text='Elige un proyecto para ejecutar',
                                 fg=COLOR_TEXTO,
                                 font=("NotoSansCJKTC", 13),
                                 width=30,
                                 bg=COLOR_FONDO)

    etiqueta_descripcion.grid(row=6, column=0)

    # Listbox
    # https://github.com/Akascape/CTkListbox
    listbox = CTkListbox(panel_izquierdo,
                      width=22,
                      height=250,
                      button_color= "#ffffff",
                      highlight_color= "#d1d5db",
                      font=("NotoSansCJKTC", 11),
                      fg_color= "#f0f2f5",
                      border_color= "#d1d5db",
                      hover_color= "#d1d5db",
                      )

    listbox.pack(pady= 5)
    listbox.bind("<Double-1>", lambda event: functions.boton(listbox, panel_derecho, COLOR_PANEL))

    # Agregar elementos al Listbox
    listbox.insert(END, f"{models.Data_1.dia}: {models.Data_1.titulo}")
    listbox.insert(END, f"{models.Data_2.dia}: {models.Data_2.titulo}")
    listbox.insert(END, f"{models.Data_3.dia}: {models.Data_3.titulo}")
    listbox.insert(END, f"{models.Data_4.dia}: {models.Data_4.titulo}")
    listbox.insert(END, f"{models.Data_5.dia}: {models.Data_5.titulo}")
    listbox.insert(END, f"{models.Data_6.dia}: {models.Data_6.titulo}")
    listbox.insert(END, f"{models.Data_7.dia}: {models.Data_7.titulo}")
    listbox.insert(END, f"{models.Data_8.dia}: {models.Data_8.titulo}")
    listbox.insert(END, f"{models.Data_9.dia}: {models.Data_9.titulo}")
    listbox.insert(END, f"{models.Data_10.dia}: {models.Data_10.titulo}")
    listbox.insert(END, f"{models.Data_11.dia}: {models.Data_11.titulo}")
    listbox.insert(END, f"{models.Data_12.dia}: {models.Data_12.titulo}")
    listbox.insert(END, f"{models.Data_13.dia}: {models.Data_13.titulo}")
    listbox.insert(END, f"{models.Data_14.dia}: {models.Data_14.titulo}")
    listbox.insert(END, f"{models.Data_15.dia}: {models.Data_15.titulo}")
    listbox.insert(END, f"{models.Data_16.dia}: {models.Data_16.titulo}")

    listbox.pack(fill= "both", pady= 20, padx= 48)


    # Botón de Ejecutar
    boton_ejecutar = ctk.CTkButton(panel_boton,
                            text="Ejecutar",
                            fg_color= COLOR_BOTON,
                            border_width=2,
                            font=("NotoSansCJKTC", 13),
                            width= 90,
                            height= 30,
                            corner_radius= 5,
                            border_color= "#2c3e50",
                            command= lambda: functions.boton(listbox, panel_derecho, COLOR_PANEL))

    boton_ejecutar.grid(row=9, column=1, padx= 13)


    # Botón de Información
    boton_informacion = ctk.CTkButton(panel_boton,
                            text = "Información",
                            fg_color = "#c2c3c2",
                            border_width = 2,
                            font = ("NotoSansCJKTC", 13),
                            width = 90,
                            height = 30,
                            corner_radius = 5,
                            text_color= "#FFFFFF",
                            border_color= "#2c3e50",
                            command = lambda: functions.informacion(panel_derecho, COLOR_PANEL))

    boton_informacion.grid(row=9, column=0)


    # Iniciar la aplicación
    aplicacion.mainloop()


# Detección de Errores
except SyntaxError:
    print("")
    print("🚨⏐ ¡Error detectado! (SyntaxError)")
    errores("🚨⏐ ¡Error detectado! (SyntaxError)")

except NameError as e:
    print("")
    print(f"🚨⏐ ¡Error detectado! (NameError){e}")
    errores("🚨⏐ ¡Error detectado! (NameError)")

except TypeError:
    print("")
    print(f"🚨⏐ ¡Error detectado! (TypeError)")
    errores("🚨⏐ ¡Error detectado! (TypeError)")

except ValueError:
    print("")
    print("🚨⏐ ¡Error detectado! (ValueError)")
    errores("🚨⏐ ¡Error detectado! (ValueError)")

except KeyError:
    print("")
    print("🚨⏐ ¡Error detectado! (KeyError)")
    errores("🚨⏐ ¡Error detectado! (KeyError)")

except AttributeError:
    print("")
    print("🚨⏐ ¡Error detectado! (AttributeError)")
    errores("🚨⏐ ¡Error detectado! (AttributeError)")

except ZeroDivisionError:
    print("")
    print("🚨⏐ ¡Error detectado! (ZeroDivisionError)")
    errores("🚨⏐ ¡Error detectado! (ZeroDivisionError)")

except (ModuleNotFoundError, ImportError):
    print("")
    print("🚨⏐ ¡Error detectado! (ImportError / ModuleNotFoundError)")
    errores("🚨⏐ ¡Error detectado! (ImportError / ModuleNotFoundError)")

except FileNotFoundError:
    print("")
    print("🚨⏐ ¡Error detectado! (FileNotFoundError)")
    errores("🚨⏐ ¡Error detectado! (FileNotFoundError)")

except PermissionError:
    print("")
    print("🚨⏐ ¡Error detectado! (PermissionError)")
    errores("🚨⏐ ¡Error detectado! (PermissionError)")

except IOError:
    print("")
    print("🚨⏐ ¡Error detectado! (IOError)")
    errores("🚨⏐ ¡Error detectado! (IOError)")

except RuntimeError:
    print("")
    print("🚨⏐ ¡Error detectado! (RuntimeError)")
    errores("🚨⏐ ¡Error detectado! (RuntimeError)")

# Errores específicos de Tkinter
except tkinter.TclError:
    print("")
    print(f"🚨⏐ ¡Error detectado! (Tkinter TclError)")
    errores("🚨⏐ ¡Error detectado! (Tkinter TclError)")

