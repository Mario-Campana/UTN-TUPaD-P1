# Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva 
# una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
# de forma clara.


#Funciones

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b !=0 else "No es posible dividir por cero"
    
    return (suma,resta,multiplicacion,division)

#Programa principal
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

operaciones = operaciones_basicas(a,b)

print(f"suma = {operaciones[0]}")
print(f"resta = {operaciones[1]}")
print(f"multiplicación = {operaciones[2]}")
print(f"división = {operaciones[3]}")