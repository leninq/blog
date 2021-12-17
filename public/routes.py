# mi_proyecto/app/public/routes.py

from flask import render_template

from . import public

@public.route('/index'):
def index():
    # Nuestro código
    return render_template('...')
