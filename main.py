import os

#Fichero de lectura
# Abre un archivo en modo escritura ('w' para escribir)
with open('archivo.txt', 'w') as archivo:
    # Escribe contenido en el archivo
    archivo.write('Hola, este es un ejemplo de archivo de texto.\n')
    archivo.write('¡Python es increíble!')
# El archivo se cierra automáticamente al salir del bloque 'with'

# Abre un archivo en modo lectura ('r' para leer)
with open('archivo.txt', 'r') as archivo:
    # Lee el contenido completo del archivo
    contenido = archivo.read()
    print(contenido)
# El archivo se cierra automáticamente al salir del bloque 'with'

# Abre un archivo en modo añadir ('a' para añadir)
with open('archivo.txt', 'a') as archivo:
    # Añade más contenido al archivo
    archivo.write('\nEsto se añadió después del contenido existente.')
# El archivo se cierra automáticamente al salir del bloque 'with'

# Abre un archivo en modo lectura ('r' para leer)
with open('archivo.txt', 'r') as archivo:
    # Lee el contenido completo del archivo
    contenido = archivo.read()
    print(contenido)
# El archivo se cierra automáticamente al salir del bloque 'with'


# Nombre del archivo que deseas borrar
nombre_archivo = 'archivo.txt'

# Verifica si el archivo existe antes de intentar borrarlo
if os.path.exists(nombre_archivo):
    # Borra el archivo
    os.remove(nombre_archivo)
    print(f'El archivo {nombre_archivo} ha sido borrado.')
else:
    print(f'El archivo {nombre_archivo} no existe.')
