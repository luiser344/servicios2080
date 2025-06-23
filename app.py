from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/contacto', methods=['POST'])
def contacto():
    nombre = request.form['nombre']
    correo = request.form['correo']
    mensaje = request.form['mensaje']
    
    with open('clientes.csv', mode='a', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([nombre, correo, mensaje])
    
    return redirect('/')

@app.route('/clientes')
def mostrar_clientes():
    clientes = []
    if os.path.exists('clientes.csv'):
        with open('clientes.csv', newline='', encoding='utf-8') as archivo:
            reader = csv.reader(archivo)
            for fila in reader:
                clientes.append({
                    'nombre': fila[0],
                    'correo': fila[1],
                    'mensaje': fila[2]
                })
    return render_template('clientes.html', clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True)
