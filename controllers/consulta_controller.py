from flask import Blueprint, render_template, request, redirect, url_for
import models.consulta_model as model

consulta_bp = Blueprint('consulta', __name__, url_prefix='/consultas')

@consulta_bp.route('/')
def index():
    return render_template('consultas/index.html', consultas=model.obtener_todos())

@consulta_bp.route('/form', methods=['GET', 'POST'])
@consulta_bp.route('/form/<int:id>', methods=['GET', 'POST'])
def formulario(id=None):
    consulta = model.obtener_por_id(id) if id else None
    if request.method == 'POST':
        if id:
            model.actualizar(id, request.form)
        else:
            model.guardar(request.form)
        return redirect(url_for('consulta.index'))
    return render_template('consultas/form.html', consulta=consulta)

@consulta_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    model.eliminar(id)
    return redirect(url_for('consulta.index'))
