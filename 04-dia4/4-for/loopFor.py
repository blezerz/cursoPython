lista=['a','b','c']
#el ciclo for sirve para repetir una seccuenca una cantidad de veces predeterminada
for letra in lista:
    print(f"la letra es {letra}")

#podemos devovlver otras cosas de la variable del for como por ejemplo el indice 
for letra in lista:
    numeroLetra= letra.index(letra)+1
    print(f"Letra{numeroLetra}: {letra}")

lista=['pablo','laura','fede','luis','julia']

for nombre in lista:
    #startswith sirve para buscar algo con un determinado caracter
    if nombre.startswith("l"):
        print(nombre)
    else:
        print('Nombre que no comienza con l')


#-...................................
numeros=[1,2,3,4,5,]
mi_valor=0
for numero in numeros:
    mi_valor= mi_valor + numero
print(mi_valor)

#___________________________________-
#se pueden recorrer las palabras e impirmiras con la variable de loops, se puede reccorrer en una lista en un tuple en un diccionario y en un set
palabra="python"
for letra in palabra:
    print(letra)

#se pueden recorrer listas dentro de listas
#esto imprimira cada lista
for objeto in[[1,2],[3,4],[5,6]]:
    print(objeto)

#en la primara variable se guarda el primer dato de la lista y en la segunda el segundo dato, esto segun corresponda
#cantidad de informacion segun la lista
for a,b in[[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

#for en diccionario
#esto imprimira solo la clave y no el valor del diccionario
dic={'clave1':'a','clave2':'b','clave3':'c'}
for item in dic:
    print(item)

#si le agregamos el items() ahi se imprimira el item completo del diccionario clave mas valor
dic={'clave1':'a','clave2':'b','clave3':'c'}
for item in dic.items():
    print(item)

#esto imprimira el valor iteranod uno en uno 
dic={'clave1':'a','clave2':'b','clave3':'c'}
for item in dic.values():
    print(item)

#items tambien los podemos serar con 2 variables en el for una tomara la clave y otra el valor
dic={'clave1':'a','clave2':'b','clave3':'c'}
for a,b in dic.items():
    print(b)