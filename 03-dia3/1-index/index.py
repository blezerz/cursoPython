miTexto="Esto es una preuba"
#con numero negativo cuenta de izquerda a derecha
resultado=miTexto[9]
print(resultado)

miTexto="Esto es una prueba"
#con el metodo index podemos buscar el indice de un caracter
resultado=miTexto.index("n")
print(resultado)
#con una palabra, nos dara el idice de donde empieza una palabra
resultado=miTexto.index("n")
print(resultado)

#si un caracter se repite mostrara el indice de la primera encontrada
resultado=miTexto.index("a")
print(resultado)

#le podemos dar parametros desde donde empezar a buscar y asta donde
resultado=miTexto.index("a",5,10)
print(resultado)

#rindex hace lo mismo per alrevez buscando de izquerda a derecha
resultado=miTexto.rindex("a",5,10)
print(resultado)

