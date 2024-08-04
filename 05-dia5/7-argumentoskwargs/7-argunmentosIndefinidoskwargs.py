#los kwargs ademas de que nos deja la cantidad de valores como indefinidos
#nos deja darle una clave y nos devolvera un diccioonarop

#def suma(**kwargs):
#    print(type(kwargs))
#suma(x=3, y=5, z=2)

def suma(**kwargs):
    total=0
    #por cada elemento en kwars  nos devolvera sus datos 
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        #suma el valor de cada valor en el kwargs
        total += valor
    return total

#accionamos la funciony le mandamos los datos de clave y valor
print(suma(x=3, y=5 , z=2))

#en este orden se deven poner los elementos 
def prueba(num1, num2, *args, **kwargs):
    #mostramos los int
    print(f'el primer valor es {num1}')
    print(f'el segundo valor es {num2}')
    
    #mostramos los elementos arg
    for arg in args:
        print(f'arg = {arg}')
    
    #mostramos la clave y valores de los **kwargs
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

prueba(15,50,3,40,35,32,12,64, x='uno', y=2, z="tres")


