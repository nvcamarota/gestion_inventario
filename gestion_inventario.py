"""
GESTIÓN DE INVENTARIO (CSV)
Contexto: Diseña un programa que permita gestionar un inventario de productos en una tienda.
El sistema debe:
    • Registrar productos en un archivo inventario.csv (nombre, cantidad, precio).
    • Leer el archivo y mostrar el inventario.
    • Calcular el valor total del inventario (cantidad x precio).

Instrucciones:
    • Usa el módulo csv para escribir y leer el archivo.
    • Implementa un menú para las opciones; agregar producto, mostrar inventario y salir.
"""

import csv

archivo_inventario = 'archivo_inventario.csv'

with open(archivo_inventario, 'w', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['Nombre', 'Cantidad', 'Precio'])
    
while True:
    print('\nGestión de inventario: ')
    print('1. Agregar producto.')
    print('2. Mostrar inventario.')
    print('3. Salir.')
    
    opcion = int(input('\n¿Qué acción desea realizar? [1-3]: '))
    
    if opcion == 1:
        nombre = input('Nombre del producto: ').capitalize()
        cantidad = int(input(f'Cantidad del producto "{nombre}": '))
        precio = float(input(f'Precio del producto "{nombre}": $'))
        
        with open(archivo_inventario, 'a', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([nombre, cantidad, precio])
        print('¡Producto guardado exitosamente!')
    
    elif opcion == 2:
        print('\nMostrar inventario:')
        valor_total = 0
        with open(archivo_inventario, 'r') as archivo:
            lector = csv.reader(archivo)
            for i, fila in enumerate(lector):
                if i == 0:
                    print(f'{fila[0]:<15} {fila[1]:<10} {fila[2]:<10}')
                else:
                    print(f'{fila[0]:<15} {fila[1]:<10} {fila[2]:<10}')
                    valor_total += int(fila[1]) * float(fila[2])
        
        print(f'\nValor del inventario: {valor_total:.2f}')
        
    elif opcion == 3:
        print('Saliendo del sistema.')
        break
    
    else:
        print('Opción inválida. Sigue participando.')