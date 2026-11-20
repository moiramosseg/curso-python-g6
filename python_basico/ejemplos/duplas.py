
cumpleanos = (15, "marzo", 2010)
coordenadas_tupiza = (-21.44, -65.72)


print(cumpleanos[1])      # "marzo"
print(cumpleanos.count("marzo"))

# Desempaquetar: asignar cada valor a una variable
dia, mes, anio = cumpleanos
print(f"Nací el {dia} de {mes} de {anio}")

# Esto da ERROR, porque las tuplas no se pueden modificar:
# cumpleanos[0] = 20   ❌ TypeError