def Perfumeria(funcion):
    print("")
    print(f"Su turno es: P-{funcion}")
    print("Aguarde y espere a ser atendido")

def Farmacia(funcion):
    print("")
    print(f"Su turno es: F-{funcion}")
    print("Aguarde y espere a ser atendido")

def Cosmetica(funcion):
    print("")
    print(f"Su turno es: C-{funcion}")
    print("Aguarde y espere a ser atendido")


def Perfumeria_Cuenta():
    num = 1
    while True:
        yield num
        num += 1


def Farmacia_Cuenta():
    num = 1
    while True:
        yield num
        num += 1


def Cosmetica_Cuenta():
    num = 1
    while True:
        yield num
        num += 1


