from flask import Blueprint, render_template, request, redirect, url_for
import models.paciente_model as model

paciente_bp = Blueprint('paciente', __name__, url_prefix='/pacientes')

@paciente_bp.route('/')
def index():
    return render_template('pacientes/index.html', pacientes=model.obtener_todos())

@paciente_bp.route('/form', methods=['GET', 'POST'])
@paciente_bp.route('/form/<int:id>', methods=['GET', 'POST'])
def formulario(id=None):
    paciente = model.obtener_por_id(id) if id else None
    if request.method == 'POST':
        if id:
            model.actualizar(id, request.form)
        else:
            model.guardar(request.form)
        return redirect(url_for('paciente.index'))
    return render_template('pacientes/form.html', paciente=paciente)

@paciente_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    model.eliminar(id)
    return redirect(url_for('paciente.index'))
