import csv
import os

def exportar_reporte_txt(nombre_archivo, datos_organizados):
    """
    Genera un reporte legible en formato de texto plano (.txt).
    Recibe el nombre del archivo final y un diccionario con el resumen de los cambios.
    """
    try:
        # Asegurar que el archivo se guarde con la extensión correcta
        if not nombre_archivo.endswith('.txt'):
            nombre_archivo += '.txt'
            
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write("==================================================\n")
            archivo.write("         REPORTE DE OPTIMIZACIÓN DE ARCHIVOS     \n")
            archivo.write("==================================================\n\n")
            
            total_archivos = 0
            for carpeta, archivos in datos_organizados.items():
                archivo.write(f"📂 Carpeta Destino: {carpeta}\n")
                archivo.write("-" * 40 + "\n")
                if not archivos:
                    archivo.write("  (No se procesaron archivos para esta categoría)\n")
                for item in archivos:
                    archivo.write(f"  • {item}\n")
                    total_archivos += 1
                archivo.write("\n")
                
            archivo.write("=" * 50 + "\n")
            archivo.write(f"Total de archivos procesados exitosamente: {total_archivos}\n")
            archivo.write("=" * 50 + "\n")
            
        print(f"[+] Reporte de texto generado con éxito: {nombre_archivo}")
        return True
    except Exception as e:
        print(f"[-] Error al generar el reporte TXT: {e}")
        return False

def exportar_reporte_csv(nombre_archivo, datos_organizados):
    """
    Genera un reporte estructurado en formato tabular (.csv).
    """
    try:
        if not nombre_archivo.endswith('.csv'):
            nombre_archivo += '.csv'
            
        # Definimos las columnas del reporte tabular
        columnas = ['Carpeta Destino', 'Nombre del Archivo']
        
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
            escritor = csv.writer(archivo_csv)
            # Escribir la cabecera
            escritor.writerow(columnas)
            
            # Escribir las filas con los datos de los archivos procesados
            for carpeta, archivos in datos_organizados.items():
                for item in archivos:
                    escritor.writerow([carpeta, item])
                    
        print(f"[+] Reporte tabular CSV generado con éxito: {nombre_archivo}")
        return True
    except Exception as e:
        print(f"[-] Error al generar el reporte CSV: {e}")
        return False