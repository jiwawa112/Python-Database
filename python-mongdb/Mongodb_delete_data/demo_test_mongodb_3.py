"""
删除集合中的所有文档
delete_many() 方法如果传入的是一个空的查询对象，则会删除集合中的所有文档
"""

import pymongo

myclient = pymongo.MongoClient("127.0.0.1", 27017)
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

x = mycol.delete_many({})

print(x.deleted_count, "个文档已删除")