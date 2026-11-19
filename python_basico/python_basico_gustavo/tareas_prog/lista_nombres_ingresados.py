nombres_ingresados = []
print ("ingresa cuantos nombres deseas ingresar")
cantidad = int(input())
while cantidad > 0:
    nombre = input("Ingrese un nombre: ")
    nombres_ingresados.append(nombre)
    cantidad -= 1
print("Nombres ingresados:")
for nombre in nombres_ingresados:
    print(nombre)
print("quieres ordenar la lista de nombres? (si/no)")
respuesta = input()
if respuesta == "si":
    nombres_ingresados.sort()
    print("Nombres ordenados:")
    for nombre in nombres_ingresados:
        print(nombre)
else:
    print( )

    
