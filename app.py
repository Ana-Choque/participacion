from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'mi_secreto'  # Necesario para usar sesiones y mensajes flash

# Diccionario de usuarios (nombre de usuario y contraseña) simulando una base de datos
usuarios = {
    'usuario1': 'contraseña1',
    'usuario2': 'contraseña2'
}

@app.route('/')
def index():
    # Verifica si el usuario está autenticado en la sesión
    if 'username' in session:
        return redirect(url_for('welcome'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Validación de credenciales
        if username in usuarios and usuarios[username] == password:
            session['username'] = username
            flash('Has iniciado sesión exitosamente', 'success')
            return redirect(url_for('welcome'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')

    return render_template('login.html')

@app.route('/bienvenida')
def welcome():
    # Verifica si el usuario está autenticado
    if 'username' in session:
        return render_template('bienvenida.html', username=session['username'])
    else:
        flash('Por favor inicia sesión primero', 'error')
        return redirect(url_for('login'))

@app.route('/login')
def logout():
    # Cierra la sesión del usuario
    session.pop('username', None)
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)