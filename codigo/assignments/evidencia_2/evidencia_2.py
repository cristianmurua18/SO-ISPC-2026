"""
Módulo: evidencia_2.py

Descripción:
    Este módulo implementa un programa que compara el rendimiento de tres métodos
    diferentes para buscar números primos en un rango específico:
    
    1. MONOHILO: Búsqueda secuencial en un único hilo (línea base)
    2. MULTIHILOS: Búsqueda paralela usando threading (múltiples hilos en un proceso)
    3. MULTIPROCESOS: Búsqueda paralela usando multiprocessing (múltiples procesos)
    
    El objetivo es medir y comparar tiempos de ejecución, uso de CPU y memoria
    para analizar el impacto del GIL de Python y la planificación del SO.
"""

import time
from assignments.evidencia_2.funciones import es_primo, buscar_primos, buscar_primos_thread, buscar_primos_mp
from assignments.evidencia_2.mensajes import CALCULANDO_PRIMOS_MONO, CALCULANDO_PRIMOS_MP, CALCULANDO_PRIMOS_MULTI, ERROR_MENU, ESPERANDO_RESULTADOS, MENU_PRINCIPAL, get_mensaje_exito
from assignments.evidencia_2.constantes import LIMITE_SUPERIOR, RANGOS
from utils.clear_console import clear_console
import threading
import multiprocessing

