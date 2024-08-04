from io import *
#llama al archivo
mi_archivo = open('06-dia6\prueba.txt')
#lee el archivo en modo paiton
print(mi_archivo.read())



#para obtener una linea en especifico se puede hacer con readline()
una_linea=mi_archivo.readline()
#escribiria la primera linea
print(una_linea)

#si sobreescribimos de la misma manera con readline la variable pasaremos a la segunda linea 
una_linea=mi_archivo.readline()
#imprimimos la segunda linea
print(una_linea.rstrip())

#por defecto se imprime un salto de linea si quisieramos cancelar ese salto de linea podemos aplicar 
#el metodo rstrip()s

#cerrar archivo
mi_archivo.close()

#podemos recorrer las lineas del texto

for l in mi_archivo:
    print('aqui dice')

#cib readlines() nos deja 