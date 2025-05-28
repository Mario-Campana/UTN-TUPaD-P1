'''
Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función 
para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el 
número que indique el usuario
'''

def factorial(num):
    if num == 0: 
        return 1 
    else: 
        return num * factorial(num-1)

#main

num = int(input("Ingrese un número para conocer su factorial: "))
print(f"El factorial de {num} es {factorial(num)}.")