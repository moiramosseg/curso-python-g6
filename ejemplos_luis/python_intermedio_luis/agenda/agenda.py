class agenda:
    def __init__(self, contactos, dispositivo):
        self.contactos = contactos
        self.dispositivo = dispositivo

    def agregar_contacto(self, contacto):
        self.contactos.add(contacto)

    def eliminar_contacto(self, contacto):
        self.contactos.remove(contacto)

    def buscar_contacto(self, nombre):

    def ver_contactos(self):