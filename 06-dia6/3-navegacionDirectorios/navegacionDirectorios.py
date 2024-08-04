import os
#os representa el sistema y con os.getcwd nos da el directorio o ruta donde estampos trabajando
ruta= os.getcwd()

print(ruta)

#nos permite establecer una ruta distinta
#de esta manera se deve trabajar con doble barra inveritda
ruta = os.chdir('C:\\Users\\byron\\Documents\\Curso Python\\06-dia6\\3-navegacionDirectorios')

#ahora podemos abrir directamente el arvhico en cualquier otra carpeta
archivo=open('otroArchivo.txt')
print(archivo.read())
archivo.close()

#tambien podemos crear una nueva carpeta en algun directorio con el metodo makedirs()
#ruta = os.makedirs('C:\\Users\\byron\\Documents\\Curso Python\\06-dia6\\3-navegacionDirectorios\\carpetaDesdePy')


#teniendo una ruta podemos obtener el ultimo directorio el penultimo o ambos
ruta = ('C:\\Users\\byron\\Documents\\Curso Python\\06-dia6\\3-navegacionDirectorios\\carpetaDesdePy')

#obtejenemos el ultimo archivo de nuestra ruta
elemento = os.path.basename(ruta)

#obtenemos el penultimo archivo de nuestra ruta
elemento = os.path.dirname(ruta)

#obtenemos los dos en una tupla
elemento = os.path.split(ruta)


#podemos elminar algun directorio
os.rmdir('C:\\Users\\byron\\Documents\\Curso Python\\06-dia6\\3-navegacionDirectorios\\carpetaDesdePy')

