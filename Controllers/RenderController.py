from flask import render_template, Blueprint

render_bp = Blueprint('render', __name__)

@render_bp.route('/')
def logins():
    return render_template('home.html')

@render_bp.route('/pendaftaran')
def pendaftaran():
    return render_template('pendaftaran.html')