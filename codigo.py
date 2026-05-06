import os
from PIL import Image

# Crear carpeta donde se guardarán las copias
os.makedirs("imagenes", exist_ok=True)

# Cargar la imagen original
imagen = Image.open("Foto proyecto.jpeg")  # asegúrate que el nombre coincida

# Número de copias
cantidad = 50

# Crear copias
for i in range(cantidad):
    nombre = f"imagenes/img_{i}.jpg"
    imagen.save(nombre)

print(f"Se generaron {cantidad} imágenes correctamente")
