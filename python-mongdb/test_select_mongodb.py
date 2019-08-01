import pymongo

myclient = pymongo.MongoClient('127.0.0.1', 27017)
mydb = myclient['runoobdb']
mycol = mydb["sites"]

# find_one()方法查询集合中的一条数据。
x = mycol.find_one()
print(x)

# find()方法可以查询集合中的所有数据，类似 SQL 中的 SELECT * 操作。
for x in mycol.find():
    print(x)



# find()方法查询指定字段的数据，将希望返回的字段对应值设置为1，不希望返回的字段设置为0。
# for x in mycol.find{}, {"_id": 0, "name": 1, "alexa": 1}):
#     print(x, '\n')
# 除了 _id 你不能在一个对象中同时指定0和1，如果你设置了一个字段为 0，则其他都为 1，反之亦然。
for x in mycol.find({}, {'_id': 0, "name": 1, "address": 1}):
    print(x, '\n')

"""
根据指定条件查询
在find()中设置参数来过滤数据。
以下实例查找 address 字段为 "Park Lane 38" 的数据：
"""
myquery = {"name": "RUNOOB"}
# mydoc = mycol.find(myquery)
for x in mycol.find(myquery):
    print(x)

"""
高级查询
查询的条件语句中，使用修饰符。
以下实例用于读取name字段中第一个字母ASCII值大于 "H" 的数据，大于的修饰符条件为 {"$gt": "H"} :
"""
myquery = {"name": {"$gt": "H"}}
# mydoc = mycol.find(myquery)
for x in mycol.find(myquery):
    print(x)

"""
正则表达式查询
正则表达式修饰符只用于搜索字符串的字段。
以下实例用于读取name字段中第一个字母为 "R" 的数据，正则表达式修饰符条件为 {"$regex": "^R"}
"""
myquery = {"name": {"$regex": "^R"}}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

"""
返回指定条数记录
对查询结果设置指定条数的记录可以使用limit()方法，该方法只接受一个数字参数。
以下实例返回3条文档记录：
"""
myresult = mycol.find().limit(3)
for x in myresult:
    print(x)