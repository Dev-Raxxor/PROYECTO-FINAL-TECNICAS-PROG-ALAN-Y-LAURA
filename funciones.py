# Función Que Muestra El Menú Principal / Otros Menús Con Información
def MostrarMenu (opcion:int):

    #Función Que Ayuda Con La Estructura De La Tabla
    def EspaciosMenu (opcion:int):
        if opcion == 1: return f"{' ' * 23}|{' ' * 52}|\n{' ' * 23}|" #Para El Encabezado
        else: return f"\n{' ' * 23}|{'-' * 52}|\n{' ' * 23}|" #Para El Resto Del Cuerpo De La Tabla

    if opcion == 1:
        menuItems = [ #Opciones Menú Principal
                f" Sistema de Análisis de Ventas - Menú Principal     |\n{' ' * 23}|{' ' * 52}|",  
                " 1. Mostrar Resumen Inicial                         |",    
                " 2. Estimar Ventas Futuras De Un Producto           |",  
                " 3. Simular Compra                                  |",
                " 4. Revisión de productos dentro de un presupuesto  |",
                " 5. Análisis de clientes y productos                |",
                " 6. Informes gráficos                               |",
                " 7. Salir                                           |"
        ]      
    else: 
        menuItems = [ #Opciones Informes Gráficos
            f"       Informes Gráficos - Menú de Opciones         |\n{' ' * 23}|{' ' * 52}|",  
            " 1. Ventas totales por categoría                    |",    
            " 2. Productos más vendidos                          |",  
            " 3. Tendencias de ventas por fecha                  |",
            " 4. Comparativo de ventas por categoría             |",
            " 5. Gráfico de tendencia de ventas                  |",
            " 6. Volver al menú principal                        |"
        ]

    #Imprimir La Tabla
    print(' ' * 23 + '-' * 54)
    for i, item in enumerate(menuItems):
        print(EspaciosMenu(1) + item if i == 0 else EspaciosMenu(2) + item, end = ' ')
    print('\n' + ' ' * 23 + '-' * 54)

# Función Que Valida La Opción Ingresada Por El Usuario Para Un Menú
def ValidarMenu (limInferior:int, limSuperior:int, format):

    while True:
        try:
            opcion = int(input(format + 'Ingrese la opción: '))
    
            # Verifica si la opción no está en el rango permitido
            if not (limInferior <= opcion <= limSuperior):
                
                print(format + f'Error: Opción fuera de rango. Ingrese un número entre {limInferior} y {limSuperior}.')
            
            else: return opcion # Si la opción es válida, sale del bucle
        
        except ValueError:
            
            # Muestra el mensaje de error
            print(format + 'Error: Ingrese un número entero.')

#3
def EstimarVentasMesProximo (categoria):

    import pandas as pd
    # Carga los datos de ventas
    df = pd.read_csv('./archivosActualizadosTiendaCsv/ventasActualizadas.csv')

    # Filtrar solo las columnas necesarias: id_producto y cantidad
    df_filtrado = df[['id_producto', 'cantidad']]


# 5
# Función Que Genera Las Combinaciones De Productos Con Un Presupuesto
def PosiblesComprasPorPresupuesto (presupuesto:float, format):
    
    # Función De Bakctracking Para la Generación De Las Combinaciones
    def GenerarCombinacionesProductos (combinacionActual, indice, totalActual):
        nonlocal mejoresCombinaciones, cantidad_max_productos, presupuesto # -> Variables No Locales

        if totalActual > presupuesto: # -> Condición Para Hacer La Vuelta Atrás (Bakctracking)
            return
        
        # Calcula la cantidad de productos actuales en la combinación
        cantidadActual = len(combinacionActual)

        if cantidadActual > cantidad_max_productos:

            cantidad_max_productos = cantidadActual # Si la nueva combinación tiene más productos, actualiza la cantidad máxima
            
            mejoresCombinaciones = [combinacionActual.copy()] # Se hace una copia para evitar cambios accidentales
        
        elif cantidadActual == cantidad_max_productos:
            
            # Si la nueva combinación tiene la misma cantidad de productos que la mejor hasta ahora, se añade a la lista de mejores combinaciones
            mejoresCombinaciones.append(combinacionActual.copy())
        
        # Iterar sobre los productos restantes para añadirlos a la combinación actual
        for i in range(indice, len(productos)):

            # Añadir el producto actual a la combinación actual
            producto, precio = productos[i]
            combinacionActual.append((producto, precio))

            GenerarCombinacionesProductos(combinacionActual, i + 1, totalActual + precio) # Llamado Recursivo
            combinacionActual.pop() # Ya que cada vez que se salga de la llamada recursvia fue por un exceso en el presupuesto, entonces se quita la última opción añadida

    # Inicio De La Función Para Mostrar Las Combinaciones
    import pandas as pd

    # Leer el archivo CSV
    df = pd.read_csv('./archivosTiendaCsv/productos.csv')

    productos = [] # Lista vacía para almacenar los productos con sus precios

    # Usar zip() para recorrer simultáneamente la columna de productos y precios
    for tipo, valor in zip(df['nombre'], df['precio']): productos.append((f'{tipo}', valor))

    productos = tuple(productos)  # Convertir la lista a tupla
    
    # Variables globales para las mejores combinaciones
    mejoresCombinaciones = []
    cantidad_max_productos = 0
            
    # Llamar a la función de bakctracking para generar las combinaciones
    GenerarCombinacionesProductos([], 0, 0)
    
    # Mostrar resultados
    if mejoresCombinaciones:
        print(format + f"Combinaciones con máximo de productos ({cantidad_max_productos} productos):")
        
        for i, combinacion in enumerate(mejoresCombinaciones):
            total = sum(precio for _, precio in combinacion)
            print(format + f"Combinación {i + 1}: {combinacion}, Total: ${total}")
    
    else:
        print(format + "No hay combinaciones posibles.")

