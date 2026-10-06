from flask import Flask, redirect, url_for

# Importar los 4 Blueprints creados en controllers/
from controllers.paciente_controller import paciente_bp
from controllers.medicos_controllers import medicos_bp
from controllers.consulta_controller import consulta_bp
from controllers.tratamientos_controllers import tratamientos_bp

app = Flask(__name__)

# Registrar los controladores
app.register_blueprint(paciente_bp)
app.register_blueprint(medicos_bp)
app.register_blueprint(consulta_bp)
app.register_blueprint(tratamientos_bp)

# Ruta principal que redirige automáticamente a la lista de pacientes
@app.route('/')
def home():
    return redirect(url_for('paciente.index'))

if __name__ == '__main__':
    app.run(debug=True)
