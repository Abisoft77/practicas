# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    datos = {
        'nombre': request.form['nombre_cliente'],
        'factura': request.form['numero_factura'],
        'fecha': request.form['fecha_emision'],
        'total': request.form['total_factura'],
        'nit': request.form['nit_cliente']
    }
    return render_template('resultado.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)