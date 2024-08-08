import os
from pathlib import Path
from os import system

mi_ruta= Path(Path.home(),'Recetas')

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1

    return contador

    
def inicio():
    system('cls')
    print('*' * 50)
    print("Bienvenido al administrador de recetas")
    print('*' * 50)
    print('\n')
    print(f"Las Recetas se encuentran en {mi_ruta}")
    print(f"Total Recetas:{contar_recetas(mi_ruta)}")

    eleccion_menu= 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print('Elige una opcion:')
        print('''
[1]Leer Receta
[2]Crear receta nueva
[3]Crear categoria nueva
[4]Eliminar Recerta
[5]Eliminar categoria
[6]Salir del progarama''')
eleccion_menu = input()

inicio()

menu = 0 
if menu == 1:
    #mostrar Categorias
    #Elegir categoria
    #mostrar Recetas
    #elegir Receta
    #leer receta
    #volver al inicio
    pass
elif menu == 2:
    #mostrar Categoria
    #Elegir categoria
    #crear Receta nueva
    #volver a incio
    pass
elif menu==3:
    #crear categoria
    #volver inicio
    pass
elif menu ==4:
    #mostrar Categorias
    #Elegir categoria
    #mostrar Recetas
    #elegir Receta
    #Eliminar Receta receta
    #volver al inicio
    pass
elif menu == 5:
    #mostrar categoria
    #elegir categoria
    #eliminar categoria
    #volver inicio
    pass
elif menu ==6:
    #finalizar programa
    pass