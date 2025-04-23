# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

#Ingreso del número por el usuario.
numero = int(input("Ingresa un número: "))

# Verificamos si es negativo
signo = -1 if numero < 0 else 1
numero = abs(numero)

#Convertimos a cadena, invertimos, y volvemos a convertir a número

invertido = int(str(numero)[::-1]) * signo

print("Número invertido:", invertido)