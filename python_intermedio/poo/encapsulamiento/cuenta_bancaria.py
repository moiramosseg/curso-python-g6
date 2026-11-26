class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular #privado
        self.__saldo = saldo #privado

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    #metodo privado: solo clase
    def __sumar__(self):
        print ("metodo privado")

    #metodo publico acceso todos
    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("Monto invalido")
        self.__saldo += monto

    #metodo protegido: objeto y sus hijos
    def _restar_(self):
        print ("Metodo Protegido")

        


