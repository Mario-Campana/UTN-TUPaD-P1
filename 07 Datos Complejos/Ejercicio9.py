# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
# Permití consultar qué actividad hay en cierto día y hora.


agenda = {
    ("lunes", "10:00"): "Reunión con equipo",
    ("martes", "14:00"): "Clase de inglés",
    ("miércoles", "09:00"): "Formación en SQL",
    ("viernes", "18:00"): "Cena con amigos"
}

# Solicitar al usuario un día y una hora
dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (formato HH:MM): ")

# Buscar en la agenda
clave = (dia, hora)

if clave in agenda:
    print(f"\nActividad programada para {dia} a las {hora}: {agenda[clave]}")
else:
    print(f"\nNo hay ninguna actividad programada para {dia} a las {hora}.")