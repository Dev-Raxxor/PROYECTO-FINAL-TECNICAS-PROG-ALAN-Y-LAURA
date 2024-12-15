#Función Que Muestra El Menú Principal / Otros Menús Con Información
def MostrarMenu (opcion:int):

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

    #Función Que Ayuda Con La Estructura De La Tabla
    def EspaciosMenu (opcion:int):
        if opcion == 1: return f"{' ' * 23}|{' ' * 52}|\n{' ' * 23}|" #Para El Encabezado
        else: return f"\n{' ' * 23}|{'-' * 52}|\n{' ' * 23}|" #Para El Resto Del Cuerpo De La Tabla

def PosiblesComprasPorPresupuesto (presupuesto:int):
    import pandas as pd

    preciosProductos = {}
    # Leer el archivo CSV
    df = pd.read_csv('./archivosTiendaCsv/productos.csv')
    # Usar zip() para recorrer simultáneamente la columna de productos (df[1]) y la de precios (df.iloc[:, -1])
    for tipo, valor in zip(df['nombre'], df['precio']):
        preciosProductos[tipo] = valor

    productos = list(preciosProductos.items())  # Convertimos a una lista de tuplas [(nombre1, precio1), (nombre2, precio2), ...]

    cantidad_max_productos = 0
    mejoresCombinaciones = []
    cantidad_productos = 0
    
    for combinacion in combinaciones:
        
        total = sum(precio for _, precio in combinacion)  # Sumar los precios de la combinación
        cantidad_productos = len(combinacion)  # Cantidad de productos en esta combinación
        
        if total <= presupuesto:  # Si la combinación está dentro del presupuesto
            
            if cantidad_productos > cantidad_max_productos:  # Si se encuentra una combinación con más productos
                
                cantidad_max_productos = cantidad_productos  # Actualizar la mayor cantidad de productos
                
                mejoresCombinaciones = [combinacion]  # Reemplazar la lista con la nueva mejor combinación
            
            elif cantidad_productos == cantidad_max_productos:  # Si hay otra combinación con la misma cantidad de productos
                
                mejoresCombinaciones.append(combinacion)  # Agregar esta combinación a la lista de mejores combinaciones
            
            
    for combinacion in mejoresCombinaciones:

        total = sum(precio for _, precio in combinacion)  # Sumar los precios de la combinación
        if total <= presupuesto:
            print(f"Combinación máxima de productos que puedes comprar: {cantidad_max_productos}")
            for nombre, precio in combinacion:
                print(f"  - {nombre}: ${precio}")
            print(f"Total: ${total}\n")


   
          

PosiblesComprasPorPresupuesto(1300)

        

        
        

"""def FuncionesArchivos(opciones:int, ruta:str):


MostrarMenu(2)"""
