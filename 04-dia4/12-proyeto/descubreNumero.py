from random import randint
nombre=input("cual es tu nombre?")
intentos=int(5)
numero=int(randint(1,10))
for n in range(5):
        numeroUsuario = int(input("Escoge un número del 1 al 10: "))
        if numeroUsuario == numero:
            print("!correcto")
            break 
        elif numeroUsuario > numero:
            intentos=intentos-1
            print(f"es un numero menor y te quedan {intentos} intentos")

        else:
            intentos=intentos-1
            print(f"es un numero mayor te quedan {intentos} intentos")

if intentos !=0:
     print("Felidades has Ganado")
else:
     print("lo sineto has perdido")