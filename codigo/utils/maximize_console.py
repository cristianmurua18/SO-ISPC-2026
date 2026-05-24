import os
import ctypes


def maximize_console(zoom=28):

    if os.name != "nt":
        return

    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(),
                                    3)

    LF_FACESIZE = 32

    class COORD(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    class CONSOLE_FONT_INFOEX(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_ulong), ("nFont", ctypes.c_ulong),
                    ("dwFontSize", COORD), ("FontFamily", ctypes.c_uint),
                    ("FontWeight", ctypes.c_uint),
                    ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

    font = CONSOLE_FONT_INFOEX()

    font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)

    font.dwFontSize.Y = zoom

    font.FaceName = "Consolas"

    ctypes.windll.kernel32.SetCurrentConsoleFontEx(
        ctypes.windll.kernel32.GetStdHandle(-11), False, ctypes.pointer(font))
