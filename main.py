#Importaciones necesarias
import os; import funcionesA; import funcionesL

# Limpiar la consola antes de mostrar cualquier cosa
os.system('cls' if os.name == 'nt' else 'clear') 

def main():

    opcion:int = 0
    format = '\n' + ' ' * 23
    mensajeAdios = (
        format + '-' * 41 +
        format + '| Gracias por utilizar nuestro sistema  |' +
        format + '-' * 41
    )

    while True:

        # Limpiar la consola antes de mostrar cualquier cosa
        os.system('cls' if os.name == 'nt' else 'clear') 

        print(' ')
        funcionesA.MostrarMenu(1)
        
        opcion = funcionesA.ValidarMenu(1, 7, format)
    
        match opcion:

            case 1:

                funcionesL.MostrarResumenInicial(format)

            case 2:
                
                funcionesA.EstimarVentasMesProximo(format)

            case 3:
               
                funcionesA.SimularCompra(format)
            
            case 4:

                funcionesA.PosiblesComprasPorPresupuesto(format)
            
            case 5:

                funcionesL.AnalisisClientesProductos(format)

            case 6:
                print(format + 'Esta opción aún no está disponible.')

            case 7:
                
                print(mensajeAdios)
                break

        print(format + 'Ingrese (1) para volver al menú principal o (0) para salir del programa')
        
        opcion = funcionesA.ValidarMenu(0, 1, format)

        if opcion == 0:
            print(mensajeAdios)
            break

    print('\n')

main()