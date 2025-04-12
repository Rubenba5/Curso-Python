def contar_primos(numero):
    if numero < 2:
        return 0

    primos = []

    for num in range(2, numero + 1):
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)

    return len(primos)


