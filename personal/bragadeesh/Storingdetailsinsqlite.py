from rottentomatoes import RT
from imdbpie import Imdb
import sqlite3
import re
api = '43h3hy2a4r6cuf3h3d4tzkqy'
movie = raw_input("Enter movie name:")
movie_details=RT(api).search(movie)

conn = sqlite3.connect('Seriesmanagerdatabase.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Rottentomatoes_movie(name text,year int,mpaa_rating text,release_date text,synopsis text,audience_score real,critics_score real)''')

text = '"title":"(.+?)"'
pattern = re.compile(text)
name = re.findall(pattern,movie_details)

text = '"year":"(.+?)"'
pattern = re.compile(text)
year = re.findall(pattern,movie_details)

text = '"mpaa_rating":"(.+?)"'
pattern = re.compile(text)
mpaa_rating = re.findall(pattern,movie_details)

text = '"release_date":{(.+?)}'
pattern = re.compile(text)
year = re.findall(pattern,movie_details)

text = '"audience_score":"(.+?)"'
pattern = re.compile(text)
audience_score = re.findall(pattern,movie_details)

text = '"critics_score":"(.+?)"'
pattern = re.compile(text)
critics_score = re.findall(pattern,movie_details)

c.execute("INSERT INTO Rottentomatoes_movie VALUES(name,year,mpaa_rating,release_date,audience_score,critics_score")
conn.commit()
print "Details from Rottentomatoes:\n"
for row in c.execute('SELECT * FROM Rottentomatoes_movie ORDER audience_score'):
    print row
conn.close()


imdb = Imdb()
imdb.find_by_title(movie)
c.execute('''CREATE TABLE IF NOT EXISTS imdb_movie(name text,year int,mpaa_rating text,release_date text,genre text,runtime text,plot text,language text,director text,writer text,actors text,metascore real,imdb_rating real,imdb_votes int)''')

text = '"Title":"(.+?)"'
pattern = re.compile(text)
name = re.findall(pattern,movie_details)

text = '"Year":"(.+?)"'
pattern = re.compile(text)
year = re.findall(pattern,movie_details)

text = '"Rated":"(.+?)"'
pattern = re.compile(text)
mpaa_rating = re.findall(pattern,movie_details)

text = '"Released":"(.+?)"'
pattern = re.compile(text)
release_date = re.findall(pattern,movie_details)

text = '"Genre":"(.+?)"'
pattern = re.compile(text)
genre = re.findall(pattern,movie_details)

text = '"Runtime":"(.+?)"'
pattern = re.compile(text)
runtime = re.findall(pattern,movie_details)

text = '"Plot":"(.+?)"'
pattern = re.compile(text)
plot = re.findall(pattern,movie_details)

text = '"Language":"(.+?)"'
pattern = re.compile(text)
language = re.findall(pattern,movie_details)

text = '"Director":"(.+?)"'
pattern = re.compile(text)
director = re.findall(pattern,movie_details)

text = '"Writer":"(.+?)"'
pattern = re.compile(text)
writer = re.findall(pattern,movie_details)

text = '"Actors":"(.+?)"'
pattern = re.compile(text)
actors = re.findall(pattern,movie_details)

text = '"Metascore":"(.+?)"'
pattern = re.compile(text)
metascore = re.findall(pattern,movie_details)

text = '"imdbRating":"(.+?)"'
pattern = re.compile(text)
imdb_rating = re.findall(pattern,movie_details)

text = '"imdbVotes":"(.+?)"'
pattern = re.compile(text)
imdb_vote = re.findall(pattern,movie_details)

c.execute("INSERT INTO imdb_movie VALUES(name,year,mpaa_rating,release_date,genre,runtime,plot,language,director,writer,actors,metascore,imdb_rating,imdb_votes")
conn.commit()
print "Details from IMDB:\n"
for row in c.execute('SELECT * FROM imdb_movie ORDER imdb_rating'):
    print row
conn.close()
