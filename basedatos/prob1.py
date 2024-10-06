import sqlite3

# establecemos la conexión con la base de datos, de no existir la crea
#  ruta a archivo de la base de datos
with sqlite3.connect('base.db') as connection:
    pass # cierra la conexión a la base de datos

# creamos la sentencia SQL
# Insertamos un dato en la tabla de ventas
# Insertamos muchos datos en la tabla de ventas

# al insertar muchos valores, requerimos una lista de tuplas
with sqlite3.connect('base.db') as conexion:
    cursor = conexion.cursor()

    # Recuperamos los registros de la tabla de usuarios
    cursor.execute("SELECT * FROM ventas")

    # Mostrar el cursos a ver que hay ?
    print(cursor)

    # Recorremos el primer registro con el método fetchone, devuelve una tupla
    ventas = cursor.fetchall()
    pass

for venta in ventas:
    print(venta)

