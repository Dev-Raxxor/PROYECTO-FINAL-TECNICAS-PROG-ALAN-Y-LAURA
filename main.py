#Importaciones necesarias
import os; import funciones; #import matplotlib.pyplot as plt

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
        funciones.MostrarMenu(1)
        
        opcion = funciones.ValidarMenu(1, 7, format)
    
        match opcion:

            case 1:
                print(format + 'Esta opción aún no está disponible.')

            case 2:
                print(format + 'Esta opción aún no está disponible.')

            case 3:

                funciones.SimularCompra(format)
            
            case 4:

                print(format + 'Esta opción aún no está disponible.')
            
            case 5:

                while True:
                    try:
                        presupuesto = float(input(format + 'Ingrese su presupuesto: '))
    
                        # Verifica si la opción no está en el rango permitido
                        if not (presupuesto >= 0.1):
                
                            print(format + f'Error: Opción fuera de rango. Ingrese un número mayor que 0.1')
            
                        else: break # Si la opción es válida, sale del bucle
        
                    except ValueError:
            
                        # Muestra el mensaje de error
                        print(format + 'Error: Ingrese un valor numérico.')

                funciones.PosiblesComprasPorPresupuesto(presupuesto, format)

            case 6:
                print(format + 'Esta opción aún no está disponible.')

            case 7:
                
                print(mensajeAdios)
                break

        print(format + 'Ingrese (1) para volver al menú principal o (0) para salir del programa')
        
        opcion = funciones.ValidarMenu(0, 1, format)
        if opcion == 0:
            print(mensajeAdios)
            break

    print('\n')

main()