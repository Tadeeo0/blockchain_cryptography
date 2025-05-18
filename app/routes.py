from flask import Blueprint, render_template, redirect, url_for, flash, request
from sqlalchemy import text
from sqlalchemy import func
from datetime import datetime
from sqlalchemy import func

bp = Blueprint('main', __name__)

#Principal (Login)
@bp.route('/', methods=['GET', 'POST'])
def home():
    return render_template('login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        
        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('main.home'))
    
    # Si es GET, solo mostrar el formulario
    return render_template('register.html')

@bp.route('/dashboard', methods=['GET', 'POST'])
def home_view():
    return render_template('home_view.html')

@bp.route('/logout', methods=['POST'])
def logout():
    return redirect(url_for('main.home'))