def evidencia_2():
    """
    Función principal que implementa un menú interactivo para comparar
    tres métodos de búsqueda de números primos.
    
    Flujo:
        1. Muestra un menú con opciones (1: Monohilo, 2: Multihilos, 3: Multiprocesos)
        2. Según la opción, ejecuta el método correspondiente
        3. Mide el tiempo de ejecución
        4. Muestra los resultados
        5. Repite hasta que el usuario selecciona salir (opción 0)
    """
    while True:
        # Limpia la pantalla y muestra el menú principal
        clear_console()

        # Intenta obtener la opción del menú del usuario
        try:
            menu = int(input(MENU_PRINCIPAL))                                                                                                                                                                               

        # Si el usuario ingresa un valor que no es número, captura la excepción
        except ValueError:
            clear_console()
            input(ERROR_MENU)
            continue

        # ========== OPCIÓN 1: BÚSQUEDA MONOHILO (SECUENCIAL) ==========
        if menu == 1:
            """
            Método secuencial: Un único hilo busca todos los números primos.
            Este es el método de referencia para comparar con los otros métodos.
            
            Proceso:
            1. Se ejecuta un único hilo que busca primos desde 1 hasta LIMITE_SUPERIOR
            2. Se mide el tiempo de inicio y fin
            3. Se calcula el tiempo total empleado
            """
            clear_console()

            print('=== EJECUCIÓN MONOHILO EN PROCESO ===\n\n')

            # Muestra mensaje informativo
            print(CALCULANDO_PRIMOS_MONO)

            # Indica que se espera por los resultados
            print(ESPERANDO_RESULTADOS)

            # Registra el tiempo de inicio
            tiempo_inicio = time.time()

            # PASO 1: Busca todos los números primos en el rango completo (método secuencial)
            primos_encontrados = buscar_primos(1 , LIMITE_SUPERIOR)

            # Registra el tiempo de finalización
            tiempo_fin = time.time()

            # PASO 2: Calcula el tiempo total de ejecución
            tiempo_total = tiempo_fin - tiempo_inicio

            # Muestra los resultados: cantidad de primos y tiempo empleado
            input(get_mensaje_exito(primos_encontrados, tiempo_total))

        # ========== OPCIÓN 2: BÚSQUEDA MULTIHILOS (THREADING) ==========
        elif menu == 2:
            """
            Método con múltiples hilos (threading):
            Se dividen los rangos de búsqueda entre varios hilos que ejecutan
            simultáneamente en el mismo proceso (comparten memoria).
            
            Nota: El GIL (Global Interpreter Lock) limita el paralelismo real en Python.
            
            Proceso:
            1. Se divide el rango de números en RANGOS
            2. Se crea un hilo por cada rango
            3. Todos los hilos se inician simultáneamente
            4. Se espera a que todos terminen (join)
            5. Se recopilan los resultados
            """
            clear_console()

            print('=== EJECUCIÓN MULTIHILOS EN PROCESO ===\n\n')

            # Muestra mensaje informativo
            print(CALCULANDO_PRIMOS_MULTI)

            # Indica que se espera por los resultados
            print(ESPERANDO_RESULTADOS)

            # Registra el tiempo de inicio
            tiempo_inicio = time.time()

            # PASO 1: Inicializa una lista compartida para almacenar resultados de todos los hilos
            resultado = []       # Los hilos escribirán en esta lista compartida
            hilos = []           # Lista para guardar referencias a los hilos creados

            # PASO 2: Crea un hilo por cada rango de búsqueda
            for inicio, fin in RANGOS:     
                # Crea un nuevo hilo que ejecutará la función buscar_primos_thread
                hilo = threading.Thread(
                    target=buscar_primos_thread,
                    args=(inicio, fin, resultado)  # Pasa el rango y la lista compartida
                )
                hilos.append(hilo)      # Guarda la referencia del hilo en la lista
                hilo.start()            # Inicia la ejecución del hilo (cede control al SO)

            # PASO 3: Espera a que todos los hilos terminen su ejecución
            for hilo in hilos:      
                hilo.join()             # Bloquea hasta que el hilo termine

            # Registra el tiempo de finalización
            tiempo_fin = time.time()

            # PASO 4: Calcula el tiempo total de ejecución
            tiempo_total = tiempo_fin - tiempo_inicio

            # Muestra los resultados: cantidad de primos y tiempo empleado
            input(get_mensaje_exito(resultado, tiempo_total))
        
        # ========== OPCIÓN 3: BÚSQUEDA MULTIPROCESOS (MULTIPROCESSING) ==========
        elif menu == 3:
            """
            Método con múltiples procesos (multiprocessing):
            Se crea un proceso independiente del SO para cada rango de búsqueda.
            Cada proceso tiene su propio intérprete de Python y memoria.
            
            Ventaja: Evita las limitaciones del GIL, permite paralelismo real en CPUs multinúcleo.
            
            Proceso:
            1. Se crea un Manager para compartir datos entre procesos (IPC)
            2. Se crea una Cola (Queue) para comunicación entre procesos
            3. Se crea un proceso independiente por cada rango
            4. El SO asigna CPU a cada proceso
            5. Se espera a que todos terminen (join)
            6. Se recopilan los resultados de la Cola
            """
            clear_console()

            print('=== EJECUCIÓN EN VARIOS PROCESOS EN PROGRESO ===\n\n')

            # Muestra mensaje informativo
            print(CALCULANDO_PRIMOS_MP)

            # Indica que se espera por los resultados
            print(ESPERANDO_RESULTADOS)

            # Registra el tiempo de inicio
            tiempo_inicio = time.time()

            # PASO 1: Crea un Manager para permitir compartir datos entre procesos
            manager = multiprocessing.Manager() # Manager crea un objeto que permite IPC (Inter-Process Communication)
            
            # PASO 2: Crea una Cola (queue) para comunicación sincronizada entre procesos
            cola = manager.Queue()    # Cada proceso depositará sus resultados aquí
            procesos = []             # Lista para guardar referencias a los procesos creados

            # PASO 3: Crea un proceso independiente por cada rango de búsqueda
            for inicio, fin in RANGOS:
                # Crea un nuevo proceso que ejecutará la función buscar_primos_mp
                # Cada proceso es independiente con su propia memoria e intérprete de Python
                proceso = multiprocessing.Process(
                    target=buscar_primos_mp,
                    args=(inicio, fin, cola)  # Pasa el rango y la cola para resultados
                )
                procesos.append(proceso)      # Guarda la referencia del proceso
                proceso.start() # Inicia el proceso (el SO asigna CPU y recursos)

            print(f"Procesos creados: {len(procesos)}")
                    
            # PASO 4: Espera a que TODOS los procesos terminen su ejecución
            for proceso in procesos:    
                proceso.join()          # Bloquea hasta que el proceso termine
            print("Procesos terminados, leyendo resultados...")   
            
            # PASO 5: Recopila los resultados de cada proceso desde la Cola
            resultado = []

            for i in range(len(procesos)):
                print(f"Recibiendo resultado {i+1}")
                # Obtiene los datos que cada proceso depositó en la cola
                datos = cola.get()
                # Agrega los primos encontrados por este proceso al resultado total
                resultado.extend(datos)

           #  for _ in procesos:
           #     resultado.extend(cola.get())

            # Registra el tiempo de finalización
            tiempo_fin = time.time()
            
            # PASO 6: Calcula el tiempo total de ejecución
            tiempo_total = tiempo_fin - tiempo_inicio

            # Muestra los resultados: cantidad de primos y tiempo empleado
            input(get_mensaje_exito(resultado, tiempo_total))

        # ========== OPCIÓN 4: VER SÍNTESIS DEL INFORME ==========
        elif menu == 4:
            # Muestra información sobre la síntesis del informe técnico (en desarrollo)
            clear_console()

            input(
                '=== SÍNTESIS DEL INFORME TÉCNICO - EVIDENCIA 2 ===\n\n'
                + '-' * 130 +
                '\nNOTA: En proceso... Aguarde a la proxima entrega.\n'
                + '-' * 130 + '\n\nPresione ENTER para continuar ')

        # ========== OPCIÓN 0: SALIR DEL PROGRAMA ==========
        elif menu == 0:
            # Limpia la pantalla y sale del bucle, terminando el programa
            clear_console()
            break

        # ========== OPCIÓN INVÁLIDA ==========
        else:
            # Si el usuario ingresa un número que no corresponde a ninguna opción
            clear_console()
            input('Opción no válida. Presione ENTER para continuar ')
