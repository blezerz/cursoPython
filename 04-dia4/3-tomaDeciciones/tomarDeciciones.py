if 10 > 9:
    print("es correcto")
else:
    print("no es correcto")

mascota="perro"
#con if tenemos condiciones para que se ejecute algo segun los valores de comaracion
if mascota=="gato":
    print("Tienes un gato")
elif mascota =="perro":
    print("tienes un perro")
elif mascota=="pez":
    print("tines un pez")
else:
    print("no se que mascota tienes")

#podemos anidar los if
edad=16
calificacion=9
if edad <18:
    print("Eres menor de edad")
    if calificacion >=7:
        print("aporbado")
    else:
        print("no aprobado")
else:
    print("eres adulto")


