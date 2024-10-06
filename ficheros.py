"""
**Ejercicio**

Tienes un fichero <code>ventas.csv</code> que contiene datos de ventas en formato CSV.  
Cada línea del fichero tiene la siguiente estructura: <code>fecha,producto,cantidad,precio_unitario</code>. 
Debes leer el fichero, procesar los datos y calcular el total de ventas por producto. Finalmente, debes escribir 
los resultados en un nuevo fichero <code>total_ventas.txt</code>.

"""
import pprint
ruta='/workspaces/python_modulo5./ventas.csv'

with open(ruta) as file:
    lineas=file.readlines()


dicx_agrupado={}

for linea in lineas:
    fecha,producto,cantidad,precio_unitario=linea.strip().split(',')
    
    cantidad=int(cantidad)
    precio_unitario=float(precio_unitario)
    print(f'Producto: {producto}, Cantidad {cantidad}, Precio unit:{precio_unitario}')

    if not producto in dicx_agrupado.keys():
            dicx_agrupado[producto] = {'cantidad': cantidad, 'precio_unitario': precio_unitario}
            continue
   
    dicx_agrupado[producto]['cantidad'] += cantidad
    
pprint.pprint(dicx_agrupado)


for producto, data in dicx_agrupado.items():
     dicx_agrupado[producto]['precio_total']=data['cantidad']*data['precio_unitario']

pprint.pprint(dicx_agrupado)


ruta='/workspaces/python_modulo5./total_ventas.txt'
with open (ruta,mode='w') as file:
    file.write('Producto,Cantidad,Precio Unitario,Precio total\n')

    for producto, data in dicx_agrupado.items():
        linea=f'Producto: {producto}, TotalVentas: {data['precio_total']}\n'
        file.write(linea)

