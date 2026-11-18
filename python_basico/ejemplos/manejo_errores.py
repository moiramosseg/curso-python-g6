def ingreso_altura():
    altura = float(input("Ingresa tu Altura: "))
    return altura

try:
    ingreso_altura()
except ValueError:
    print("Tipo Invalido... Ingresa de nuevo")
    ingreso_altura()


