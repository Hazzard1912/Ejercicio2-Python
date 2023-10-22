import sys
from database import connect_db
from mysql.connector import Error


def procesar_archivo(archivo):
    try:
        with open(archivo, "r") as archivo:
            
                contenido = archivo.readlines()

                nombrearchivo = archivo.name
                
                cantlineas = len(contenido)
                
                cantpalabras = sum(len(linea.split()) for linea in  contenido)
                
                cantcaracteres = sum(len(linea) for linea in    contenido)

                return nombrearchivo, cantlineas, cantpalabras, cantcaracteres
            
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encontró.")
         
            
def grabar_en_db(nombrearchivo, cantlineas, cantpalabras, cantcaracteres):
    try:   
        connection = connect_db()
        cursor = connection.cursor()

        insert_query = "INSERT INTO informacion (nombrearchivo, cantlineas, cantpalabras, cantcaracteres) VALUES (%s, %s, %s, %s)"

        datos = (nombrearchivo, cantlineas, cantpalabras,   cantcaracteres)

        cursor.execute(insert_query, datos)
        
        select_query = "SELECT * FROM informacion;"
        cursor.execute(select_query)
        
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
            
        # TODO: Mostrar los registros en una grid paginados por pantalla y opción de descargar a pdf (TCPDF o FPDF)

        connection.commit()
        print("Se han insertado los datos en la base de dato")
        
    except Error as e: 
        print(f"Error en la base de datos: {e}")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")


def main(archivo) -> None :
    
        nombrearchivo, cantlineas, cantpalabras, cantcaracteres = procesar_archivo(archivo)
        
        grabar_en_db(nombrearchivo=nombrearchivo, cantlineas=cantlineas, cantpalabras=cantpalabras, cantcaracteres=cantcaracteres)
            
        
# Validación ejecución desde terminal
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Debe pasar el numero correcto de argumentos")
    else:
        archivo = sys.argv[1]
        main(archivo)
        
# No comprendo como resolver lo de usar TCPDF o FPDF para
# trabajar lo del pdf desde python...