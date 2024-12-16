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

    elif opcion == 2:

        menuItems = [  # Opciones Menú de Compra
                f"       Sistema de Compras - Menú de Productos       |\n{' ' * 23}|{' ' * 52}|",  
                "   101. Laptop - $1200                              |",    
                "   102. Smartphone - $700                           |",  
                "   103. Jeans - $50                                 |",
                "   104. Chaqueta - $120                             |",
                "   105. Manzanas - $2                               |"
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
    print('\n' + ' ' * 23 + '-' * 54)
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





























































# 2
def EstimarVentasMesProximo (producto, format):

    # Función Para Obtener La Cantidad De Meses Según El Producto
    def ObtenerMesesVentas(producto):
        import pandas as pd

        # Carga los datos de ventas
        df = pd.read_csv('./archivosActualizadosTiendaCsv/ventasActualizadas.csv')

        # Filtrar solo las columnas necesarias: id_producto y fecha
        dfFiltrado = df[['id_producto', 'fecha']].copy()

        # Asegurarse de que la columna 'fecha' sea de tipo datetime
        dfFiltrado['fecha'] = pd.to_datetime(dfFiltrado['fecha'])

        # Filtrar por un id_producto específico
        dfMeses = dfFiltrado[dfFiltrado['id_producto'] == producto].copy()

        # Crear una nueva columna con el formato año-mes
        dfMeses['año_mes'] = dfMeses['fecha'].dt.to_period('M')

        # Obtener los meses únicos en los que se ha vendido el producto
        meses = dfMeses['año_mes'].unique()

        # Retornar el número de meses
        return len(meses)
    
    # Función Para Obtener La Cantidad De Ventas Según El Producto
    def ObtenerCantidadVentasProducto(producto):
        import pandas as pd

        # Carga los datos de ventas
        df = pd.read_csv('./archivosActualizadosTiendaCsv/ventasActualizadas.csv')

        # Filtrar solo las columnas necesarias: id_producto y cantidad
        dfFiltrado = df[['id_producto', 'cantidad']].copy()

        # Filtrar por un id_producto específico
        dfFiltrado = dfFiltrado[dfFiltrado['id_producto'] == producto]

        # Calcular la suma de la cantidad de productos vendidos para ese id_producto
        cantidadVentas = dfFiltrado['cantidad'].sum()

        return cantidadVentas
    
    # Formula para la estimación
    estimacionVentas = ObtenerCantidadVentasProducto(producto) / ObtenerMesesVentas(producto)

    print(format + '-' * 75, end = ' ')
    print(format + f'| Estimación de ventas en el mes próximo para el producto {producto}: {estimacionVentas:.2f}       |', end = ' ')
    print(format + '-' * 75)

# 3
def SimularCompra (format):
    import pandas as pd
    from datetime import datetime

    print(format + '-' * 85, end = ' ')

   # Carga los datos
    global dfVentas  # Usamos global porque dfVentas está en el ámbito global
    dfVentas = pd.read_csv('./archivosActualizadosTiendaCsv/ventasActualizadas.csv')

    global dfClientes  # Usamos global para modificar dfClientes
    dfClientes = pd.read_csv('./archivosTiendaCsv/clientes.csv')

    global dfProductos  # Usamos global para modificar dfProductos
    dfProductos = pd.read_csv('./archivosTiendaCsv/productos.csv')

    # Función para buscar cliente
    def buscarCliente(id, format):
        cliente = dfClientes[dfClientes['id_cliente'] == id]
        
        # Si cliente está vacío no existe y crea uno
        if cliente.empty:
            print(format + "¡Vaya!, Parece que eres nuevo, te registraremos.")
            crearCliente(id, format)
        else:
            print(format + f"Cliente encontrado, bienvenido: {cliente.iloc[0]['nombre']} {cliente.iloc[0]['apellido']}")

    # Función para crear un nuevo cliente
    def crearCliente(id, format):

        global dfClientes

        # Solicitar información para el nuevo cliente
        nombre = input(format + "Ingrese el nombre: ")
        apellido = input(format + "Ingrese el apellido: ")
        edad = int(input(format + "Ingrese la edad: "))
        email = f"{nombre.lower()}.{apellido.lower()}@gmail.com"

        # Crear un nuevo DataFrame con el cliente
        nuevo_cliente = pd.DataFrame([[id, nombre, apellido, edad, email]], columns=['id_cliente', 'nombre', 'apellido', 'edad', 'email'])

        # Añadirlo al DataFrame de clientes
        dfClientes = pd.concat([dfClientes, nuevo_cliente], ignore_index = True)

        # Guardar los cambios en el CSV
        dfClientes.to_csv('./archivosTiendaCsv/clientes.csv', index = False)
        print(format + f"Cliente {nombre} {apellido} creado con éxito!")
    
    # Función para simular la compra
    def realizarCompra(id_cliente):

        global dfVentas, dfProductos

        print(format + "¡Comencemos con la simulación!")
        totalVenta = 0
        continuar = True

        while continuar:

            MostrarMenu(2)
            id_producto = int(input(format + "Ingrese el ID del producto que desea comprar: "))
            
            # Filtrar el producto según el ID ingresado por el usuario
            producto = dfProductos[dfProductos['id_producto'] == id_producto]
            
            # Si producto no está disponible
            if producto.empty:
                print(format + "Producto no encontrado, por favor ingrese un ID válido.")
                continue
            
            cantidad = int(input(format + f"Ingrese la cantidad de {producto.iloc[0]['nombre']} que desea comprar: "))
            
            #Cálculo del precio de la sub-venta
            totalProducto = producto.iloc[0]['precio'] * cantidad
            totalVenta += totalProducto

            #Definir la fecha como la fecha actual de ejecución del programa
            fecha = datetime.now().strftime('%Y-%m-%d')

            # Registrar la venta
            id_venta = len(dfVentas) + 1  # Generar un ID de venta único, consecuente al orden del archivo
            nueva_venta = pd.DataFrame([[id_venta, id_producto, id_cliente, cantidad, fecha, totalProducto]],
                                        columns=['id_venta', 'id_producto', 'id_cliente', 'cantidad', 'fecha', 'total'])
            
            # Añadirlo al DataFrame de ventas
            dfVentas = pd.concat([dfVentas, nueva_venta], ignore_index=True)

            # Guardar los cambios en el CSV de ventas
            dfVentas.to_csv('./archivosActualizadosTiendaCsv/ventasActualizadas.csv', index = False)

            print(format + f"Producto añadido. Total de la venta hasta ahora: ${totalVenta}")
            continuar = input(format + "¿Desea seguir comprando? (si/no): ").lower() == 'si'

        print(format + f"Compra finalizada. Total de la compra: ${totalVenta}")

    # Función para manejar la compra
    def iniciarCompra():

        id_cliente = int(input(format + "Ingrese su ID de cliente para iniciar la compra: "))

        buscarCliente(id_cliente, format)
        realizarCompra(id_cliente)

    # Iniciar el proceso de compra
    iniciarCompra()

    print(format + '-' * 85, end = ' ')
    
# 4
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
        print(format + '-' * 95)
        print(format + f"    Combinaciones con máximo de productos ({cantidad_max_productos}) productos:")
        
        for i, combinacion in enumerate(mejoresCombinaciones):
            total = sum(precio for _, precio in combinacion)
            print(format + f"    Combinación {i + 1}: {combinacion}, Total: ${total}")

        print(format + '-' * 95)
    
    else:
        print(format + "No hay combinaciones posibles.")

# 5
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