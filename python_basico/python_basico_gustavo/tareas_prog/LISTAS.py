nombres = ["luis", "gustavo", "alan", "celso"]
nombres_ordenados = sorted(nombres)
print(nombres_ordenados)
print(len(nombres_ordenados))
print(list(reversed(nombres_ordenados)))
nuevo_nombre = input("Ingrese un nuevo nombre: ")
nombres_ordenados.append(nuevo_nombre)
nuevo_nombre = input()
print (nombres_ordenados)