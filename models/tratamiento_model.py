from config import ejecutar_sql

def obtener_todos():
    return ejecutar_sql("SELECT * FROM tratamientos", fetch=True)

def obtener_por_id(id_t):
    return ejecutar_sql("SELECT * FROM tratamientos WHERE id_tratamiento = %s", (id_t,), fetch_one=True)

def guardar(datos):
    sql = "INSERT INTO tratamientos (descripcion, costo, id_consulta) VALUES (%s, %s, %s)"
    ejecutar_sql(sql, (datos['descripcion'], datos['costo'], datos['id_consulta']))

def actualizar(id_t, datos):
    sql = "UPDATE tratamientos SET descripcion=%s, costo=%s, id_consulta=%s WHERE id_tratamiento=%s"
    ejecutar_sql(sql, (datos['descripcion'], datos['costo'], datos['id_consulta'], id_t))

def eliminar(id_t):
    ejecutar_sql("DELETE FROM tratamientos WHERE id_tratamiento = %s", (id_t,))