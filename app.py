from flask import Flask, render_template, request, redirect
from Modelo.estudiante import EstudianteDB

app = Flask(__name__)
db = EstudianteDB()

@app.route('/')
def index():
    estudiantes = db.listar_estudiantes()
    return render_template('listar.html', estudiantes=estudiantes)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        db.agregar_estudiante(request.form['cedula'], request.form['nombre'], request.form['direccion'], request.form['telefono'])
        return redirect('/')
    return render_template('agregar.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    estudiante = db.obtener_estudiante(id)
    if request.method == 'POST':
        db.actualizar_estudiante(id, request.form['cedula'], request.form['nombre'], request.form['direccion'], request.form['telefono'])
        return redirect('/')
    return render_template('editar.html', estudiante=estudiante)

@app.route('/eliminar/<int:id>', methods=['GET', 'POST'])
def eliminar(id):
    estudiante = db.obtener_estudiante(id)
    if request.method == 'POST':
        db.eliminar_estudiante(id)
        return redirect('/')
    return render_template('eliminar.html', estudiante=estudiante)

if __name__ == '__main__':
    app.run(debug=True)
