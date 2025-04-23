# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

#Variable acumuladora.
sumatoria2 = 0

#Ingreso del primer número por el usuario.
x = int(input("Ingrese un número positivo: "))

#Manejo de valores menores a 0
if x <= 0:
    print("El número ingresado no es positivo, intente nuevamente.")
#Sumas hasta el número ingresado.
else:
    for c in range(0,x+1):
        sumatoria2 += c
    print("La suma desde 0 hasta", x, "es igual a", sumatoria2)