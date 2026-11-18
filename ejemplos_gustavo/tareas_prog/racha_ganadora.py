enteroT = int(input())
for caso in range(1,enteroT+1):
    resultados = input().strip()
    actual = 0
    mejor = 0

    for racha in resultados:
        if (racha == "G"):
            actual += 1
            if (actual > mejor):
                mejor = actual
        else:
            actual = 0
    print(f"(Caso #{caso}: {mejor})")