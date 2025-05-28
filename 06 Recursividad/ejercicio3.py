'''
Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
utilizando la fórmula n**m= n*n**(m-1). Prueba esta función en un algoritmo general.
'''

def potencia(base,exponente):
    if base == 1:
        return 1
    elif base == 0: return 0
    else:
        return base * (base**(exponente-1))
    

#main
base = int(input("Ingrese la base para el cálculo de la potencia: "))
exponente = int(input("Ingrese el exponente para el cálculo de la potencia: "))

print(f"{base} a la potencia de {exponente} es: {potencia(base,exponente)}")