from pathlib import Path, PureWindowsPath

#con path se deve ocupar solo un / y no el \\ 
carpeta = Path("/Users/byron/Documents/Curso Python/06-dia6/4-pathlib/prueba.txt")

#de esta forma leemos los archivos y no ncesitamos abrirlos o cerrarlos 
print(carpeta.read_text())

#metodo name nos devolvera el nombre del arvhico
print(carpeta.name)

#nos devovlera que tipo de archivo con suffix
print(carpeta.suffix)

#nos devolvera el nombre sin la terminacion stem
print(carpeta.stem)

#una forma de verificar si el archivo exite 

if not carpeta.exists():
    print('Este archivo no existe')
else:
    print('este archivo si existe')


#nos entregara la ruta en fomrato windows
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)