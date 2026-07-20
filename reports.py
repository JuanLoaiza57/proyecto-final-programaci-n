import csv
import os

def exportar_reporte_txt(nombre_archivo, datos_organizados):
    try:
        if not nombre_archivo.endswith('.txt'):
            nombre_archivo += '.txt'
            
        total_archivos = sum(len(archivos) for archivos in datos_organizados.values())
        
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write("==================================================\n")
            archivo.write("   REPORTE TÉCNICO: AUTOMATIZACIÓN DE ARCHIVOS    \n")
            archivo.write("==================================================\n\n")
            
            # SECCIÓN DE ESTADÍSTICAS OBLIGATORIA POR LA RÚBRICA
            archivo.write("📊 ESTADÍSTICAS GENERALES DE CLASIFICACIÓN\n")
            archivo.write(f"• Total de archivos procesados: {total_archivos}\n")
            for carpeta, archivos in datos_organizados.items():
                cantidad = len(archivos)
                porcentaje = (cantidad / total_archivos * 100) if total_archivos > 0 else 0
                archivo.write(f"  - {carpeta}: {cantidad} archivo(s) ({porcentaje:.1f}%)\n")
            archivo.write("\n" + "-"*50 + "\n\n")
            
            archivo.write("📂 DETALLE DE MOVIMIENTOS POR CATEGORÍA\n")
            for carpeta, archivos in datos_organizados.items():
                archivo.write(f"\n[+] Carpeta Destino: {carpeta}\n")
                archivo.write("------------------------------------------\n")
                if not archivos:
                    archivo.write("    (No se procesaron archivos para esta categoría)\n")
                for item in archivos:
                    archivo.write(f"    • {item}\n")
                    
            archivo.write("\n==================================================\n")
            archivo.write("           FIN DEL REPORTE AUTOMÁTICO            \n")
            archivo.write("==================================================\n")
            
        print(f"[+] Reporte TXT con estadísticas generado: {nombre_archivo}")
        return True
    except Exception as e:
        print(f"[-] Error al generar el reporte TXT: {e}")
        return False

def exportar_reporte_csv(nombre_archivo, datos_organizados):
    try:
        if not nombre_archivo.endswith('.csv'):
            nombre_archivo += '.csv'
            
        columnas = ['Carpeta Destino', 'Nombre del Archivo']
        
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
            escritor = csv.writer(archivo_csv)
            escritor.writerow(columnas)
            
            for carpeta, archivos in datos_organizados.items():
                for item in archivos:
                    escritor.writerow([carpeta, item])
                    
        print(f"[+] Reporte tabular CSV generado con éxito: {nombre_archivo}")
        return True
    except Exception as e:
        print(f"[-] Error al generar el reporte CSV: {e}")
        return False