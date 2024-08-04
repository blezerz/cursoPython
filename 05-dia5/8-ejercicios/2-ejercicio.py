def devolver_alrvez(palabra):
    lista=[]
    for letra in palabra:
        lista.append(letra)
    lista.sort()
    for letra in lista:
        print(letra)
    return lista

palabra=devolver_alrvez("Byron")
print(palabra)