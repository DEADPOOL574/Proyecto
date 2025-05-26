from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
# Importamos para cifrar y verificar contraseñas
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# ¡IMPORTANTE! Cambia esta clave secreta por una cadena larga y aleatoria en producción
app.secret_key = 'mi_clave_secreta_super_segura_y_unica_123456789'

# --- Función para conectar a la Base de Datos PostgreSQL ---
def conectar():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            database="Bd_Escuela",
            user="postgres",
            password="1234",
            port="5432"
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# --- Rutas de la Aplicación ---

@app.route('/')
def index():
    return redirect(url_for('iniciar_sesion'))

# Ruta para la página de inicio de sesión
@app.route('/iniciar_sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'POST':
        # Capturamos el email (gmail) y la contraseña del formulario de login
        gmail = request.form.get('gmail')
        password = request.form.get('password')

        if not gmail or not password:
            flash('Por favor, ingresa tu email y contraseña.', 'error')
            return redirect(url_for('iniciar_sesion'))

        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                # 1. Buscamos el usuario por su email (gmail)
                # Seleccionamos el 'contra_hash' (contraseña cifrada) de la BD
                cursor.execute("SELECT contra_hash FROM usuarios WHERE gmail = %s", (gmail,))
                resultado = cursor.fetchone() # Obtiene la fila encontrada o None

                if resultado:
                    # El email existe, ahora verificamos la contraseña
                    hashed_password_from_db = resultado[0]
                    # 2. Comparamos la contraseña ingresada con el hash almacenado
                    if check_password_hash(hashed_password_from_db, password):
                        # Las contraseñas coinciden: ¡Inicio de sesión exitoso!
                        flash('Inicio de sesión exitoso!', 'success')
                        return redirect(url_for('bienvenido'))
                    else:
                        # Contraseña incorrecta
                        flash('Contraseña incorrecta.', 'error')
                else:
                    # El email no fue encontrado en la base de datos
                    flash('Email no registrado.', 'error')
                
                return redirect(url_for('iniciar_sesion'))

            except Exception as e:
                # Manejo de errores de base de datos durante el login
                print(f"Error al intentar iniciar sesión: {e}")
                flash('Ocurrió un error al iniciar sesión. Inténtalo de nuevo.', 'error')
                return redirect(url_for('iniciar_sesion'))
            finally:
                # Aseguramos que el cursor y la conexión se cierren
                if cursor: cursor.close()
                if conexion: conexion.close()
        else:
            # Error si no se pudo conectar a la base de datos
            flash('No se pudo conectar a la base de datos.', 'error')
            return redirect(url_for('iniciar_sesion'))

    return render_template('IniciarSesion.html')

# Ruta para el registro de usuario
@app.route('/registrarse', methods=['GET', 'POST'])
def registrarse():
    if request.method == 'POST':
        # Capturamos los datos del formulario de registro
        nombre = request.form.get('nombre')
        gmail = request.form.get('gmail')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # 1. Validaciones básicas de los campos del formulario
        if not all([nombre, gmail, password, confirm_password]):
            flash('Por favor, completa todos los campos.', 'error')
            return redirect(url_for('registrarse'))

        if password != confirm_password:
            flash('Las contraseñas no coinciden.', 'error')
            return redirect(url_for('registrarse'))

        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()

                # 2. Verificamos si el email (gmail) ya existe en la BD
                cursor.execute("SELECT id FROM usuarios WHERE gmail = %s", (gmail,))
                if cursor.fetchone():
                    flash('El email ya está registrado. Por favor, inicia sesión o usa otro email.', 'error')
                    return redirect(url_for('registrarse'))

                # 3. Ciframos la contraseña antes de guardarla en la base de datos
                # NUNCA guardes contraseñas en texto plano
                hashed_password = generate_password_hash(password)

                # 4. Insertamos el nuevo usuario en la tabla 'usuarios'
                # Asegúrate de que las columnas ('nombre', 'gmail', 'contra_hash') coincidan con tu BD
                insert_query = "INSERT INTO usuarios (nombre, gmail, contra_hash) VALUES (%s, %s, %s)"
                cursor.execute(insert_query, (nombre, gmail, hashed_password))
                conexion.commit() # Confirmamos los cambios en la base de datos

                flash('¡Registro exitoso! Ahora puedes iniciar sesión.', 'success')
                return redirect(url_for('iniciar_sesion'))

            except Exception as e:
                # Manejo de errores de base de datos durante el registro
                conexion.rollback() # Deshacemos cualquier cambio si hay un error
                print(f"Error al registrar usuario: {e}")
                flash('Ocurrió un error al intentar registrar el usuario. Por favor, inténtalo de nuevo.', 'error')
                return redirect(url_for('registrarse'))
            finally:
                # Aseguramos que el cursor y la conexión se cierren
                if cursor: cursor.close()
                if conexion: conexion.close()
        else:
            # Error si no se pudo conectar a la base de datos
            flash('No se pudo conectar a la base de datos para el registro.', 'error')
            return redirect(url_for('registrarse'))

    return render_template('Registrarse.html')

# Rutas de recuperar_contra y codigo (sin lógica de BD, solo para navegación)
# Se mantienen para que los enlaces HTML no den error de ruta
@app.route('/recuperar_contra', methods=['GET', 'POST'])
def recuperar_contra():
    if request.method == 'POST':
        # Esta ruta solo redirige para fines de navegación
        return redirect(url_for('codigo'))
    return render_template('RecuperarContra.html')

@app.route('/codigo', methods=['GET', 'POST'])
def codigo():
    if request.method == 'POST':
        # Esta ruta solo redirige para fines de navegación
        return redirect(url_for('iniciar_sesion'))
    return render_template('Codigo.html')

# Página de bienvenida después del login exitoso
@app.route('/bienvenido')
def bienvenido():
    flash('¡Bienvenido al sistema!', 'success')
    return "<h1>Bienvenido al sistema</h1><p>Has iniciado sesión correctamente.</p><a href='/iniciar_sesion'>Volver al Login</a>"

if __name__ == '__main__':
    app.run(debug=True)