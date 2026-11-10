#si ambos son multiplo de 3 y 5, imprime fizzbuzz
#si solo es multiplo de 5, imprime buzz
#si solo es multiplo de 3, imprime fizz

print("ingresa un limite")

n = int(input())

for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)
