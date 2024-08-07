def menuInicial():
    primeraOpcion=input("""Escoje una opcion
1)Leer una Receta
2)Cargar nueva Receta
3)Crear nueva Categoria
4)Eliminar Receta
5)Elimnar Categoria
6)Finalizar Programa
""")
    return primeraOpcion

menuUno=9
while True:
    try:
        menuUno=int(menuInicial())
        if menuUno <=1 and menuUno >=6:
            print('correcto')
            break
    except:
        print('ingrese dato correcto')


print(menuUno)
    