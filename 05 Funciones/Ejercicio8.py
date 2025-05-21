# Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura 
# en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a 
# la función para mostrar el resultado con dos decimales.


#Funciones
def calcular_imc(peso, altura):
    IMC = peso/(altura**2)
    return IMC

#Programa principal

print("A continuación deberá ingresar su peso y altura para saber su índice de masa corporal.")
peso = int(input("Ingrese su peso en kilogramos: "))
altura = int(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso,altura)

print(f"Su IMC es {imc}")