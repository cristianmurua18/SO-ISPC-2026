"""
Módulo: evidencia_2.py

Descripción:
    Menú interactivo que permite al usuario seleccionar y ejecutar tres estrategias
    diferentes de búsqueda de números primos (secuencial, multihilo, multiproceso)
    para comparar su rendimiento.
"""

from assignments.evidencia_2.funciones import (
    ejecutar_monohilo,
    ejecutar_multihilo,
    ejecutar_multiproceso,
)
from assignments.evidencia_2.mensajes import (
    CALCULANDO_PRIMOS_MONO,
    CALCULANDO_PRIMOS_MP,
    CALCULANDO_PRIMOS_MULTI,
    ERROR_MENU,
    ESPERANDO_RESULTADOS,
    MENU_PRINCIPAL,
    get_mensaje_exito,
)
from assignments.evidencia_2.constantes import LIMITE_SUPERIOR, RANGOS
from utils.clear_console import clear_console


def evidencia_2() -> None:
    """
    Controlador de menú para la Evidencia 2.

    Presenta opciones al usuario y delega la ejecución a las funciones
    correspondientes en el módulo de funciones.
    """
    while True:
        clear_console()

        try:
            menu = int(input(MENU_PRINCIPAL))
        except ValueError:
            clear_console()
            input(ERROR_MENU)
            continue

        if menu == 1:
            _mostrar_prueba_monohilo()

        elif menu == 2:
            _mostrar_prueba_multihilo()

        elif menu == 3:
            _mostrar_prueba_multiproceso()

        elif menu == 4:
            _mostrar_informe()

        elif menu == 0:
            clear_console()
            break

        else:
            clear_console()
            input('Opción no válida. Presione ENTER para continuar ')


def _mostrar_prueba_monohilo() -> None:
    """Muestra la interfaz y ejecuta la prueba secuencial."""
    clear_console()
    print('=== EJECUCIÓN MONOHILO EN PROCESO ===\n\n')
    print(CALCULANDO_PRIMOS_MONO)
    print(ESPERANDO_RESULTADOS)

    primos, tiempo = ejecutar_monohilo(LIMITE_SUPERIOR)
    input(get_mensaje_exito(primos, tiempo))


def _mostrar_prueba_multihilo() -> None:
    """Muestra la interfaz y ejecuta la prueba con threading."""
    clear_console()
    print('=== EJECUCIÓN MULTIHILOS EN PROCESO ===\n\n')
    print(CALCULANDO_PRIMOS_MULTI)
    print(ESPERANDO_RESULTADOS)

    primos, tiempo = ejecutar_multihilo(RANGOS)
    input(get_mensaje_exito(primos, tiempo))


def _mostrar_prueba_multiproceso() -> None:
    """Muestra la interfaz y ejecuta la prueba con multiprocessing."""
    clear_console()
    print('=== EJECUCIÓN EN VARIOS PROCESOS EN PROGRESO ===\n\n')
    print(CALCULANDO_PRIMOS_MP)
    print(ESPERANDO_RESULTADOS)

    primos, tiempo = ejecutar_multiproceso(RANGOS)
    input(get_mensaje_exito(primos, tiempo))


def _mostrar_informe() -> None:
    """Muestra la síntesis del informe técnico (en desarrollo)."""
    clear_console()
    input(
        '=== SÍNTESIS DEL INFORME TÉCNICO - ABP ===\n\n'
        + '-' * 130
        + '\nNOTA: VER INFORME ENTREGA FINAL ABP.\n'
        + '-' * 130
        + '\n\nPresione ENTER para continuar '
    )
