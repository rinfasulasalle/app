def get_matriculas(nombre_archivo):
    # Lista para almacenar los códigos
    codigos = []
    # Abro el archivo CSV en modo lectura
    with open(nombre_archivo, 'r') as archivo_csv:
        # Leo todas las líneas del archivo
        lineas = archivo_csv.readlines()
        # Itero sobre las líneas y elimina los espacios en blanco
        codigos = [linea.strip() for linea in lineas]
    return codigos
# ----------------------------------------------------------
import os
def get_archivos_pdf(directorio):
    archivos_pdf = []  # Creo una lista para almacenar los nombres de archivos PDF encontrados
    # Itero a través de los directorios y archivos utilizando os.walk
    for _, _, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo.lower().endswith(".pdf"):  # Compruebo si el archivo tiene extensión .pdf
                archivos_pdf.append(archivo)  # Agrego el nombre del archivo a la lista
    return archivos_pdf
# ----------------------------------------------------------
LICENCIAS = get_matriculas('pdf/DATA LICENCIAS DE CONDUCIR DUMMIE.csv')
PDFS = (get_archivos_pdf('pdf'))
LOGO = 'https://play-lh.googleusercontent.com/0XXTsNgg5RXGqoDMxwDHpG7A_UlImfGs0CK3jcnm5isWkO4CEz5DP17Pkz46JCihyN4'
