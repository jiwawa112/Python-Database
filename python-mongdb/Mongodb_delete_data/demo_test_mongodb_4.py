"""
删除集合
我们可以使用 drop() 方法来删除一个集合。
以下实例删除了 customers 集合
"""

import pymongo

myclient = pymongo.MongoClient("127.0.0.1", 27017)
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

mycol.drop()