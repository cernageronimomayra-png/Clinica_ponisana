from config import ejecutar_sql

def obtener_todos():
    return ejecutar_sql("SELECT * FROM medicos", fetch=True)

def obtener_por_id(id_m):
    return ejecutar_sql("SELECT * FROM medicos WHERE id_medico = %s", (id_m,), fetch_one=True)

def guardar(datos):
    sql = "INSERT INTO medicos (nombre, especialidad, horario) VALUES (%s, %s, %s)"
    valores = (datos['nombre'], datos['especialidad'], datos['horario'])
    ejecutar_sql(sql, valores)

def actualizar(id_m, datos):
    sql = "UPDATE medicos SET nombre=%s, especialidad=%s, horario=%s WHERE id_medico=%s"
    valores = (datos['nombre'], datos['especialidad'], datos['horario'], id_m)
    ejecutar_sql(sql, valores)

def eliminar(id_m):
    ejecutar_sql("DELETE FROM medicos WHERE id_medico = %s", (id_m,))