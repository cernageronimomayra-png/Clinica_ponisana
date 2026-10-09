from flask import Blueprint, render_template, request, redirect, url_for
import models.medico_model as model

medico_bp = Blueprint('medico', __name__, url_prefix='/medicos')

@medico_bp.route('/')
def index():
    return render_template('medicos/index.html', medicos=model.obtener_todos())

@medico_bp.route('/form', methods=['GET', 'POST'])
@medico_bp.route('/form/<int:id>', methods=['GET', 'POST'])
def formulario(id=None):
    medico = model.obtener_por_id(id) if id else None
    if request.method == 'POST':
        if id:
            model.actualizar(id, request.form)
        else:
            model.guardar(request.form)
        return redirect(url_for('medico.index'))
    return render_template('medicos/form.html', medico=medico)

@medico_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    model.eliminar(id)
    return redirect(url_for('medico.index'))

