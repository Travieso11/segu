import hashlib
import os

def calcular_hash_md5(ruta_archivo):
    """Calcula el hash MD5 de un archivo."""
    md5_hash = hashlib.md5()
    with open(ruta_archivo, "rb") as archivo:
        for byte_block in iter(lambda: archivo.read(4096), b""):
            md5_hash.update(byte_block)
    return md5_hash.hexdigest()

def comparar_hashes_en_carpeta(carpeta, hash_conocido):
    """Compara los hashes de todos los archivos .jpg en una carpeta con un hash conocido."""
    for archivo in os.listdir(carpeta):
        if archivo.lower().endswith('.jpg'):
            ruta_archivo = os.path.join(carpeta, archivo)
            hash_generado = calcular_hash_md5(ruta_archivo)
            print(f"Comparando {archivo}... Hash generado: {hash_generado}")
            if hash_generado == hash_conocido:
                print(f"¡Coincide con {archivo}!")
                return  # Detener la comparación al encontrar el primer archivo coincidente
    print("No se encontraron coincidencias.")

# Ruta de la carpeta que contiene las imágenes
carpeta_imagenes = "/home/asier/Descargas/imagen"  # Cambia esto por la ruta a tu carpeta
hash_conocido = "e5ed313192776744b9b93b1320b5e268"  # Reemplaza esto con el hash que tienes

comparar_hashes_en_carpeta(carpeta_imagenes, hash_conocido)

