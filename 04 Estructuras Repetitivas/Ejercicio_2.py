#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

#Ingreso el número entero y lo guardo en una variable
num_entero = int(input("Ingrese un número entero: "))
cant_digitos = 0

#Manejo ingreso de 0
if num_entero == 0:
    cant_digitos = 1

#Manejo números negativos (paso a positivo antes de bucle)
if num_entero <= 0:
    num_entero = -num_entero

#Bucle para contar digitos
while num_entero >= 1:
    num_entero = num_entero // 10
    cant_digitos += 1


print(f"La cantidad de digitos del número ingresado es {cant_digitos}")