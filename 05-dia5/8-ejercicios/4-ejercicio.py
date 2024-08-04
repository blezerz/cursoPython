def contar_primos(*args):
    contPrimos=0
    for arg in args:
        
        if arg%1 == 0 and arg%arg==0 and arg>1:
            contPrimos+=1
    if contPrimos==0:
        print("no se encontraron numeros primos")
    else:
        print(f"se encontraron{contPrimos}")

contar_primos(1,4,5,7,6,0,4)