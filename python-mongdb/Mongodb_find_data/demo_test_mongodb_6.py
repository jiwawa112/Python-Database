"""
高级查询
查询的条件语句中，我们还可以使用修饰符。
以下实例用于读取 name 字段中第一个字母 ASCII 值大于 "H" 的数据，大于的修饰符条件为 {"$gt": "H"} :
"""

import pymongo

myclient = pymongo.MongoClient('127.0.0.1', 27017)
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

myquery = {"name": {"$gt": "H"}}

# mydoc = mycol.find(myquery)

for x in mycol.find(myquery):
    print(x)