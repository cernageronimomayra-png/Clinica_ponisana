from flask import Blueprint, render_template, request, redirect, url_for
import models.paciente_model as model

# Definimos el Blueprint para Pacientes
paciente_bp = Blueprint('paciente', __name__, url_prefix='/pacientes')

# 1. Ruta para listar todos los pacientes
@paciente_bp.route('/')
def index():
    pacientes = model.obtener_todos()
    return render_template('pacientes/index.html', pacientes=pacientes)

# 2. Ruta para mostrar el formulario de CREAR paciene
@paciente_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        # Guardamos en BD y redirigimos a la lista
        model.guardar(request.form)
        return redirect(url_for('paciente.index'))
    
    # Muestra el formulario vacío para registrar
    return render_template('pacientes/crear.html')

# 3. Ruta para EDITAR paciente existente
@paciente_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    paciente = model.obtener_por_id(id)
    if request.method == 'POST':
        # Actualizamos en BD y redirigimos
        model.actualizar(id, request.form)
        return redirect(url_for('paciente.index'))
    
    # Carga la vista de edición enviando los datos actuales del paciente
    return render_template('pacientes/editar.html', paciente=paciente)

# 4. Ruta para ELIMINAR paciente
@paciente_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    model.eliminar(id)
    return redirect(url_for('paciente.index'))