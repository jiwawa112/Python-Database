"""
返回 _id 字段
insert_one() 方法返回 InsertOneResult 对象，该对象包含 inserted_id 属性，它是插入文档的 id 值。
"""

import pymongo

myclient = pymongo.MongoClient("127.0.0.1", 27017)
mydb = myclient['runoobdb']
mycol = mydb["sites"]

mydict = {"name": "Google", "alexa": "1", "url": "https://www.google.com" }
x = mycol.insert_one(mydict)

# 如果我们在插入文档时没有指定_id，MongoDB会为每个文档添加一个唯一的id
# inserted_id()方法返回每一个插入文档的_id
print(x.inserted_id)