import csv
import os

ARCHIVO = "contactos.csv"
CAMPOS = ["nombre", "telefono", "correo"]


def cargar_contactos():
    contactos = []
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            for fila in csv.DictReader(f):
                contactos.append(fila)
    return contactos


def guardar_contactos(contactos):
    with open(ARCHIVO, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(contactos)


def mostrar_menu():
    print("\n===== MI AGENDA =====")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")


def agregar(contactos):
    nombre = input("Nombre: ").strip().title()
    if not nombre:
        print("El nombre no puede estar vacío")
        return
    telefono = input("Teléfono: ").strip()
    correo = input("Correo: ").strip().lower()
    contactos.append({"nombre": nombre, "telefono": telefono, "correo": correo})
    guardar_contactos(contactos)
    print(f"{nombre} fue agregado")


def ver(contactos):
    if not contactos:
        print("La agenda está vacía")
        return
    for i, c in enumerate(contactos, start=1):
        print(f"{i}. {c['nombre']} | {c['telefono']} | {c['correo']}")


def buscar(contactos):
    texto = input("¿A quién buscas? ").strip().lower()
    encontrados = [c for c in contactos if texto in c["nombre"].lower()]
    if encontrados:
        ver(encontrados)
    else:
        print("No encontré a nadie con ese nombre")


def eliminar(contactos):
    ver(contactos)
    if not contactos:
        return
    try:
        numero = int(input("Número del contacto a eliminar: "))
        if numero < 1:
            raise IndexError
        borrado = contactos.pop(numero - 1)
    except ValueError, IndexError:
        print("Número no válido")
        return
    guardar_contactos(contactos)
    print(f"{borrado['nombre']} fue eliminado")


def main():
    contactos = cargar_contactos()
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        match opcion:
            case "1":
                agregar(contactos)
            case "2":
                ver(contactos)
            case "3":
                buscar(contactos)
            case "4":
                eliminar(contactos)
            case "5":
                print("¡Hasta pronto!")
                break
            case _:
                print("Opción no válida")


main()