from perro import Perro
from gato import Gato

def main():
    gaturro = Gato("Peluza", "Siames")
    cachoro = Perro("Dalto", "pastor aleman")

    print (f"Soy un {gaturro.hablar()} nombre {gaturro.nombre}")
    print (f"Soy un {cachoro.hablar()} nombre {cachoro.nombre}")

main()