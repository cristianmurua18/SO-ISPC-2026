# Documentación del Proyecto - Sistemas Operativos

## Información General

| Campo | Detalle |
|-------|---------|
| **Materia** | Sistemas Operativos - TSDS |
| **Año** | 2026 |
| **Entrega** | Parcial 2 - Primer codificación |
| **Grupo** | "En Blanco" |
| **Docente** | Nicolas Viale |

### Integrantes

- Battista, Mariano Iván
- Gatica, Pablo Emiliano
- Gonzalez, Javier Alexis
- Molina, Agustina
- Murua Ayosa, Christian José
- Ranieri, Marysol

---

## Estructura del Proyecto

```
codigo/
├── main.py                          # Punto de entrada de la aplicación
├── .vscode/
│   └── settings.json                # Configuración del editor VS Code
├── assignments/
│   ├── evidencia_1/
│   │   └── evidencia_1.py           # Propuesta y definición del proyecto
│   └── evidencia_2/
│       ├── evidencia_2.py           # Menú y ejecución de pruebas (secuencial, multihilo, multiproceso)
│       └── funciones.py             # Funciones de cálculo de primos (compartidas entre estrategias)
└── utils/
    ├── clear_console.py             # Utilidad para limpiar la consola
    └── maximize_console.py          # Utilidad para maximizar y configurar la consola
```

---

## Flujo de Ejecución Paso a Paso

### Paso 1: Inicio de la aplicación (`main.py`)

Al ejecutar `main.py`, lo primero que ocurre es la importación de módulos:

```python
from utils.maximize_console import maximize_console
from utils.clear_console import clear_console
from assignments.evidencia_1.evidencia_1 import evidencia_1
from assignments.evidencia_2.evidencia_2 import evidencia_2
```

Se importan:
- `maximize_console`: función para maximizar la ventana de consola y ajustar la fuente.
- `clear_console`: función para limpiar el contenido de la consola.
- `evidencia_1`: función que muestra la propuesta del proyecto.
- `evidencia_2`: función que ejecuta el benchmark de cálculo de números primos (secuencial, multihilo y multiproceso).

Todo el código ejecutable está encapsulado dentro de una función `main()` que se invoca mediante el guard:

```python
if __name__ == "__main__":
    main()
```

> **Nota técnica:** Este guard es indispensable en Windows para el correcto funcionamiento de `multiprocessing`. Sin él, cada proceso hijo re-ejecutaría el script completo al ser creado mediante `spawn`, causando un bloqueo infinito.

---

### Paso 2: Preparación de la consola

```python
maximize_console(25)
clear_console()
```

1. **`maximize_console(25)`**: Maximiza la ventana de la consola de Windows y establece el tamaño de fuente en 25 puntos con tipografía "Consolas".
2. **`clear_console()`**: Limpia la pantalla de la consola para presentar una interfaz limpia al usuario.

---

### Paso 3: Pantalla de presentación

```python
intro = input('Aprendizaje Basado en Proyectos (ABP)\n\nSistemas Operativos...\n\nPresione ENTER para continuar ')
```

Se muestra una pantalla introductoria con:
- Nombre de la metodología (ABP)
- Materia y año
- Tipo de entrega
- Nombre del grupo
- Lista de participantes
- Nombre del docente

El programa queda en espera hasta que el usuario presione **ENTER**.

---

### Paso 4: Bucle principal del menú

```python
while True:
    clear_console()
    maximize_console(21)
    try:
        menu = int(input('...Ingrese N° de opción: '))
    except ValueError:
        ...
```

Se inicia un bucle infinito (`while True`) que:

1. **Limpia la consola** al inicio de cada iteración.
2. **Ajusta el tamaño de fuente** a 21 puntos mediante `maximize_console(21)` para una mejor visualización del menú.
3. **Muestra el menú principal** con la descripción del proyecto y las opciones disponibles:
   - `1` - Entrega Parcial 1 (Propuesta y definición)
   - `2` - Entrega Parcial 2 (Primer codificación)
   - `0` - Salir
3. **Lee la entrada del usuario** y la convierte a entero.

---

### Paso 5: Manejo de errores de entrada

```python
except ValueError:
    clear_console()
    input('¡ERROR!\n\nPor favor, ingrese un NÚMERO válido. Presione ENTER para continuar ')
    continue
```

Si el usuario ingresa un valor que no es numérico (por ejemplo, letras o caracteres especiales), se captura la excepción `ValueError`, se muestra un mensaje de error y se vuelve al inicio del bucle con `continue`.

---

### Paso 6: Procesamiento de la opción seleccionada

#### Opción 1 → `evidencia_1()`

```python
if menu == 1:
    evidencia_1()
```

