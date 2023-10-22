import mysql.connector
from mysql.connector import Error

# Establecemos la conexión
def connect_db():

  try:
    connection = mysql.connector.connect(host='localhost',  database='datosdb', user='root', password='R5GYjo%8XYih5u')

    if connection.is_connected():
      db_info = connection.get_server_info()
      print("Conectado a MySQL Server version ", db_info)
      cursor = connection.cursor()
      cursor.execute("select database();")
      recort = cursor.fetchone()
      return connection

  except Error as e:
    print(f"Error al conectarse a MySQL {e}")