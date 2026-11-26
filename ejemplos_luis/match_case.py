from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

entrada = input("Escribe 'red', 'blue' o 'green': ")

try:
    color = Color(entrada)
    
    match color:
        case Color.RED:
            print("¡Veo rojo!")
        case Color.GREEN:
            print("El pasto es verde")
        case Color.BLUE:
            print("Siento tristeza :(")
            
except ValueError:
   
    print("¡Error! Ese color no está en la lista permitida.")