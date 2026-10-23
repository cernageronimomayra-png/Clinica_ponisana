from config import ejecutar_sql

def obtener_todos():
    return ejecutar_sql("SELECT * FROM tratamientos", fetch=True)

def obtener_por_id(id_t):
    return ejecutar_sql("SELECT * FROM tratamientos WHERE id_tratamiento = %s", (id_t,), fetch_one=True)

def guardar(datos):
    # Insertamos los 3 campos definidos en la base de datos
    sql = "INSERT INTO tratamientos (nombre, dosis, duracion) VALUES (%s, %s, %s)"
    valores = (
        datos.get('nombre', ''),
        datos.get('dosis', ''),
        datos.get('duracion', '')
    )
    ejecutar_sql(sql, valores)

def actualizar(id_t, datos):
    # Actualizamos los campos usando la clave primaria id_tratamiento
    sql = "UPDATE tratamientos SET nombre=%s, dosis=%s, duracion=%s WHERE id_tratamiento=%s"
    valores = (
        datos.get('nombre', ''),
        datos.get('dosis', ''),
        datos.get('duracion', ''),
        id_t
    )
    ejecutar_sql(sql, valores)

def eliminar(id_t):
    ejecutar_sql("DELETE FROM tratamientos WHERE id_tratamiento = %s", (id_t,))