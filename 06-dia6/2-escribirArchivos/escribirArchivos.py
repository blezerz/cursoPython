#al darle un segundo parametro al archivo agrehar='a'; 
# sobreescribir = 'w' ;solo lectura='r'
#si no ponemos nada se abrikra como solo lectura
archivo = open('06-dia6/2-escribirArchivos/prueba.txt','w')
#este metodo elimina el texto anterior dejando solo el nuevo
archivo.write('Soy el nuevo texto 2')

#tenemos el metodo writelines que nos permite agregar una lista de string a un archivo
#esto escribe las palbra una detras de otra
lista = ['hola','mundo','aqui','estoy']
archivo.writelines(lista)


#si queremos agregarle un espacio entre ellas se puede usar un for in 
for p in lista:
    archivo.writelines(p + ' ' )
archivo.close()

#con al dejamos el cursor al final del archivo por ello solo agregaria datos 
archivo = open('06-dia6/2-escribirArchivos/prueba.txt','a')

archivo.write('soy agregar')

