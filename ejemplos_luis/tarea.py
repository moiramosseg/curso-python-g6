# Comprobar el numero de studiantes par o impar de un numero N 
"""numero_estudiantes = int(input())

if numero_estudiantes % 2 == 0:
    print("PAR")
else:
    print("IMPAR")"""

# Leer la temperatura T en grados Celsius dada por la estacion meteorologica
"""temperatura = int(input())

if temperatura < 15:
    print("FRIO")
elif temperatura <= 25:
    print("TEMPLADO")
else:
    print("CALOR")"""

# Leer el año entero y comprobar si es bisiesto segun las reglas dadas
"""año = int(input())

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("BISIESTO")
else:
    print("NORMAL")"""

#suma de numeros de Gauss desde el 1 hasta N
"""numero = int(input())
suma = 0
for i in range(1, numero+1):
    suma += i
print(suma)"""

#la racha ganadora
enterot = int(input())
for caso in range(1, enterot + 1):
    resultados = input().strip()
    actual = 0
    mejor = 0

    for racha in resultados:
        if(racha == "G"):
            actual = actual + 1
            
            if(actual > mejor):
                mejor = actual
        else:
            actual = 0
    print(f"(Caso #{caso}): {mejor}")