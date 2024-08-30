#atributos de instancias

#creamos la clase
class Pajaro:
    #creamos un construcctor de esta forma cada ves que se cree un objeto sos atributos podran ser distintos
    #pasandolos como parametros
    def __init__(self, color,especie):
        self.color = color
        self.especie = especie
    
    #si creamos un atributo fuera del constructor entonces todos los objetos creados a partir de esta lcase
    #compartiran el mismo atributo 

    alas= True
#creamos el objeto y le damos el parametro que nos esta dando 
mi_pajaro = Pajaro('negro','Tucan')

#podemos llamar al atributo de la clase de la misma manera que a un string
print(mi_pajaro.color)

#podemos llamarlos en una oracion

print(f'mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}')

print(Pajaro.alas)