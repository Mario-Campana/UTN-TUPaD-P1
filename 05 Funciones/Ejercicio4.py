# Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva 
# el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva
# el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los 
# resultados.

#Importación de libreria math---------------------------------------------------------------------------------
import math

#Funciones----------------------------------------------------------------------------------------------------
def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return math.pi * 2 * radio

#Programa principal-------------------------------------------------------------------------------------------

radio = float(input("Ingrese el valor del radio para saber el área y el perímetro del circulo correspondiente  : "))

#Uso las funciones guardando los resultados en variables y redondeando a dos valores
area = round(calcular_area_circulo(radio),2)
perimetro = round(calcular_perimetro_circulo(radio),2)

print(f"El área del circulo es {area} mientras que su perímetro es {perimetro}." )