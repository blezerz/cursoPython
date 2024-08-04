def dobleCero(*args):
    lista=[]
    for arg in args:
        lista.append(arg)
    cont=0
    for num in lista:
        
        if num == 0:
            cont +=1
    if cont > 1 :
        return True
    else:
        return False
    
print(dobleCero(1,6,1,4,4,0))
