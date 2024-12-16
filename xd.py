import matplotlib.pyplot as plt


def cargar_graficas(productos,ventas,clientes):
    while True:
        # Mini menú
        print("\n--- Menú de Opciones ---")
        print("1. Ventas Totales Por Categoria")
        print("2. Productos mas Vendidos")
        print("3. Tendencias de venta")
        print("4. Comparativo de ventas por categoria")
        print("5. Grafico de tendencia de ventas")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            print('Ventas totales:')
            ventas_totales_grafica(ventas,productos)
        elif opcion == '2':
            print("Productos mas vendidos:")
            productos_mas_vendidos(ventas,productos)
        elif opcion == '3':
            print("Tendencia de ventas")
            tendencias_ventas(ventas, productos)
        elif opcion == '4':
            print("Comparativo de ventas por categoría: ")
            comparativo_ventas_categoria(ventas,productos)
        elif opcion == '5':
            grafica_tendencia_ventas(ventas)
        elif opcion == '6':
            print("¡Hasta luego!")
            break #Salir del mini menu de informes graficos
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 6.")

def ventas_totales_grafica(ventas_read,productos_read):
    productos = {producto[0]: producto[2] for producto in productos_read}
    categorias = {}
    for venta in ventas_read:
        id_producto = venta[1]
        cantidad = int(venta[2])
        categoria = productos.get(id_producto,"Sin categoría")
        categorias[categoria]= categorias.get(categoria,0) + cantidad
        print(categorias.keys())
    plt.bar(categorias.keys(),categorias.values())
    plt.title("Ventas Totales por Categoria")
    plt.xlabel("Categorías")
    plt.ylabel("Cantidad Vendida")
    plt.show()
def productos_mas_vendidos(ventas_read, productos_read):
    productos = {producto[0]: producto[1] for producto in productos_read}
    conteo_ventas = {}
    # Contar Ventas de cada produco
    for venta in ventas_read:
        id_producto = venta[1]
        cantidad = int(venta[2])
        
        # Acumular la cantidad vendida por cada producto
        if id_producto in conteo_ventas:
            conteo_ventas[id_producto] += cantidad
        else:
            conteo_ventas[id_producto] = cantidad
    
    # Ordenar los productos por ventas de mayor a menor
    productos_ordenados = sorted(conteo_ventas.items(), key=lambda x: x[1], reverse=True)
    
    # Tomar los 3 productos más vendidos
    top_3_productos = productos_ordenados[:3]
    
    # Preparar datos para la gráfica
    nombres_productos = []
    ventas_productos = []
    
    # Convertir los productos a nombres
    for id_producto, ventas in top_3_productos:
        nombre_producto = productos.get(id_producto, "Producto desconocido")
        nombres_productos.append(nombre_producto)
        ventas_productos.append(ventas)
    
    # Crear la gráfica de barras
    plt.bar(nombres_productos, ventas_productos)
    plt.title("Top 3 Productos más vendidos")
    plt.xlabel("Productos")
    plt.ylabel("Cantidad Vendida")
    plt.show()
def tendencias_ventas(ventas_read, productos_read):
    productos = {producto[0]: producto[1] for producto in productos_read}
    
    ventas_por_fecha = {}
    
    for venta in ventas_read:
        fecha = venta[3]  # La fecha está en la posición 3 del CSV
        cantidad = int(venta[2])  # La cantidad está en la posición 2
        id_producto = venta[1]  # El ID de producto está en la posición 1
        
        if fecha in ventas_por_fecha:
            ventas_por_fecha[fecha] += cantidad
        else:
            ventas_por_fecha[fecha] = cantidad
    
    fechas_ordenadas = sorted(ventas_por_fecha.keys())
    
    cantidades_ventas = [ventas_por_fecha[fecha] for fecha in fechas_ordenadas]
    
    plt.plot(fechas_ordenadas, cantidades_ventas, marker='o')
    plt.title("Tendencia de Ventas por Fecha")
    plt.xlabel("Fecha")
    plt.ylabel("Cantidad Vendida")
    plt.grid(True, linestyle='--', alpha=0.7)  
    plt.tight_layout() 
    plt.show()

