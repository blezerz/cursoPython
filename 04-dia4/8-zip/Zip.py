#zip sirve para poder unir 2 listas distintas en tuples

nombre=["ana","Hugo","Valeria"]
edades=[65,29,42,23]
ciudades=["madird","barcelona","berlin"]
#creamos una lista convinada con zip
combinados=list(zip(nombre,edades,ciudades))
#asigna por orden de listas los elementos
#llega asta la lista mas corta luego los demas los ignora
print(combinados)

#podemos recorer los elemnetos de un tuples con un for dandole mas elementos al for
for nombre,edad,ciudad in combinados:
    print(f"{nombre}, tiene {edad} años y vive en{ciudad}")
