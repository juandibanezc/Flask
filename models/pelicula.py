#API TheMovieDB al database
import json
from urllib.request import urlopen
from pandas import json_normalize
import pandas as pd
from flask import Flask

API_KEY = '2f2afdb5112f67ccfa2eaa96eb8aebe8'
save_doc = 'movie'

#URL de moviedb
url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=es-CO&page=1'
r = urlopen(url)

#datos en json
datos = json.loads(r.read())

#Convert the Json file into a DB
df= json_normalize(datos['results'])

#Safe the Json file 
df.to_csv(save_doc+'.csv')

#DB con Peewee
from peewee import *

db = SqliteDatabase('Peliculas.db')

class Pelicula(Model):
    adult = TextField()
    backdrop_path = TextField()
    genre_ids = TextField()
    original_language = TextField()
    original_title = TextField() 
    overview = TextField()
    popularity = TextField()
    poster_path = TextField()
    release_date = DateField()
    title = TextField()
    video = TextField()
    vote_average = TextField()
    vote_count = TextField()

    class Meta:
        database = db

if __name__ == '__main__':
    new = df['genre_ids'].astype(str).str.split(",", n = -1, expand = True)
    new[0] = new[0].str.lstrip('[').str.rstrip(']')
    df['genre_ids'] = new[0]

    print(df.head())
    db.connect()
    db.create_tables([Pelicula])
    Pelicula.insert_many(df.to_dict(orient='records')).execute()
