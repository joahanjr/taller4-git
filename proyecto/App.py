from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index_():
    return render_template('index.html')

@app.route ('/index.html')
def index():
    return render_template('index.html')

@app.route ('/servicios.html')
def servicios():
    return render_template('servicios.html')

@app.route ('/especialidades.html')
def especialidades():
    return render_template ('especialidades.html')

@app.route ('/quienesSomos.html')
def quienesSomos():
    return render_template ('quienesSomos.html')

@app.route ('/contacto.html')
def contacto():
    return render_template ('contacto.html')

@app.route ('/cita.html')
def cita():
    return render_template ('cita.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)