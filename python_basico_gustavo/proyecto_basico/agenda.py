import csv
import os

carpeta_proyecto = os.path.dirname(__file__)
agenda_csv = os.path.join(carpeta_proyecto, 'contactos_agenda.csv')
contactos = []

def cargar_contactos():
    # Revisa si el archivo existe antes de abrirlo
    if os.path.exists(agenda_csv):
        with open(agenda_csv, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for fila in reader:
                contactos.append(fila)

def guardar_contactos(contactos):
    with open(agenda_csv, 'w', newline='', encoding='utf-8') as csvfile:
        base_contactos = ['nombre', 'telefono', 'gmail']
        writer = csv.DictWriter(csvfile, fieldnames=base_contactos)
        writer.writeheader()
        for contacto in contactos:
            writer.writerow(contacto)

def agregar_contacto(contactos):
    print("Agregar contacto")
    try:
        nombre = str(input("Ingresa tu nombre: "))
    except ValueError:
        print("Ingresa un nombre válido")
        return
    nombre = nombre.title()
    
    try:
        telefono = int(input("Ingresa tu telefono: "))
    except ValueError:
        print("Ingresa un teléfono válido")
        return

    try:
        gmail = str(input("Ingresa tu correo electronico: "))
    except ValueError:
        print("Ingresa un correo electrónico válido")
        return
    gmail = gmail.lower()

    contactos.append({"nombre": nombre, "telefono": telefono, "gmail": gmail})

    guardar_contactos(contactos)
    print(f"{nombre} fue agregado")

def ver_contactos(contactos):
    print("Ver contactos")
    if len(contactos) == 0:
        print("La agenda está vacía.")
    else:
        numero = 1
        for contacto in contactos:
            print(f"{numero}. {contacto['nombre']} | {contacto['telefono']} | {contacto['gmail']}")
            numero = numero + 1

def buscar_contacto(contactos):
    print("Buscar contacto")
    if len(contactos) == 0:
        print("La agenda está vacía.")
        return

    texto_buscar = input("Ingresa el nombre a buscar: ")
    encontrados = 0

    for contacto in contactos:
        if texto_buscar.lower() in contacto["nombre"].lower():
            print(f"- {contacto['nombre']} | {contacto['telefono']} | {contacto['gmail']}")
            encontrados = encontrados + 1

    if encontrados == 0:
        print("No se encontraron coincidencias.")

def eliminar_contacto(contactos):
    print("Eliminar contacto")
    if len(contactos) == 0:
        print("La agenda está vacía.")
        return

    ver_contactos(contactos)

    try:
        numero_eliminar = int(input("Número del contacto a eliminar: "))

        if numero_eliminar < 1 or numero_eliminar > len(contactos):
            print("Número no válido")
        else:
            # Restamos 1 porque las listas empiezan en 0
            eliminado = contactos.pop(numero_eliminar - 1)
            guardar_contactos(contactos)
            print(f"{eliminado['nombre']} fue eliminado")
    except ValueError:
        print("Número no válido")

def salir():
    print("Adiosito!")

#OPCION DEL MENU
cargar_contactos()

while True:
    print("======== MI AGENDA ========")
    print("Bienvenido a mi agenda")
    print("Selecciona una opcion del menu")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    try:
        opcion_menu = int(input("Ingresa la opcion: "))
    except ValueError:
        print("\nIngresa un número válido del 1 al 5\n")
        continue

    match opcion_menu:
        case 1:
            agregar_contacto(contactos)
        case 2:
            ver_contactos(contactos)
        case 3:
            buscar_contacto(contactos)
        case 4:
            eliminar_contacto(contactos)
        case 5:
            salir()
            break
        case _:
            print("Invalido") 