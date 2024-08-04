def cheaquear_3_cifras(numero):
    return numero in range (100,1000)

suma=586+402

resultado =cheaquear_3_cifras(235)
print(resultado)
##revisamos que en una lista de numeros verfique cada elemento de ella
def cheaquear_3_cifras2(lista):

    nLista =[]

    for n in lista:
        if n in range(100,1000):
            #en return se corta la funcion
            nLista.append(n)
        else:
            pass
    return nLista

resultado = cheaquear_3_cifras2([55,99,600])