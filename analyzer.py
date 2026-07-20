import re


def leer_archivo_por_lineas(ruta_archivo):
    """
    Generador que lee un archivo línea por línea de manera eficiente
    para no saturar la memoria RAM.
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                # yield devuelve la línea actual y pausa la ejecución
                yield linea.strip()
    except FileNotFoundError:
        print(f"❌ Error: El archivo en '{ruta_archivo}' no existe.")
    except PermissionError:
        print(f"❌ Error: No tienes permisos para leer el archivo.")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")


def analizar_contenido(ruta_archivo):
    """
    Función principal que consume el generador y busca patrones usando Regex.
    Estructura los resultados en listas y diccionarios.
    """
    print(f"\n🔍 Iniciando análisis del archivo: {ruta_archivo}")
    
    # 1. Definición de Patrones con Expresiones Regulares (Regex)
    regex_correo = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    regex_telefono = r'\+?\d{10,12}'  # Captura números de 10 a 12 dígitos
    regex_fecha = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'  # Captura formatos DD-MM-AAAA o DD/MM/AAAA
    
    # 2. Estructuras de datos para almacenar coincidencias
    correos_encontrados = []
    telefonos_encontrados = []
    fechas_encontradas = []
    
    # 3. Consumir el generador línea por línea (Lectura eficiente)
    lineas_generador = leer_archivo_por_lineas(ruta_archivo)
    
    for linea in lineas_generador:
        # Buscar correos
        correos = re.findall(regex_correo, linea)
        if correos:
            correos_encontrados.extend(correos)
            
        # Buscar teléfonos
        telefonos = re.findall(regex_telefono, linea)
        if telefonos:
            telefonos_encontrados.extend(telefonos)
            
        # Buscar fechas
        fechas = re.findall(regex_fecha, linea)
        if fechas:
            fechas_encontradas.extend(fechas)
            
    # 4. Limpieza de duplicados
    correos_unicos = list(set(correos_encontrados))
    telefonos_unicos = list(set(telefonos_encontrados))
    fechas_unicas = list(set(fechas_encontradas))

    # 5. Estructurar el resumen final
    resumen = {
        "correos": correos_unicos,
        "telefonos": telefonos_unicos,
        "fechas": fechas_unicas,
        "total_correos": len(correos_unicos),
        "total_telefonos": len(telefonos_unicos),
        "total_fechas": len(fechas_unicas)
    }
    
    return resumen


if __name__ == "__main__":
    ruta_prueba = "tests_sample/documento1.txt"
    resultados = analizar_contenido(ruta_prueba)
    
    if resultados:
        print("\n--- RESUMEN DE HALLAZGOS ---")
        print(f"Correos detectados: {resultados['correos']}")
        print(f"Telefonos detectados: {resultados['telefonos']}")
        print(f"Fechas detectadas: {resultados['fechas']}")
        print(f"Total Correos: {resultados['total_correos']}")
        print(f"Total Telefonos: {resultados['total_telefonos']}")
        print(f"Total Fechas: {resultados['total_fechas']}")