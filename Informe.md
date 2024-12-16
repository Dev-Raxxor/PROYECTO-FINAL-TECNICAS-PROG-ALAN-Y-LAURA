INFORME PROYECTO FINAL. 

--------Organización y explicación del Sistema--------
El proyecto está dividido en módulos y funciones independientes para facilitar su mantenimiento y comprensión:

1. Carga y análisis de datos:

MostrarResumenInicial() analiza los archivos CSV y muestra un resumen inicial.
AuxiliarMostrarResumenInicial() crea una matriz para vincular productos, clientes y ventas.

2. Estimación de ventas futuras: 

EstimarVentasMesProximo() utiliza un algoritmo de Divide y Vencerás para predecir las ventas del próximo mes.

3. Simulación de compra:

SimularCompra() permite al cliente simular compras y actualiza los registros de ventas y clientes.

4. Revisión de productos por presupuesto:

PosiblesComprasPorPresupuesto() utiliza Backtracking para encontrar combinaciones óptimas de productos dentro de un presupuesto.

5. Análisis de clientes y productos:

AnalisisClientesProductos() aplica Fuerza Bruta para encontrar clientes con mayores compras en categorías específicas.

--------Estrategias Algorítmicas Utilizadas--------
En el proyecto se incorporaron las técnicas de programación vistas en clase que fueron requeridas para cada función del programa. 

1. Divide y Vencerás (Estimación de Ventas Futuras)
La función EstimarVentasMesProximo() divide las ventas históricas en segmentos temporales (meses) para analizar tendencias y proyectar ventas futuras.

Durante el proceso se realizo lo siguiente:
Filtrar las ventas de un producto específico.
Dividir los datos por mes para obtener la cantidad promedio.
Combinar los resultados para estimar las ventas del próximo mes.

2. Backtracking (Revisión de Productos por Presupuesto)
La función PosiblesComprasPorPresupuesto() encuentra combinaciones de productos que maximizan la cantidad de unidades sin exceder un presupuesto.

Durante el proceso se realizo lo siguiente:
Generar todas las combinaciones posibles de productos usando recursión.
Evalúar cada combinación y retroceder (backtrack) si el presupuesto es excedido.
Seleccionar las combinaciones que maximizan el número de productos comprados.

3. Fuerza Bruta (Análisis de Clientes y Productos)
La función AnalisisClientesProductos() identifica a los clientes con más compras en una categoría seleccionada.

Durante el proceso se realizo lo siguiente:
Itera por todas las ventas, clientes y productos.
Busca coincidencias entre categorías y clientes.
Encuentra al cliente con la mayor cantidad de compras.

Nueva alternativa:
Se implementó una nueva alternativa sobre el actual algoritmo de fuerza bruta. 
Esta nueva alternativa contiene en algunas secciones del código implementaciones con fuerza bruta, pero en comparación del actual representa mucha más eficiencia.

