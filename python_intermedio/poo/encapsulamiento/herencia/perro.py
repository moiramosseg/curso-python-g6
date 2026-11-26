from animal import Animal

class Perro(Animal):
    def __init__(selft, nombre, raza):
        super().__init__(nombre)
        selft.raza = raza

    #Sobreescritura de metodos
    def hablar(selft):
        return "Guau guau"

    
