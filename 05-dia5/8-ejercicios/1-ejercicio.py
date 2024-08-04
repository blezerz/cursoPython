def devolver_distintos(*args):
    lista=[]
    suma=0
    for valor in args:
        lista.append(valor)
        suma+=valor
    minimo=min(lista)
    maximo = max(lista)
    

    if suma >15:
        return max
    elif suma < 10 :
        return minimo
    else:
        for valor in lista:
            if valor !=minimo and valor != maximo:
                resultado= valor
        return resultado
    

numeros=devolver_distintos(1,5,6)
print(numeros)