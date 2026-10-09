import mysql.connector

def ejecutar_sql(query, params=(), fetch=False, fetch_one=False):
    conexion = mysql.connector.connect(
        host="localhost", user="root", password="", database="clinica_ponisana"
    )
    cursor = conexion.cursor(dictionary=True)
    cursor.execute(query, params)
    
    resultado = None
    if fetch_one:
        resultado = cursor.fetchone()
    elif fetch:
        resultado = cursor.fetchall()
    else:
        conexion.commit()
        
    cursor.close()
    conexion.close()
    return resultado