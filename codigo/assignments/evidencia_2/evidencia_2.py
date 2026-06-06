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

    """
    while True:
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
            clear_console()

            print('=== EJECUCIÓN MONOHILO EN PROCESO ===\n\n')

            print(CALCULANDO_PRIMOS_MONO)

            print(ESPERANDO_RESULTADOS)

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
            clear_console()

            print('=== EJECUCIÓN MULTIHILOS EN PROCESO ===\n\n')

            print(CALCULANDO_PRIMOS_MULTI)

            print(ESPERANDO_RESULTADOS)

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
            clear_console()

            print('=== EJECUCIÓN EN VARIOS PROCESOS EN PROGRESO ===\n\n')

            print(CALCULANDO_PRIMOS_MP)

            print(ESPERANDO_RESULTADOS)

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