Llama a la función `evidencia_1()` que muestra la propuesta y definición del proyecto (ver detalle más adelante).

#### Opción 2 → `evidencia_2()`

```python
elif menu == 2:
    evidencia_2()
```

Llama a la función `evidencia_2()` que ejecuta el benchmark de cálculo de números primos (ver detalle más adelante).

#### Opción 0 → Salir

```python
elif menu == 0:
    clear_console()
    break
```

Limpia la consola y sale del bucle con `break`, finalizando la aplicación.

#### Opción no válida

```python
else:
    clear_console()
    input('Opción no válida. Presione ENTER para continuar ')
```

Si se ingresa un número que no corresponde a ninguna opción, se muestra un mensaje y se vuelve al menú.

---

## Módulos Utilitarios (`utils/`)

### `clear_console.py`

```python
import os

def clear_console():
    os.system("cls")
```

**Función:** Ejecuta el comando `cls` del sistema operativo Windows para limpiar todo el contenido visible en la terminal.

**Flujo:**
1. Importa el módulo `os` de la librería estándar de Python.
2. Ejecuta `cls` como un comando del sistema.

---

### `maximize_console.py`

```python
import os
import ctypes

def maximize_console(zoom=28):
    ...
```

**Función:** Maximiza la ventana de la consola de Windows y configura la fuente a un tamaño personalizable.

**Flujo detallado:**

1. **Verificación del sistema operativo:**
   ```python
   if os.name != "nt":
       return
   ```
   Si no se está ejecutando en Windows (`"nt"`), la función retorna inmediatamente sin hacer nada.

2. **Maximizar la ventana:**
   ```python
   ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 3)
   ```
   - `GetConsoleWindow()`: obtiene el handle (identificador) de la ventana de consola actual.
   - `ShowWindow(..., 3)`: el valor `3` corresponde a `SW_MAXIMIZE`, que maximiza la ventana.

3. **Definición de estructuras C:**
   Se definen las estructuras `COORD` y `CONSOLE_FONT_INFOEX` usando `ctypes.Structure` para interactuar con la API de Windows a bajo nivel.

4. **Configuración de la fuente:**
   ```python
   font = CONSOLE_FONT_INFOEX()
   font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
   font.dwFontSize.Y = zoom
   font.FaceName = "Consolas"
   ```
   - Se crea una instancia de `CONSOLE_FONT_INFOEX`.
   - Se establece el tamaño de la estructura.
   - Se define la altura de la fuente con el valor del parámetro `zoom` (por defecto 28, en `main.py` se usa 25 para la intro y 21 para el menú).
   - Se establece "Consolas" como la tipografía.

5. **Aplicación de la fuente:**
   ```python
   ctypes.windll.kernel32.SetCurrentConsoleFontEx(
       ctypes.windll.kernel32.GetStdHandle(-11), False, ctypes.pointer(font))
   ```
   - `GetStdHandle(-11)`: obtiene el handle de salida estándar (`STD_OUTPUT_HANDLE`).
   - `SetCurrentConsoleFontEx`: aplica la nueva configuración de fuente a la consola.

---

## Módulos de Evidencias (`assignments/`)

### `evidencia_1.py` - Propuesta y Definición del Proyecto

```python
from utils.clear_console import clear_console

def evidencia_1():
    clear_console()
    input('1- Opción elegida\n...\nPresione ENTER para continuar ')
```

**Función:** Presenta al usuario la propuesta completa del proyecto en formato texto.

**Flujo:**
1. Limpia la consola.
2. Muestra un texto extenso que incluye:
   - **Opción elegida:** Opción A — Threads vs Procesos.
   - **Objetivo del proyecto:** Analizar el impacto del SO en el rendimiento de Python al usar hilos vs procesos.
   - **Plan de trabajo:** Definición del problema, implementación de versiones (secuencial, threading, multiprocessing), ejecución de experimentos, análisis de resultados y organización del equipo.
3. Espera a que el usuario presione ENTER para retornar al menú principal.

---

### `funciones.py` - Módulo de Funciones de Cálculo

Este archivo centraliza toda la lógica de cálculo de números primos, separada del módulo de interfaz. Contiene 4 funciones:

#### `es_primo(n)` - Verificación de primalidad

```python
def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True
```

**Algoritmo (sin optimización deliberada):**

1. Si `n ≤ 1` → no es primo.
2. Si `n == 2` → es primo (único primo par).
3. Si `n` es par → no es primo.
4. Se itera desde 3 hasta `n - 1`, de 2 en 2 (solo impares).
5. Si algún divisor divide exactamente a `n` → no es primo.
6. Si no se encontró ningún divisor → es primo.

