from flask import Flask, jsonify
import mysql.connector, json

# Inicializa la aplicación Flask
app = Flask(__name__)

def get_db_connection():

    connection = mysql.connector.connect(
        host="localhost",  # Cambia a la dirección de tu servidor MySQL si es necesario
        user="grupo3",  # Sustituye con tu nombre de usuario de MySQL
        password="taller2",  # Sustituye con tu contraseña de MySQL
        database="CompanyDB"  # Cambia al nombre de tu base de datos
    )
    return connection


@app.route('/employees', methods=['GET'])
def get_employees():

    # Establece una conexión a la base de datos
    connection = get_db_connection()

    # Crea un cursor para interactuar con la base de datos
    cursor = connection.cursor()

    # Llama al procedimiento almacenado 'GetEmployees'
    cursor.callproc('GetEmployees')

    # Itera sobre los resultados devueltos por el procedimiento almacenado
    for result in cursor.stored_results():
        # Asume que el procedimiento devuelve los resultados en formato JSON
        employees_json = result.fetchall()[0][0]

    # Cierra el cursor y la conexión a la base de datos
    cursor.close()
    connection.close()
  
    # Convierte en formato json
    employees_json = json.loads(employees_json)
    
    # Devuelve los resultados en formato JSON
    return jsonify({"employess_json": employees_json})


if __name__ == '__main__':
    # Ejecuta el servidor Flask en modo depuración
    app.run(debug=True)
