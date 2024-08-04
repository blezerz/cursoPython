#los set solo permiten un argunmento por eso se deve poner dentron de algun tipo de llavce () [] {}
#no tiene un orden interno y son unicos y no se puede repetir sus datos
#no permite ni tipo lista ni diccionarios
mi_set=set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

#lo que si aceptan son otros taples
otro_set=set((1,2(3,4),5))

#se puede hacer consultas
print(2 in mi_set)

#union de set con el metodo union
s1={1,2,3}
s2={3,4,5}
s3=s1.union(s2)

#si los elemntos se llegan a repetir solo dejara 1
print(s3)

#se pueden agregar elemeentos con add
s1.add(4)

#se puede eliminar datos apuntando al dato 
s1.remove(3)

#se puede elminar elementos con pop
s1.pop()

#el motod clear nos vacia por completo el set
s1.clear()


