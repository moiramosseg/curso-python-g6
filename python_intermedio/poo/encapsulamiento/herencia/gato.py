from animal import Animal

class Gato(Animal):
    def __init__(selft, nombre, raza):
        super().__init__(nombre)
        selft.raza = raza

    #Sobreescritura de metodos
    def hablar(selft):
        return "Miau Miau"