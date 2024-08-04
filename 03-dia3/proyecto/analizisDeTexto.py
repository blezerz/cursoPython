
#el usuario deve ingresar un texto
textoUsuario=input("ingresa un texto").lower
listaLetras=[]
#el usuario deve pedir 3 letras a eleccion
letra1=input("ingresa la primera letra").lower
letra2=input("ingresa la segunda letra").lower
letra3=input("ingresa la tercera letra").lower
listaLetras.append(letra1)
listaLetras.append(letra2)
listaLetras.append(letra2)

#devolver cunatas veces se repitieron estas letras 
conteoLetra1=(textoUsuario.count(listaLetras[0]))
conteoLetra2=(textoUsuario.count(listaLetras[1]))
conteoLetra3=(textoUsuario.count(listaLetras[2]))
print(f"la letra {listaLetras[0]} se a repetido: {conteoLetra1}")
print(f"la letra {listaLetras[1]} se a repetido: {conteoLetra2}")
print(f"la letra {listaLetras[3]} se a repetido: {conteoLetra3}")

#cuantas palabras tiene el texto
listTextoUsuario=textoUsuario.split()#divide el texto en una lista separada por espacios
contTexto=len(listTextoUsuario)
print(f"El Texto tiene un total de : {contTexto}")

#cual es la primera letra del texto y la utlima
primeraLetra=textoUsuario[0]
ultimaletra=textoUsuario[-1]
print(f"La primera letra del texto es: {primeraLetra}")
print(f"La ultima letra del texto es: {ultimaletra}")

#invertir el orden de las palabras
listaInvertida=listTextoUsuario
listaInvertida.reverse()
textoInverso=" ".join(listaInvertida)

#el sistema dira si esta la palabra python
print(f"El texto invertido seria :\n{textoInverso}")

print("python" in listTextoUsuario)



