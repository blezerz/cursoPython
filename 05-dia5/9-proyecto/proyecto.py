from random import *
listaPalabras=["hola","pelota",'rio','azul','rayoz','avion','coco']
def palabraSecreta(listaPalabra):
    lista=[]
    txtPalabraSecreta = choice(listaPalabra)
    for letra in txtPalabraSecreta:
        lista.append(letra)
    return lista


def listaIncognita(lista1):
    lista=[]
    for i in lista1:
        lista.append('_')
    return lista

def obtenerLetra():
    a=input('escoje una letra al azar: ')
    return a

def juego():
    #lista de la palabra secreta
    palabraJuego=palabraSecreta(listaPalabras)
    palabraIncognita=(listaIncognita(palabraJuego))
    contVida=5
    while contVida>0:

        print (palabraIncognita)
        letra=obtenerLetra()
        print(letra)
        if letra in palabraJuego and letra not in palabraIncognita:
            for a,i in enumerate(palabraJuego):
                if letra==i:
                    palabraIncognita[a]=i
        elif letra in palabraIncognita:
            print('Esa Letra ya la has seleccionado con anterioridad')
                    
        else :
            contVida-=1
            print(f'te quedan {contVida}')
        if contVida ==0:
            print('se te acabaron las vidas')
            break
        if palabraIncognita==palabraJuego:
            print('has adivando la palabra')
            break

                      
juego()

