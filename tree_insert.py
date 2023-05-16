from client import client


# 루트 노드 생성
client.treetest.maintree.insert_one({"_id":0,"name": "root"})

# 새로운 주제 생성
client.treetest.maintree.insert_one({"_id":1,"name": "math"})
client.treetest.maintree.insert_one({"_id":2,"name": "science"})
client.treetest.maintree.insert_one({"_id":3,"name": "dataScience"})
client.treetest.maintree.insert_one({"_id":4,"name": "physical" })

# 상위 주제와 하위 주제를 연결
client.treetest.maintree.update_one({"name": "math"}, {"$set": {"parent": "root"}})
client.treetest.maintree.update_one({"name": "science"}, {"$set": {"parent": "root"}})

# 하위 주제에 새로운 하위 주제 추가
client.treetest.maintree.update_one({"name": "dataScience"}, {"$set": {"parent": "science"}})
client.treetest.maintree.update_one({"name": "physical"}, {"$set": {"parent": "science"}})
