# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.


# Crear un diccionario para almacenar los contactos
agenda = {}

# Cargar 5 contactos
print("CARGA DE CONTACTOS:")
for contacto in range(5):
    nombre = input(f"Ingresá el nombre del contacto {contacto + 1}: ")
    numero = input(f"Ingresá el número telefónico de {nombre}: ")
    agenda[nombre] = numero

# Consultar un número por nombre
print("\nCONSULTA DE NÚMERO:")
nombre_buscar = input("Ingresá el nombre del contacto que querés buscar: ")

if nombre_buscar in agenda:
    print(f"El número de {nombre_buscar} es: {agenda[nombre_buscar]}")
else:
    print("Contacto no encontrado.")