#año bisiesto = año divisible por 4 y 400, pero por 100 es normal 
año = int(input("ingresa un año: "))

if (año % 4 == 0 and año % 100 == 0 ) and (año % 400 == 0) :
    print("BISIESTO")
else:
    print("NORMAL")

