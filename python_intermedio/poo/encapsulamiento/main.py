from cuenta_bancaria import CuentaBancaria
def main():
    cuenta_Moises = CuentaBancaria("Cta Moises")
    monto = 1000
    cuenta_Moises.depositar(monto)
    
    
    print (cuenta_Moises.saldo)

main()    


