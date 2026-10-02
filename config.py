import mysql.connector

def obtener_conexion():
    """Función para establecer la conexión con MySQL."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="clinica_ponisana"
    )
