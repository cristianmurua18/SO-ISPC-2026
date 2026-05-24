from utils.maximize_console import maximize_console
from utils.clear_console import clear_console
from assignments.evidencia_1.evidencia_1 import evidencia_1
from assignments.evidencia_2.evidencia_2 import evidencia_2

maximize_console(24)
clear_console()

intro = input(
    'Aprendizaje Basado en Proyectos (ABP)\n\nSistemas Operativos - TSDS - 2026\n\nEntrega Parcial 2 - Primer codificación\nPrimer entrega de parte de la codificación del caso elegido. Mínimo un 25% del total del proyecto.\n\nNombre del grupo: "En Blanco"\n\nParticipantes:\nBattista, Mariano Iván\nGatica, Pablo Emiliano\nGonzalez, Javier Alexis\nMolina, Agustina\nMurua Ayosa, Christian José\nRanieri, Marysol\n\nDocente\nNicolas Viale\n\n\nPresione ENTER para continuar '
)

while True:
    clear_console()

    try:
        menu = int(
            input(
                'Análisis del rendimiento de aplicaciones Python en función del sistema operativo.\n\nObjetivo:\nAnalizar cómo distintos mecanismos del sistema operativo afectan el rendimiento de una aplicación Python, mediante la implementación\nde diferentes estrategias de ejecución y su evaluación experimental.\n\nConsigna general:\nCada grupo deberá desarrollar una aplicación en Python y analizar su comportamiento bajo distintas condiciones de ejecución,\nevaluando el impacto de:\n\n* Procesos\n* Threads\n* I/O bloqueante vs asincrónico\n* Uso de memoria\n* (OPCIONAL) Contenedores\n\n\nA continuación, elija una opción:\n\n1 - Entrega Parcial 1 – Propuesta y definición del proyecto\nPresentación del problema a resolver, fundamentación, objetivos del proyecto (ENTREGADO)\n\n2 - Entrega Parcial 2 - Primer codificación\nPrimer entrega de parte de la codificación del caso elegido. Mínimo un 25% del total del proyecto (A EVALUAR)\n\n0 - Salir\n\n\n\nIngrese N° de opción: '
            ))

    except ValueError:
        clear_console()
        input(
            '¡ERROR!\n\nPor favor, ingrese un NÚMERO válido. Presione ENTER para continuar '
        )
        continue

    if menu == 1:
        evidencia_1()

    elif menu == 2:
        evidencia_2()

    elif menu == 0:
        clear_console()
        break

    else:
        clear_console()
        input('Opción no válida. Presione ENTER para continuar ')
