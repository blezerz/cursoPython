palabra='python'
#de esta forma puedo crear una lista con cada letra del string
letra =[letra for letra in palabra]

print(letra)

#valores numericos y  con if 
lista= [n if n*2 > 10 else "no" for n in range(0,21,2)]

#metros a pies
pies=[10,20,30,40,50]
metros=[ n*3.281 for n in pies]
