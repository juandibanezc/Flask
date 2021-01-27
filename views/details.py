from flask import render_template, Blueprint

from models.pelicula import Pelicula

perfil = Blueprint('perfil', __name__)


@perfil.route('/detalles/<id>/')
def detail(id):
    pelicula = Pelicula.get(
        id=id
    )
    return render_template('detail.html', movie=pelicula)