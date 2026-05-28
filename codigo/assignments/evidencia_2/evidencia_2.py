import time
from assignments.evidencia_2.funciones import es_primo, buscar_primos, buscar_primos_thread, buscar_primos_mp
from assignments.evidencia_2.mensajes import CALCULANDO_PRIMOS_MONO, CALCULANDO_PRIMOS_MP, CALCULANDO_PRIMOS_MULTI, ERROR_MENU, ESPERANDO_RESULTADOS, MENU_PRINCIPAL, get_mensaje_exito
from assignments.evidencia_2.constantes import LIMITE_SUPERIOR, RANGOS
from utils.clear_console import clear_console
import threading
import multiprocessing

def evidencia_2():
    while True:
        clear_console()

        try:
            menu = int(input(MENU_PRINCIPAL))                                                                                                                                                                               

        except ValueError:
            clear_console()
            input(ERROR_MENU)
            continue

        if menu == 1: #--- MONOHILO --- 
            clear_console()

            print('=== EJECUCIÓN MONOHILO EN PROCESO ===\n\n')

            print(CALCULANDO_PRIMOS_MONO)

            print(ESPERANDO_RESULTADOS)

            tiempo_inicio = time.time()

            primos_encontrados = buscar_primos(1 , LIMITE_SUPERIOR)

            tiempo_fin = time.time()

            tiempo_total = tiempo_fin - tiempo_inicio

            input(get_mensaje_exito(primos_encontrados, tiempo_total))

        elif menu == 2: #--- MULTI HILOS ---

            clear_console()

            print('=== EJECUCIÓN MULTIHILOS EN PROCESO ===\n\n')

            print(CALCULANDO_PRIMOS_MULTI)

            print(ESPERANDO_RESULTADOS)

            tiempo_inicio = time.time()  

            resultado = []       # Lista compartida entre threads
            hilos = []   

             # Se crea un thread por cada rango
            for inicio, fin in RANGOS:     
                hilo = threading.Thread(
                    target=buscar_primos_thread,
                    args=(inicio, fin, resultado)
                )
                hilos.append(hilo)      # Guardamos referencia del thread
                hilo.start()        # Ejecución del thread

            # Esperamos a que todos los threads finalicen
            for hilo in hilos:      
                hilo.join()

            tiempo_fin = time.time()

            tiempo_total = tiempo_fin - tiempo_inicio

            input(get_mensaje_exito(resultado, tiempo_total))
        
        elif menu == 3: #--- MULTI PROCESOS ---

            clear_console()

            print('=== EJECUCIÓN EN VARIOS PROCESOS EN PROGRESO ===\n\n')

            print(CALCULANDO_PRIMOS_MP)

            print(ESPERANDO_RESULTADOS)

            tiempo_inicio = time.time()

            manager = multiprocessing.Manager() # Manager crea un objeto que permite compartir datos entre procesos
            cola = manager.Queue()    # Cola para comunicación entre procesos (IPC)
            procesos = []

            for inicio, fin in RANGOS:
                # Se crea un proceso independiente del sistema operativo
                proceso = multiprocessing.Process(
                    target=buscar_primos_mp,
                    args=(inicio, fin, cola)
                )
                procesos.append(proceso)
                proceso.start() # El sistema operativo asigna CPU a este proceso (Cada proceso tiene su propia memoria)

            print(f"Procesos creados: {len(procesos)}")
                    
            # Esperamos a que TODOS los procesos terminen
            for proceso in procesos:    
                proceso.join()
            print("Procesos terminados, leyendo resultados...")   
            
            resultado = []

            for i in range(len(procesos)):
                print(f"Recibiendo resultado {i+1}")
                datos = cola.get()
                resultado.extend(datos)

           #  for _ in procesos:
           #     resultado.extend(cola.get())

            tiempo_fin = time.time()
            tiempo_total = tiempo_fin - tiempo_inicio

            input(get_mensaje_exito(resultado, tiempo_total))

        elif menu == 4:
            clear_console()

            input(
                '=== SÍNTESIS DEL INFORME TÉCNICO - EVIDENCIA 2 ===\n\n'
                + '-' * 130 +
                '\nNOTA: En proceso... Aguarde a la proxima entrega.\n'
                + '-' * 130 + '\n\nPresione ENTER para continuar ')

        elif menu == 0:
            clear_console()
            break

        else:
            clear_console()
            input('Opción no válida. Presione ENTER para continuar ')
