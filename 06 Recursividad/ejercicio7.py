'''
Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el 
siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y 
devuelva el total de bloques que necesita para construir toda la pirámide.

'''

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n-1)
    
#main
num_bloques_base = int(input("Ingrese la cantidad de bloques correspondiente a la base de la pirámide: "))

print(f"La cantidad de bloques necesarios para formar una pirámide con base {num_bloques_base} es {contar_bloques(num_bloques_base)}.")