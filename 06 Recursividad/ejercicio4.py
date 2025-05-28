'''
Crear una función recursiva en Python que reciba un número entero positivo en base decimal y 
devuelva su representación en binario como una cadena de texto.
'''
from math import trunc # Importa la función trunc de la librería math para truncar números decimales

def binario(n):
    binFinal = ""  # Variable para almacenar el resultado final en formato binario
    binArray = []  # Lista para almacenar los dígitos binarios
    if n == 0:
        binArray[0] = 0  # Manejo del caso especial cuando n es 0
    else:
        # Bucle para dividir el número por 2 y extraer el residuo
        while n != 0:
            entero = trunc(n / 2)  # Obtener la parte entera de n dividido por 2
            decimal = n % 2  # Obtener el residuo (0 o 1)
            n = entero  # Actualizar n para el siguiente ciclo
            binArray.append(decimal)  # Agregar el dígito binario a la lista
    binArray = binArray[::-1]  # Invertir la lista para obtener el orden correcto
    for i in binArray:
        binFinal = binFinal + str(i)  # Concatenar los dígitos binarios en un string
    return binFinal  # Retornar el resultado en formato binario


#main
decimal = int(input("Ingrese un número decimal para transformarlo en binario: "))
print(f"El número {decimal} en binario es {binario(decimal)}.")

