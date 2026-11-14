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


def obtener_seleccion(limite):
    if limite < 1:
        print("Error: el límite debe ser mayor que cero.")
        return
    while True:
        try:
            seleccion = int(input("Seleccione una opción: "))

            #if 1 <= seleccion <= 4:  opción más legible
            if seleccion > 0 and seleccion < 5:
                return seleccion
            else:
                print("Opción no válida. Seleccione 1, 2, 3 o 4.")

        except ValueError:
            print("Entrada inválida: debes escribir un número entero.")



def obtener_texto(mensaje):
    while True:
        #.strip(): elimina los espacios en blanco de los extremos de una cadena.
        texto = input(mensaje).strip()
        if texto == "":
            print("El campo no puede estar vacío.")
        else:
            return texto
        

def buscar_producto(productos, nombre):
    for producto in productos:
        if producto['nombre'].lower().strip() == nombre.lower().strip():
            return producto
    return None

def editar_producto(productos):
    nombre = obtener_texto("Ingrese el nombre del producto que desea editar: ")
    producto = buscar_producto(productos, nombre)

    if producto is None:
        print("No se encontró un producto con ese nombre.")
        return
    
    print("\nProducto encontrado:\n")
    print(f"Nombre: {producto['nombre']}")
    print(f"Categoría: {producto['categoria']}")
    print(f"Precio: ${producto['precio']:,.2f}")
    print(f"Stock: {producto['stock']}")

    print("\n¿Qué atributo desea modificar?")
    print("1. Modificar nombre")
    print("2. Modificar categoría")
    print("3. Modificar precio")
    print("4. Modificar stock")

    seleccion = obtener_seleccion(4)

    if seleccion == 1:
        nuevo_nombre = obtener_texto("Ingrese el nuevo nombre: ")
        producto_encontrado = buscar_producto(productos,nuevo_nombre)

        if producto_encontrado is not None and producto_encontrado is not producto:
            print("Ya existe un producto con ese nombre.")
            return
        #return no solamente sirve para devolver un valor. También podemos utilizarlo
        #para finalizar anticipadamente la ejecución de una función.
        else:
            producto['nombre'] = nuevo_nombre
    
    elif seleccion == 2:
        producto['categoria'] = obtener_texto("Ingrese la nueva categoría: ")
    elif seleccion == 3:
        producto['precio'] = obtener_precio()
    elif seleccion == 4:
        producto['stock'] = obtener_stock()
    
    print("\nProducto actualizado correctamente.")

productos=[{
    "nombre": "Mouse",
    "categoria": "Periféricos",
    "precio": 45000,
    "stock": 8
}]



editar_producto(productos)
