#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en 
# los videos o bien investigar cómo funciona el indexing con números negativos! 
# animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]    #Defino la lista animales con los elementos originales

#Modifico los elementos pedidos
animales[1] = "loro"
animales[-1] = "oso"

#Imprimo por pantalla la lista modificada
print(animales)