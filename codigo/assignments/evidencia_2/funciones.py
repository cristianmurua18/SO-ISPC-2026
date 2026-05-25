def es_primo(n): # Verifica si un número es primo
    if n <= 1:   # Los números <= 1 no son primos
        return False

    if n == 2:   # 2 es el único primo par
        return True

    if n % 2 == 0:  # Si es divisible por 2, no es primo
        return False

    for i in range(3, n, 2):    # Recorre solo números impares (optimización simple)
        if n % i == 0:   # Encontró divisor → no es primo
            return False
    return True     # Si no encontró divisores, es primo

def buscar_primos(inicio, fin):  # Función base: ejecuta el cálculo de forma secuencial
    primos_encontrados = []
    for numero in range(inicio, fin + 1):
        if es_primo(numero):
            primos_encontrados.append(numero)
    return primos_encontrados    # Devuelve la lista de resultados


def buscar_primos_thread(inicio, fin, resultado):     # Usa memoria compartida (lista resultado)
    primos = buscar_primos(inicio, fin)      # Cada thread agrega sus resultados a la lista compartida (varios threads escriben en la misma estructura)
    resultado.extend(primos)


def buscar_primos_mp(inicio, fin, cola):    # No comparte memoria → usa IPC (cola)
    try:
        print(f"START {inicio}-{fin}")

        primos = buscar_primos(inicio, fin)     # Cada proceso envía su resultado al proceso principal mediante la cola (Inter Process Communication)

        print(f"END {inicio}-{fin}")

        cola.put(primos)
        print(f"PUT OK {inicio}-{fin}")

    except Exception as e:
        print(f"ERROR en {inicio}-{fin}: {e}")

