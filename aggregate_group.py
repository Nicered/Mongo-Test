from models import MFlixSampleModel
from pymongo import ASCENDING


model = MFlixSampleModel()

# 영화들을 연도별로 그룹화
stage_group_year = {
    "$group":{
        "_id":"$year",
        # 각 영화 수
        "movie_count":{"$sum":1}
    }
}

stage_match_year = {
    "$match":{
        "year":{
            "$type":"number"
        }
    }
}

stage_sort_year_asc = {
    "$sort":{"_id":ASCENDING}
}

pipeline = [
    # 주의! 순서도 중요함.
    stage_match_year,
    stage_group_year,    
    stage_sort_year_asc
]
results = model.movies.aggregate(pipeline)
for year_summary in results: 
    print(year_summary)