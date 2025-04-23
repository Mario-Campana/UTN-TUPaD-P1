# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#Importo el módulo random que me permite generar valores aleatorios. Uso la función randint entre 0 y 9.
from random import *
num_secreto = randint(0, 9)

#Ingreso del primer valor por el usuario.
num_ingresado = int(input("Adivina el número (entre 0 y 9):"))

#Bucle con los siguientes valores ingresados.
while num_secreto != num_ingresado:
    print("¡Vuelve a intentarlo!")
    num_ingresado = int(input("Adivina el número (entre 0 y 9):"))

print("¡Has acertado, felicitaciones!")