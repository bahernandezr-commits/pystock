print("Bienvenido a PyStock")

productos = []

while True:
    print("\n=== PYSTOCK ===\n")
    print("1. Registrar producto")
    print("2. Consultar productos")
    print("3. Salir")

    seleccion = int(input("\nSeleccione una opcion: "))

    if seleccion == 1:
        nombre_producto = input("Nombre del producto: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        while precio <= 0:
            print("El precio debe ser mayor que cero")
            precio = float(input("Precio: "))
        stock = int(input("Cantidad en stock: "))
        while stock < 0:
            print("El stock no puede contener valores negativos")
            stock = int(input("Cantidad en stock: "))
        producto = {"nombre":nombre_producto,
                    "categoria":categoria,
                    "precio":precio,
                    "stock":stock}
        productos.append(producto)

        print("\nProducto registrado.\n")

    elif seleccion == 2:
        if productos:
            print("\n=== Productos ===\n")

            for i, producto in enumerate(productos, start=1):
                print(f"Producto: {i}")
                print(f"Nombre: {producto["nombre"]}")
                print(f"Categoría: {producto["categoria"]}")
                print(f"Precio: ${producto["precio"]}")
                print(f"Stock: {producto["stock"]}\n")
            # for i in range(len(productos)):
            #     print(f"Producto {i+1}")
            #     print(f"Nombre: {productos[i]["nombre"]}")
            #     print(f"Categoría: {productos[i]["categoria"]}")
            #     print(f"Precio: ${productos[i]["precio"]}")
            #     print(f"Stock: {productos[i]["stock"]}\n")
        else:
            print("\nNo hay productos registrados.")
        
    elif seleccion == 3:
        print("Saliendo de PyStock...")
        break
    else:
        print("\nOpción no válida. Seleccione 1, 2 o 3.")

# producto1 = {"nombre":"arroz",
#                     "categoria":"granos",
#                     "precio":1234,
#                     "stock":9}

# producto2 = {"nombre":"lentejas",
#                     "categoria":"granos",
#                     "precio":5678,
#                     "stock":6}

# productos = [producto1, producto2]
