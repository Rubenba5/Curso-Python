def ejericio_2(palabra):
    lista = []

    for letra in palabra:
        lista.append(letra)

    lista_sin_repetidos = list(dict.fromkeys(lista))
    lista_sin_repetidos.sort()

    return(lista_sin_repetidos)

d = ejericio_2("entretenido")
print(d)