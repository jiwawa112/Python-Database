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