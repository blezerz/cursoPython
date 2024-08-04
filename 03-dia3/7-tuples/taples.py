#los tuple son inmutables, no se pueden cambiar
mi_tuple=(1,2,2)

#si se asigna la misma cantida de variables que los elementos que tena un tuple, se asignara un valor por variable
x,y,z=mi_tuple
print(x)

#podemos transformar un tuple a una lista para asi nodufuarlo y viserversa
mi_tuple=list(mi_tuple)

#con el metodo count, podemos contar cuantas veces se repite un valor
print(mi_tuple.count(2))

#con el metodo index, buscamos el indice del elemnto

print(mi_tuple.index(1))
