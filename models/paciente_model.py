from config import ejecutar_sql

def obtener_todos():
    return ejecutar_sql("SELECT * FROM pacientes", fetch=True)

def obtener_por_id(id_p):
    return ejecutar_sql("SELECT * FROM pacientes WHERE id_paciente = %s", (id_p,), fetch_one=True)

def guardar(datos):
    sql = "INSERT INTO pacientes (nombre, rut, telefono, direccion, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s)"
    ejecutar_sql(sql, (datos['nombre'], datos['rut'], datos['telefono'], datos['direccion'], datos['fecha_nacimiento']))

# models/paciente_model.py

def actualizar(id_paciente, datos):
    # Hay 5 marcadores %s en la consulta SQL
    sql = """
        UPDATE pacientes 
        SET nombre=%s, rut=%s, telefono=%s, direccion=%s, fecha_nacimiento=%s 
        WHERE id_paciente=%s
    """
    
    # Creamos una tupla con exactamente 6 valores ordenada en el mismo orden que la SQL:
    # 1. nombre, 2. rut, 3. telefono, 4. direccion, 5. fecha_nacimiento, 6. id_paciente
    valores = (
        datos['nombre'],
        datos['rut'],
        datos['telefono'],
        datos['direccion'],
        datos['fecha_nacimiento'],
        id_paciente # ¡No olvides el ID para la cláusula WHERE!
    )
    
    # Enviamos la consulta con la tupla exacta de parámetros
    ejecutar_sql(sql, valores)
def eliminar(id_p):
    ejecutar_sql("DELETE FROM pacientes WHERE id_paciente = %s", (id_p,))