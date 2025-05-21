# Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y 
# devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando 
# esta función.

#Funciones
def calcular_promedio(a, b, c):
    return (a+b+c)/3

#Programa principal
print("Ingrese a continuación tres números enteros positivos para calcular su promedio.")

a = int(input("Ingrese el primer número positivo: ")) 
while a < 0:
    a = int(input("Ingrese el primer número positivo: ")) 

b = int(input("Ingrese el segundo número positivo: ")) 
while b < 0:
    b = int(input("Ingrese el segundo número positivo: ")) 

c = int(input("Ingrese el tercer número positivo: ")) 
while c < 0:
    c = int(input("Ingrese el tercer número positivo: ")) 

promedio = calcular_promedio(a,b,c)

print(f"El promedio de los números ingresados es {promedio}")
