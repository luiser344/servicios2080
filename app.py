from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)  # 👈 Esto debe estar antes de usar @app.route

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/contacto', methods=['POST'])
def contacto():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    correo = request.form['correo']
    mensaje = request.form['mensaje']

    with open('clientes.csv', mode='a', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([nombre, telefono, correo, mensaje])

    return render_template('index.html', mensaje_exito=True)

if __name__ == '__main__':
    app.run()
