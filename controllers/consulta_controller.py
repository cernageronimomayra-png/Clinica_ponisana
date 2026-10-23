from flask import Blueprint, render_template, request, redirect, url_for
import models.consulta_model as model
import models.paciente_model as paciente_model
import models.medico_model as medico_model

consulta_bp = Blueprint('consulta', __name__, url_prefix='/consultas')

@consulta_bp.route('/')
def index():
    return render_template('consultas/index.html', consultas=model.obtener_todos())

@consulta_bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        model.guardar(request.form)
        return redirect(url_for('consulta.index'))
    

    pacientes = paciente_model.obtener_todos()
    medicos = medico_model.obtener_todos()
    return render_template('consultas/crear.html', pacientes=pacientes, medicos=medicos)

@consulta_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    consulta = model.obtener_por_id(id)
    if request.method == 'POST':
        model.actualizar(id, request.form)
        return redirect(url_for('consulta.index'))
    

    pacientes = paciente_model.obtener_todos()
    medicos = medico_model.obtener_todos()
    return render_template('consultas/editar.html', consulta=consulta, pacientes=pacientes, medicos=medicos)

@consulta_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    model.eliminar(id)
    return redirect(url_for('consulta.index'))