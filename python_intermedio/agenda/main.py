from contacto import Contacto
from agenda import Agenda

def main():
    agenda_python = Agenda('Moises Ramos Segovia')
    
    #contactos
    contacto_moises = Contacto("Moises",6789089, "moises@gmail.com")
   

    #agregando contactos
    agenda_python.agregar_contacto(contacto_moises)

main()
