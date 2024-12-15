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

# Función Que Genera Las Combinaciones De Productos Con Un Presupuesto
def PosiblesComprasPorPresupuesto (presupuesto:float):
    
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
        print(f"Combinaciones con máximo de productos ({cantidad_max_productos} productos):")
        
        for i, combinacion in enumerate(mejoresCombinaciones):
            total = sum(precio for _, precio in combinacion)
            print(f"Combinación {i + 1}: {combinacion}, Total: ${total}")
    
    else:
        print("No hay combinaciones posibles.")