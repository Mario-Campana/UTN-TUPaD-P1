'''
Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
'''

def fibonacci(pos):
    if pos == 0 or pos == 1:
        return pos
    else:
        return fibonacci(pos - 1) + fibonacci (pos - 2)
    
#main
posicion = int(input("Ingrese hasta que posición de fibonacci desea ver: "))

for i in range(0,posicion+1):
    print(f"La posición {posicion} de fibonacci es: {fibonacci(i)}")
    