> **Nota didáctica:** Se ha removido deliberadamente la optimización de la raíz cuadrada (`math.isqrt(n)`) para forzar una carga de trabajo CPU-Bound masiva y controlada, con fines estrictamente experimentales.

#### `buscar_primos(inicio, fin)` - Búsqueda secuencial

```python
def buscar_primos(inicio, fin):
    primos_encontrados = []
    for numero in range(inicio, fin + 1):
        if es_primo(numero):
            primos_encontrados.append(numero)
    return primos_encontrados
```

Recorre el rango `[inicio, fin]` y retorna una lista con todos los primos encontrados. Es la función base utilizada tanto en la versión secuencial como internamente por las versiones concurrentes.

#### `buscar_primos_thread(inicio, fin, resultado)` - Versión para hilos

```python
def buscar_primos_thread(inicio, fin, resultado):
    primos = buscar_primos(inicio, fin)
    resultado.extend(primos)
```

Wrapper para uso con `threading.Thread`. Recibe una **lista compartida** (`resultado`) y agrega directamente los primos encontrados. Los hilos comparten el mismo espacio de memoria del proceso padre, por lo que pueden escribir en la misma estructura de datos.

#### `buscar_primos_mp(inicio, fin, cola)` - Versión para procesos

```python
def buscar_primos_mp(inicio, fin, cola):
    try:
        primos = buscar_primos(inicio, fin)
        cola.put(primos)
    except Exception as e:
        print(f"ERROR en {inicio}-{fin}: {e}")
```

Wrapper para uso con `multiprocessing.Process`. Como cada proceso tiene su **propia memoria aislada**, no puede escribir en una lista compartida. En su lugar, usa una `Queue` (cola de comunicación entre procesos — IPC) para enviar los resultados al proceso principal.

---

### `evidencia_2.py` - Benchmark CPU-Bound: Secuencial, Multihilo y Multiproceso

#### Estructura general

Este módulo implementa un sub-menú propio con cinco opciones:
- `1` - Ejecutar prueba secuencial (monohilo)
- `2` - Ejecutar prueba multihilo (threading)
- `3` - Ejecutar prueba multiproceso (multiprocessing)
- `4` - Ver informe (síntesis técnica)
- `0` - Volver al menú principal

#### Importaciones

```python
import time
from assignments.evidencia_2.funciones import es_primo, buscar_primos, buscar_primos_thread, buscar_primos_mp
from utils.clear_console import clear_console
import threading
import multiprocessing
```

#### Función principal: `evidencia_2()`

```python
def evidencia_2():
    while True:
        clear_console()
        try:
            menu = int(input('...Ingrese N° de opción: '))
        except ValueError:
            ...

        if menu == 1:   # Secuencial
            ...
        elif menu == 2: # Multihilo
            ...
        elif menu == 3: # Multiproceso
            ...
        elif menu == 4: # Ver informe
            ...
        elif menu == 0: # Volver
            break
```

**Flujo detallado:**

1. **Sub-menú con bucle propio:** Se presenta un menú contextual que describe la propuesta elegida, los objetivos de la fase y qué se espera comprobar.

2. **Opción 1 - Prueba secuencial (monohilo):**
   - Limpia la consola y muestra encabezado `=== EJECUCIÓN MONOHILO EN PROCESO ===`.
   - **Límite superior:** 150,000.
   - Muestra guía de verificación en tiempo real (Administrador de Tareas).
   - Ejecuta `buscar_primos(1, limite_superior)` de forma directa y secuencial.
   - Registra y muestra el tiempo total de ejecución.
   - Espera ENTER para volver al sub-menú.

3. **Opción 2 - Prueba multihilo (threading):**
   - Limpia la consola y muestra encabezado `=== EJECUCIÓN MULTIHILOS EN PROCESO ===`.
   - **Límite superior:** 150,000.
   - **División del trabajo en 4 rangos:** `(1, 37500)`, `(37500, 75000)`, `(75000, 112500)`, `(112500, 150000)`.
   - Crea 4 instancias de `threading.Thread`, cada una ejecutando `buscar_primos_thread` con un rango y una lista compartida `resultado`.
   - Inicia todos los hilos con `.start()` y espera su finalización con `.join()`.
   - Registra y muestra el tiempo total de ejecución.
   - Espera ENTER para volver al sub-menú.

4. **Opción 3 - Prueba multiproceso (multiprocessing):**
   - Limpia la consola y muestra encabezado `=== EJECUCIÓN EN VARIOS PROCESOS EN PROGRESO ===`.
   - **Límite superior:** 150,000.
   - Crea un `multiprocessing.Manager()` y una `Queue` para comunicación entre procesos (IPC).
   - **División del trabajo en 4 rangos:** mismos que la versión multihilo.
   - Crea 4 instancias de `multiprocessing.Process`, cada una ejecutando `buscar_primos_mp` con un rango y la cola.
   - Inicia todos los procesos con `.start()` y espera su finalización con `.join()`.
   - Recoge los resultados de la cola con `cola.get()`.
   - Registra y muestra el tiempo total de ejecución.
   - Espera ENTER para volver al sub-menú.

