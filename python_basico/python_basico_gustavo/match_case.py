from enum import Enum

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    YELLOW = 'yellow'

user_input = input("Enter a color (red, green, blue, yellow): ")

try:
    # Intentamos convertir la entrada a un miembro de Color
    color = Color(user_input)
except ValueError:
    # Si no es válido, asignamos None o un valor que el match pueda manejar
    color = None

match color:
    case Color.RED:
        print("You selected red.")
    case Color.GREEN:
        print("Grass is green.")
    case Color.BLUE:
        print("I'm feeling the blues :(")
    case Color.YELLOW:
        print("You selected yellow.")
    case _:
        print("Invalid color selected.")
