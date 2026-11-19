import csv

with open('names.csv','w', newline='') as csvfile:
    fieldnames = ['nombre', 'apellido']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'nombre': 'Luis', 'apellido': 'Gonzalez'})
    writer.writerow({'nombre': 'Juan', 'apellido': 'Perez'})
    writer.writerow({'nombre': 'Maria', 'apellido': 'Gomez'})