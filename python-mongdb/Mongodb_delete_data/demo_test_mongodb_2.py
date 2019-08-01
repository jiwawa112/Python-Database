""""
删除多个文档
我们可以使用 delete_many() 方法来删除多个文档，该方法第一个参数为查询对象，指定要删除哪些数据。
删除所有 name 字段中以 F 开头的文档:
"""

import pymongo

myclient = pymongo.MongoClient("127.0.0.1", 27017)
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

myquery = {"name": {"$regex": "^F"}}

x = mycol.delete_many(myquery)

print(x.deleted_count, "个文档已删除")