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
    for n in range(1, 1001):
        yield n


def Farmacia_Cuenta():
    for n in range(1, 1001):
        yield n


def Cosmetica_Cuenta():
    for n in range(1, 1001):
        yield n