def comparativo_ventas_categoria(ventas_read, productos_read):
    productos = {producto[0]: producto[2] for producto in productos_read}
    
    ventas_categorias = {}
    precios_categorias = {}
    
    for venta in ventas_read:
        id_producto = venta[1]
        cantidad = int(venta[2])
        categoria = productos.get(id_producto, "Sin Categoría")
        
        precio = next((float(producto[3]) for producto in productos_read if producto[0] == id_producto), 0)
        
        ventas_categorias[categoria] = ventas_categorias.get(categoria, 0) + cantidad
        precios_categorias[categoria] = precios_categorias.get(categoria, 0) + (cantidad * precio)
        
    categorias = list(ventas_categorias.keys())
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6)) #Figura con dos subplots
    
    ax1.bar(categorias, ventas_categorias.values())
    ax1.set_title("Cantidad Vendida por categoria")
    ax1.set_xlabel("Categorías")
    ax1.set_ylabel("Cantidad Vendida")
    
    ax2.bar(categorias, precios_categorias.values())
    ax2.set_title("Ingresos por Categoría")
    ax2.set_xlabel("Categorías")
    ax2.set_ylabel("Ingresos ($)")
    
    plt.tight_layout()
    
    plt.show()
        # Creo que puede hacerse mejor

def grafica_tendencia_ventas(ventas):
    ventas_fecha = {}
    for venta in ventas:
        fecha = venta[3]
        cantidad = int(venta[2])
        
        ventas_fecha[fecha] = ventas_fecha.get(fecha, 0) + cantidad
    fechas_ordenadas = sorted(ventas_fecha.keys())
    cantidad_ventas = [ventas_fecha[fecha] for fecha in fechas_ordenadas]
    
    plt.plot(fechas_ordenadas, cantidad_ventas, marker= 'o', linestyle = '-', linewidth = 2, markersize = 8)
    plt.title("Tendencia de Ventas")
    plt.xlabel("Fecha")
    plt.ylabel("Cantidad Vendida")
    
    for i, cantidad in enumerate(cantidad_ventas):
        plt.text(fechas_ordenadas[i],cantidad, str(cantidad))
    plt.tight_layout()
    plt.show()





def main():
    # Instanciar la clase para analizar archivos
    analizador = AnalizarArchivos()
    
    # Rutas de los archivos CSV
    clientes_path = 'datos/clientes.csv'
    productos_path = 'datos/productos.csv'
    ventas_path = 'datos/ventas.csv'

    # Cargar los datos desde los archivos CSV
    analizador.cargar_datos(clientes_path, productos_path, ventas_path)

    # Obtener los productos cargados
    productos = analizador.obtener_productos()
    ventas = analizador.obtener_ventas()
    clientes = analizador.obtener_clientes()
    
    # Menú de opciones
    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Resumen de datos")
        print("2. Estimar ventas futuras de un producto")
        print("3. Simulación de compra")
        print("4. Revisión de productos dentro de un presupuesto ")
        print("5. Relacion Productos-Clientes")
        print("6. Informes Graficos")
        print("7. Salir")
        
        opcion = input("Seleccione una opción (1-7): ")

        if opcion == '1':
            mostrar_resumen(analizador) 
        elif opcion == '2':
            mostrar_menu(analizador)
        elif opcion == '3':
            # Ejecutar la simulación de compra
            simular_compra(productos)
        elif opcion == '4':
            revision_presupuesto()
        elif opcion == '5':
            ProductoCliente(ventas,productos,clientes)           
            print("----")
        elif opcion == '6':
            print('Cargando graficas...')
            cargar_graficas(productos,ventas,clientes)
        elif opcion == '7':
            print("¡Hasta luego!")
            break  # Salir del programa

        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 7.")

main()