from flask import Flask 
from flask import render_template 
from models.pelicula import Pelicula
from views.details import perfil
import sqlite3
from decouple import config as config_decouple

@app.route('/')
def home_page():
    peliculas = Pelicula.select()
    
    return render_template('index.html', datos=peliculas)

def create_app(enviroment):
    app = Flask(__name__)
    app.register_blueprint(perfil)

    app.config.from_object(enviroment)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app

enviroment = config['development']
if config_decouple('PRODUCTION', default=False):
    enviroment = config['production']

app = create_app(enviroment)

"""
app = Flask(__name__)
app.register_blueprint(perfil)

@app.route('/')
def home_page():
    peliculas = Pelicula.select()
    
    return render_template('index.html', datos=peliculas)

if __name__ == '__main__':
    app.run(debug=True)
"""