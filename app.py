from flask import Flask, jsonify, render_template
import pymysql

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    'host': 'beztemoivhfz3gme6cg2-mysql.services.clever-cloud.com',
    'user': 'ueimrvxlppm556x2',
    'password': 'g4RxFIaDLiTjAdDY1DZZ',
    'database': 'beztemoivhfz3gme6cg2',
    'port': 3306
}

# Función para obtener el último registro
def get_last_report():
    connection = pymysql.connect(**db_config)
    with connection.cursor() as cursor:
        cursor.execute("SELECT zona, hora, observaciones FROM reporte ORDER BY numero DESC LIMIT 1")
        result = cursor.fetchone()
    connection.close()
    return result if result else (None, None, None)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-new-number')
def check_new_number():
    last_report = get_last_report()
    zone, time, observations = last_report
    return jsonify({
        'newNumber': zone,  # Aquí puedes ajustar si necesitas un número específico
        'message': f'Nuevo registro en {zone} a las {time}: {observations}'
    })

if __name__=='__main__':
    app.run(debug=True)