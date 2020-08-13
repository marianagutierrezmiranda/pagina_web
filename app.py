from flask import Flask, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb://mariana:Mariana767@localhost/alumnos'
db = SQLAlchemy(app)


class Alumno(db.Model):
    nombre = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    apellido = db.Column(db.String(80), unique=True, nullable=False)
    genero = db.Column(db.String(80), unique=True, nullable=False)

    # def __repr__(self):
        # return '<User %r>' % self.username


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar_alumno', methods=['POST'])
def registro():
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    genero = request.form.get('genero')
    alumno = Alumno(nombre=nombre, apellido=apellido, genero=genero)
    return 'Su registro fue exitoso'



