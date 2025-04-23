#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

#Ingreso de los números que forman el intervalo y defino la variable suma para acumular las sucesivas sumas
num1 = int(input("Ingrese la cota inferior. Debe ser un número entero: "))
num2 = int(input("Ingrese la cota superior. Debe ser también un número entero: "))
suma = 0

if num1 > num2:
    print("La cota inferior debe ser menor a la cota superior, intente nuevamente.")
else:
#Bucle for para realizar la suma.
    print("A continuación se muestra la suma de los números correspondientes al intervalo sin incluir los extremos.")
    for i in range(num1+1,num2):
        suma += i

    print("La suma es", suma)   #Muestro resultado por pantalla.