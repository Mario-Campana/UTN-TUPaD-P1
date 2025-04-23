# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

#Pido el primer número a ingresar. Defino la variable para acumular.
num = int(input("Ingrese un número (ingrese un 0 para salir): "))
sumatoria = 0


#Bucle mientras el número ingresado no sea 0.
while num != 0:
    sumatoria += num
    num = int(input("Ingrese el siguiente número a ser sumado (ingrese un 0 para salir): "))

print("La sumatoria de los números ingresados es", sumatoria)