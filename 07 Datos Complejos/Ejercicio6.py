# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno.

# Diccionario para guardar los alumnos y sus notas
alumnos = {}

# Ingreso de datos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i + 1}: ")
    print(f"Ingresá las 3 notas de {nombre}:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

# Cálculo y muestra de promedios
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{nombre}: {promedio}")