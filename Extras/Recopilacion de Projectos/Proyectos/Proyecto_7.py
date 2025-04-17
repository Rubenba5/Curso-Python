# Librerias
from os import system

# Clase Persona Información
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apelllido = apellido


# Clase Cliente del Banco
class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Usted se llama {self.nombre} {self.apelllido}, su número de cuenta es {self.numero_cuenta} con un balance de {self.balance}€."

    def depositar(self):
        Cantidad = int(input("Cuánto desea depositar en su cuenta: "))
        self.balance += Cantidad
        print(f"Su cuenta ahora tiene un saldo de {self.balance}€")

    def retirar(self):

        Cantidad = int(input("Cuánto desea retirar en su cuenta: "))
        if self.balance > Cantidad:
            self.balance -= Cantidad
            print(f"Su cuenta ahora tiene un saldo de {self.balance}€")

        else:
            print("No tienes suficiente saldo para poder retirar dicha cantidad.")


# Funciones
def crear_cliente():
    Nombre = input("Introduce tu nombre: ")
    Apellido = input("Introduce tu apellido: ")
    Numero_Cuenta = input("Introduce el número de cuenta deseado: ")
    Cliente_Nuevo = Cliente(Nombre, Apellido, Numero_Cuenta, 0 )
    return Cliente_Nuevo


def inicio(cliente):
    Bucle = 0
    while Bucle == 0:
        print("")
        print(f"Bienvenido, {cliente.nombre} ({cliente.numero_cuenta})")
        print(f"Su saldo es de {cliente.balance}€")
        print("Puede Depositar(1), Retirar(2) o Salir(3)")
        Accion = input("Que desea hacer: ")

        if Accion == "1":
            cliente.depositar()

        elif Accion == "2":
            cliente.retirar()

        elif Accion == "3":
            Bucle = 1
            quit()


# Ejecucion
cliente_nuevo = crear_cliente()
inicio(cliente_nuevo)





