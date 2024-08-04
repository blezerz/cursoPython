#el loops while sirve mientra el una condicion se cumpla 

monedas= 5

#es necesario tener una linea que aga que se cumpla la condicion
while monedas>0:
    print(f"Tengo {monedas} monedas")
    monedas =monedas-1
else:
    print("no quedan monedas")

#podemos hacer que el usuario escoja cunaod mterminar el loops
respuesta="s"
while respuesta =="s":
    respuesta=input("quires seguir? (s/n)")
else:
    print("Gracias")

#metodo pass que sirve para pasar el loop sin ejecutar nada

while respuesta=="s":
    pass

#existre brack que sirve para romper el ciclo y salir de el lopps

nombre=input("tu nombre: ")
for letra in nombre:
    if letra=="r":
        break
    print(letra)


#existre continue que pase al siginete ciclo sin ejecutar nada

nombre=input("tu nombre: ")
for letra in nombre:
    if letra=="r":
        continue
    print(letra)