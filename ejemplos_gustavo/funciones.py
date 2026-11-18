#calculadora con que realiza operaciones basicas
# las cuatro basicas
print("----------------------------------------------")
print("--------------CALCULADORA BASICA--------------")
print("----------------------------------------------")


operacion.split = (f primer_nro = input(), operacion = input(), segundo_nro = int(input()))
#operacion = input()
#segundo_nro = int(input())
print({primer_nro},{operacion},{segundo_nro})


print ((f"numeros ingresados: {primer_nro} y {segundo_nro}"))

def multiplicar(primer_nro, segundo_nro):
        resultado_de_multiplicar = primer_nro * segundo_nro
        
    
        print(f"El resultado de la multiplicacion es: {resultado_de_multiplicar}")

def dividir(primer_nro, segundo_nro):
        resultado_de_dividir = primer_nro / segundo_nro
        print(f"El resultado de la division es: {resultado_de_dividir}")

def sumar(primer_nro, segundo_nro):
        resultado_de_sumar = primer_nro + segundo_nro
        print(f"El resultado de la suma es: {resultado_de_sumar}")

def restar(primer_nro, segundo_nro):
        resultado_de_restar = primer_nro - segundo_nro
        print(f"El resultado de la resta es: {resultado_de_restar}")

if operacion == "*":
    multiplicar(primer_nro, segundo_nro)
elif operacion == "/":
    dividir(primer_nro, segundo_nro)
elif operacion == "+":
    sumar(primer_nro, segundo_nro)
elif operacion == "-":
    restar(primer_nro, segundo_nro)

print (operacion)

#print("----------------------------------------------")
#print("------------------RESULTADOS------------------")
#print("----------------------------------------------")


#RESULTADOS
#multiplicar(primer_nro, segundo_nro)
#dividir(primer_nro, segundo_nro)
#sumar(primer_nro, segundo_nro)
#restar(primer_nro, segundo_nro)
