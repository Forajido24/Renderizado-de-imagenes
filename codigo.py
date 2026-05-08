import os
from PIL import Image
from PIL import ImageFilter
import time as tm
from multiprocessing import Pool


def procesar_imagen(ruta):
    # Abrir imagen
    img = Image.open(ruta)
    
    # Aplicar filtro (escala de grises)
    #img = img.convert("L")
    img = img.filter(ImageFilter.FIND_EDGES)
    
    # Crear carpeta de salida si no existe
    os.makedirs("procesadas", exist_ok=True)
    
    # Obtener nombre de la imagen
    nombre = os.path.basename(ruta)
    
    # Guardar imagen procesada
    nueva_ruta = os.path.join("procesadas", nombre)
    img.save(nueva_ruta)

def secuencial():
    ruta = "imagenes"
    lista_imagenes = os.listdir(ruta)
    inicio = tm.time()
    for image in lista_imagenes:
        ruta_completa = os.path.join(ruta, image)
        procesar_imagen(ruta_completa)
    fin = tm.time()
    print("Se ha terminado el procesado")
    print("Tiempo de ejecución secuencial : ", fin-inicio)


def paralelo():
    ruta = "imagenes"
    lista_imagenes = [os.path.join(ruta,archivo) for archivo in os.listdir(ruta)]
    inicio= tm.time()
    with Pool() as p:
        p.map(procesar_imagen, lista_imagenes)
    fin= tm.time()
    print("Se ha terminado el procesado")
    print("Tiempo de ejecución paralelo : ", fin-inicio)



if __name__ == "__main__":
    
    # Crear carpeta donde se guardarán las copias
    os.makedirs("imagenes", exist_ok=True)

    # Cargar la imagen original
    imagen = Image.open("foto/Foto_proyecto.jpeg")  # asegúrate que el nombre coincida

    # Número de copias
    cantidad = 50

    # Crear copias
    for i in range(cantidad):
        nombre = f"imagenes/img_{i}.jpg"
        imagen.save(nombre)

    print(f"Se generaron {cantidad} imágenes correctamente")

    ts = secuencial()

    tp = paralelo()
