from flask import Blueprint, render_template, request, redirect, url_for
import models.tratamiento_model as model

# Definimos el Blueprint para Tratamientos
tratamientos_bp = Blueprint('tratamientos', __name__, url_prefix='/tratamientos')

# 1. Ruta principal para listar tratamientos
@tratamientos_bp.route('/')
def index():
    tratamientos = model.obtener_todos()
    return render_template('tratamientos/index.html', tratamientos=tratamientos)

# 2. Ruta para CREAR tratamiento
@tratamientos_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        model.guardar(request.form)
        return redirect(url_for('tratamientos.index'))
    return render_template('tratamientos/crear.html')

# 3. Ruta para EDITAR tratamiento
@tratamientos_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    tratamiento = model.obtener_por_id(id)
    if request.method == 'POST':
        model.actualizar(id, request.form)
        return redirect(url_for('tratamientos.index'))
    return render_template('tratamientos/editar.html', tratamiento=tratamiento)

# 4. Ruta para ELIMINAR tratamiento
@tratamientos_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    model.eliminar(id)
    return redirect(url_for('tratamientos.index'))