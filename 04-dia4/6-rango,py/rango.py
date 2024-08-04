#con range podemos dar distintos tipos de rango a distintas cosas 
#por ejemplo en for , esto ara que se ejecute 5 veces
for numero in range(5):
    print(numero)


#si le agregamos un segundo parametro dira desde donde asta donde
for numero in range(1,15):
    print(numero)

#al agregarle un tercer parametro establecemos cada cuantos pasos se saltara el numero
for numero in range(1,15,3):
    print(numero)



#para crear listas, esto creara una lista del 1 al 100 
lista=list(range(1,101))
print(lista)

