from client import client

# 인덱싱
result = client.mflixTest.movies.create_index([('title', 'text')])