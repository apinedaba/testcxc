# app.py
from flask import Flask, jsonify, request
from models import db, Agency, Profession, Ethnicity, Gender, Employee
from etl import cargar_catalogos, cargar_empleados

app = Flask(__name__)

# Configuración de la base de datos (PostgreSQL o MySQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:password@db:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db.init_app(app)

# Ruta para inicializar la base de datos
@app.route('/init_db')
def init_db():
    db.create_all()
    return "Base de datos creada con éxito"

@app.route('/load_employees', methods=['POST'])
def load_employees():
    types = ("csv", "xslx")    
    if 'file' not in request.files.keys():
        return  jsonify({
            "response":"No hay archivo",
            "data":request.files['file'].filename,
            "status_code":400
        }), 400
    employee_file = request.files['file']
    if employee_file.filename.endswith(types) is not True:
        return  jsonify({
            "response":"El archivo no es de un formato permitido",
            "status_code":400
        }), 400
    return cargar_empleados(employee_file)

@app.route('/load_catalogs', methods=['POST'])
def load_catalogs():
    types = ("csv", "xslx")    
    if 'file' not in request.files.keys():
        return  jsonify({
            "response":"No hay archivo",
            "status_code":400
        }), 400
    catalog_file = request.files['file']
    if catalog_file.filename.endswith(types) is not True:
        return  jsonify({
            "response":"El archivo no es de un formato permitido",
            "status_code":400
        }), 400
    return cargar_catalogos(catalog_file)


if __name__ == '__main__':
    app.run(debug=True)
