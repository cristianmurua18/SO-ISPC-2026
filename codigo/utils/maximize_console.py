import os
import ctypes


def maximize_console(zoom: int = 28) -> None:
    """
    Maximiza la ventana de la consola de Windows y ajusta el tamaño de la fuente.
    
    Esta función solo funciona en Windows (sistemas con kernel NT). En otros
    sistemas operativos, la función termina sin hacer nada.
    
    Args:
        zoom (int): Tamaño de la fuente en píxeles (por defecto: 28)
    """
    
    # VERIFICAR SISTEMA OPERATIVO
    # os.name devuelve "nt" en Windows, "posix" en Linux/Mac, etc.
    # Si NO es Windows, la función termina sin ejecutar el resto del código
    if os.name != "nt":
        return

    # MAXIMIZAR LA VENTANA DE LA CONSOLA
    # Llamar a la API de Windows ShowWindow con el parámetro 3 (SW_MAXIMIZE)
    # GetConsoleWindow() obtiene el manejador de la ventana de consola actual
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(),
                                    3)

    # Definir la constante para el tamaño del buffer de nombres de fuentes (32 caracteres)
    LF_FACESIZE = 32

    # ESTRUCTURA DE COORDENADAS
    # Replica la estructura COORD de Windows (contiene coordenadas X, Y)
    # Usada para especificar dimensiones en píxeles (ancho x alto)
    class COORD(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    # ESTRUCTURA DE INFORMACIÓN DE FUENTE DE CONSOLA
    # Replica la estructura CONSOLE_FONT_INFOEX de Windows API
    # Contiene todos los parámetros necesarios para configurar la fuente
    class CONSOLE_FONT_INFOEX(ctypes.Structure):
        _fields_ = [
            ("cbSize", ctypes.c_ulong),           # Tamaño de la estructura en bytes
            ("nFont", ctypes.c_ulong),            # Índice de la fuente
            ("dwFontSize", COORD),                # Tamaño de la fuente (X=ancho, Y=alto)
            ("FontFamily", ctypes.c_uint),        # Familia de la fuente
            ("FontWeight", ctypes.c_uint),        # Peso de la fuente (grosor)
            ("FaceName", ctypes.c_wchar * LF_FACESIZE)  # Nombre de la fuente
        ]

    # CREAR INSTANCIA DE LA ESTRUCTURA DE FUENTE
    # Se inicializa una estructura vacía que será rellenada con los valores
    font = CONSOLE_FONT_INFOEX()

    # ESTABLECER EL TAMAÑO DE LA ESTRUCTURA
    # Windows requiere saber el tamaño de la estructura para validarla
    font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)

    # ESTABLECER EL TAMAÑO VERTICAL DE LA FUENTE
    # El parámetro zoom controla la altura de los caracteres en píxeles
    # Y es el alto, X sería el ancho (aunque normalmente se deja en 0)
    font.dwFontSize.Y = zoom

    # ESTABLECER EL NOMBRE DE LA FUENTE
    # Usar "Consolas" que es una fuente monoespaciada clara y legible
    # (disponible en todas las versiones modernas de Windows)
    font.FaceName = "Consolas"

    # APLICAR LA NUEVA CONFIGURACIÓN DE FUENTE A LA CONSOLA
    # GetStdHandle(-11) obtiene el manejador de salida estándar (STDOUT)
    # False indica que no se debe usar el búfer
    # ctypes.pointer(font) pasa un puntero a la estructura con los datos
    ctypes.windll.kernel32.SetCurrentConsoleFontEx(
        ctypes.windll.kernel32.GetStdHandle(-11), False, ctypes.pointer(font))
