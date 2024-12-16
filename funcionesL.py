#1
def MostrarResumenInicial(format):
    import csv
    clientes = []
    productos = []
    ventas = []

    # Se leen los csv de clientes, productos y ventas, luego estos datos se guardan en 3 listas ya definidas anteriormente 
    with open('./archivosTiendaCsv/clientes.csv', 'r') as archivoCliente:
        lector_csv = csv.reader(archivoCliente)
        next(lector_csv)

        for cliente in lector_csv:
            clientes.append(cliente)

    with open('./archivosTiendaCsv/productos.csv', 'r') as archivoProducto:
        lector_csv = csv.reader(archivoProducto)
        next(lector_csv)

        for producto in lector_csv:
            productos.append(producto)

    with open('./archivosActualizadosTiendaCsv/ventasActualizadas.csv', 'r') as archivoVentas:
        lector_csv = csv.reader(archivoVentas)
        next(lector_csv)

        for venta in lector_csv:
            ventas.append(venta)

    # Contar filas en las listas para saber el total de cada uno de estos
    cantidad_clientes = len(clientes)
    cantidad_productos = len(productos)
    cantidad_ventas = len(ventas)

    # Mostrar el total de clientes, productos y ventas 
    print(format + '-' * 85)
    print(format + f'Número total de clientes: {cantidad_clientes}')
    print(format + f'Número total de productos: {cantidad_productos}')
    print(format + f'Número total de ventas: {cantidad_ventas}')

    # Llamar a la función ObtenerMatrizVentas y obtener la matriz ventas
    matriz_ventas = AuxiliarMostrarResumenInicial()

    # Encontrar el valor más alto en la columna 3 y guardar todas las filas correspondientes
    max_cantidad = -float('inf')
    filas_maximas = []
    #Se recorre la matriz ventas en la columna 3 y se va comparando para saber 
    for venta in matriz_ventas:
        if venta[2] > max_cantidad:
            max_cantidad = venta[2]
            filas_maximas = [venta]
        elif venta[2] == max_cantidad:
            filas_maximas.append(venta)

    # Imprimir los datos en los que se encontro la cantidad más alta
    for fila in filas_maximas:
        print(" ")
        print(format + "El producto con la cantidad de ventas más altas es: ", fila[5], format + "\n" + format + "Se encuentra en la categoría de: ", fila[4], format + "\n" + format + "Cuenta con ", fila[2]," ventas")

    print(format + '-' * 85)

#5
#La función AnalisisClientesProductos cuenta con un algoritmo ineficiente utilizando fuerza bruta, 
# el algoritmo mejorado que igual incluye fuerza bruta lo dejamos en el informe

