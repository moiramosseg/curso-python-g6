array_notas = [90, 70, 51, 50]
edades = [20, 21, 18, 60]
array_nombres = ["queso", "luis", "moises"]

#P1: listar las notas aprobadas, que existen en las notas
for index_nota in range(len(array_notas)):
    print (index_nota)
    
    if array_notas[index_nota] >= 51:
       print ("Aprobado")
       print (array_notas[index_nota])
       
    else: 
       print ("Reprobado")
       print (array_notas[index_nota])
       
"""#i es indice
i = 0
i = 1
i = 2
i = 3
#len es tamaño 
len => 4"""