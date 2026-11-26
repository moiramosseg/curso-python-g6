class contactos:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def actualizar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono

    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email

contacto_luis = contactos("Luis", 123456789, "lmenchacacruz@gmail.com")
print(contacto_luis.nombre)

contacto_luis.actualizar_nombre("Luis Menchaca")
print(contacto_luis.nombre)