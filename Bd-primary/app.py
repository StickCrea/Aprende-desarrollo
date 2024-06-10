from flask import Flask, render_template, request
from bd import conectar
from datetime import datetime

app = Flask(__name__)
    #Función que encapsula la llamada a la función conectar().
    #Retorna una conexión a la base de datos.
    
def obtener_conexion():
    return conectar() # Llama a la función conectar() para obtener la conexión


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar', methods=['POST'])

def registrar():
        # Obtener los datos del formulario
        username = request.form['username']
        email = request.form['email']
        keypass = request.form['keypass']
   
        # Insertar en la base de datos
        conn = obtener_conexion()
        if conn is None:
             return "Error: No se pudo conectar a la base de datos"
        cursor = conn.cursor()
        query = "INSERT INTO usuarios (Username, email, keypass) VALUES (%s, %s, %s)"
        values = (username, email, keypass)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        return "Usuario registrado correctamente"
if __name__ == '__main__':
    app.run(debug=True)


