from pathlib import Path

#con el metodo home obtengo la base 
base= Path.home()
#se pueden ir agregando secciones para crear la ruta relativa
guia = Path('Barcelona','Sagrada_familia')
print(base)
print(guia)

#podemos pasarle la variable mas secciones para llegar a una ruta y podemos agregar un path dentro de otro
guia= Path(base,'Europa','Espania',Path('Barcelona','Sagrada_familia'))
print(guia)

#podemos cambiar el ultimo archivo y manteniendo la ruta con with_na
guia2= guia.with_name("La_Pedrera.txt")
print(guia2)

#podemos llamar al directorio anterior ya seleccionado de una ruta con parent
print(guia.parent)

#si agregamos otro parent bajara uno mas en la ruta
print(guia.parent.parent)
print(base)


#enumeracion de los archivos txt de ese directorio
#nos posiconamos en el home y entramos a la carpeta Europa
guia = Path(Path.home(),'Europa')
#ingresamos en un ciclo for con Glob para iterar sobre esos archivos
for txt in Path(guia).glob('*/*.txt'):
    print(txt)

#si agregamos un segundo ** mostrara todos los archivos seleccionados
#desde el directorio seleccionado y todos sos directorios sigientes
for txt in Path(guia).glob('**/*.txt'):
    print(txt)



#para recuperar una parte de una ruta podemos ocupara .relative y le 
guia=Path("Europa","Espania","Barcelona","Sagrada_Familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to(Path("Europa","Espania"))
print(en_europa)
print(en_espania)