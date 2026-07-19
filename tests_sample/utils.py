import os
import time

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_segundos(segundos):
    """Genera una pausa en la ejecución antes de continuar."""
    time.sleep(segundos)