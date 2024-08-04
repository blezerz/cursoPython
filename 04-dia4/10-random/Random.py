from random import *
#nos da un numero decimal del 1 lal 50
aleatorio=randint(1,50)
print(aleatorio)
#uniform nos da un numero con decimales 
#agregamos round(redondeo)para controlar los decimales
aleatorio=round(uniform(1,50),2)
print(aleatorio)


#random
#nos data la fraccion de un entero va vacio y simpre
#entregara un decimal entre 0 y 1
aleatorio=random()
print(aleatorio)

#choise nos permite actuar sobre algun elemento de coleccion
#como una lista
colores=['azul','rojo','verde','amarillo']
aleatorio=choice(colores)
#nos entregara un elemento aletorio de la lista
print(aleatorio)


#shuffle actua sobre la lista y la reordena al azar
numeros=list(range(5,50,5))
shuffle(numeros)
print(numeros)