#IMDB
from imdbpie import Imdb
import Main
import sqlite3
import json
def details(movie,detailinfo):
    imdb = Imdb()
    movie_data=imdb.find_by_title(movie)
    json_data = json.loads(movie_data)[0]
    detail = json_data[detailinfo]
    return detail

class IMDB(Main.Datafetch):

    def __init__(self,movie_name):
        self.movie = movie_name
        self.movie_details=RT(api).search(self.movie)
    def display_name(self):
        print "Movie"
        return details(self.movie,'Title')
    def display_description(self):
        print "Description:"
        return details(self.movie,'Description')
    def display_year(self):
        print "Year:"
        return details(self.movie,'Year')
    def display_rating(self):
        print "Rating:"
        return details(self.movie,'Rated')
    def display_actors(self):
        print "Actors"
        return details(self.movie,'Actors')
    def display_writer(self):
        print "Writer"
        return details(self.movie,'Writer')
    def display_director(self):
        print "Director:"
        return details(self.movie,'Director')
    def display_plot(self):
        print "Plot:"
        return details(self.movie,'Plot')
    def display_language(self):
        print "Language:"
        return details(self.movie,'Language')

movie = raw_input("Enter movie name:")
movie1 = IMDB(movie)
conn = sqlite3.connect('Seriesmanagerdatabase.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS IMDB_movie(movie text,description text,year int,rating real,actors text,writer text,director text,plot text,language text)''')
c.execute("INSERT INTO IMDB_movie VALUES(display_name(movie1),display_description(movie1),display_year(movie1),display_rating(movie1),display_actors(movie1),display_writer(movie1),display_director(movie1),display_plot(movie1),display_language(movie1))")
conn.commit()
print "Details from IMDB:\n"
for row in c.execute('SELECT * FROM IMDB_movie ORDER rating'):
    print row
conn.close()

