# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")


# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 
# Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Ingresa tu nombre:")
print(f"¡Hola {nombre}, mucho gusto!")


# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla 
# una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, 
# el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo 
# si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Ingresa tu nombre por favor: ")
apellido = input("Ahora ingresa tu apellido: ")
edad = int(input("A continuación, ingresa tu edad: "))
lugar = input("¿En qué país vives? ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}. ")


#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = int(input("Ingrese el valor del radio del círculo para saber perímetro y área: "))

print("El perímetro del círculo es ", 3.14*radio)
print("El área del círculo es ", 3.14*radio**2)


#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

print("A continuación, se calculará el equivalente en horas a la cantidad de segundos que ingrese por la terminal. ")
segs = int(input("Ingrese la cantidad de segundos para el cálculo: "))

horas = segs // 3600
resto = segs % 3600

print(f"{segs} segundos equivale a {horas} hora/s y {resto} segundos")


#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

tabla = int(input("Ingrese un número para ver su tabla de multiplicar: "))

print("1 x", tabla, "=", 1 * tabla)
print("2 x", tabla, "=", 2 * tabla)
print("3 x", tabla, "=", 3 * tabla)
print("4 x", tabla, "=", 4 * tabla)
print("5 x", tabla, "=", 5 * tabla)
print("6 x", tabla, "=", 6 * tabla)
print("7 x", tabla, "=", 7 * tabla)
print("8 x", tabla, "=", 8 * tabla)
print("9 x", tabla, "=", 9 * tabla)
print("10 x", tabla, "=", 10 * tabla)


#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, 
# dividirlos, multiplicarlos y restarlos.

print("A continuación, ingrese dos números enteros (num1 y num 2) distintos de 0: ")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

print(f"num 1 + num2 = {num1 + num2}")
print(f"num 1 - num2 = {num1 - num2}")
print(f"num 1 x num2 = {num1 * num2}")
print(f"num 1 / num2 = {num1 / num2}")


#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que 
# el índice de masa corporal se calcula del siguiente modo: IMC = peso en KG / (altura en metros)**2

print("Cálculo del indice de masa corporal.")
peso = int(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / altura**2

print(f"Su índide de masa corporal es: {imc}")



#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 
# Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5 x 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

print("Paso de grados Celsius al equivalente en grados Fahrenheit.")
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = 9/5 * celsius + 32

print(f"{celsius} grados celsius equivalen a {fahrenheit} grados fahrenheit")


#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio de los números ingresados es {promedio}")