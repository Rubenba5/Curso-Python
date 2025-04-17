Numero_Introducido = input("Dime un número: ")
Numero_Operado = input("Dime el numero que desea operar: ")
Solucion = ""
print("Por que desea operar:")
print("Multiplicar (1), Dividir (2), Sumar (3), Restar (4)")
Operador = int(input("Introduce el número: "))

if Operador == 1:
    Solucion = int(Numero_Introducido) * int(Numero_Operado)
    print(f"La solución de {Numero_Introducido} x {Numero_Operado} es igual a {Solucion}")

elif Operador == 2:
    Solucion = int(Numero_Introducido) / int(Numero_Operado)
    print(f"La solución de {Numero_Introducido} : {Numero_Operado} es igual a {Solucion}")

elif Operador == 3:
    Solucion = int(Numero_Introducido) + int(Numero_Operado)
    print(f"La solución de {Numero_Introducido} + {Numero_Operado} es igual a {Solucion}")

elif Operador == 4:
    Solucion = int(Numero_Introducido) - int(Numero_Operado)
    print(f"La solución de {Numero_Introducido} - {Numero_Operado} es igual a {Solucion}")

else:
    print("El caracter no es un número.")