def AnalisisClientesProductos():
    def seleccionar_categoria():
        def mostrar_menu():
            print("Seleccione una categoría:")
            print("1. Ropa")
            print("2. Electrónica")
            print("3. Alimentos")
            print("0. Salir")

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

    # Se llama a la funcion seleccionar_categoria para que muestre el menú, además se le muestra al usuario que opción que seleccionó
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
        # El id clientes, id productos y cantidad se ingresarán en una lista 
        for fila in lector_csv:
            id_cliente = int(fila[2])  # El ID de cliente está en la columna 2
            cantidad = int(fila[3])    # La cantidad está en la columna 3
            id_producto = int(fila[1]) # El ID del producto está en la columna 1
            ventas.append([id_cliente, id_producto, cantidad])

    # Leer CSV de clientes y almacenar los datos en un diccionario
    clientes = {}
    with open('clientes.csv', 'r') as archivo_clientes:
        lector_clientes = csv.reader(archivo_clientes)
        next(lector_clientes)  # Omitir cabecera
        # El id clientes y nombre clientes se ingresarán en un diccionario
        for fila in lector_clientes:
            id_cliente = int(fila[0])  # ID del cliente está en la columna 0
            nombre_cliente = fila[1]
            clientes[id_cliente] = nombre_cliente

    # Leer CSV de productos y almacenar los datos en un diccionario
    productos = {}
    with open('productos.csv', 'r') as archivo_productos:
        lector_productos = csv.reader(archivo_productos)
        next(lector_productos)  # Omitir cabecera
        for fila in lector_productos:
            id_producto = int(fila[0])  # ID del producto está en la columna 0
            categoria = fila[2]  # Categoría del producto está en la columna 2
            productos[id_producto] = categoria

    # Agregar la categoría y el nombre del cliente a cada entrada en la lista de ventas usando diccionarios
    for venta in ventas:
        id_cliente = venta[0]
        id_producto = venta[1]

        # Buscar el nombre del cliente usando diccionarios
        nombre_cliente = clientes.get(id_cliente, "Desconocido")

        # Buscar la categoría del producto usando diccionarios
        categoria_producto = productos.get(id_producto, "Desconocida")

        venta.append(nombre_cliente)  # Agregar el nombre del cliente a la entrada de venta
        venta.append(categoria_producto)  # Agregar la categoría a la entrada de venta

    # Filtrar ventas por categoría seleccionada y encontrar la cantidad más alta en la categoría
    max_cantidad = -float('inf')
    ventas_maximas = []  # Lista para almacenar ventas con la cantidad más alta
    for venta in ventas:
        if venta[4] == categoria_seleccionada:  # Verificar si la categoría coincide con la seleccionada
            if venta[2] > max_cantidad:
                max_cantidad = venta[2]
                ventas_maximas = [venta]  # Reiniciar la lista con la nueva cantidad más alta
            elif venta[2] == max_cantidad:
                ventas_maximas.append(venta)  # Agregar a la lista si la cantidad es igual al máximo

    # Mostrar el resultado
    if ventas_maximas:
        print(f"Clientes que más han comprado en esta categoría:")
        for venta in ventas_maximas:
            print(venta[3])  # Imprimir solo el nombre del cliente
    else:
        print(f"No se encontraron ventas en la categoría {categoria_seleccionada}")

Gracias al uso eficiente de diccionarios y una búsqueda lineal, el algoritmo mejorado optimiza significativamente el tiempo de ejecución al evitar búsquedas innecesarias. Esto lo hace adecuado para manejar grandes volúmenes de datos de manera rápida y eficiente.

--------Desafíos Enfrentados--------
Durante la realización del proyecto pudimos enfrentarnos a diversos desafios que dificultaron en cierta medida la estructuración e implementación de la solución con la cual pensábamos cumplir cada uno de los requerimientos solicitados. 
Entre los desafios que enfrentamos están:

1. Optimización de fuerza bruta:
La función inicial para analizar clientes tenía un rendimiento ineficiente debido a la búsqueda lineal. Fue un poco complicado pensar en otra solución que fuera mucho más eficiente.

2. Abstracción.
El mayor desafio fue codificar la solución que teniamos en mente.

3. Modularización del código:
Dividir el código en funciones independientes permitió una mayor claridad y fácil depuración.

--------Macroalgoritmo con Precondiciones y Postcondiciones--------
1. Mostrar Resumen Inicial

Precondiciones:
Los archivos productos.csv, ventas.csv y clientes.csv existen y tienen el formato correcto.

Postcondición:
Se muestra un resumen en pantalla con la información solicitada.

2. Estimación de Ventas Futuras

Precondiciones:
Datos de ventas disponibles en el archivo CSV.

Postcondición:
La estimación de ventas se muestra al usuario.

3. Simulación de Compra

Precondiciones:
El cliente debe ingresar su ID.
Los productos seleccionados deben existir en el catálogo.

Postcondición:
Los archivos se actualizan con la nueva compra y se muestra el total.

4. Revisión de Productos por Presupuesto

Precondiciones:
El presupuesto ingresado es mayor que cero.

Postcondición:
Se muestran las combinaciones de productos que cumplen con el presupuesto.
