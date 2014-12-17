#Program to get synopsis of a movie from rotten tomatoes:
import urllib2
import re
api = '43h3hy2a4r6cuf3h3d4tzkqy'
print('Enter the name of the movie:')
name = input()
req = urllib2.Request('http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey='+ api +'&q='+ name +'&page_limit=1')
response = urllib2.urlopen(req)
page = response.read()
print "Start"
text = '"synopsis":"(.+?)"'
pattern = re.compile(text)
synopsis = re.findall(pattern,page)
print('The synopsis of your movie is described:')
print synopsis
print "Stop"
