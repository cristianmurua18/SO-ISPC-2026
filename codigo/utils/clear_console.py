import os


def clear_console() -> None:
    """
    Limpia la pantalla de la consola de forma multiplataforma.
    
    Esta función detecta el sistema operativo y ejecuta el comando
    correspondiente para limpiar la pantalla:
    - Windows: utiliza el comando 'cls'
    - Linux/Mac: utiliza el comando 'clear'
    
    Returns:
        None
    """
    
    # DETECTAR EL SISTEMA OPERATIVO Y EJECUTAR EL COMANDO APROPIADO
    # os.name devuelve:
    #   - "nt" en Windows (sistema operativo con kernel NT)
    #   - "posix" en Linux/Mac (sistemas operativos POSIX)
    #
    # Se utiliza una expresión ternaria (condicional) para elegir el comando:
    # - Si es Windows: ejecuta "cls" (Clear Screen)
    # - Si no es Windows: ejecuta "clear" (comando estándar en Unix/Linux/Mac)
    #
    # os.system() toma el comando y lo ejecuta en la shell del sistema
    os.system("cls" if os.name == "nt" else "clear")
