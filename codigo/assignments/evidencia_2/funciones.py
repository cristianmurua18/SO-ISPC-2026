def es_primo(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True

def buscar_primos(inicio, fin):
    primos_encontrados = []
    for numero in range(inicio, fin + 1):
        if es_primo(numero):
            primos_encontrados.append(numero)
    return primos_encontrados

def buscar_primos_mp(inicio, fin, cola):
    primos_encontrados = []

    for numero in range(inicio, fin + 1, cola):

        if es_primo(numero):
            primos_encontrados.append(numero)

    cola.put(primos_encontrados)
