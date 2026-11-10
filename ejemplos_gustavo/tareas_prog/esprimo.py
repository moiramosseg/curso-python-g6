n = int(input("ingresa un numero para saber si es primo o no:  "))

if n < 1:
    print("El número debe ser mayor o igual a 1. Intenta de nuevo.")
    n = int(input())

elif n % n == 0:
    print("SI") 
elif n % n == 1:
    print("NO")   