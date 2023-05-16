from client import client

def mongo_search(collection,query):
    # MongoDB 콜렉션 내 데이터 조회
    result = []
    for doc in collection.find(query):
        result.append(doc)
        
    return result


# DB 리스트 가져오기
print("DB 리스트 가져오기",client.list_database_names())

# DB 접근
db = client["mflixTest"]

# DB의 Collection 검색
print("DB의 Collection 검색",db.list_collection_names())

# Collection 접근
movies = db.movies
comments = db.comments
sessions = db.sessions
theaters = db.theaters
users = db.users

# 컬렉션 내 도큐먼트 조회
# 영화 한개
print("영화 한개: ",movies.find_one())
# 영화의 갯수
print("총 영화 갯수: ",movies.count_documents({}))
# 캐스트에 john ott이 들어간 영화 조회
print("캐스트에 john ott이 들어간 영화  : ",mongo_search(movies,{"cast":"John Ott"}))
# 장르가 short인 영화
print("장르가 short인 영화 : ",[short_movie['title'] for short_movie in mongo_search(movies,{"genres":"Short"})])

