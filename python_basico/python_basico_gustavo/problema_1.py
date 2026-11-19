#curso 5C
index_notas2 = [36, 81, 21, 55, 51, 40, 100, 90, 92, 81]
print("notas aprobadas ")  
for index_notas in range(len(index_notas2)):
    
 if index_notas2[index_notas] > 51: 
  print(index_notas2[index_notas])
        
 print("notas reprobados")    
 if index_notas2[index_notas] < 51:
      
        print(index_notas2[index_notas])

 print("notas excelentes")
 if index_notas2[index_notas] > 90:
        
        print(index_notas2[index_notas])
    