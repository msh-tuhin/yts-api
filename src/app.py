import requests
import json

import src.methods

result = requests.get("https://yts.ag/api/v2/list_movies.json?order_by=asc")
json_data = result.content.decode('utf-8')
dic = json.loads(json_data)
print(dic.keys())
movies = dic['data']['movies']
total_movies = dic['data']['movie_count']
output_file = "C:\\Users\\Tuhin\\Desktop\\movie_data.txt"

src.methods.fulldata("C:\\Users\\Tuhin\\Desktop\\movie_details.txt", movies)
src.methods.getdata(output_file, movies, fields=['title', 'year', 'rating', 'runtime',
                                                 'id', 'date_uploaded'])
