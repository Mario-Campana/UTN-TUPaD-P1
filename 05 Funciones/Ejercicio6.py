# Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima 
# la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

#Funciones
def tabla_multiplicar(num):
    print(f"1 * {num} = {1*num}")
    print(f"2 * {num} = {2*num}")
    print(f"3 * {num} = {3*num}")
    print(f"4 * {num} = {4*num}")
    print(f"5 * {num} = {5*num}")
    print(f"6 * {num} = {6*num}")
    print(f"7 * {num} = {7*num}")
    print(f"8 * {num} = {8*num}")
    print(f"9 * {num} = {9*num}")
    print(f"10 * {num} = {10*num}")

#Programa principal
numero= int(input("Ingrese un número positivo para ver su tabla de multiplicar: "))

while numero < 0:
    numero= int(input("Ingrese un número para ver su tabla de multiplicar: "))

tabla_multiplicar(numero)
