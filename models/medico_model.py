from config import ejecutar_sql

def obtener_todos():
    return ejecutar_sql("SELECT * FROM medicos", fetch=True)

def obtener_por_id(id_m):
    return ejecutar_sql("SELECT * FROM medicos WHERE id_medico = %s", (id_m,), fetch_one=True)

def guardar(datos):
    sql = "INSERT INTO medicos (nombre, especialidad, telefono, email) VALUES (%s, %s, %s, %s)"
    ejecutar_sql(sql, (datos['nombre'], datos['especialidad'], datos['telefono'], datos['email']))

def actualizar(id_m, datos):
    sql = "UPDATE medicos SET nombre=%s, especialidad=%s, telefono=%s, email=%s WHERE id_medico=%s"
    ejecutar_sql(sql, (datos['nombre'], datos['especialidad'], datos['telefono'], datos['email'], id_m))

def eliminar(id_m):
    ejecutar_sql("DELETE FROM medicos WHERE id_medico = %s", (id_m,))