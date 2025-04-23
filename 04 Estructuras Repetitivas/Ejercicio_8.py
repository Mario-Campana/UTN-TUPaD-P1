# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

#Instrucción para el usuario y definición de las variables que cuentan según las condiciones.
print("A continuación deberá ingresar una lista de 100 números enteros.")
positivos = 0
negativos = 0
pares = 0
impares = 0
ceros = 0


#Bucle para ingreso de números.
for z in range (0,100):
    n = int(input("Ingrese el siguiente número: "))

#Condicional para notar negativos, positivos y ceros.
    if n < 0:
        negativos += 1
    elif n > 0:
        positivos += 1
    else:
        ceros += 1

#Condicional para contar pares e impares.
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1


#Salida con las respuestas según los números ingresados.
print("La cantidad de números positivos ingresados es", positivos)
print("La cantidad de números negativos ingresados es", negativos)
print("La cantidad de números ceros ingresados es", ceros)
print("La cantidad de números pares ingresados es", pares)
print("La cantidad de números impares ingresados es", impares)