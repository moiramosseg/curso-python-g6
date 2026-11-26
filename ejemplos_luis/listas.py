nombres = ["Luis", "Gustavo", "Axel", "Cecilia"]
nombres_ordenado = sorted(nombres)
print(nombres_ordenado)
print(list(reversed(nombres_ordenado)))

nombre_nuevo = input("")
nombres_ordenado.append(nombre_nuevo)
print(list(sorted(nombres_ordenado)))
