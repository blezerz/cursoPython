miLista= ["a","b","c"]
#las listas pueden contener objetos de diferentes tipos de datos
otraLista = ["hola",55,6.1]
print(type(miLista))

#con len podemos ver cuantos elementos tiene una lista
resultado=len(miLista)
print(resultado)

#podemos indexar las listas
resultado=miLista[0:3]
#asignar un elemento de un a lista a una variable

elemntoLista=miLista[1]
print(elemntoLista)

#podemos crear una lista uniendo 2 o mas listas
listaUnida=(miLista+otraLista)
#podemos sobreescribir elmentos de las listas
listaUnida[0]="alfa"
print(listaUnida)

#metodo append agrega un elemento al ultimo de la linea
listaUnida.append("g")
print(listaUnida)

#metodo pop elimina un elemento de la lista
#si se deja sin parametros elimina el ultimo elemento
listaUnida.pop()
print(listaUnida)
#si se le asigna un parametro parametro eliminara ese lugar de la lista
listaUnida.pop(2)
print(listaUnida)
#se puede guardar en una variable el elemento eliminado con pop
eliminado=listaUnida.pop(0)
print(eliminado)

#metodo sort, el metodo ordena la lista de menor a mayor o por alfabeto, pero no devulve nada
#actua subre la misma lista y no puede ser asignado como variable
lista10=['g','o','b','m','c']
lista10.sort()
print(lista10)
#metodo reverse, ordena pero al reves y trabaja de la misma manera que sort
lista10.reverse()
print(lista10)

