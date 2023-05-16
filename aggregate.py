from models import MFlixSampleModel
from pymongo import ASCENDING
import pprint

model = MFlixSampleModel()

# 1. 검색 파이프 라인 만들기

# 제목이 A Star is Born인 영화를 찾는다.
search_by_name = {
    "$match":{
        "title":"Hallway"
    }
}

# 연도 오름차순으로 정렬한다.
sort_by_asc = {
    "$sort":{"year":ASCENDING}
}

pipeline=[
    search_by_name,sort_by_asc
]
# 2. 집계하기
results = model.movies.aggregate(pipeline)

# 3. 결과 출력
for movie in results:    
    print(" * {title}, {first_castmember}, {year}".format(
         title=movie["title"],
         first_castmember=movie["cast"][0],
         year=movie["year"],
   ))

# 다른 컬렉션에 관련 데이터 조회
stage_lookup_comments = {
    "$lookup":{
        "from":"comments",
        "localField":"_id",
        "foreignField":"movie_id",
        "as":"related_comments"
    }
}

# 5개만 가져옴
stage_limit_5 ={
    "$limit":5
}

pipeline=[
    stage_lookup_comments,stage_limit_5
]

results = model.movies.aggregate(pipeline)

for movie in results:
    print(movie)
    
# 댓글이 2개 이상인 영화만 조회

# 각 영화의 댓글 갯수 계산
stage_add_comments_count = {
    "$addFields":{
        "comments_count":{
            "$size":"$related_comments"
        }
    }
}

# 2개 이상인 영화만 가져오기
stage_match_with_comments={
    "$match":{
        "comments_count":{
            "$gt":2
        }
    }
}

pipeline=[
    stage_lookup_comments,stage_add_comments_count,stage_match_with_comments,stage_limit_5
]
results = model.movies.aggregate(pipeline)
for movie in results:
   print(movie["title"])
   print("Comment count:", movie["comments_count"])

   # Loop through the first 5 comments and print the name and text:
   for comment in movie["related_comments"][:5]:
         print(" * {name}: {text}".format(
            name=comment["name"],
            text=comment["text"]))