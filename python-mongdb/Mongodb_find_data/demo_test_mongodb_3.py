"""
查询指定字段的数据
我们可以使用 find()方法来查询指定字段的数据，将希望返回的字段对应值设置为1，不希望返回的字段设置为0。
"""

import pymongo

myclient = pymongo.MongoClient('127.0.0.1', 27017)
mydb = myclient['runoobdb']
mycol = mydb["sites"]

# for x in mycol.find({}, {"_id": 0, "name": 1, "alexa": 1}):
#     print(x, '\n')

# 除了 _id 你不能在一个对象中同时指定0和1，如果你设置了一个字段为 0，则其他都为 1，反之亦然。
for x in mycol.find({}, {'_id': 0, "name": 1, "address": 1}):
    print(x, '\n')
