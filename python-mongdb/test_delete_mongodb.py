"""
我们可以使用 delete_one() 方法来删除一个文档，该方法第一个参数为查询对象，指定要删除哪些数据。
"""

import pymongo

myclient = pymongo.MongoClient("127.0.0.1", 27017)
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

myquery = {"name": "Taobao"}
mycol.delete_one(myquery)

# 删除后输出
for x in mycol.find():
    print(x)

# 删除多个文档
# 我们可以使用delete_many()方法来删除多个文档，该方法第一个参数为查询对象，指定要删除哪些数据。
# 删除所有 name 字段中以 F 开头的文档:
myquery = {"name": {"$regex": "^F"}}
x = mycol.delete_many(myquery)
print(x.deleted_count, "个文档已删除")


# 删除集合中的所有文档
# delete_many()方法如果传入的是一个空的查询对象，则会删除集合中的所有文档
x = mycol.delete_many({})
print(x.deleted_count, "文档已删除")

# drop()方法删除一个集合。
mycol.drop()