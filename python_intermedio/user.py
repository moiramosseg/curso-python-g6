# Usuario de whatsApp
class Usuario:
    #Atributos de Usuario
    def __init__(self, nombre, nro_telf):
        self.nombre = nombre
        self.nro_telf = nro_telf
    
    #Metodos del Usuario
    def on_line(self):
        print ("estoy en linea")

    def off_line(self):
        print ("estoy fuera linea")


#Instancia de Clase Usuario
luis = Usuario("Luis", 67890745)
print (luis.off_line())

gustavo = Usuario("Gustavo", 78654321)
print (gustavo.on_line())