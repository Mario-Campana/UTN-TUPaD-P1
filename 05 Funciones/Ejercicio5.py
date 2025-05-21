# Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como 
# parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos 
# y mostrar el resultado usando esta función.


#Funciones
def segundos_a_horas(segundos):
    return round (segundos / 3600, 2)

#Programa principal
segundos = int(input("Ingrese una cantidad de segundos para saber a cuántas horas equivalen: "))

horas = segundos_a_horas(segundos)

print(f"La cantidad de segundos ingresada ({segundos}) equivale a {horas} hora/s.")