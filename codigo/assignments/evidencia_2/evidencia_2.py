import time
from assignments.evidencia_2.funciones import es_primo, buscar_primos, buscar_primos_thread, buscar_primos_mp
from utils.clear_console import clear_console
import threading
import multiprocessing

def evidencia_2():
    while True:
        clear_console()

        try:
            menu = int(
                input(
                    'PROPUESTA ELEGIDA:\nANÁLISIS DE RENDIMIENTO DE APLICACIONES EN FUNCIÓN DEL SISTEMA OPERATIVO: THREADS VS PROCESOS\n\nObjetivo de esta Fase:\nEstablecer la "Línea de Base" experimental del proyecto mediante una ejecución puramente secuencial y monohilo.\n\n¿Qué se espera comprobar y realizar?\n\nCarga CPU-Bound: Forzar un estrés real y controlado en el procesador mediante un algoritmo exhaustivo de cálculo de números primos\n(Rango: 1 a 150.000), habiendo removido deliberadamente optimizaciones matemáticas con fines estrictamente didácticos.\n\nAislamiento de Recursos: Demostrar empíricamente cómo el Planificador del Sistema Operativo asigna esta tarea a un único hilo,\nsaturando un solo núcleo lógico al 100% de su capacidad mientras el resto de la arquitectura permanece en reposo.\n\nTelemetría de Base: Registrar el tiempo exacto de procesamiento secuencial puro para utilizarlo como métrica de control\ncomparativa frente a las futuras implementaciones concurrentes y paralelas.\n\n\nA continuación, elija una opción:\n\n1 - Ejecutar prueba secuencial\n\n2 - Ejecutar prueba multihilo\n\n3 - Ejecutar prueba multiproceso\n\n4 - Ver informe\n\n0 - Volver\n\n\n\nIngrese N° de opción: '
                ))

        except ValueError:
            clear_console()
            input(
                '¡ERROR!\n\nPor favor, ingrese un NÚMERO válido. Presione ENTER para continuar '
            )
            continue

        if menu == 1: #--- SECUENCIAL --- 
            clear_console()

            limite_superior = 200000

            print('=== EJECUCIÓN EN PROCESO ===\n\n')

            print(
                f'Calculando números primos desde el 1 hasta el {limite_superior}...\n\n\nPROCESAMIENTO EN CURSO, AGUARDE POR FAVOR...\n\n\nEl proceso activo se encuentra en estado de Ejecución (Running) bajo Modo Usuario.\n\nGuía de Verificación en Tiempo Real:\n\n1. Abra el Administrador de Tareas (Windows) o ejecute "htop" (Linux).\n\n2. En la pestaña de Procesos, localice la instancia activa de "python.exe" correspondiente a este script.\n\n3. Diríjase a la pestaña de Rendimiento -> CPU.\n\n4. Haga clic derecho sobre el gráfico de CPU y seleccione: "Cambiar gráfico a -> Procesadores lógicos"\n\n5. Observe cómo la carga de trabajo CPU-Bound es ejecutada por un único hilo principal de manera secuencial.\n\n6. Dependiendo del Scheduler del sistema operativo, el hilo puede migrar dinámicamente entre distintos núcleos lógicos,\npor lo que la actividad puede distribuirse visualmente entre varios procesadores.\n\n7. Aun así, el consumo total permanecerá limitado aproximadamente a la capacidad de ejecución de un único thread lógico,\nlo que evidencia la naturaleza secuencial y monohilo de esta implementación.'
            )

            print('=== VERSIÓN SECUENCIAL ===\n\n')

            tiempo_inicio = time.time()

            primos_encontrados = buscar_primos(1 , limite_superior)

            tiempo_fin = time.time()

            tiempo_total = tiempo_fin - tiempo_inicio

            input(
                f'¡Cálculo finalizado con éxito!\nCantidad de números primos encontrados: {len(primos_encontrados)}\nTiempo total de ejecución: {tiempo_total: .4f} segundos\nPresione ENTER para continuar '
            )

        elif menu == 2: #--- MULTI HILOS ---

            clear_console()

            limite_superior = 200000

            print('=== EJECUCIÓN EN PROCESO ===\n\n')

            print(
                f'Calculando números primos desde el 1 hasta el {limite_superior}...\n\n\nPROCESAMIENTO EN CURSO, AGUARDE POR FAVOR...\n\n\nEl proceso activo se encuentra en estado de Ejecución (Running) bajo Modo Usuario.\n\nGuía de Verificación en Tiempo Real:\n\n1. Abra el Administrador de Tareas (Windows) o ejecute "htop" (Linux).\n\n2. En la pestaña de Procesos, localice la instancia activa de "python.exe" correspondiente a este script.\n\n3. Diríjase a la pestaña de Rendimiento -> CPU.\n\n4. Haga clic derecho sobre el gráfico de CPU y seleccione: "Cambiar gráfico a -> Procesadores lógicos"\n\n5. Observe cómo la carga de trabajo CPU-Bound es ejecutada por un único hilo principal de manera secuencial.\n\n6. Dependiendo del Scheduler del sistema operativo, el hilo puede migrar dinámicamente entre distintos núcleos lógicos,\npor lo que la actividad puede distribuirse visualmente entre varios procesadores.\n\n7. Aun así, el consumo total permanecerá limitado aproximadamente a la capacidad de ejecución de un único thread lógico,\nlo que evidencia la naturaleza secuencial y monohilo de esta implementación.'
            )

            print('=== VERSIÓN MULTIHILO ===\n\n')

            tiempo_inicio = time.time()  

            resultado = []       # Lista compartida entre threads
            hilos = []   

            # División del problema en partes (paralelización manual)
            rangos = [          
            (1, 37500),
            (37500, 75000),
            (75000, 112500),
            (112500, 150000)
            ]

             # Se crea un thread por cada rango
            for inicio, fin in rangos:     
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

            input(
                f'¡Cálculo finalizado con éxito!\nCantidad de números primos encontrados: {len(resultado)}\nTiempo total de ejecución: {tiempo_total: .4f} segundos\nPresione ENTER para continuar '
            )
        
        elif menu == 3: #--- MULTI PROCESOS ---

            clear_console()

            limite_superior = 150000

            print('=== EJECUCIÓN EN PROCESO ===\n\n')

            print(
                f'Calculando números primos desde el 1 hasta el {limite_superior}...\n\n\nPROCESAMIENTO EN CURSO, AGUARDE POR FAVOR...\n\n\nEl proceso activo se encuentra en estado de Ejecución (Running) bajo Modo Usuario.\n\nGuía de Verificación en Tiempo Real:\n\n1. Abra el Administrador de Tareas (Windows) o ejecute "htop" (Linux).\n\n2. En la pestaña de Procesos, localice la instancia activa de "python.exe" correspondiente a este script.\n\n3. Diríjase a la pestaña de Rendimiento -> CPU.\n\n4. Haga clic derecho sobre el gráfico de CPU y seleccione: "Cambiar gráfico a -> Procesadores lógicos"\n\n5. Observe cómo la carga de trabajo CPU-Bound es ejecutada por un único hilo principal de manera secuencial.\n\n6. Dependiendo del Scheduler del sistema operativo, el hilo puede migrar dinámicamente entre distintos núcleos lógicos,\npor lo que la actividad puede distribuirse visualmente entre varios procesadores.\n\n7. Aun así, el consumo total permanecerá limitado aproximadamente a la capacidad de ejecución de un único thread lógico,\nlo que evidencia la naturaleza secuencial y monohilo de esta implementación.'
            )

            print('=== VERSIÓN MULTIPROCESOS ===\n\n')

            tiempo_inicio = time.time()


            manager = multiprocessing.Manager() # Manager crea un objeto que permite compartir datos entre procesos
            cola = manager.Queue()    # Cola para comunicación entre procesos (IPC)
            procesos = []


            rangos = [
            (1, 37500),
            (37500, 75000),
            (75000, 112500),
            (112500, 150000)
            ]

            for inicio, fin in rangos:
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

            input(
                f'¡Cálculo finalizado con éxito!\nCantidad de números primos encontrados: {len(resultado)}\nTiempo total de ejecución: {tiempo_total: .4f} segundos\nPresione ENTER para continuar '
            )

        elif menu == 4:
            clear_console()

            input(
                '=== SÍNTESIS DEL INFORME TÉCNICO - EVIDENCIA 2 ===\n\n1. GESTIÓN Y CONTROL DE PROCESOS:\n● Al seleccionar la prueba, el Kernel del sistema operativo crea un proceso independiente, asignándole un Identificador de Proceso\n(PID) y un Bloque de Control de Proceso (PCB) únicos en el espacio de memoria del núcleo.\n\n● Estado Bloqueado: Mientras la pantalla aguarda la interacción o el ingreso por teclado del usuario, el proceso pasa al estado\nde espera, liberando la totalidad de la CPU.\n\n● Estado en Ejecución: Al presionar ENTER, el planificador (Scheduler) otorga un turno físico en el procesador, moviendo el proceso\na ejecución activa para resolver el algoritmo.\n\n\n2. ANILLOS DE PRIVILEGIO Y MODOS DE EJECUCIÓN:\n● Modo Usuario (Anillo 3): Aquí se ejecuta el cómputo puro del bucle secuencial y la lógica matemática encargada\nde evaluar las divisiones. Es un entorno seguro y restringido.\n\n● Modo Kernel (Anillo 0): El proceso muta temporalmente a este modo mediante Llamadas al Sistema (Syscalls) para interactuar con\nlos recursos físicos: al medir el tiempo exacto (time.time), escribir en la terminal (print) o limpiar el búfer de la consola.\n\n\n3. COMPORTAMIENTO DEL HARDWARE (CÓMPUTO PESADO):\n● La eliminación de la optimización de la raíz cuadrada fuerza una carga de trabajo masiva y continua orientada\nestrictamente a la CPU dentro del rango de 1 a 150.000.\n\n● Al ser una ejecución síncrona y monohilo, el planificador del núcleo aísla y satura al 100% de su capacidad un único núcleo lógico,\nmanteniendo el resto de la arquitectura del procesador en estado de reposo.\n\n● El tiempo total registrado funciona como la métrica de control o \"línea de base\" fundamental para contrastar la eficiencia del\nhardware frente a las futuras implementaciones concurrentes y paralelas.\n\n'
                + '-' * 130 +
                '\nNOTA: El desarrollo y desglose de estos fundamentos teóricos se encuentra presentado de manera formal dentro del documento técnico\nen formato PDF entregado en la documentación oficial de esta fase.\n'
                + '-' * 130 + '\n\nPresione ENTER para continuar ')

        elif menu == 0:
            clear_console()
            break

        else:
            clear_console()
            input('Opción no válida. Presione ENTER para continuar ')
