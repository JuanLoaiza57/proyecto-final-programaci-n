import sys
import os

# Importación de los módulos del equipo
import organizer
import analyzer
import reports
import auditor
import utils

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def leer_opcion():
    """Lee la opción del usuario y valida que sea un número entero."""
    try:
        opcion = input("Seleccione una opción (1-5): ").strip()
        # Validamos si está vacío
        if not opcion:
            raise ValueError("No ingresó ninguna opción.")
        return opcion
    except Exception as e:
        print(f"\n[-] Error en la entrada de datos: {e}")
        return None

def mostrar_menu():
    limpiar_pantalla()
    print("=" * 50)
    print("        SISTEMA DE PROCESAMIENTO DE DATOS        ")
    print("=" * 50)
    print(" 1. Módulo de Organización (organizer.py)")
    print(" 2. Módulo de Análisis (analyzer.py)")
    print(" 3. Módulo de Reportes (reports.py)")
    print(" 4. Módulo de Auditoría (auditor.py)")
    print(" 5. Salir del Sistema")
    print("=" * 50)

def main():
    # Variable temporal para guardar el último resultado y poder generar reportes
    ultimo_resumen = None

    while True:
        mostrar_menu()
        opcion = leer_opcion()
        
        if not opcion:
            utils.esperar_segundos(2)
            continue

        if opcion == "1":
            limpiar_pantalla()
            print("[+] MÓDULO DE ORGANIZACIÓN DE ARCHIVOS\n")
            ruta = input("Ingrese la ruta de la carpeta a organizar: ").strip()
            
            print("\n¿Desea ejecutar en Modo Simulación (Dry-Run)?")
            simular = input(" (S para Sí / N para Ejecución Real): ").strip().upper()
            modo_simulacion = False if simular == 'N' else True
            
            # Llamamos a tu función de organizer.py
            ultimo_resumen = organizer.clasificar_por_extension(ruta, modo_simulacion)
            input("\nPresione Enter para volver al menú principal...")
            
        elif opcion == "2":
            limpiar_pantalla()
            print("[+] MÓDULO DE ANÁLISIS ESTADÍSTICO\n")
            # Aquí invocará tu compañero su lógica de analyzer.py
            input("\nPresione Enter para volver al menú principal...")
            
        elif opcion == "3":
            limpiar_pantalla()
            print("[+] MÓDULO DE GENERACIÓN DE REPORTES\n")
            if not ultimo_resumen:
                print("[-] No hay datos recientes de organización para generar un reporte.")
                print("    Por favor, ejecute el Módulo 1 primero.")
            else:
                nombre = input("Ingrese el nombre para los archivos de reporte: ").strip()
                # Ejecutamos las dos funciones que creaste en reports.py
                reports.exportar_reporte_txt(nombre, ultimo_resumen)
                reports.exportar_reporte_csv(nombre, ultimo_resumen)
            input("\nPresione Enter para volver al menú principal...")
            
        elif opcion == "4":
            limpiar_pantalla()
            print("[+] MÓDULO DE AUDITORÍA Y LOGS\n")
            # Aquí invocará tu compañero su lógica de auditor.py
            input("\nPresione Enter para volver al menú principal...")
            
        elif opcion == "5":
            print("\nCerrando el sistema de forma segura. ¡Hasta luego!")
            sys.exit()
            
        else:
            print("\n[-] Opción inválida. Intente nuevamente de 1 a 5.")
            utils.esperar_segundos(2)

if __name__ == "__main__":
    main()