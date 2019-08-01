"""
插入指定 _id 的多个文档
我们也可以自己指定 id，插入，以下实例我们在 site2 集合中插入数据，_id 为我们指定的：
"""

import pymongo

myclient = pymongo.MongoClient("127.0.0.1", 27017)
mydb = myclient['runoobdb']
mycol = mydb["sites"]

mylist = [
  { "_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
  { "_id": 2, "name": "Google", "address": "Google 搜索"},
  { "_id": 3, "name": "Facebook", "address": "脸书"},
  { "_id": 4, "name": "Taobao", "address": "淘宝"},
  { "_id": 5, "name": "Zhihu", "address": "知乎"}
]

x = mycol.insert_many(mylist)

# 输出插入的所有文档对应的_id值
print(x.inserted_ids)