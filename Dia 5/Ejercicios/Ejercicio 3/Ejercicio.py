def ejercicio_3(*args):

    lista = list(args)
    posicion_0 = lista.index(0)
    posicion_siguiente = lista[posicion_0 + 1]

    if posicion_siguiente == 0:
        return True

    else:
        return False





