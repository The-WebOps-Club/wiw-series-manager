#Rotten tomatoes
from rottentomatoes import RT
import json
api = '43h3hy2a4r6cuf3h3d4tzkqy'
#def details(movie,detailinfo):
movie_data = RT(api).search('Interstellar')
json_data = json.loads(movie_data)[0]
detail = json_data['synopsis']
print detail
#details('Interstellar','synopsis')
