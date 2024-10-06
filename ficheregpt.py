ruta = '/workspaces/python_modulo5./ventas.csv'

# Leer el archivo CSV
with open(ruta) as file:
    lineas = file.readlines()

# Diccionario para agrupar los productos
dicx_agrupado = {}

# Procesar cada línea del archivo CSV
for linea in lineas:
    fecha, producto, cantidad, precio_unitario = linea.strip().split(',')

    cantidad = int(cantidad)
    precio_unitario = float(precio_unitario)
    
    # Si el producto no está en el diccionario, lo agregamos
    if producto not in dicx_agrupado:
        dicx_agrupado[producto] = {'cantidad': cantidad, 'precio_unitario': precio_unitario}
    else:
        # Si ya está, actualizamos la cantidad
        dicx_agrupado[producto]['cantidad'] += cantidad

# Calcular el total de ventas y escribir el archivo de salida
ruta_salida = '/workspaces/python_modulo5./total_ventas.txt'
with open(ruta_salida, mode='w') as file:
    file.write('Producto,Cantidad,Precio Unitario,Precio Total\n')

    for producto, data in dicx_agrupado.items():
        cantidad_total = data['cantidad']
        precio_unitario = data['precio_unitario']
        precio_total = cantidad_total * precio_unitario
        linea = f'Producto: {producto}, Cantidad: {cantidad_total}, Precio Unitario: {precio_unitario:.2f}, Precio Total: {precio_total:.2f}\n'
        file.write(linea)

print(f"Archivo {ruta_salida} creado con éxito.")
