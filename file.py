#instrucciones

from dotenv import load_dotenv
import os
import pyodbc
import pandas as pd
# Cargar variables de entorno
load_dotenv()

# Cargar las credenciales de la base de datos desde el archivo .env
DB_SERVER = os.getenv("DB_SERVER")
DB_NAME = os.getenv("DB_NAME")

if not all([DB_SERVER, DB_NAME]):
    print("Error: Faltan variables de entorno")
else:
    connection_string = (
        f'DRIVER={{SQL Server}};'
        f'SERVER={DB_SERVER};'  # nombre de servidor
        f'DATABASE={DB_NAME};'  # nombre de base de datos
        f'Trusted_Connection=yes;'
)

# CREAR LA CONEXION
try:
    conn = pyodbc.connect(connection_string)  # abrir la conexion
    print("Conexión exitosa")

# Aquí realizar las operaciones sobre la base de datos
# ----------------------------------------------------------------------
# Leer la consulta desde el archivo .sql
    with open("select_tb_Rotaciones.sql", "r", encoding="utf-8") as file:
        query = file.read()  # Lee el contenido del archivo
# Ejecutar la consulta y guardarla en un DataFrame
    df_Rot = pd.read_sql(query, conn)
    print(df_Rot.head())

    with open("select_tb_Sastifaccion.sql", "r", encoding="utf-8") as file:
        query = file.read()  
    df_Sast = pd.read_sql(query, conn)
    print(df_Sast.head())

#----------------------------------------------------------------------
    conn.close()  # cerrar la conexion

except pyodbc.Error as ex:
    sqlstate = ex.args[0]
    error_message = ex.args[1]
    print(f"Error de conexión: {sqlstate}")
    print(f"Mensaje detallado: {error_message}")

