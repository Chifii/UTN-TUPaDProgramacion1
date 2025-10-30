archivo_productos = "productos.txt"

try:
    with open(archivo_productos, "r", encoding="utf-8") as archivo:
        pass
except FileNotFoundError:
    with open(archivo_productos, "w", encoding="utf-8") as archivo:
        archivo.write("Lapicera,120.5,30\n")
        archivo.write("Cuaderno,85.0,50\n")
        archivo.write("Marcador,95.75,25\n")
    print(f"Archivo '{archivo_productos}' creado con productos iniciales")

def mostrar_productos():
    try:
        with open(archivo_productos, "r", encoding="utf-8") as archivo:
            print("=== PRODUCTOS DISPONIBLES ===")
            for linea in archivo:
                linea_limpia = linea.strip()
                if linea_limpia:
                    datos = linea_limpia.split(",")
                    if len(datos) == 3:
                        nombre, precio, cantidad = datos
                        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
    except FileNotFoundError:
        print("El archivo de productos no existe")

def cargar_productos_en_lista():
    productos = []
    try:
        with open(archivo_productos, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                if linea_limpia:
                    datos = linea_limpia.split(",")
                    if len(datos) == 3:
                        nombre, precio, cantidad = datos
                        producto = {
                            "nombre": nombre,
                            "precio": float(precio),
                            "cantidad": int(cantidad)
                        }
                        productos.append(producto)
    except FileNotFoundError:
        print("El archivo de productos no existe")
    
    return productos

def buscar_producto_por_nombre(productos):
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    encontrado = False
    
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            print("=== PRODUCTO ENCONTRADO ===")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}")
            encontrado = True
            break
    
    if not encontrado:
        print(f"Error: El producto '{nombre_buscar}' no existe en el inventario")

def guardar_productos_actualizados(productos):
    with open(archivo_productos, "w", encoding="utf-8") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Productos actualizados guardados en el archivo")

def programa_completo():
    print("=== SISTEMA DE GESTIÓN DE PRODUCTOS ===")
    
    while True:
        print("\nOpciones:")
        print("1. Mostrar todos los productos")
        print("2. Buscar producto por nombre")
        print("3. Agregar nuevo producto")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == "1":
            productos = cargar_productos_en_lista()
            print("\n=== TODOS LOS PRODUCTOS ===")
            for i, producto in enumerate(productos, 1):
                print(f"{i}. Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
        
        elif opcion == "2":
            productos = cargar_productos_en_lista()
            buscar_producto_por_nombre(productos)
        
        elif opcion == "3":
            productos = cargar_productos_en_lista()
            print("\n=== AGREGAR NUEVO PRODUCTO ===")
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            cantidad = int(input("Cantidad del producto: "))
            
            nuevo_producto = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            }
            productos.append(nuevo_producto)
            guardar_productos_actualizados(productos)
            print(f"Producto '{nombre}' agregado exitosamente")
        
        elif opcion == "4":
            print("¡Gracias por usar el sistema de gestión de productos!")
            break
        
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

programa_completo()
