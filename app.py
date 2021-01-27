from flask import Flask 
from flask import render_template 
from models.pelicula import Pelicula
from views.details import perfil
import sqlite3

app = Flask(__name__)
app.register_blueprint(perfil)

@app.route('/')
def home_page():
    peliculas = Pelicula.select()
    
    return render_template('index.html', datos=peliculas)

if __name__ == '__main__':
    app.run(debug=True)