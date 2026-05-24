import time
import math
from utils.clear_console import clear_console


def es_primo(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    limite = math.isqrt(n) + 1

    for i in range(3, limite, 2):
        if n % i == 0:
            return False
    return True


def evidencia_2():
    clear_console()

    print('=== EJECUCIÓN PARCIAL 2: VERSIÓN SECUENCIAL ===\n')

    limite_superior = 100000

    print(
        f'Calculando números primos desde el 1 hasta el {limite_superior}...')

    tiempo_inicio = time.time()

    primos_encontrados = []

    for numero in range(1, limite_superior, +1):
        if es_primo(numero):
            primos_encontrados.append(numero)

    tiempo_fin = time.time()

    tiempo_total = tiempo_fin - tiempo_inicio

    input(
        f'\n¡Cálculo finalizado con éxito!\nCantidad de números primos encontrados: {len(primos_encontrados)}\nTiempo total de ejecución: {tiempo_total: .4f} segundos\n\n\nPresione ENTER para continuar '
    )
