# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.


# Solicitar al usuario una frase
frase = input("Ingresá una frase: ")

# Separamos en palabras (se usa split por defecto, separa por espacios. Pasamos a minúsculas las palabras)
palabras = frase.lower().split()

# Obtener palabras únicas usando un set
palabras_unicas = set(palabras)
print("\nPalabras únicas:")
print(palabras_unicas)

# Contar la cantidad de veces que aparece cada palabra
conteo_palabras = {}

for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

print("\nFrecuencia de cada palabra:")
for palabra, cantidad in conteo_palabras.items():
    print(f"{palabra}: {cantidad}")