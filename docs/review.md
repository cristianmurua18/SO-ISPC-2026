# Code Review — Proyecto SO-ISPC-2026

> **Fecha:** 29 de mayo de 2026  
> **Revisión sobre:** Entrega Parcial 2 — Primer codificación  
> **Alcance:** Análisis completo de arquitectura, buenas prácticas, seguridad, rendimiento y aspectos no contemplados.

---

## Resumen Ejecutivo

El proyecto presenta una estructura clara y organizada para un trabajo académico. La separación en módulos (`funciones.py`, `mensajes.py`, `constantes.py`) demuestra intención de modularidad. Sin embargo, existen varias áreas de mejora relacionadas con thread safety, eficiencia en el uso de multiprocessing, ausencia de tests, y prácticas de código que podrían elevar significativamente la calidad del proyecto.

---

## Índice

1. [Problemas Críticos](#1-problemas-críticos)
2. [Buenas Prácticas de Programación](#2-buenas-prácticas-de-programación)
3. [Arquitectura y Organización](#3-arquitectura-y-organización)
4. [Rendimiento y Concurrencia](#4-rendimiento-y-concurrencia)
5. [Portabilidad y Compatibilidad](#5-portabilidad-y-compatibilidad)
6. [Testing y Calidad](#6-testing-y-calidad)
7. [Gestión de Proyecto](#7-gestión-de-proyecto)
8. [Aspectos No Contemplados](#8-aspectos-no-contemplados)
9. [Resumen de Recomendaciones](#9-resumen-de-recomendaciones)

---

## 1. Problemas Críticos

### 1.1 Thread Safety en `buscar_primos_thread`

```python
def buscar_primos_thread(inicio, fin, resultado):
    primos = buscar_primos(inicio, fin)
    resultado.extend(primos)  # ⚠️ NO es thread-safe
```

**Problema:** Múltiples hilos escriben simultáneamente en la misma lista (`resultado`) sin ningún mecanismo de sincronización. Aunque en CPython `list.extend()` es técnicamente atómico debido al GIL, **depender de esto es una mala práctica** porque:

- No es una garantía documentada del lenguaje.
- No funciona en otras implementaciones (PyPy, Jython, etc.).
- Contradice los principios que el proyecto intenta demostrar sobre exclusión mutua.

**Solución recomendada:** Usar un `threading.Lock()` para proteger la sección crítica, o bien utilizar una `queue.Queue` que es inherentemente thread-safe.

### 1.2 Uso de `Manager().Queue()` en lugar de `multiprocessing.Queue()`

```python
manager = multiprocessing.Manager()
cola = manager.Queue()
```

**Problema:** `Manager()` crea un **proceso servidor adicional** para gestionar objetos compartidos. Esto introduce overhead innecesario (un proceso extra, serialización via Proxy objects, comunicación por sockets). Para una simple Queue, es excesivo.

**Solución recomendada:** Usar `multiprocessing.Queue()` directamente, que es más eficiente para este caso de uso.

### 1.3 Bloqueo potencial en `cola.get()`

```python
for i in range(len(procesos)):
    datos = cola.get()  # ⚠️ Puede bloquear indefinidamente
```

**Problema:** Si un proceso hijo falla silenciosamente y no deposita datos en la cola, `cola.get()` bloqueará el programa principal para siempre sin posibilidad de recuperación.

**Solución recomendada:** Usar `cola.get(timeout=60)` con manejo de `queue.Empty`, o verificar el `exitcode` de cada proceso antes de leer la cola.

---

## 2. Buenas Prácticas de Programación

### 2.1 Type Hints (Anotaciones de Tipo)

Ninguna función del proyecto (excepto `clear_console`) tiene anotaciones de tipo. Esto dificulta la legibilidad y el mantenimiento.

**Ejemplo actual:**
```python
def es_primo(n):
def buscar_primos(inicio, fin):
```

**Ejemplo mejorado:**
```python
def es_primo(n: int) -> bool:
def buscar_primos(inicio: int, fin: int) -> list[int]:
```

### 2.2 Importación no utilizada

En `evidencia_2.py` se importa `es_primo` pero nunca se usa directamente en ese módulo:

```python
from assignments.evidencia_2.funciones import es_primo, buscar_primos, ...
```

Las importaciones innecesarias ensucian el namespace y confunden al lector.

### 2.3 Prints de debug en código de producción

En `buscar_primos_mp`:
```python
print(f"START {inicio}-{fin}")
print(f"END {inicio}-{fin}")
print(f"PUT OK {inicio}-{fin}")
```

Y en `evidencia_2.py`:
```python
print(f"Procesos creados: {len(procesos)}")
print("Procesos terminados, leyendo resultados...")
print(f"Recibiendo resultado {i+1}")
```

**Problema:** Estos mensajes de depuración no deberían estar en el código entregable. Si se necesitan para diagnóstico, deberían usar el módulo `logging` con niveles configurables.

### 2.4 Código comentado residual

```python
#  for _ in procesos:
#     resultado.extend(cola.get())
```

El código comentado no aporta valor y genera ruido. Si se necesita historial, para eso está Git.

### 2.5 Comentarios excesivos y redundantes

Muchos comentarios repiten exactamente lo que el código ya dice de forma obvia:

```python
# Registra el tiempo de inicio
tiempo_inicio = time.time()

# Registra el tiempo de finalización
tiempo_fin = time.time()
```

Los comentarios deberían explicar **por qué**, no **qué**. El código bien escrito es auto-documentado para el "qué".

### 2.6 Docstrings dentro de bloques `if/elif`

```python
if menu == 1:
    """
    Método secuencial: Un único hilo busca todos los números primos...
    """
```

**Problema:** Un docstring dentro de un bloque `if` no es un docstring válido — es simplemente una cadena que se crea y descarta. Solo las funciones, clases y módulos soportan docstrings. Esto debería ser un comentario multilínea con `#`.

### 2.7 Inconsistencia en el idioma

El código mezcla español e inglés sin criterio claro:
- Variables en español: `resultado`, `primos_encontrados`, `tiempo_inicio`
- Módulos en español: `funciones.py`, `mensajes.py`, `constantes.py`
- Imports en inglés: `threading`, `multiprocessing`, `time`

**Recomendación:** Para un proyecto académico en español está bien usar nombres en español, pero ser consistente. Lo ideal es elegir un idioma y mantenerlo (la industria prefiere inglés para el código).

---

## 3. Arquitectura y Organización

### 3.1 Función `evidencia_2()` demasiado larga

La función `evidencia_2()` tiene ~240 líneas con toda la lógica de las tres pruebas inlined. Esto viola el principio de responsabilidad única (SRP).

**Recomendación:** Extraer cada prueba en su propia función:
```python
def ejecutar_monohilo() -> None: ...
def ejecutar_multihilo() -> None: ...
def ejecutar_multiproceso() -> None: ...
```

### 3.2 Strings de UI en `main.py` y `evidencia_1.py`

En `evidencia_2` se separaron correctamente los mensajes a `mensajes.py`, pero en `main.py` y `evidencia_1.py` todo el texto está embebido directamente en las llamadas a `input()`.

**Recomendación:** Aplicar el mismo patrón de `mensajes.py` consistentemente en todo el proyecto.

### 3.3 Rangos hardcodeados y acoplados

```python
LIMITE_SUPERIOR = 150000

RANGOS = [
    (1, 37500),
    (37501, 75000),
    (75001, 112500),
    (112501, 150000)
]
```

**Problema:** Si se cambia `LIMITE_SUPERIOR`, los rangos NO se actualizan automáticamente. Esto es propenso a errores.

**Recomendación:** Calcular los rangos dinámicamente:
```python
def generar_rangos(limite: int, num_partes: int) -> list[tuple[int, int]]:
    paso = limite // num_partes
    return [(i * paso + 1, (i + 1) * paso) for i in range(num_partes)]
```

### 3.4 Ausencia de `__main__.py`

No existe un archivo `__main__.py` que permita ejecutar el proyecto como paquete:
```bash
python -m codigo
```

Actualmente solo se puede ejecutar con `python main.py` desde dentro del directorio `codigo/`.

---

## 4. Rendimiento y Concurrencia

### 4.1 No se mide CPU ni memoria

El proyecto declara en sus objetivos:
> "Comparar tiempos de ejecución entre threading y multiprocessing. Analizar el uso de CPU y memoria en cada enfoque."

Sin embargo, **solo se mide el tiempo de ejecución**. No hay código que registre:
- Uso de CPU (% por proceso/hilo)
- Consumo de memoria (RSS, heap)
- Cantidad de context switches

**Recomendación:** Usar `psutil` para medir CPU y memoria, o al menos `resource` (Unix) / `tracemalloc` (stdlib) para memoria.

### 4.2 No se usa `multiprocessing.Pool`

El patrón actual (crear procesos manualmente + Queue + join) es verbose y error-prone. `multiprocessing.Pool` maneja todo esto de forma más idiomática:

```python
with multiprocessing.Pool(processes=4) as pool:
    resultados = pool.starmap(buscar_primos, RANGOS)
```

Esto elimina la necesidad de Manager, Queue, y la recopilación manual de resultados.

### 4.3 No se adapta al hardware

El número de rangos (4) está hardcodeado. No se considera la cantidad real de núcleos del sistema:

```python
import os
num_cores = os.cpu_count()  # Adaptar al hardware disponible
```

### 4.4 No se ejecutan múltiples iteraciones

El proyecto menciona en su plan:
> "Cada versión será ejecutada múltiples veces para obtener valores promedio"

Pero el código ejecuta cada prueba una sola vez. Para un análisis estadístico significativo, se deberían ejecutar N iteraciones y calcular media, desviación estándar, y descartar outliers.

### 4.5 Ausencia de warm-up

La primera ejecución siempre es más lenta (carga de módulos, cache frío). Un benchmark riguroso debería incluir una ejecución de warm-up descartable.

---

## 5. Portabilidad y Compatibilidad

### 5.1 `maximize_console.py` es exclusivamente Windows

La función usa `ctypes.windll` que solo existe en Windows. Aunque hay un guard (`if os.name != "nt": return`), **no ofrece alternativa** para Linux/Mac.

### 5.2 Mensaje de F11 asume Windows

```python
'Presione F11 para maximizar la consola en windows\n\n'
```

Debería adaptarse al SO del usuario o eliminarse.

### 5.3 Sin `requirements.txt` ni `pyproject.toml`

Aunque el proyecto solo usa la stdlib, es buena práctica incluir:
- `requirements.txt` (aunque esté vacío, documenta que no hay dependencias externas)
- O mejor, un `pyproject.toml` con la versión mínima de Python requerida

### 5.4 Sin especificación de versión de Python

No se documenta qué versión de Python se requiere. El uso de f-strings implica Python 3.6+, pero `list[int]` en type hints requiere 3.9+.

---

## 6. Testing y Calidad

### 6.1 Ausencia total de tests

No hay ningún archivo de test en el proyecto. Para un proyecto que compara algoritmos, los tests son esenciales para:
- Verificar que `es_primo()` funciona correctamente (casos borde: 0, 1, 2, 3, números grandes)
- Verificar que las tres versiones (secuencial, threads, procesos) producen el mismo resultado
- Verificar que los rangos cubren todo el espacio sin gaps ni solapamientos

**Tests mínimos recomendados:**
```python
def test_es_primo_casos_borde():
    assert not es_primo(0)
    assert not es_primo(1)
    assert es_primo(2)
    assert es_primo(3)
    assert not es_primo(4)

def test_consistencia_metodos():
    resultado_secuencial = buscar_primos(1, 1000)
    resultado_threads = ...  # ejecutar con threads
    resultado_procesos = ...  # ejecutar con procesos
    assert sorted(resultado_secuencial) == sorted(resultado_threads)
    assert sorted(resultado_secuencial) == sorted(resultado_procesos)
```

### 6.2 Sin linter ni formatter configurado

No hay configuración de:
- `flake8` / `ruff` para linting
- `black` / `autopep8` para formateo
- `mypy` para type checking

Un archivo `.flake8` o `pyproject.toml` con configuración de herramientas de calidad elevaría el proyecto.

### 6.3 Sin CI/CD

No hay configuración de GitHub Actions u otro CI para ejecutar tests automáticamente en cada push.

---

## 7. Gestión de Proyecto

### 7.1 Sin `README.md` en la raíz

No existe un README en la raíz del proyecto que explique:
- Cómo instalar/ejecutar el proyecto
- Requisitos previos
- Estructura del proyecto
- Cómo contribuir (para proyectos grupales)

### 7.2 Sin instrucciones de ejecución claras

¿Desde dónde se ejecuta? ¿`python main.py`? ¿`python codigo/main.py`? ¿Hay que estar dentro de `codigo/`?

### 7.3 Documentación duplicada

La información del grupo y el proyecto está duplicada en:
- `main.py` (pantalla de bienvenida)
- `evidencia_1.py` (propuesta completa)
- `docs/documentacion.md`

Debería haber una única fuente de verdad.

---

## 8. Aspectos No Contemplados

### 8.1 Manejo de señales e interrupciones

Si el usuario presiona `Ctrl+C` durante una ejecución larga (especialmente en multiprocesos), los procesos hijos pueden quedar huérfanos. No hay manejo de `KeyboardInterrupt` ni cleanup de procesos.

### 8.2 Resultados no persistidos

Los tiempos de ejecución solo se muestran en pantalla y se pierden al cerrar. Para un análisis comparativo real, deberían guardarse en archivo (CSV, JSON) para posterior análisis y graficación.

### 8.3 Sin visualización de resultados

El proyecto menciona "tablas y/o gráficos" en su plan pero no implementa ninguno. Librerías como `matplotlib` o incluso tablas ASCII en consola mejorarían la presentación.

### 8.4 Sin comparación automática

No hay una opción que ejecute las tres pruebas secuencialmente y presente una tabla comparativa. El usuario debe ejecutar cada una manualmente y anotar los tiempos.

### 8.5 Sin información del sistema

Para un análisis de rendimiento, es fundamental registrar:
- CPU (modelo, frecuencia, núcleos físicos/lógicos)
- RAM disponible
- Sistema operativo y versión
- Versión de Python

Esto se puede obtener con `platform` y `psutil`.

### 8.6 Overhead de multiprocessing no aislado

El tiempo medido en multiprocesos incluye:
- Creación del Manager (proceso extra)
- Creación y spawn de procesos
- Serialización/deserialización de datos (pickling)
- Comunicación IPC

Sería valioso medir y reportar estos overheads por separado para entender el costo real del paralelismo.

### 8.7 Sin control de reproducibilidad

No hay seed ni condiciones fijas para garantizar que las ejecuciones sean comparables. Aunque para primos esto es determinístico, sería buena práctica documentar las condiciones del benchmark.

### 8.8 GIL no queda demostrado empíricamente

El proyecto menciona el GIL como factor clave, pero no muestra empíricamente que threading NO mejora tiempos en CPU-bound. Sería muy valioso mostrar que:
- Tiempo threading ≈ Tiempo secuencial (por el GIL)
- Tiempo multiprocesos << Tiempo secuencial (paralelismo real)

---

## 9. Resumen de Recomendaciones

### Prioridad Alta (Correcciones necesarias)

| # | Problema | Archivo | Impacto |
|---|----------|---------|---------|
| 1 | Thread safety: usar Lock en lista compartida | `funciones.py` | Correctitud |
| 2 | Reemplazar `Manager().Queue()` por `multiprocessing.Queue()` | `evidencia_2.py` | Rendimiento |
| 3 | Agregar timeout a `cola.get()` | `evidencia_2.py` | Robustez |
| 4 | Eliminar prints de debug | `funciones.py`, `evidencia_2.py` | Limpieza |
| 5 | Eliminar import no usado (`es_primo`) | `evidencia_2.py` | Limpieza |

### Prioridad Media (Mejoras significativas)

| # | Mejora | Beneficio |
|---|--------|-----------|
| 6 | Agregar type hints a todas las funciones | Legibilidad, mantenibilidad |
| 7 | Calcular rangos dinámicamente | Evitar inconsistencias |
| 8 | Extraer lógica de pruebas a funciones separadas | SRP, legibilidad |
| 9 | Implementar medición de CPU y memoria con `psutil` | Cumplir objetivos del proyecto |
| 10 | Agregar tests unitarios | Verificar correctitud |
| 11 | Persistir resultados en archivo | Análisis posterior |
| 12 | Manejar `KeyboardInterrupt` y cleanup de procesos | Robustez |

### Prioridad Baja (Nice to have)

| # | Mejora | Beneficio |
|---|--------|-----------|
| 13 | Agregar `README.md` en la raíz | Documentación |
| 14 | Configurar linter (`ruff`) y formatter (`black`) | Consistencia |
| 15 | Agregar ejecución múltiple con estadísticas | Rigor científico |
| 16 | Implementar tabla comparativa automática | UX |
| 17 | Registrar info del sistema en cada benchmark | Reproducibilidad |
| 18 | Usar `multiprocessing.Pool` | Código más idiomático |
| 19 | Agregar `pyproject.toml` con versión de Python | Gestión de proyecto |
| 20 | Agregar `__main__.py` | Ejecución como paquete |

---

## Conclusión

El proyecto tiene una base sólida y cumple con su propósito educativo de demostrar las diferencias entre ejecución secuencial, multihilo y multiproceso. La documentación interna es extensa y las explicaciones didácticas en los mensajes al usuario son un punto fuerte.

Las principales áreas de mejora se centran en:
1. **Correctitud concurrente** (thread safety)
2. **Completar las métricas prometidas** (CPU, memoria — no solo tiempo)
3. **Agregar tests** para garantizar que los tres métodos producen resultados idénticos
4. **Limpieza de código** (debug prints, imports no usados, comentarios redundantes)

Con estas mejoras, el proyecto pasaría de ser un buen trabajo académico a un ejemplo robusto y profesional de análisis de rendimiento en Python.