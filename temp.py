'''
2. Tienes un fichero <code>temperaturas.txt</code> que contiene registros de temperaturas diarias en formato CSV. 
Cada línea del fichero tiene la siguiente estructura: <code>fecha,temperatura</code>. Debes leer el fichero, calcular la temperatura promedio, 
la temperatura máxima y la mínima. Finalmente, debes escribir los resultados en un nuevo fichero <code>resumen_temperaturas.txt</code>.
'''

path='/workspaces/python_modulo5./temperaturas.txt'


with open(path,mode='r') as file:
    lineas= file.readlines()

temperaturas = []

for linea in lineas:
    _, temperatura =linea.strip().split(',')

    temperatura = float(temperatura)
    temperaturas.append(temperatura)
print(temperaturas)

temperatura_max=max(temperaturas)
temperatura_min=min(temperaturas)
temperatura_prom=sum(temperaturas)/len(temperaturas)

print(f'Temperatura maxima: {temperatura_max}')
print(f'Temperatura minima: {temperatura_min}')
print(f'Temperatura promedio: {temperatura_prom}')


with open('/workspaces/python_modulo5./resumen_temperaturas.txt',mode='w') as file:
    file.write(f'Temperatura maxima: {temperatura_max}\n')
    file.write(f'Temperatura minima: {temperatura_min}\n')
    file.write(f'Temperatura promedio: {temperatura_prom:.2f}\n')
    print('Se copiaron los datos exitosamente')