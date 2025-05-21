# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius 
# y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

# Funciones
def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

# Programa principal

celsius = float(input("Ingrese una temperatura en grados Celsius y se devolverá el valor en grados Fahrenheit: "))
fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius} grados Celsius corresponden a {fahrenheit} grados Fahrenheit.")