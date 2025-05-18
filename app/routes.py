from flask import Blueprint, render_template, redirect, url_for, flash, request

bp = Blueprint('main', __name__)

# Página principal
@bp.route('/')
def home():
    return render_template('base.html')

# Ruta para historial de tokens
@bp.route('/historial')
def mostrar_historial():
    historial_ficticio = [
        {'fecha': '30-04-2025', 'tipo': 'Cartón', 'cantidad': '2.0 kg', 'tokens': 20},
        {'fecha': '01-05-2025', 'tipo': 'Vidrio', 'cantidad': '0.8 kg', 'tokens': 8},
        {'fecha': '03-05-2025', 'tipo': 'Lata', 'cantidad': '1.5 kg', 'tokens': 15},
        {'fecha': '03-05-2025', 'tipo': 'Cartón', 'cantidad': '2.0 kg', 'tokens': 20},
        {'fecha': '06-05-2025', 'tipo': 'Plastico', 'cantidad': '2.0 kg', 'tokens': 20},
        {'fecha': '06-05-2025', 'tipo': 'Vidrio', 'cantidad': '0.8 kg', 'tokens': 8},
        {'fecha': '09-05-2025', 'tipo': 'Vidrio', 'cantidad': '0.8 kg', 'tokens': 8},
        {'fecha': '13-05-2025', 'tipo': 'Cartón', 'cantidad': '2.0 kg', 'tokens': 20},
        {'fecha': '16-05-2025', 'tipo': 'Lata', 'cantidad': '1.5 kg', 'tokens': 15}
    ]
    total = sum(item['tokens'] for item in historial_ficticio)
    return render_template('historial.html', historial=historial_ficticio, total_tokens=total)

    