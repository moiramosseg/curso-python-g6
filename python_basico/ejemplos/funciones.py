#calculadora con que realize las operaciones basicas
# muntiflicacion, division, resta y suma
primer_nro = float (input("Ingresa el primer Nro. "))
segundo_nro = float (input("Ingresa el segundo Nro. "))
operacion  = str(input("Ingresa la operacion. "))

print ((f"numeros {primer_nro} segundo {segundo_nro}"))

def multiplicar(nro_uno, nro_dos):
    resultado_multiplicar = nro_uno * nro_dos
    #print(resultado_multiplicar)
    return resultado_multiplicar

def dividir(nro_uno, nro_dos):
    resultado = nro_uno / nro_dos
    print(resultado)

def sumar(nro_uno, nro_dos):
    resultado = nro_uno + nro_dos
    print(resultado)

def restar(nro_uno, nro_dos):
    resultado = nro_uno - nro_dos
    print(resultado)


if(operacion == "+"):
    sumar(primer_nro, segundo_nro)
elif(operacion == "-"):
    restar(primer_nro, segundo_nro)
elif(operacion == "*"):
   resultado = multiplicar(primer_nro, segundo_nro)
   print(f"retorno reultado {resultado}")
elif(operacion == "/"):
    dividir(primer_nro, segundo_nro)
else:
    print ("Operacion no valida")

