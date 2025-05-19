from flask import Blueprint, render_template, redirect, url_for, flash, request

bp = Blueprint('main', __name__)

#Principal
@bp.route('/')
def home():
    return render_template('login.html')

#Registro
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        
        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('main.home'))
    

    return render_template('register.html')

#Dash principal
@bp.route('/dashboard', methods=['GET', 'POST'])
def home_view():
    return render_template('home_view.html')

#Cerrar sesion
@bp.route('/logout', methods=['POST'])
def logout():
    return redirect(url_for('main.home'))


# Ruta para historial de tokens
@bp.route('/historial')
def mostrar_historial():
    return render_template('historial.html')

#Ruta para intercambiar tokens
@bp.route('/canjear')
def canjear_tokens():
    total_tokens = 134
    premios = [
        {
            'titulo': 'Tarjeta de regalo Netflix',
            'descripcion': '1 mes gratis de Netflix',
            'tokens': 1000,
            'imagen': 'netflix.jpg'
        },
        {
            'titulo': 'Tarjeta Amazon',
            'descripcion': 'Cupón de 200 pesos en Amazon',
            'tokens': 500,
            'imagen': 'amazon.png'
        },
        {
            'titulo': 'Youtube Premium',
            'descripcion': '1 mes gratis de Youtube Premium',
            'tokens': 800,
            'imagen': 'youtube.jpg'
        },
        {
            'titulo': 'Bolsa ecológica',
            'descripcion': 'Bolsa reutilizable de tela',
            'tokens': 20,
            'imagen': 'bolsa.jpeg'
        },
        {
            'titulo': 'ONG',
            'descripcion': 'Dona 100 pesos a organizacion patito',
            'tokens': 50,
            'imagen': 'ong.jpeg'
        },
        {
            'titulo': 'Descuento Adidas',
            'descripcion': '1000 pesos de descuento en tiendas Adidas',
            'tokens': 5000,
            'imagen': 'adidas.png'
        },
    ]
    return render_template('canjear.html', premios=premios, total_tokens=total_tokens)

#Mapa puntos de reciclaje
@bp.route('/mapa')
def mapa_view():
    centros = [
        {"nombre": "Punto A: Plaza liberación", "lat": 20.677075732853243, "lon": -103.34617531444539},
        {"nombre": "Punto B: Parque Revolucion", "lat": 20.67481534457495, "lon": -103.35568005913393},
        {"nombre": "Punto C: Mercado Libertad", "lat": 20.675534856586236, "lon": -103.33983074749807},
        {"nombre": "Punto D: Minerva", "lat": 20.674615, "lon": -103.385707},
        {"nombre": "Punto E: Templo expiatorio", "lat": 20.673222795785332, "lon": -103.35894564749809},
    ]
    return render_template("mapa.html", centros=centros)