5. **Opción 4 - Ver informe:**
   - Muestra una síntesis del informe técnico que abarca:
     - **Gestión y Control de Procesos:** Creación de proceso, estados Bloqueado y En Ejecución, rol del Scheduler.
     - **Anillos de Privilegio:** Modo Usuario (Anillo 3) para el cómputo puro, Modo Kernel (Anillo 0) para syscalls.
     - **Comportamiento del Hardware:** Saturación de núcleos lógicos, métrica de línea de base.
   - Espera ENTER para volver al sub-menú.

6. **Opción 0 - Volver:** Limpia la consola y retorna al menú principal con `break`.

---

## Diagrama de Flujo General

```
┌─────────────────────────────┐
│         INICIO              │
│    (Ejecutar main.py)       │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│  maximize_console(25)       │
│  clear_console()            │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│  Pantalla de presentación   │
│  (espera ENTER)             │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│  Limpiar consola            │◄──────────────────┐
│  maximize_console(21)       │                   │
│  Mostrar menú principal     │                   │
│  Leer opción del usuario    │                   │
└─────────────┬───────────────┘                   │
              │                                   │
              ▼                                   │
┌─────────────────────────────┐                   │
│  ¿Entrada válida (número)?  │                   │
│                             │                   │
│  NO → Mostrar error ────────────────────────────┤
│                             │                   │
│  SÍ ↓                       │                   │
└─────────────┬───────────────┘                   │
              │                                   │
              ▼                                   │
┌─────────────────────────────┐                   │
│  ¿Qué opción se eligió?    │                   │
│                             │                   │
│  1 → evidencia_1() ─────────────────────────────┤
│  2 → evidencia_2() ─────────────────────────────┤
│  0 → SALIR (break)         │                   │
│  Otro → "Opción no válida" ─────────────────────┘
└─────────────┬───────────────┘
              │ (opción 0)
              ▼
┌─────────────────────────────┐
│           FIN               │
└─────────────────────────────┘
```

---

## Tecnologías y Dependencias

| Elemento | Detalle |
|----------|---------|
| **Lenguaje** | Python 3 |
| **Librerías estándar** | `os`, `ctypes`, `time`, `threading`, `multiprocessing` |
| **Librerías externas** | Ninguna (no requiere `pip install`) |
| **Sistema operativo** | Windows (la función `maximize_console` y `clear_console` usan comandos específicos de Windows) |

---

## Conceptos de Sistemas Operativos Aplicados

El proyecto compara tres estrategias de ejecución sobre la misma tarea CPU-intensiva (cálculo de primos hasta 150,000):

| Estrategia | Módulo Python | Memoria | Paralelismo real | Limitación |
|------------|---------------|---------|------------------|------------|
| **Secuencial** | — | Un solo espacio | No | Un solo núcleo |
| **Threading** | `threading` | Compartida (misma lista) | No (GIL) | Global Interpreter Lock |
| **Multiprocessing** | `multiprocessing` | Aislada (IPC vía Queue) | Sí | Overhead de creación de procesos |

### Conceptos demostrados:

- **Planificación de CPU:** El Scheduler del SO asigna tiempo de CPU a hilos y procesos. En la versión secuencial se satura un solo núcleo; en multiproceso se distribuye la carga.
- **GIL (Global Interpreter Lock):** En la versión multihilo, a pesar de crear 4 threads, el GIL de CPython impide la ejecución paralela real de código Python, resultando en tiempos similares o peores que la versión secuencial.
- **IPC (Inter-Process Communication):** La versión multiproceso usa `Manager().Queue()` para que los procesos hijos envíen resultados al proceso padre, ya que no comparten memoria.
- **Guard `__main__`:** Indispensable en Windows porque `multiprocessing` usa `spawn` (re-importa el módulo). Sin el guard, los procesos hijos ejecutarían el script completo.
- **Memoria compartida vs aislada:** Los threads escriben directamente en una lista compartida (`resultado.extend()`), mientras que los procesos envían datos mediante una cola (`cola.put()`).

---

## Cómo Ejecutar

1. Abrir una terminal en la carpeta `codigo/`.
2. Ejecutar:
   ```bash
   python main.py
   ```
3. Seguir las instrucciones en pantalla.

> **Nota:** La aplicación está diseñada para ejecutarse en **Windows** debido al uso de `ctypes` para manipular la consola y el comando `cls` para limpiar la pantalla.