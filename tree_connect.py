from client import client
import time

maintree =client.treetest.maintree

# 조상노드 검색
def find_anscestor(node):
    anscestor = []
    while node != "root":
        # 이름이 root가 아니면 계속해서 부모 노드를 찾는다.
        # 무조건 초기값은 root로 설정해야 한다.
        node = maintree.find_one({"name":node})["parent"]
        anscestor.append(node)
    # 마지막에 리스트에 담긴 것을 역순으로 돌려야함.
    anscestor.reverse()
    return anscestor

def update_ancestor(node):
    ancestor = find_anscestor(node)
    return maintree.update_one({"name":node},{"$set":{"ancestor":ancestor}})

datascience = maintree.find({"name":"dataScience"})


# 검색형식으로 연결하는 방법
# pipeline =[
#     {"$match":{"name":"dataScience"}},
#     {"$graphLookup":{
#         "from":"maintree",
#         "startWith":"$parent",
#         "connectFromField":"parent",
#         "connectToField":"name",
#         "as":"ancestors"
#     }},
#     {"$limit":1}
# ]
# results = maintree.aggregate(pipeline)

# root- science - dataScience 
result = update_ancestor("dataScience")
print(result)
# root - science - physical
result = update_ancestor("physical")
print(result)