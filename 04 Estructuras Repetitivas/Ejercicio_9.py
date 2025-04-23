# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcula la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

#Instrucción para el usuario y definición de la variable acumuladora en 0.
print("A continuación deberá ingresar una lista de 100 números enteros.")
suma = 0

#Bucle para el ingreso de los números. Se va acumulando la suma.
for t in range (0,100):
    a = int(input("Ingrese el siguiente número: "))
    suma += a

#Calculo de la media de los 100 números ingresados.
media = suma / 100

#Muestro por pantalla la respuesta.
print("La media de los números ingresados es", media)