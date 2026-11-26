import csv
import os

def agregar_contacto():
    print("Agregar contacto")
    nombre = str(input("Ingresa tu nombre: "))
    telefono = int(input("Ingresa tu telefono: "))
    gmail = str(input("Ingresa tu correo electronico: "))


def ver_contactos():

    print("Ver contactos")

def buscar_contacto():

    print("Buscar contacto")

def eliminar_contacto():

    print("Eliminar contacto")

def salir():

    print("Adiosito!")

#bienvenida
print("======== MI AGENDA ========")
print("Bienvenido a mi agenda")
print("Selecciona una opcion del menu")
print("1. Agregar contacto")
print("2. Ver contactos")
print("3. Buscar contacto")
print("4. Eliminar contacto")
print("5. Salir")

opcion_menu = int(input("Ingresa la opcion: "))

match opcion_menu:
    case 1:
        agregar_contacto()
    case 2:
        ver_contactos()
    case 3:
        buscar_contacto()
    case 4:
        eliminar_contacto()
    case 5:
        salir()
    case _:
        print("Invalido")