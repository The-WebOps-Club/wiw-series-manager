
#Main function
class Datafetch:    
    def __init__(self,movie_name):
        self.movie = movie_name
    def display_name(self,movie):
        print "Movie:"+ "Not Applicable"
    def display_description(self):
        print "Description:" + "Not Applicable"
    def display_year(self):
        print "Year:" + "Not Applicable"
    def display_rating(self):
        print "Rating:"+ "Not Applicable"
    def display_actors(self,actor):
        print "Actors:"+"Not Applicable"
    def display_writer(self,writer):
        print "Writer:" + "Not Applicable"
    def display_director(self,director):
        print "Director:" + "Not Applicable"
    def display_plot(self,plot):
        print "Plot:" + "Not Applicable"
    def display_language(self,language):
        print "Language:" + "Not Applicable"


movie1 = Datafetch('Interstellar')
movie1.display_description()







#Rotten tomatoes
from rottentomatoes import RT
import re
api = '43h3hy2a4r6cuf3h3d4tzkqy'
movie_details=RT(api).search(movie)

class Rottentomatoes(Datafetch):
    
    
    text = '"year":"(.+?)"'
    pattern = re.compile(text)
    year = re.findall(pattern,movie_details)

    text = '"synopsis":"(.+?)"'
    pattern = re.compile(text)
    description = re.findall(pattern,movie_details)

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
    
    def __init__(self,movie_name):
        self.movie = movie_name
    def display_name(self,movie):
        print "Movie"+ movie
    def display_description(self):
        print "Description:" + description
    def display_year(self):
        print "Year:" + year
    def display_rating(self):
        print "Rating:"+ mpaa_rating
    def display_actors(self,actor):
        print "Actors:"
        print ', '.join(actor)
    def display_writer(self,writer):
        print "Writer:"
        print ', '.join(writer)
    def display_director(self,director):
        print "Director:"
    def display_plot(self,plot):
        print "Plot:"
    def display_language(self,language):
        print "Language:"

movie1 = Rottentomatoes('Interstellar')
movie1.display_description()

