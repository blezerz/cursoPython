def suma(a,b):
    return a+b

print (suma(5,6))

#con *args que toma la cantidad de parametors de una 
#funcion como indefinido, asi el usuario puede ingresar
#mas de un dato como argumento

def suma2(*args):
    for arg in args:
        total += arg
    return total
print (suma(5,6,5,4,6,4,2,))
