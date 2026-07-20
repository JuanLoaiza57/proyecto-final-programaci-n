import os
import shutil

# Diccionario de extensiones predefinidas para clasificar los archivos
DICCIONARIO_EXTENSIONES = {
    'Documentos': ['.txt', '.pdf', '.docx', '.xlsx', '.pptx', '.csv'],
    'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Audios': ['.mp3', '.wav', '.flac'],
    'Ejecutables': ['.exe', '.msi'],
    'Comprimidos': ['.zip', '.rar', '.tar', '.gz']
}

def clasificar_por_extension(ruta_carpeta, modo_simulacion=True):
    """
    Escanea una carpeta y organiza los archivos en subcarpetas según su extensión.
    """
    # Diccionario para recolectar qué archivos se moverían (sirve para los reportes)
    resumen_procesamiento = {clave: [] for clave in DICCIONARIO_EXTENSIONES.keys()}
    resumen_procesamiento['Otros'] = []
    
    if not os.path.exists(ruta_carpeta):
        print(f"[-] La ruta especificada no existe: {ruta_carpeta}")
        return resumen_procesamiento

    print("\n" + "="*50)
    print(f" PROCESANDO CARPETA: {ruta_carpeta} " + ("(MODO SIMULACIÓN)" if modo_simulacion else "(MODO REAL)"))
    print("="*50)

    # Listar todos los elementos dentro de la carpeta seleccionada
    for elemento in os.listdir(ruta_carpeta):
        ruta_completa = os.path.join(ruta_carpeta, elemento)
        
        # Ignorar si es una carpeta (solo procesamos archivos físicos)
        if os.path.isdir(ruta_completa):
            continue
            
        # Obtener el nombre del archivo y su extensión en minúsculas
        nombre_archivo, extension = os.path.splitext(elemento)
        extension = extension.lower()
        
        # Buscar a qué categoría pertenece la extensión
        categoria_encontrada = 'Otros'
        for categoria, extensiones_validas in DICCIONARIO_EXTENSIONES.items():
            if extension in extensiones_validas:
                categoria_encontrada = categoria
                break
                
        # Registrar el archivo en nuestro resumen
        resumen_procesamiento[categoria_encontrada].append(elemento)
        
        if modo_simulacion:
            print(f"[Simulación] El archivo '{elemento}' se movería a la carpeta -> [{categoria_encontrada}]")
        else:
            # --- MODO REAL ---
            carpeta_destino = os.path.join(ruta_carpeta, categoria_encontrada)
            os.makedirs(carpeta_destino, exist_ok=True)
            shutil.move(ruta_completa, os.path.join(carpeta_destino, elemento))
            print(f"[Movido] '{elemento}' -> Carpeta [{categoria_encontrada}]")

    print("\n[+] Análisis de organización finalizado.")
    return resumen_procesamiento