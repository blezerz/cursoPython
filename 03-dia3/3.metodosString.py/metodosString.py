texto="este es el texto de bim"
#metodo todo en mayusculas
resultado= texto.upper()
print(resultado)
#podemos darle el indice a texto y a ese caracter lo dejara en mayuscula
resultado= texto[3].upper()
print(resultado)

#metodo todo en minusculas
resultado= texto.lower()
print(resultado)
#podemos darle el indice a texto y a ese caracter lo dejara en mayuscula
resultado= texto[3].lower()
print(resultado)


#separa en una lista las palabras 
resultado= texto.split()
print(resultado)
#si en los parametros le doy un caracter tomara a ese caracter como el separador 
resultado= texto[3].split("t")
print(resultado)

a="Aprender"
b="python"
c= "es"
d="genial"
#creara una lista con las palabras de sus variables
e=" ".join([a,b,c,d])
print(e)

#cambia la los caracteres por los indicados
resultado=texto.replace("Federico","Todos")