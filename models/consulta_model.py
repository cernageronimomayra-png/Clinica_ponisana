from config import ejecutar_sql

def obtener_todos():
    # Definimos la consulta SQL utilizando INNER JOIN para enlazar los registros
    # y 'AS' para crear los alias nombre_paciente y nombre_medico
    sql = """
        SELECT 
            c.id_consulta,
            c.fecha,
            c.hora,
            c.motivo,
            p.nombre AS nombre_paciente,
            m.nombre AS nombre_medico
        FROM consultas c
        INNER JOIN pacientes p ON c.id_paciente = p.id_paciente
        INNER JOIN medicos m ON c.id_medico = m.id_medico
    """
    # Retornamos el resultado procesado mediante tu función genérica ejecutar_sql
    return ejecutar_sql(sql, fetch=True)

def obtener_por_id(id_c):
    return ejecutar_sql("SELECT * FROM consultas WHERE id_consulta = %s", (id_c,), fetch_one=True)

def guardar(datos):
    sql = "INSERT INTO consultas (fecha, hora, motivo, id_paciente, id_medico) VALUES (%s, %s, %s, %s, %s)"
    ejecutar_sql(sql, (datos['fecha'], datos['hora'], datos['motivo'], datos['id_paciente'], datos['id_medico']))

def actualizar(id_c, datos):
    sql = "UPDATE consultas SET fecha=%s, hora=%s, motivo=%s, id_paciente=%s, id_medico=%s WHERE id_consulta=%s"
    ejecutar_sql(sql, (datos['fecha'], datos['hora'], datos['motivo'], datos['id_paciente'], datos['id_medico'], id_c))

def eliminar(id_c):
    ejecutar_sql("DELETE FROM consultas WHERE id_consulta = %s", (id_c,))