#6
def AnalisisClientesProductos():
    import csv;
    #Menú para seleccionar la categoria en la que se desea conocer el cliente que mas ha comprado 
    def seleccionar_categoria():
        def mostrar_menu():
            print("Seleccione una categoría:\n1. Ropa\n2. Electrónica\n3. Alimentos\n")
            
        def leer_opcion():
            try:
                opcion = int(input("Elija una opción (0 para salir): "))
                return opcion
            except ValueError:
                print("Por favor, ingrese un número válido.")
                return -1

        categoria_seleccionada = None  # Variable para guardar el string de la categoría
        while True:
            mostrar_menu()
            opcion = leer_opcion()

            if opcion == 1:
                categoria_seleccionada = "Ropa"
                break
            elif opcion == 2:
                categoria_seleccionada = "Electronica"
                break
            elif opcion == 3:
                categoria_seleccionada = "Alimentos"
                break
            elif opcion == 0:
                print("Saliendo del programa...")
                categoria_seleccionada = None  # No hay selección
                break
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")

        return categoria_seleccionada  # Retorna el string de la categoría seleccionada

    # Se llama a la funcion seleccionar_categoria para que mjuestre el menú, además se le muestra al usuario que opción que selecciono
    categoria_seleccionada = seleccionar_categoria()  # Llamada a la función
    if categoria_seleccionada:
        print(f"La categoría seleccionada es: {categoria_seleccionada}")
    else:
        print("No se seleccionó ninguna categoría.")
        return  # Salir si no se seleccionó ninguna categoría

    # Leer CSV de ventas
    ventas = []
    with open('ventas.csv', 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        next(lector_csv)
        #El id clientes, id productos y cantidad se ingresaran en una lista 
        for fila in lector_csv:
            id_cliente = int(fila[2])  # El ID de cliente está en la columna 2
            cantidad = int(fila[3])    # La cantidad está en la columna 3
            id_producto = int(fila[1]) # El ID del producto está en la columna 1
            ventas.append([id_cliente, id_producto, cantidad])

    # Leer CSV de clientes y almacenar los datos en una lista
    clientes = []
    with open('clientes.csv', 'r') as archivo_clientes:
        lector_clientes = csv.reader(archivo_clientes)
        next(lector_clientes)  # Omitir cabecera
        #El id clientes, y nombre clientes se ingresaran en otra lista 
        for fila in lector_clientes:
            id_cliente = int(fila[0])  # ID del cliente está en la columna 0
            nombre_cliente = fila[1]
            clientes.append([id_cliente, nombre_cliente])

    # Leer CSV de productos y almacenar los datos en una lista
    productos = []
    with open('productos.csv', 'r') as archivo_productos:
        lector_productos = csv.reader(archivo_productos)
        next(lector_productos)  # Omitir cabecera
        for fila in lector_productos:
            id_producto = int(fila[0])  # ID del producto está en la columna 0
            categoria = fila[2]  # Categoría del producto está en la columna 1
            productos.append([id_producto, categoria])

    # Se agrega a la lista ventas 
    for venta in ventas:
        id_cliente = venta[0]
        id_producto = venta[1]

        # Buscar el nombre del cliente 
        nombre_cliente = "Desconocido"
        for cliente in clientes:
            if cliente[0] == id_cliente:
                nombre_cliente = cliente[1]
                break

        # Buscar la categoría del producto 
        categoria_producto = "Desconocida"
        for producto in productos:
            if producto[0] == id_producto:
                categoria_producto = producto[1]
                break

        venta.append(nombre_cliente)  # Agregar el nombre del cliente a la entrada de venta
        venta.append(categoria_producto)  # Agregar la categoría a la entrada de venta

    # Filtrar ventas por categoría seleccionada y encontrar la cantidad más alta en la categoría 
    max_cantidad = -float('inf')
    cliente_maximo = None
    for venta in ventas:
        if venta[4] == categoria_seleccionada:  # Verificar si la categoría coincide con la seleccionada
            if venta[2] > max_cantidad:
                max_cantidad = venta[2]
                cliente_maximo = venta[3]

    # Mostrar el resultado
    if cliente_maximo:
        print(f"{cliente_maximo} tiene la mayor cantidad de compras con un total de  {max_cantidad} compras en la categoría {categoria_seleccionada}.")
    else:
        print(f"No se encontraron ventas en la categoría {categoria_seleccionada}")

    # Imprimir la lista final de ventas (no)
    print("\nEstado final de la lista de ventas:")
    for venta in ventas:
        print(venta)
        