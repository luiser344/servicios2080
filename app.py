from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/contacto', methods=['POST'])
def contacto():
    nombre = request.form['nombre']
    correo = request.form['correo']
    telefono = request.form['telefono']
    mensaje = request.form['mensaje']
    
    # Guardar datos en CSV (agrega columnas: nombre, correo, telefono, mensaje)
    with open('clientes.csv', mode='a', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([nombre, correo, telefono, mensaje])
    
    return render_template('index.html', enviado=True)

@app.route('/clientes')
def clientes():
    clientes = []
    try:
        with open('clientes.csv', newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if fila:
                    clientes.append({
                        'nombre': fila[0],
                        'correo': fila[1],
                        'telefono': fila[2] if len(fila) > 2 else '',
                        'mensaje': fila[3] if len(fila) > 3 else ''
                    })
    except FileNotFoundError:
        pass  # archivo no existe aún
    
    return render_template('clientes.html', clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True)
