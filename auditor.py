import os
import time
from datetime import datetime


LOG_FILE = "audit.log"


def registrar_log(mensaje):
    """
    Guarda un mensaje en el archivo audit.log con fecha y hora.
    """
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as archivo:
            fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            archivo.write(f"[{fecha}] {mensaje}\n")
    except Exception as e:
        print(f"Error al escribir el log: {e}")


def auditor(func):
    """
    Decorador personalizado.
    Registra la ejecución de funciones, mide el tiempo
    y captura excepciones.
    """
    def wrapper(*args, **kwargs):

        inicio = time.perf_counter()

        try:
            resultado = func(*args, **kwargs)

            tiempo = time.perf_counter() - inicio

            registrar_log(
                f"Función '{func.__name__}' ejecutada correctamente "
                f"({tiempo:.4f} segundos)"
            )

            return resultado

        except Exception as e:

            registrar_log(
                f"ERROR en '{func.__name__}': {e}"
            )

            print(f"\nError: {e}")

    return wrapper
@auditor
def crear_snapshot(ruta):
    """
    Crea un snapshot del estado actual de una carpeta.
    Guarda el nombre del archivo y su fecha de modificación.
    """

    snapshot = {}

    try:

        if not os.path.exists(ruta):
            raise FileNotFoundError("La carpeta no existe.")

        for archivo in os.listdir(ruta):

            ruta_completa = os.path.join(ruta, archivo)

            if os.path.isfile(ruta_completa):

                snapshot[archivo] = os.path.getmtime(ruta_completa)

        registrar_log("Snapshot creado correctamente.")

        return snapshot

    except Exception as e:

        registrar_log(f"Error creando snapshot: {e}")
        print(e)

        return {}
    
    @auditor
    def comparar_snapshots(snapshot_anterior, snapshot_actual):
        """
     Compara dos snapshots e identifica archivos
     agregados, eliminados y modificados.
     """

    agregados = []
    eliminados = []
    modificados = []

    # Archivos agregados
    for archivo in snapshot_actual:
        if archivo not in snapshot_anterior:
            agregados.append(archivo)

    # Archivos eliminados
    for archivo in snapshot_anterior:
        if archivo not in snapshot_actual:
            eliminados.append(archivo)

    # Archivos modificados
    for archivo in snapshot_actual:
        if archivo in snapshot_anterior:
            if snapshot_actual[archivo] != snapshot_anterior[archivo]:
                modificados.append(archivo)

    registrar_log("Comparación de snapshots realizada.")

    return {
        "agregados": agregados,
        "eliminados": eliminados,
        "modificados": modificados
    }

@auditor
def ejecutar_auditoria():
    """
    Ejecuta el módulo de auditoría.
    """

    ruta = input("Ingrese la ruta de la carpeta a auditar: ").strip()

    snapshot1 = crear_snapshot(ruta)

    input("\nRealice cambios en la carpeta y luego presione Enter...")

    snapshot2 = crear_snapshot(ruta)

    cambios = comparar_snapshots(snapshot1, snapshot2)

    print("\n===== RESULTADOS =====")

    print("\nArchivos agregados:")
    if cambios["agregados"]:
        for archivo in cambios["agregados"]:
            print(f" + {archivo}")
    else:
        print("Ninguno")

    print("\nArchivos eliminados:")
    if cambios["eliminados"]:
        for archivo in cambios["eliminados"]:
            print(f" - {archivo}")
    else:
        print("Ninguno")

    print("\nArchivos modificados:")
    if cambios["modificados"]:
        for archivo in cambios["modificados"]:
            print(f" * {archivo}")
    else:
        print("Ninguno")
