'''
Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo 
(numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
'''

def contar_digito(numero, digito):
    # Caso base: si el número tiene un solo dígito
    if numero < 10:
        return 1 if numero == digito else 0
    # Comparar el último dígito del número
    ultimo = numero % 10
    # Llamada recursiva con el resto del número
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
    
#main
veces_que_aparece_1 = contar_digito(111235691,1)

print(veces_que_aparece_1)
