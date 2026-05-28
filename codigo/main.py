"""
Módulo: main.py

Descripción:
    Este es el punto de entrada principal del proyecto de Aprendizaje Basado en Proyectos (ABP)
    sobre Sistemas Operativos.
    
    El programa implementa un menú interactivo que permite acceder a diferentes evidencias
    y evaluaciones del proyecto, donde se analiza cómo el sistema operativo influye en el
    rendimiento de aplicaciones Python.
    
    Estructura del proyecto:
    - Evidencia 1: Propuesta y definición del proyecto
    - Evidencia 2: Primer codificación - Comparación de métodos de búsqueda de primos
    
    Grupo: "En Blanco"
    Asignatura: Sistemas Operativos - TSDS - 2026
    Docente: Nicolas Viale
"""

from utils.maximize_console import maximize_console
from utils.clear_console import clear_console
from assignments.evidencia_1.evidencia_1 import evidencia_1
from assignments.evidencia_2.evidencia_2 import evidencia_2

def main():
    """
    Función principal que controla el flujo del programa.
    
    Responsabilidades:
    1. Inicializa la interfaz (maximiza y limpia la consola)
    2. Muestra pantalla de bienvenida con información del proyecto y grupo
    3. Presenta un menú interactivo de opciones
    4. Direcciona al usuario hacia la evidencia seleccionada
    5. Valida la entrada del usuario
    
    Menú de opciones:
    - 1: Evidencia 1 - Propuesta y definición del proyecto (ya entregada)
    - 2: Evidencia 2 - Primer codificación del proyecto (en evaluación)
    - 0: Salir del programa
    """
    # PASO 1: Maximiza la consola a 25 líneas y limpia la pantalla
    maximize_console(25)
    clear_console()

    # PASO 2: Muestra pantalla de bienvenida con información del grupo y proyecto
    intro = input(
        'Presione F11 para maximizar la consola en windows\n\n'
        'Aprendizaje Basado en Proyectos (ABP)\n\nSistemas Operativos - TSDS - 2026\n\nNombre del grupo: "En Blanco"\n\nParticipantes:\nBattista, Mariano Iván\nGatica, Pablo Emiliano\nGonzalez, Javier Alexis\nMolina, Agustina\nMurua Ayosa, Christian José\nRanieri, Marysol\n\nDocente\nNicolas Viale\n\n\nPresione ENTER para continuar '
    )

    # PASO 3: Inicia bucle principal del menú (se repite hasta que el usuario elige salir)
    while True:
        # Limpia la pantalla antes de mostrar el menú
        clear_console()
        
        # Ajusta la altura de la consola para el menú (21 líneas)
        maximize_console(21)

        # PASO 4: Intenta obtener la opción del usuario
        try:
            # Muestra el menú principal con información del proyecto y opciones disponibles
            menu = int(
                input(
                    'Análisis del rendimiento de aplicaciones Python en función del sistema operativo.\n\nObjetivo:\nAnalizar cómo distintos mecanismos del sistema operativo afectan el rendimiento de una aplicación Python, mediante la implementación\nde diferentes estrategias de ejecución y su evaluación experimental.\n\nConsigna general:\nCada grupo deberá desarrollar una aplicación en Python y analizar su comportamiento bajo distintas condiciones de ejecución,\nevaluando el impacto de:\n\n* Procesos\n* Threads\n* I/O bloqueante vs asincrónico\n* Uso de memoria\n* (OPCIONAL) Contenedores\n\nEl objetivo es responder: ¿Cómo influye el sistema operativo en el rendimiento de una aplicación?\n\n\nA continuación, elija una opción:\n\n1 - Entrega Parcial 1 – Propuesta y definición del proyecto\nPresentación del problema a resolver, fundamentación, objetivos del proyecto (ENTREGADO)\n\n2 - Entrega Parcial 2 - Primer codificación\nPrimer entrega de parte de la codificación del caso elegido. Mínimo un 25% del total del proyecto (A EVALUAR)\n\n0 - Salir\n\n\n\nIngrese N° de opción: '
                ))

        # PASO 5: Captura el error si el usuario ingresa un valor que no es número
        except ValueError:
            clear_console()
            input(
                '¡ERROR!\n\nPor favor, ingrese un NÚMERO válido. Presione ENTER para continuar '
            )
            # Vuelve al inicio del bucle para mostrar el menú nuevamente
            continue

        # PASO 6: Procesa la opción del usuario según su elección
        if menu == 1:
            # Opción 1: Muestra Evidencia 1 (Propuesta y definición del proyecto)
            evidencia_1()

        elif menu == 2:
            # Opción 2: Muestra Evidencia 2 (Primer codificación del proyecto)
            evidencia_2()

        elif menu == 0:
            # Opción 0: Sale del programa
            # Limpia la pantalla antes de terminar
            clear_console()
            # Sale del bucle while, terminando la función main()
            break

        else:
            # Cualquier otra opción: Informa que es inválida
            clear_console()
            input('Opción no válida. Presione ENTER para continuar ')

# PUNTO DE ENTRADA DEL PROGRAMA
if __name__ == "__main__":
    """
    Punto de entrada principal del programa.
    
    Esta sentencia verifica que el archivo se ejecute directamente (no importado como módulo).
    Si es así, ejecuta la función main() que inicia el programa.
    """
    main()