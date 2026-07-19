import sys
import os

# Importación de los módulos asignados al equipo
import organizer
import analyzer
import reports
import auditor
import utils

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

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
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            limpiar_pantalla()
            print("[+] Iniciando Módulo de Organización de Archivos...\n")
            # Aquí se invoca la función principal que desarrolle el encargado de organizer.py
            # Ejemplo: organizer.ejecutar_organizacion()
            input("\nPresione Enter para volver al menú principal...")
            
        elif opcion == "2":
            limpiar_pantalla()
            print("[+] Iniciando Módulo de Análisis Estadístico...\n")
            # Aquí se invoca la lógica de analyzer.py
            input("\nPresione Enter para volver al menú principal...")
            
        elif opcion == "3":
            limpiar_pantalla()
            print("[+] Iniciando Módulo de Generación de Reportes...\n")
            # Aquí se invoca la lógica de reports.py
            input("\nPresione Enter para volver al menú principal...")
            
        elif opcion == "4":
            limpiar_pantalla()
            print("[+] Iniciando Módulo de Auditoría y Logs...\n")
            # Aquí se invoca la lógica de auditor.py
            input("\nPresione Enter para volver al menú principal...")
            
        elif opcion == "5":
            print("\nCerrando el sistema de forma segura. ¡Hasta luego!")
            sys.exit()
            
        else:
            print("\n[-] Opción inválida. Intente nuevamente.")
            utils.esperar_segundos(2) # Usando el módulo de utilidades para pausar

if __name__ == "__main__":
    main()