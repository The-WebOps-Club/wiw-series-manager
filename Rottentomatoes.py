#Rotten tomatoes
from rottentomatoes import RT
import Main
import sqlite3
import json
api = '43h3hy2a4r6cuf3h3d4tzkqy'
def details(movie,detailinfo):
    movie_data = RT(api).search(movie)
    json_data = json.loads(movie_data)[0]
    detail = json_data[detailinfo]
    print detail

class Rottentomatoes(Main.Datafetcher):

    def __init__(self,movie_name):
        self.movie = movie_name
        self.movie_details=RT(api).search(self.movie)
    def display_name(self):
        print "Movie"
        return details(self.movie,'name')
    def display_description(self):
        print "Description:"
        return details(self.movie,'synopsis')
    def display_year(self):
        print "Year:"
        return details(self.movie,'year')
    def display_rating(self):
        print "Rating:"
        return details(self.movie,'mpaa_rating')

movie = raw_input("Enter movie name:")
movie1 = Rottentomatoes(movie)
conn = sqlite3.connect('Seriesmanagerdatabase.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Rottentomatoes_movie(name text,description text,year int,rating real)''')
c.execute("INSERT INTO Rottentomatoes_movie VALUES(display_name(movie1),display_description(movie1),display_year(movie1),display_rating(movie1)")
conn.commit()
print "Details from Rottentomatoes:\n"
for row in c.execute('SELECT * FROM Rottentomatoes_movie ORDER rating'):
    print row
conn.close()

