from config import obtener_conexion

def obtener_todos_pacientes():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pacientes")
    pacientes = cursor.fetchall()
    cursor.close()
    conexion.close()
    return pacientes

def insertar_paciente(nombre, rut, telefono, direccion, fecha_nacimiento):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO pacientes (nombre, rut, telefono, direccion, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (nombre, rut, telefono, direccion, fecha_nacimiento))
    conexion.commit()
    cursor.close()
    conexion.close()

def obtener_paciente_por_id(id_paciente):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pacientes WHERE id_paciente = %s", (id_paciente,))
    paciente = cursor.fetchone()
    cursor.close()
    conexion.close()
    return paciente

def actualizar_paciente(id_paciente, nombre, rut, telefono, direccion, fecha_nacimiento):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "UPDATE pacientes SET nombre=%s, rut=%s, telefono=%s, direccion=%s, fecha_nacimiento=%s WHERE id_paciente=%s"
    cursor.execute(sql, (nombre, rut, telefono, direccion, fecha_nacimiento, id_paciente))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_paciente(id_paciente):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM pacientes WHERE id_paciente = %s", (id_paciente,))
    conexion.commit()
    cursor.close()
    conexion.close()
