#los diccionarios no tiene un orden, ademas para acceder a ellos se accede mediante sus llaves "c"
diccionario = {"c1":'valor1',"c2":'valor2'}

print(diccionario)
#accedemos al valor mediante la llave 
resultado=(diccionario["c1"])

#ejemplo de diccionario
cliente={"nombre":"juan","apellido":"Fuentes","peso":88,"talla":1.76}

consulta=(cliente["apellido"])
print(consulta)

#un diccionario puede contener todo tipo de valores incluida lista y otros diccionarios
dic={"c1":55,"c2":[10,20,30],"c3":{"s1":100,"s2":200}}



#para poder acceder a un elemento que esta dentro de una lista y este dentro de un diccionario
#le indicamos que en el diccionario en su clave c2 que tiene una lista, seleccione el elemento con indice 1
print(dic["c2"][1])
#para buscar en el diccionario dentro del diccionario
print(dic["c3"]["s2"])

#seleccioanr un elemneto lista dentor de un diccionario y dejarlo en mayuscula
dic={"c1":["a","b","c"],"c2":["d","e","f"]}
print(dic["c2"][1].upper())

#agregar un elemento
dic={1:"a",2:"c"}
print(dic)
dic[3]="c"
print(dic)

#sobreescribir un valor existente

dic[2] = "B"
print(dic)

#nos mostrara todas las claves
print(dic.keys)

#nos entregara los valores
print(dic.values())

#nos dara todos los valores
print(dic.items())