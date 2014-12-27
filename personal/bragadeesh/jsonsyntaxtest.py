from rottentomatoes import RT
import json
api = '43h3hy2a4r6cuf3h3d4tzkqy'
movie_data = RT(api).search('Interstellar')
print movie_data
#json_data = json.loads(movie_data)
#print json_data['synopsis']
movie_data = '{"foo": "{agc}", "bar": [1, 2, 3]}'
d = json.loads(movie_data)
print d['foo']
