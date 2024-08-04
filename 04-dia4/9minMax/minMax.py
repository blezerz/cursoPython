menor=min(58,96,72,64,35)
mayor=max(58,96,72,64,35)
print(mayor)
print(menor)

menor=[58,96,72,64,35]

print(f"el menor numero es {min(menor)} y el maximo es {max(menor)}")

menor=["Bim","loco","toche","ernesto","brat"]
#con las palabras funciona alfabeticamente empezando por minusculas 
print(f"la palabra mas baja del diccionario es {min(menor)}, y la palabra mas alta es {max(menor)}")
#es lo mismo con los string


#con los dicionatrios
dic={"C1":45, "C2":11}
#cuando se busca el minimo se giara por su clave pero se puede ocupar .values para que tome el valor enves de la clave
print(f"el valor mas bajo de el diccionario es {min(dic.values())}, y la clave mas baja es {min(dic)}")