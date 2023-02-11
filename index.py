from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index_():
    return render_template('index.py')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/servicios.html')
def servicios():
    return render_template( 'servicios.html')

@app.route('/especialidades.html')
def especialidades():
    return render_template ('especialidades.html')

@app.route('/quienes_somos.html')
def quienes_somos():
    return render_template ('quienes_somos.html')

@app.route ('/contacto.html')
def contacto():
    return render_template ('contacto.html')