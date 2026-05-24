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
│       └── evidencia_2.py           # Cálculo secuencial de números primos
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
- `evidencia_2`: función que ejecuta el cálculo secuencial de números primos.

---

### Paso 2: Preparación de la consola

```python
maximize_console(24)
clear_console()
```

1. **`maximize_console(24)`**: Maximiza la ventana de la consola de Windows y establece el tamaño de fuente en 24 puntos con tipografía "Consolas".
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
    try:
        menu = int(input('...Ingrese N° de opción: '))
    except ValueError:
        ...
```

Se inicia un bucle infinito (`while True`) que:

1. **Limpia la consola** al inicio de cada iteración.
2. **Muestra el menú principal** con la descripción del proyecto y las opciones disponibles:
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
   - Se define la altura de la fuente con el valor del parámetro `zoom` (por defecto 28, en `main.py` se usa 24).
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

### `evidencia_2.py` - Cálculo Secuencial de Números Primos

#### Función auxiliar: `es_primo(n)`

```python
def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limite = math.isqrt(n) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False
    return True
```

**Algoritmo de verificación de primalidad:**

1. Si `n ≤ 1` → no es primo.
2. Si `n == 2` → es primo (único primo par).
3. Si `n` es par → no es primo.
4. Se calcula el límite como `√n + 1` usando `math.isqrt()` (raíz cuadrada entera).
5. Se itera desde 3 hasta el límite, de 2 en 2 (solo impares).
6. Si algún divisor divide exactamente a `n` → no es primo.
7. Si no se encontró ningún divisor → es primo.

#### Función principal: `evidencia_2()`

```python
def evidencia_2():
    clear_console()
    print('=== EJECUCIÓN PARCIAL 2: VERSIÓN SECUENCIAL ===\n')
    limite_superior = 100000
    print(f'Calculando números primos desde el 1 hasta el {limite_superior}...')
    tiempo_inicio = time.time()
    primos_encontrados = []
    for numero in range(1, limite_superior, +1):
        if es_primo(numero):
            primos_encontrados.append(numero)
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    input(f'\n¡Cálculo finalizado con éxito!\nCantidad de números primos encontrados: {len(primos_encontrados)}\nTiempo total de ejecución: {tiempo_total: .4f} segundos\n\n\nPresione ENTER para continuar ')
```

**Flujo detallado:**

1. **Limpia la consola** y muestra un encabezado.
2. **Define el límite superior** en 100,000.
3. **Informa al usuario** que el cálculo está en progreso.
4. **Registra el tiempo de inicio** con `time.time()`.
5. **Itera por cada número** del 1 al 99,999:
   - Verifica si es primo con `es_primo()`.
   - Si lo es, lo agrega a la lista `primos_encontrados`.
6. **Registra el tiempo de fin**.
7. **Calcula el tiempo total** de ejecución.
8. **Muestra los resultados:**
   - Cantidad de primos encontrados.
   - Tiempo total de ejecución en segundos (con 4 decimales).
9. **Espera** a que el usuario presione ENTER para volver al menú.

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
│  maximize_console(24)       │
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
| **Librerías estándar** | `os`, `ctypes`, `time`, `math` |
| **Librerías externas** | Ninguna (no requiere `pip install`) |
| **Sistema operativo** | Windows (la función `maximize_console` y `clear_console` usan comandos específicos de Windows) |

---

## Conceptos de Sistemas Operativos Aplicados

El proyecto tiene como objetivo comparar distintas estrategias de ejecución concurrente. En esta entrega (Parcial 2) se implementa la **versión secuencial** como línea base para futuras comparaciones con:

- **Threading** (hilos): ejecución concurrente dentro de un mismo proceso, limitada por el GIL de Python.
- **Multiprocessing** (procesos): ejecución paralela real en múltiples núcleos de CPU.

La tarea elegida (cálculo de números primos) es **CPU-intensiva**, lo que la hace ideal para demostrar las diferencias entre estas estrategias.

---

## Cómo Ejecutar

1. Abrir una terminal en la carpeta `codigo/`.
2. Ejecutar:
   ```bash
   python main.py
   ```
3. Seguir las instrucciones en pantalla.

> **Nota:** La aplicación está diseñada para ejecutarse en **Windows** debido al uso de `ctypes` para manipular la consola y el comando `cls` para limpiar la pantalla.