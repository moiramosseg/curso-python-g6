import os
import csv
#variables globales
nombre_archivo = "contactos.csv"
cabeceras = ["Nombre", "Teléfono", "Correo"]
contactos = []

def agregar_contactos(contactos):
    
    print("Agregar")
    print("ingresa el nombre del contacto")
    nombre = str(input())
    print("ingresa el número de teléfono")
    while True:
        try: 
            telefono = int(input())
            break
        except ValueError:
            print("Por favor, ingresa un número de teléfono válido (solo dígitos).")
    
    print("ingresa el correo electrónico")
    correo = str(input())
    contactos.append((nombre, telefono, correo))
    guardar_contactos(contactos)  # Guardar los datos después de agregar un contacto
    
    print("contacto agregado")
    
# No muestra mensaje cuando no hay contactos y no existe el archivo
def mostrar_contactos():
    if not os.path.exists(nombre_archivo):
        print("No hay contactos guardados.")
        return
    
    print("Mostrar contactos:\n")
    with open(nombre_archivo, "r") as csvfile:
        lector = csv.DictReader(csvfile)
        contactos = [(row["Nombre"], row["Teléfono"], row["Correo"]) for row in lector] #row es un diccionario que representa cada fila del archivo CSV, y se accede a los valores de las columnas mediante sus nombres.
    
    if not contactos:
        print("todavia no hay contactos guardados.\n")
        return
    
    for nombre, telefono, correo in contactos:
        print(f"Nombre: {nombre}\n" f"Teléfono: {telefono}\n" f"Correo: {correo}\n")

# No existe control cuando no existen contactos
# Si no encuentra al contacto muestra si/no, pero no vuelve al menu princiapal
def buscar_contactos():
    print("Buscar contactos:")
    nombre_a_buscar = input("Ingrese el nombre del contacto a buscar: ")
    
    with open(nombre_archivo, "r") as csvfile: #abrira el archivo y lo leera con el sobrenombre de csvfile
        lector = csv.DictReader(csvfile)
        for row in lector:
            if row["Nombre"] == nombre_a_buscar: #verificara si el nombre esta en el csv
                print("Contacto encontrado:\n")
                print(f"Nombre: {row['Nombre']}\n" f"Teléfono: {row['Teléfono']}\n" f"Correo: {row['Correo']}") #lo encontro corectamente y lo imprimira
                return
    print("Contacto no encontrado")#no pudo encontrar el contacto
    print("quieres seguir buscando? (si/no)")
    
    buscar_contactos()  # Llamar a la función otra vez para buscar otro contacto

#elimina siempre cuando cuidide el caso del nombre
def eliminar_contactos():
    if not os.path.exists(nombre_archivo):
        print("\nNo hay contactos para eliminar.\n")
        return

    print("\n Eliminar Contacto: ")
    nombre_a_eliminar = input("Ingrese el nombre del contacto a eliminar: ").strip()
    
    contactos_actualizados = []
    encontrado = False

    with open(nombre_archivo, "r", encoding="utf-8") as csvfile:
        lector = csv.DictReader(csvfile)
        for row in lector:
            # Comparamos ignorando mayúsculas/minúsculas
            if row["Nombre"].lower() == nombre_a_eliminar.lower():
                encontrado = True
            else:
                # Si no es el que queremos eliminar, lo guardamos como tupla (Nombre, Teléfono, Correo)
                contactos_actualizados.append((row["Nombre"], row["Teléfono"], row["Correo"]))
    
    if encontrado:
        # Reescribimos el archivo con la lista actualizada
        guardar_contactos(contactos_actualizados)
        print(f"\n¡El contacto '{nombre_a_eliminar}' ha sido eliminado con éxito!\n")
    else:
        print(f"\nNo se encontró ningún contacto con el nombre '{nombre_a_eliminar}'.\n")

def salir():
    print("fin del programa")
    exit(False)  #hara que el while se detenga y salga del programa

def guardar_contactos(contactos):
    with open(nombre_archivo, "w", newline="") as csvfile:
        escritor = csv.DictWriter(csvfile, fieldnames=cabeceras)
        escritor.writeheader()
        for contacto in contactos:
            escritor.writerow(dict(zip(cabeceras, contacto)))
#bienvenida

while True:

    print("Bienvenido a la agenda de contactos")
    print("===== MI AGENDA =====")
    print ("1. Agregar contacto\n"
        "2. Mostrar contactos\n"
        "3. Buscar contacto\n"
        "4. Eliminar contacto\n"
        "5. Salir")
    opcion_del_menu = int(input("ingresa una opcion: "))
   
    try:
        opcion_del_menu = int(opcion_del_menu)
    except ValueError:
        opcion_del_menu = None  # Asignar un valor predeterminado para manejar la opción inválida
    
    match opcion_del_menu:
        case 1:
            agregar_contactos(contactos)
        case 2:
            mostrar_contactos()
        case 3:
            buscar_contactos()
        case 4:
            eliminar_contactos()
        case 5:
            salir()
        case _:
            print("ingresa un número válido dentro de la lista")