from flask import Blueprint, render_template, request, redirect, url_for
import models.medico_model as model

# Definimos el Blueprint para Médicos
medicos_bp = Blueprint('medicos', __name__, url_prefix='/medicos')

# 1. Ruta principal para listar médicos
@medicos_bp.route('/')
def index():
    medicos = model.obtener_todos()
    return render_template('medicos/index.html', medicos=medicos)

# 2. Ruta para CREAR médico
@medicos_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        model.guardar(request.form)
        return redirect(url_for('medicos.index'))
    return render_template('medicos/crear.html')

# 3. Ruta para EDITAR médico
@medicos_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    medico = model.obtener_por_id(id)
    if request.method == 'POST':
        model.actualizar(id, request.form)
        return redirect(url_for('medicos.index'))
    return render_template('medicos/editar.html', medico=medico)

# 4. Ruta para ELIMINAR médico
@medicos_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    model.eliminar(id)
    return redirect(url_for('medicos.index'))