"""
根据指定条件查询
我们可以在 find() 中设置参数来过滤数据。
以下实例查找 address 字段为 "Park Lane 38" 的数据：
"""

import pymongo

myclient = pymongo.MongoClient('127.0.0.1', 27017)
mydb = myclient['runoobdb']
mycol = mydb["sites"]

myquery = {"name": "RUNOOB"}

# mydoc = mycol.find(myquery)

for x in mycol.find(myquery):
    print(x)
