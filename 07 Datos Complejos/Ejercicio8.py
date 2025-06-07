# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

# Diccionario con productos y su stock inicial
stock_productos = {
    "manzanas": 10,
    "naranjas": 5,
    "peras": 8
}

# Mostrar el stock actual
print("Stock inicial:")
for producto, stock in stock_productos.items():
    print(f"{producto}: {stock} unidades")

# Solicitar al usuario el nombre de un producto
producto = input("\nIngresá el nombre de un producto: ").lower()

if producto in stock_productos:
    print(f"Stock actual de '{producto}': {stock_productos[producto]} unidades")
    
    # Preguntar si quiere agregar más unidades
    agregar = input("¿Querés agregar unidades al stock? (s/n): ").lower()
    if agregar == 's':
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] += cantidad
        print(f"Nuevo stock de '{producto}': {stock_productos[producto]} unidades")
else:
    print(f"El producto '{producto}' no existe.")
    agregar_nuevo = input("¿Querés agregarlo al stock? (s/n): ").lower()
    if agregar_nuevo == 's':
        cantidad = int(input("¿Cuántas unidades tiene?: "))
        stock_productos[producto] = cantidad
        print(f"Producto '{producto}' agregado con {cantidad} unidades.")

# Mostrar el stock final actualizado
print("\nStock final:")
for producto, stock in stock_productos.items():
    print(f"{producto}: {stock} unidades")