texto="ABCDEFGHIJKLM"
#mostrara el indice3 asta el indice 4, 
fragmento=texto[2:5]
print(fragmento)

#si se omite alguno de los 3 parametros esto lo tomara que es desde el proncipio o asta el fin
#esto dependiendo que parametro falte
fragmento=texto[:5]
print(fragmento)

fragmento=texto[2:]
print(fragmento)

#con un tercer parametro indicara saltos entre la busqueda
fragmento=texto[2:10:3]
print(fragmento)

#con numeros negativos en el salto tomara de izquerda a derecha dentro de los parametros dados
fragmento=texto[2:10:-1]
print(fragmento)
