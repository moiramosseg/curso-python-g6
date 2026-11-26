def pon_altura():
    altura = float(input("Ingresa tu altura: "))
    return altura

try:
    pon_altura()
except ValueError:
    print("Tipo invalido")
    print("Ingresa de nuevo")
    pon_altura()
