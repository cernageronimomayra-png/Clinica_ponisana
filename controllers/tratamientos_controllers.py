from flask import Blueprint, render_template, request, redirect, url_for
import models.tratamiento_model as model

tratamientos_bp = Blueprint('tratamientos', __name__, url_prefix='/tratamientos')

@tratamientos_bp.route('/')
def index():
    return render_template('tratamientos/index.html', tratamientos=model.obtener_todos())

@tratamientos_bp.route('/form', methods=['GET', 'POST'])
@tratamientos_bp.route('/form/<int:id>', methods=['GET', 'POST'])
def formulario(id=None):
    tratamiento = model.obtener_por_id(id) if id else None
    if request.method == 'POST':
        if id:
            model.actualizar(id, request.form)
        else:
            model.guardar(request.form)
        return redirect(url_for('tratamiento.index'))
    return render_template('tratamientos/form.html', tratamiento=tratamiento)

@tratamientos_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    model.eliminar(id)
    return redirect(url_for('tratamiento.index'))
