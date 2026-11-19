cumpleaños = (20, "noviembre", 2009, "noviembre")
coordenadas_tupiza = (-21.44, -65.72)


print(cumpleaños[2])
print(cumpleaños.count("noviembre"))  
#.count() cuenta cuantas veces se repite un elemento en la tupla  

dia, mes, año = cumpleaños
print(f"Naci el {dia} de {mes} del {año}")