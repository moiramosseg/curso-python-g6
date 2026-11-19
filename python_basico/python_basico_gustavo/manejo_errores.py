def ingreso_altura ():
    altura =float(input("ingresa tu altura :"))
    return altura

try:
   
   altura = ingreso_altura()
   

except ValueError:
    print("tipo invalido ")
    altura = ingreso_altura()

edad = int(input("ingresa tu edad :"))

