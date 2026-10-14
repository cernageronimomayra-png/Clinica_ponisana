from flask import Blueprint, render_template, request, redirect, url_for
import models.medico_model as model

# 1. Definición del Blueprint en plural y con su prefijo de URL
medicos_bp = Blueprint('medicos', __name__, url_prefix='/medicos')

# 2. Ruta principal (lista de médicos)
@medicos_bp.route('/')
def index():
    return render_template('medicos/index.html', medicos=model.obtener_todos())

# 3. Ruta para el formulario (Crear / Editar)
@medicos_bp.route('/form', methods=['GET', 'POST'])
@medicos_bp.route('/form/<int:id>', methods=['GET', 'POST'])
def formulario(id=None):
    medico = model.obtener_por_id(id) if id else None
    if request.method == 'POST':
        if id:
            model.actualizar(id, request.form)
        else:
            model.guardar(request.form)
        return redirect(url_for('medicos.index'))
    return render_template('medicos/form.html', medico=medico)

# 4. Ruta para eliminar
@medicos_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    model.eliminar(id)
    return redirect(url_for('medicos.index'))
