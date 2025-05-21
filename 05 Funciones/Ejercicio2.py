# Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva 
# un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

#Funciones
def saludar_usuario(nombre):
    nombre = input("Ingresa tu nombre: ")
    print(f"Hola, {nombre}! ¿Cómo estás?")
    
#Programa principal
saludar_usuario("Mario Campana")