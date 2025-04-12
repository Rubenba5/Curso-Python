def devolver_distintos(num1, num2, num3):

    Total = num1 + num2 + num3
    Minimo = min(num1, num2, num3)
    Maximo = max(num1, num2, num3)
    Valor_Medio = (num1 + num2 + num3) - Minimo - Maximo

    if Total > 15:
        return Maximo

    elif Total < 10:
        return Minimo

    elif Total in range(10,16):
        return Valor_Medio
