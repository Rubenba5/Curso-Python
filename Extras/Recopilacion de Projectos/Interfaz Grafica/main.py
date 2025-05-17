# Importar Interfaz Gráfica
from tkinter import *
from pathlib import Path

# Importar Archivos
import models
import functions

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
    aplicacion = Tk()


    # Dimensiones de la aplicación
    aplicacion.geometry("1000x600+460+240")


    # No Maximizar
    aplicacion.resizable(False, False)


    # Título / Fondo / Icono
    aplicacion.title("Recopilación de Proyectos - Rubén Blasco Armengod")
    aplicacion.config(bg=COLOR_FONDO)
    aplicacion.iconbitmap(Path(ruta, "icono.ico"))


    # Paneles
    panel_arriba = Frame(aplicacion, bd=1, relief="raised", bg=COLOR_PANEL)
    panel_arriba.pack(side="top")

    panel_abajo = Frame(aplicacion, bd=1, relief="raised", bg=COLOR_PANEL)
    panel_abajo.pack(side="bottom")

    panel_abajo_derecha = Frame(panel_abajo, bd=0, relief="raised", bg=COLOR_PANEL)
    panel_abajo_derecha.pack(side="right")

    panel_izquierdo = Frame(aplicacion, bd=0, relief="raised", bg=COLOR_FONDO)
    panel_izquierdo.pack(side="left", fill="x")

    panel_derecho = Frame(aplicacion, bd=1, relief="raised", bg=COLOR_PANEL)
    panel_derecho.pack(side="right", padx=48)

    panel_texto = Frame(panel_izquierdo, bd=0, relief="raised", bg=COLOR_FONDO)
    panel_texto.pack(side="top")

    panel_scrollbar = Frame(panel_izquierdo, bd=0, relief="raised", bg=COLOR_FONDO)
    panel_scrollbar.pack(fill="both")

    panel_boton = Frame(panel_izquierdo, bd=0, relief="raised", bg=COLOR_FONDO)
    panel_boton.pack(side="bottom")


    # Etiquetas
    etiqueta_titulo_principal = Label(panel_arriba,
                                      text="Recopilación de Proyectos - Python Total",
                                      fg=COLOR_TITULO,
                                      font=("NotoSansCJKTC", 15),
                                      width=100,
                                      bg=COLOR_PANEL)

    etiqueta_titulo_principal.pack(side="top")

    etiqueta_titulo_principal2 = Label(panel_abajo_derecha,
                                       text="",
                                       fg=COLOR_TITULO,
                                       font=("NotoSansCJKTC", 15),
                                       width=130,
                                       bg=COLOR_PANEL)

    etiqueta_titulo_principal2.pack(side="bottom")

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
    listbox = Listbox(panel_izquierdo,
                      width=22,
                      height=16,
                      selectbackground= COLOR_SELECCION,
                      selectforeground= COLOR_TITULO,
                      font=("NotoSansCJKTC", 10),
                      bg= COLOR_PANEL,
                      fg= COLOR_TEXTO,
                      bd=1,
                      relief="flat")

    listbox.pack(padx=5, pady=5)

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
    boton_ejecutar = Button(panel_boton,
                            text="Ejecutar",
                            fg="#FFFFFF",
                            bg=COLOR_BOTON,
                            bd=3,
                            font=("NotoSansCJKTC", 10),
                            width=10,
                            activebackground=COLOR_BOTON_PULSADO)

    boton_ejecutar.grid(row=9, column=1, padx= 10)
    boton_ejecutar.config(command=lambda: functions.boton(listbox))

    # Botón de Información
    boton_informacion = Button(panel_boton,
                            text="Información",
                            fg="#FFFFFF",
                            bg= "#c2c3c2",
                            bd=3,
                            font=("NotoSansCJKTC", 10),
                            width=10,
                            activebackground= "#969996")

    boton_informacion.grid(row=9, column=0)
    boton_informacion.config(command=lambda: functions.informacion)

    # Iniciar la aplicación
    aplicacion.mainloop()


# Detección de Errores
except SyntaxError:
    print("")
    print("🚨⏐ ¡Error detectado! (SyntaxError)")
    functions.errores("🚨⏐ ¡Error detectado! (SyntaxError)", panel_abajo_derecha)

except NameError:
    print("")
    print("🚨⏐ ¡Error detectado! (NameError)")
    functions.errores("🚨⏐ ¡Error detectado! (NameError)", panel_abajo_derecha)

except TypeError:
    print("")
    print("🚨⏐ ¡Error detectado! (TypeError)")
    functions.errores("🚨⏐ ¡Error detectado! (TypeError)", panel_abajo_derecha)

except ValueError:
    print("")
    print("🚨⏐ ¡Error detectado! (ValueError)")
    functions.errores("🚨⏐ ¡Error detectado! (ValueError)", panel_abajo_derecha)

except KeyError:
    print("")
    print("🚨⏐ ¡Error detectado! (KeyError)")
    functions.errores("🚨⏐ ¡Error detectado! (KeyError)", panel_abajo_derecha)

except AttributeError:
    print("")
    print("🚨⏐ ¡Error detectado! (AttributeError)")
    functions.errores("🚨⏐ ¡Error detectado! (AttributeError)", panel_abajo_derecha)

except ZeroDivisionError:
    print("")
    print("🚨⏐ ¡Error detectado! (ZeroDivisionError)")
    functions.errores("🚨⏐ ¡Error detectado! (ZeroDivisionError)", panel_abajo_derecha)

except (ModuleNotFoundError, ImportError):
    print("")
    print("🚨⏐ ¡Error detectado! (ImportError / ModuleNotFoundError)")
    functions.errores("🚨⏐ ¡Error detectado! (ImportError / ModuleNotFoundError)", panel_abajo_derecha)

except FileNotFoundError:
    print("")
    print("🚨⏐ ¡Error detectado! (FileNotFoundError)")
    functions.errores("🚨⏐ ¡Error detectado! (FileNotFoundError)", panel_abajo_derecha)

except PermissionError:
    print("")
    print("🚨⏐ ¡Error detectado! (PermissionError)")
    functions.errores("🚨⏐ ¡Error detectado! (PermissionError)", panel_abajo_derecha)

except IOError:
    print("")
    print("🚨⏐ ¡Error detectado! (IOError)")
    functions.errores("🚨⏐ ¡Error detectado! (IOError)", panel_abajo_derecha)

except RuntimeError:
    print("")
    print("🚨⏐ ¡Error detectado! (RuntimeError)")
    functions.errores("🚨⏐ ¡Error detectado! (RuntimeError)", panel_abajo_derecha)

# Errores específicos de Tkinter
except tkinter.TclError:
    print("")
    print("🚨⏐ ¡Error detectado! (Tkinter TclError)")
    functions.errores("🚨⏐ ¡Error detectado! (Tkinter TclError)", panel_abajo_derecha)

