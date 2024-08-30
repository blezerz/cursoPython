#podemos crear metodos distinbtos para cada funcion y estas se crean con def


class Pajaro:

    alas= True

    def __init__(self, color,especie):
        self.color = color
        self.especie = especie
        
    #para llamar a un elemento de la instancia del objeto llamamos a self 
    def piar(self):
        print(f'pio, mi color es {self.color}')

    #podemos agregarle variables a nustras funciones
    def volar(self, metros):
        print(f"El pajaros a volado {metros} Metros")
        self.piar()
    
    #podemos cambiar el valor de un atributo de la classe 
    def pintar_negro(self):
        self.color= 'negro'
        print(f"Ahora el pajaro es {self.color}")

    #podegomos hacer un metodo de que abarque a toda la clase no solo a la instancia
    #no se puede acceder a elemetnos de la isntancia solo de la clase en genera;
    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"Puso {cantidad} huevos")

    #no pueden accecer ni a los atributos de la clase ni a la de la instancia
    #sirve para generar metodos que no generaran cambios ni trabajar con argumentos
    #ni de clase ni e metodo 
    @staticmethod
    def mirar():
        print('el pajaro mira')
        
piolin = Pajaro('amarillo','cnario')

piolin.piar()

piolin.volar(50)

   
