from config import ejecutar_sql

def obtener_todos():
    return ejecutar_sql("SELECT * FROM pacientes", fetch=True)

def obtener_por_id(id_p):
    return ejecutar_sql("SELECT * FROM pacientes WHERE id_paciente = %s", (id_p,), fetch_one=True)

def guardar(datos):
    sql = "INSERT INTO pacientes (nombre, rut, telefono, direccion, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s)"
    ejecutar_sql(sql, (datos['nombre'], datos['rut'], datos['telefono'], datos['direccion'], datos['fecha_nacimiento']))

def actualizar(id_p, datos):
    sql = "UPDATE pacientes SET nombre=%s, rut=%s, telefono=%s, direccion=%s, fecha_nacimiento=%s WHERE id_paciente=%s"
    ejecutar_sql(sql, (datos['nombre'], datos['rut'], datos['telefono'], datos['direccion'], datos['fecha_nacimiento'], id_p))

def eliminar(id_p):
    ejecutar_sql("DELETE FROM pacientes WHERE id_paciente = %s", (id_p,))