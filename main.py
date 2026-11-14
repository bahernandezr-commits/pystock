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


def buscar_producto(productos, nombre):
    for producto in productos:
        if producto['nombre'].lower().strip() == nombre.lower().strip():
            return producto
    return None


def consultar_producto(productos):
    nombre = obtener_texto("Ingrese el nombre del producto: ")
    busqueda = buscar_producto(productos, nombre)
    if busqueda is None:
        print("No se encontró un producto con ese nombre.")
    else:
        print(f"Nombre: {busqueda['nombre']}")
        print(f"Categoría: {busqueda['categoria']}")
        '''¿Qué significa :,.2f?
        : inicia la especificación de formato.
        , separa los miles con comas.
        .2f muestra exactamente dos cifras decimales.'''
        print(f"Precio: ${busqueda['precio']:,.2f}")
        print(f"Stock: {busqueda['stock']}")


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
        #start permite especificar desde donde empezar la numeración
            print(f"Producto: {i}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Categoría: {producto['categoria']}")
            print(f"Precio: ${producto['precio']:,.2f}")
            print(f"Stock: {producto['stock']}\n")
            # for i in range(len(productos)):
            # print(f"Producto {i+1}")
            # print(f"Nombre: {productos[i]["nombre"]}")
            # print(f"Categoría: {productos[i]["categoria"]}")
            # print(f"Precio: ${productos[i]["precio"]}")
            # print(f"Stock: {productos[i]["stock"]}\n")
    else:
        print("\nNo hay productos registrados.")


def obtener_seleccion(limite):
    if limite < 1:
        print("Error: el límite debe ser mayor que cero.")
        return
    while True:
        try:
            seleccion = int(input("Seleccione una opción: "))

            #if 1 <= seleccion <= 4:  opción más legible
            if 1 <= seleccion <= limite:
                return seleccion
            else:
                print(f"Opción no válida. Seleccione los números de 1 al {limite}")

        except ValueError:
            print("Entrada inválida: debes escribir un número entero.")


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


def eliminar_producto(productos):
    nombre = obtener_texto("Ingrese el nombre del producto que desea eliminar: ")
    producto = buscar_producto(productos, nombre)

    if producto is None:
        print("No se encontró un producto con ese nombre.")
        return

    productos.remove(producto)
    print("El producto fue eliminado exitosamente.")

productos = []

while True:
    print("\n=== PYSTOCK ===\n")
    print("1. Registrar producto")
    print("2. Consultar productos")
    print("3. Buscar producto")
    print("4. Editar producto")
    print("5. Eliminar producto")
    print("6. Salir")

    seleccion = obtener_seleccion(6)

    if seleccion == 1:
        registrar_producto(productos)

    elif seleccion == 2:
        consultar_productos(productos)

    elif seleccion == 3:
        consultar_producto(productos)

    elif seleccion == 4:
        editar_producto(productos)

    elif seleccion == 5:
        eliminar_producto(productos)
        
    elif seleccion == 6:
        print("Saliendo de PyStock...")
        break