"""
Módulo: funciones.py

Descripción:
    Contiene la lógica de cálculo de números primos y las funciones de ejecución
    para cada estrategia de concurrencia (secuencial, multihilo, multiproceso).

    Se separa la lógica de cómputo de la interfaz de usuario para respetar
    el principio de responsabilidad única (SRP).
"""

import time
import threading
import multiprocessing
from queue import Empty


def es_primo(n: int) -> bool:
    """Verifica si un número es primo mediante división por tentativa."""
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    # Recorre solo impares — optimización de raíz cuadrada removida con fines didácticos
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True


def buscar_primos(inicio: int, fin: int) -> list[int]:
    """Busca números primos en el rango [inicio, fin] de forma secuencial."""
    primos_encontrados = []
    for numero in range(inicio, fin + 1):
        if es_primo(numero):
            primos_encontrados.append(numero)
    return primos_encontrados


def _buscar_primos_thread(
    inicio: int, fin: int, resultado: list[int], lock: threading.Lock
) -> None:
    """Wrapper para threading — agrega primos a lista compartida con Lock."""
    primos = buscar_primos(inicio, fin)
    with lock:
        resultado.extend(primos)


def _buscar_primos_mp(inicio: int, fin: int, cola: multiprocessing.Queue) -> None:
    """Wrapper para multiprocessing — deposita primos en la cola IPC."""
    primos = buscar_primos(inicio, fin)
    cola.put(primos)


# =============================================================================
# FUNCIONES DE EJECUCIÓN DE ESTRATEGIAS (SRP)
# =============================================================================


def ejecutar_monohilo(limite_superior: int) -> tuple[list[int], float]:
    """
    Ejecuta la búsqueda de primos de forma secuencial en un único hilo.

    Args:
        limite_superior: Número hasta el cual buscar primos (desde 1).

    Returns:
        Tupla con (lista de primos encontrados, tiempo de ejecución en segundos).
    """
    tiempo_inicio = time.time()
    primos_encontrados = buscar_primos(1, limite_superior)
    tiempo_total = time.time() - tiempo_inicio

    return primos_encontrados, tiempo_total


def ejecutar_multihilo(rangos: list[tuple[int, int]]) -> tuple[list[int], float]:
    """
    Ejecuta la búsqueda de primos dividiendo el trabajo entre múltiples hilos.

    Utiliza un Lock para proteger la escritura en la lista compartida,
    garantizando thread safety.

    Args:
        rangos: Lista de tuplas (inicio, fin) que definen los sub-rangos de búsqueda.

    Returns:
        Tupla con (lista de primos encontrados, tiempo de ejecución en segundos).
    """
    resultado: list[int] = []
    lock = threading.Lock()
    hilos: list[threading.Thread] = []

    tiempo_inicio = time.time()

    for inicio, fin in rangos:
        hilo = threading.Thread(
            target=_buscar_primos_thread,
            args=(inicio, fin, resultado, lock),
        )
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    tiempo_total = time.time() - tiempo_inicio

    return resultado, tiempo_total


def ejecutar_multiproceso(rangos: list[tuple[int, int]]) -> tuple[list[int], float]:
    """
    Ejecuta la búsqueda de primos creando un proceso independiente por cada rango.

    Cada proceso tiene su propio intérprete y memoria. Se comunica con el proceso
    principal mediante una Queue (IPC).

    Args:
        rangos: Lista de tuplas (inicio, fin) que definen los sub-rangos de búsqueda.

    Returns:
        Tupla con (lista de primos encontrados, tiempo de ejecución en segundos).
    """
    cola: multiprocessing.Queue = multiprocessing.Queue()
    procesos: list[multiprocessing.Process] = []

    tiempo_inicio = time.time()

    for inicio, fin in rangos:
        proceso = multiprocessing.Process(
            target=_buscar_primos_mp,
            args=(inicio, fin, cola),
        )
        procesos.append(proceso)
        proceso.start()

    for proceso in procesos:
        proceso.join()

    # Recopila resultados con timeout para evitar bloqueos indefinidos
    resultado: list[int] = []
    for _ in procesos:
        try:
            datos = cola.get(timeout=10)
            resultado.extend(datos)
        except Empty:
            break

    tiempo_total = time.time() - tiempo_inicio

    return resultado, tiempo_total