def AnalisisClientesProductos(format):

    print(format + '-' * 85)

    import csv;

    #Menú para seleccionar la categoría en la que se desea conocer el cliente que mas ha comprado 

    def seleccionar_categoria():

        def mostrar_menu():

            print(format + "Seleccione una categoría:\n" + format + "1. Ropa\n" + format + "2. Electrónica\n" + format + "3. Alimentos\n")

        def leer_opcion():

            try:
                opción = int(input(format + "Elija una opción (0 para salir): "))

                return opción

            except ValueError:

                print(format + "Por favor, ingrese un número válido.")

                return -1

        categoría_seleccionada = None  # Variable para guardar el string de la categoría

        while True:

            mostrar_menu()

            opción = leer_opcion()

            if opción == 1:

                categoría_seleccionada = "Ropa"
                break

            elif opción == 2:

                categoría_seleccionada = "Electronica"
                break

            elif opción == 3:

                categoría_seleccionada = "Alimentos"
                break

            elif opción == 0:

                print(format + "Saliendo del programa...")
                categoría_seleccionada = None  # No hay selección
                break

            else:
                print(format + "Opción inválida. Por favor, ingrese una opción válida.")

        return categoría_seleccionada  # Retorna el string de la categoría seleccionada

    # Se llama a la función seleccionar_categoria para que mjuestre el menú, además se le muestra al usuario que opción que seleccionó

    categoría_seleccionada = seleccionar_categoria()  # Llamada a la función

    if categoría_seleccionada:
        print(format + f"La categoría seleccionada es: {categoría_seleccionada}")

    else:

        print(format + "No se seleccionó ninguna categoría.")
        return  # Salir si no se seleccionó ninguna categoría

    # Leer CSV de ventas

    ventas = []

    with open('./archivosActualizadosTiendaCsv/ventasActualizadas.csv', 'r') as archivo_csv:

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

    with open('./archivosTiendaCsv/clientes.csv', 'r') as archivo_clientes:

        lector_clientes = csv.reader(archivo_clientes)

        next(lector_clientes)  # Omitir cabecera

        #El id clientes, y nombre clientes se ingresaran en otra lista 

        for fila in lector_clientes:

            id_cliente = int(fila[0])  # ID del cliente está en la columna 0

            nombre_cliente = fila[1]

            clientes.append([id_cliente, nombre_cliente])

    # Leer CSV de productos y almacenar los datos en una lista

    productos = []

    with open('./archivosTiendaCsv/productos.csv', 'r') as archivo_productos:

        lector_productos = csv.reader(archivo_productos)

        next(lector_productos)  # Omitir cabecera

        for fila in lector_productos:

            id_producto = int(fila[0])  # ID del producto está en la columna 0

            categoría = fila[2]  # Categoría del producto está en la columna 1

            productos.append([id_producto, categoría])

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

        categoría_producto = "Desconocida"

        for producto in productos:

            if producto[0] == id_producto:

                categoría_producto = producto[1]

                break

        venta.append(nombre_cliente)  # Agregar el nombre del cliente a la entrada de venta

        venta.append(categoría_producto)  # Agregar la categoría a la entrada de venta

    # Filtrar ventas por categoría seleccionada y encontrar la cantidad más alta en la categoría 

    max_cantidad = -float('inf')

    cliente_maximo = None

    for venta in ventas:

        if venta[4] == categoría_seleccionada:  # Verificar si la categoría coincide con la seleccionada

            if venta[2] > max_cantidad:

                max_cantidad = venta[2]

                cliente_maximo = venta[3]

    # Mostrar el resultado

    if cliente_maximo:

        print(format + f"{cliente_maximo} tiene la mayor cantidad de compras con un total de  {max_cantidad} compras en la categoría {categoría_seleccionada}.")

    else:

        print(format + f"No se encontraron ventas en la categoría {categoría_seleccionada}")

    print(format + '-' * 85)

#Función auxiliar para la opción 1 MostrarResumenInicial, en esta se devuelve una matriz, see utiliza la lógica de la opción 6 
def AuxiliarMostrarResumenInicial():

    import csv

    # Leer CSV de ventas

    ventas = []

    with open('./archivosActualizadosTiendaCsv/ventasActualizadas.csv', 'r') as archivo_csv:

        lector_csv = csv.reader(archivo_csv)

        next(lector_csv)

        # El id clientes, id productos y cantidad se ingresarán en una lista 

        for fila in lector_csv:

            id_cliente = int(fila[2])  # El ID de cliente está en la columna 2

            cantidad = int(fila[3])    # La cantidad está en la columna 3

            id_producto = int(fila[1]) # El ID del producto está en la columna 1

            ventas.append([id_cliente, id_producto, cantidad])

    # Leer CSV de clientes y almacenar los datos en una lista

    clientes = []

    with open('./archivosTiendaCsv/clientes.csv', 'r') as archivo_clientes:

        lector_clientes = csv.reader(archivo_clientes)

        next(lector_clientes)  # Omitir cabecera

        # El id clientes y nombre clientes se ingresarán en otra lista 

        for fila in lector_clientes:

            id_cliente = int(fila[0])  # ID del cliente está en la columna 0

            nombre_cliente = fila[1]

            clientes.append([id_cliente, nombre_cliente])

    # Leer CSV de productos y almacenar los datos en una lista

    productos = []

    with open('./archivosTiendaCsv/productos.csv', 'r') as archivo_productos:

        lector_productos = csv.reader(archivo_productos)

        next(lector_productos)  # Omitir cabecera

        for fila in lector_productos:

            id_producto = int(fila[0])  # ID del producto está en la columna 0

            categoría = fila[2]  # Categoría del producto está en la columna 2

            nombre = fila[1]  # Nombre del producto está en la columna 1

            productos.append([id_producto, nombre, categoría])

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

        # Buscar la categoría del producto y el nombre del producto 

        nombre = "Desconocido"

        categoría_producto = "Desconocida"

        for producto in productos:

            if producto[0] == id_producto:

                nombre = producto[1]

                categoría_producto = producto[2]

                break

        venta.append(nombre_cliente)  # Agregar el nombre del cliente a la entrada de venta

        venta.append(categoría_producto)  # Agregar la categoría a la entrada de venta

        venta.append(nombre)  # Agregar el nombre del producto a la entrada de venta

    # Retornar la matriz ventas
    return ventas