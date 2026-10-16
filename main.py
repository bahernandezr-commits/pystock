print("Bienvenido a PyStock")


def obtener_precio():
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio <= 0:
                print("El precio debe ser mayor que cero.")
            else:
                return precio
        except ValueError:
            print("Entrada inválida. El precio debe ser un valor numérico.")

def obtener_stock():
    while True:
        try:
            stock = int(input("Ingrese la cantidad en stock: "))
            if stock < 0:
                print("El stock no puede tener un valor negativo.")
            else:
                return stock
        except ValueError:
            print("Entrada inválida. El stock debe ser un número entero.")


#los argumentos pueden ser variables, listas, string, int, bool, expresiones, entre otros.
def obtener_texto(mensaje):
    while True:
        #.strip(): elimina los espacios en blanco de los extremos de una cadena.
        texto = input(mensaje).strip()
        if texto == "":
            print("El campo no puede estar vacío.")
        else:
            return texto


def producto_existe(productos, nombre):
    for producto in productos:
        if producto['nombre'].lower().strip() == nombre.lower().strip():
            return True
    return False


def registrar_producto(productos):
    nombre_producto = obtener_texto("Nombre del producto: ")

    if producto_existe(productos, nombre_producto):
        print("Ya existe un producto con ese nombre.")
        return
    
    categoria = obtener_texto("Categoría: ")
    precio = obtener_precio()
    stock = obtener_stock()

    producto = {
        "nombre":nombre_producto,
        "categoria":categoria,
        "precio":precio,
        "stock":stock
    }
    
    productos.append(producto)
    print("\nProducto registrado.\n")


def consultar_productos(productos):
    if productos:
        print("\n=== Productos ===\n")
    
        for i, producto in enumerate(productos, start=1):
            print(f"Producto: {i}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Categoría: {producto['categoria']}")
            print(f"Precio: ${producto['precio']}")
            print(f"Stock: {producto['stock']}\n")
            # for i in range(len(productos)):
            # print(f"Producto {i+1}")
            # print(f"Nombre: {productos[i]["nombre"]}")
            # print(f"Categoría: {productos[i]["categoria"]}")
            # print(f"Precio: ${productos[i]["precio"]}")
            # print(f"Stock: {productos[i]["stock"]}\n")
    else:
        print("\nNo hay productos registrados.")


def obtener_seleccion():
    while True:
        try:
            seleccion = int(input("Seleccione una opción: "))

            #if 1 <= seleccion <= 3:  opción alternativa
            if seleccion > 0 and seleccion < 4:
                return seleccion
            else:
                print("Opción no válida. Seleccione 1, 2 o 3.")

        except ValueError:
            print("Entrada inválida: debes escribir un número entero.")


productos = []

while True:
    print("\n=== PYSTOCK ===\n")
    print("1. Registrar producto")
    print("2. Consultar productos")
    print("3. Salir")

    seleccion = obtener_seleccion()

    if seleccion == 1:
        registrar_producto(productos)

    elif seleccion == 2:
        consultar_productos(productos)
        
    elif seleccion == 3:
        print("Saliendo de PyStock...")
        break