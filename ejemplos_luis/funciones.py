#calculadora con operacioens basicas
print("------Calculadora basica------")

primer_num = float(input("primer numero: "))
segundo_num = float(input("segundo numero: "))

operacion = str(input("elija la operacion a usar: "))

print((f"primero {primer_num} segundo {segundo_num}"))

def suma (nro_uno, num_dos):
    resultado_sum = nro_uno + num_dos
    print(resultado_sum)

def resta (nro_uno, num_dos):
    resultado_res = nro_uno - num_dos
    print(resultado_res)

def multiplicar (nro_uno, num_dos):
    resultado_mul = nro_uno * num_dos
    print(resultado_mul)

def division (nro_uno, num_dos):
    resultado_div = nro_uno / num_dos
    print(resultado_div)

if (operacion == "+"):
    suma(primer_num, segundo_num)
elif (operacion == "-"):
    resta(primer_num, segundo_num)
elif (operacion == "*"):
    multiplicar(primer_num, segundo_num)
elif (operacion == "/"):
    division(primer_num, segundo_num)
else:
    print("operador no valido")
