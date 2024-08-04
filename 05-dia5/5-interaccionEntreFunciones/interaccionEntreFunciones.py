from random import shuffle

#lista inicial 
palitos=["-","--","---","----"]


#mezclar palitos
#la funcuion "shuffle" nos sirve para revolver una lista
def mezclar(lista):
    shuffle(lista)
    return lista

#pedirle el intento
def probarSuerte():
    intento =""

    while intento not in ["1","2","3","4"]:
        intento=input("Elegir un numero del 1 al 4: ")

    return int(intento)


#comprobar intento
def chequearIntento(lista,intento):
    if lista[intento-1] == "-":
        print("Perdiste")
    else:
        print("te has salvado")

    print(f"te a tocado {lista[intento-1]}")
palitosMezclados=mezclar(palitos)
seleccion= probarSuerte()
chequearIntento(palitosMezclados,seleccion)
