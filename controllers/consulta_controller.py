# controllers/consulta_controller.py
from flask import Blueprint, render_template, request, redirect, url_for
import models.consulta_model as model

consulta_bp = Blueprint('consulta', __name__, url_prefix='/consultas')

# 1. Ruta para listar todas las consultas
@consulta_bp.route('/')
def index():
    return render_template('consultas/index.html', consultas=model.obtener_todos())

# 2. Ruta para mostrar el formulario de CREAR
@consulta_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        model.guardar(request.form)
        return redirect(url_for('consulta.index'))
    return render_template('consultas/crear.html')

# 3. Ruta para mostrar el formulario de EDITAR
@consulta_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    consulta = model.obtener_por_id(id)
    if request.method == 'POST':
        model.actualizar(id, request.form)
        return redirect(url_for('consulta.index'))
    return render_template('consultas/editar.html', consulta=consulta)

# 4. Ruta para ELIMINAR
@consulta_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    model.eliminar(id)
    return redirect(url_for('consulta.index'))
