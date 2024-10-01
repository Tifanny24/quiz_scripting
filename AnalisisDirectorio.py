import os
import sys

def analizar_archivos_texto(directorio):
    archivos_txt = [archivo for archivo in os.listdir(directorio) if archivo.endswith('.txt')]
    
    if not archivos_txt:
        with open(os.path.join(directorio, 'informe.txt'), 'w', encoding='utf-8') as informe:
            informe.write("No se encontraron archivos de texto.\n")
        print("No se encontraron archivos de texto. Informe generado.")
        return

    with open(os.path.join(directorio, 'informe.txt'), 'w', encoding='utf-8') as informe:
        for archivo in archivos_txt:
            ruta_archivo = os.path.join(directorio, archivo)
            
            try:
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo_actual:
                    lineas = archivo_actual.readlines()
                    total_lineas = len(lineas)
                    total_palabras = sum(len(linea.split()) for linea in lineas)
                    veces_python = sum(linea.lower().count('python') for linea in lineas)

                    informe.write(f"Nombre del archivo: {archivo}\n")
                    informe.write(f"Número de líneas: {total_lineas}\n")
                    informe.write(f"Número total de palabras: {total_palabras}\n")
                    informe.write(f"Número de veces que aparece 'Python': {veces_python}\n")
                    informe.write("\n")
                
                print(f"Análisis completado para el archivo: {archivo}")
            
            except IOError:
                print(f"Error: No se pudo leer el archivo {archivo}. Revisa los permisos del archivo.")

    print("El informe se ha generado correctamente como 'informe.txt'.")

def main():
    if len(sys.argv) != 2:
        print("Uso correcto: python analisisDirectorio.py <directorio>")
        sys.exit(1)

    directorio = sys.argv[1]
    
    if not os.path.isdir(directorio):
        print(f"Error: El directorio '{directorio}' no existe. Verifica la ruta.")
        sys.exit(1)

    analizar_archivos_texto(directorio)

if __name__ == "__main__":
    main()

