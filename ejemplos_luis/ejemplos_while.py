
"""nro_vidas = 3
while nro_vidas > 0:
    print (nro_vidas)
    nro_vidas = nro_vidas-1
print ("Has perdido tus vidas")"""

#problema
#notas del curso 5C 36,81,21,55,51,40,100,90,92,81
notas_5c = [36, 81, 21, 55, 51, 40, 100, 90, 92, 81]
print ("execelencia")
for i in range(len(notas_5c)):
    
    if (notas_5c[i] > 90):
        print (notas_5c[i])

print ("aprobaste")
for i in range(len(notas_5c)):
    
    if (notas_5c[i] >= 51):
        print (notas_5c[i])

print ("reprobaste")
for i in range(len(notas_5c)):
    
    if (notas_5c[i] < 51):
        print (notas_5c[i])