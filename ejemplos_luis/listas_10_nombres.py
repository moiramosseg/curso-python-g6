nombres = []
print("Ingrese 10 nombres: ")
for i in range(10):
    nombre = input(f"Nombre {i+1}: ")
    nombres.append(nombre)
nombres.sort()
print("--- Lista de nombres ---")
for nombre in nombres:
    print(nombre)