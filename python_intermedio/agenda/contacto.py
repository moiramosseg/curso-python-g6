class Contacto:
    def __init__(self, nombre, telefono, email):
        self._nombre = nombre
        self._telefono = telefono
        self._email = email

    def set_nombre(self,nombre_nuevo):
        self._nombre = nombre_nuevo
    
    def set_telefono(self,telefono_nuevo):
        self._telefono = telefono_nuevo
    
    def set_email(self,email_nuevo):
        self._email = email_nuevo

    def get_nombre(self):
        return self._nombre
    
    def get_telefono(self):
        return self._telefono

    def get_email(self):
        return self._email

    def mostrar(self):
        print (self._nombre)
        print (self._telefono)
        print (self._email)