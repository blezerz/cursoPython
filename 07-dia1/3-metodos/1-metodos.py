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

piolin = Pajaro('amarillo','cnario')

piolin.piar()

piolin.volar(50)

   
