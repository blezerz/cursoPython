from random import *
def lanzar_moneda():
    moneda=["Cara","Cruz"]
    lado=choice(moneda)
    return lado

lado=lanzar_moneda()
print(lado)