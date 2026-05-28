from utils.clear_console import clear_console


def evidencia_1():
    """
    Muestra la documentación y plan de trabajo del proyecto Evidencia 1.
    
    La función pausará la ejecución esperando que el usuario presione ENTER
    para continuar con el programa.
    """
    # Limpia la consola para mostrar una pantalla limpia
    clear_console()

    # Muestra el contenido del proyecto y espera confirmación del usuario
    input(
        '1- Opción elegida\n'
        'Opción A — Threads vs Procesos\n'
        'Se eligió comparar la ejecución de una misma aplicación en Python utilizando:\n'
        '● Hilos (threading)\n'
        '● Procesos (multiprocessing)\n\n'
        '2- Objetivo del proyecto\n'
        'El objetivo del proyecto es analizar cómo el sistema operativo influye en el rendimiento de\n'
        'una aplicación Python al ejecutar tareas concurrentes mediante hilos y procesos.\n'
        'En particular, se busca:\n'
        '● Comparar tiempos de ejecución entre threading y multiprocessing.\n'
        '● Analizar el uso de CPU y memoria en cada enfoque.\n'
        '● Comprender el impacto del sistema operativo en la planificación, la creación de\n'
        '  procesos e hilos y la administración de recursos.\n'
        '● Relacionar los resultados experimentales con conceptos vistos en la materia como:\n'
        '  o Ciclo de vida del proceso\n'
        '  o Planificación de CPU\n'
        '  o Exclusión mutua\n'
        '  o Modo usuario y kernel\n'
        '  o Uso de memoria\n\n'
        'Además, se evaluará cómo el Global Interpreter Lock (GIL) de Python condiciona el uso de hilos\n'
        'frente a procesos y cómo el sistema operativo maneja múltiples procesos de manera más\n'
        'eficiente en tareas intensivas de CPU.\n\n'
        '3- Plan de trabajo\n'
        'El proyecto se desarrollará siguiendo los siguientes pasos:\n\n'
        'A. Definición del problema\n'
        'Se implementará una aplicación en Python que realice una tarea intensiva de CPU (por ejemplo,\n'
        'cálculos matemáticos repetitivos) para que el uso de concurrencia tenga impacto real en el\n'
        'rendimiento.\n\n'
        'B. Implementation de versiones\n'
        'Se desarrollarán al menos dos versiones del mismo programa:\n'
        '● Versión secuencial (como referencia)\n'
        '● Versión con threading\n'
        '● Versión con multiprocessing\n'
        'Cada versión realizará exactamente la misma tarea para asegurar una comparación justa.\n\n'
        'C. Ejecución de experimentos\n'
        'Cada versión será ejecutada múltiples veces para obtener valores promedio, midiendo:\n'
        '● Tiempo total de ejecución\n'
        '● Uso de CPU\n'
        '● Consumo de memoria\n'
        'Las mediciones se realizarán utilizando herramientas del sistema operativo (por ejemplo,\n'
        'administrador de tareas o comandos del sistema) y bibliotecas básicas de Python.\n\n'
        'D. Análisis de resultados\n'
        'Los resultados se compararán mediante tablas y/o gráficos, analizando:\n'
        '● Diferencias de rendimiento entre hilos y procesos\n'
        '● Comportamiento del sistema operativo al planificar procesos vs hilos\n'
        '● Impacto del GIL en Python\n'
        '● Relación entre teoría y resultados observados\n\n'
        'E. Organización del equipo\n'
        'El trabajo se dividirá en tareas como:\n'
        '● Desarrollo del código\n'
        '● Ejecución de pruebas\n'
        '● Registro de mediciones\n'
        '● Análisis teórico\n'
        '● Redacción del informe\n'
        'Todos los integrantes participarán tanto en la parte práctica como en la teórica.\n\n\n'
        'Presione ENTER para continuar ')
