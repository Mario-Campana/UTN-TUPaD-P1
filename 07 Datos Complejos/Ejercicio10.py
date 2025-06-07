# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

# Diccionario original: países como claves, capitales como valores
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Francia": "París",
    "Italia": "Roma"
}

print("Diccionario original:")
for pais, capital in paises_capitales.items():
    print(f"{pais}: {capital}")

print("-------------------------------------------------------")

# Invertir el diccionario: capitales como claves, países como valores
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

# Mostrar el nuevo diccionario
print("Diccionario invertido (capitales → países):")
for capital, pais in capitales_paises.items():
    print(f"{capital}: {pais}")