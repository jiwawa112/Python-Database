"""
插入集合
MongoDB中的一个文档类似SQL表中的一条记录。
"""

import pymongo

# 连接mongodb数据库，连接方式为IP + 端口号
myclient = pymongo.MongoClient("127.0.0.1", 27017)

# 创建数据库"runoobdb"
mydb = myclient["runoobdb"]

# 创建集合(数据表) 数据表位于数据库内
mycol = mydb["sites"]

# 需要插入的内容
mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}

# 向数据表mydb["sites"]中插入数据：mydict
x = mycol.insert_one(mydict)
print(x)

#返回 _id 字段
#insert_one() 方法返回InsertOneResult对象，该对象包含inserted_id属性，它是插入文档的id值。
mydict = {"name": "Google", "alexa": "1", "url": "https://www.google.com"}
x = mycol.insert_one(mydict)

# 集合中插入多个文档使用insert_many()方法，该方法的第一参数是字典列表。
mylist_1 = [
  { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
  { "name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
  { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
  { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
  { "name": "Github", "alexa": "109", "url": "https://www.github.com"}
]

# insert_many() 方法返回InsertManyResult对象，该对象包含inserted_ids属性，该属性保存着所有插入文档的 id 值。
x = mycol.insert_many(mylist_1)
# 输出插入的所有文档对应的_id值
print(x.inserted_ids)

mylist_2 = [
  { "_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
  { "_id": 2, "name": "Google", "address": "Google 搜索"},
  { "_id": 3, "name": "Facebook", "address": "脸书"},
  { "_id": 4, "name": "Taobao", "address": "淘宝"},
  { "_id": 5, "name": "Zhihu", "address": "知乎"}
]

x = mycol.insert_many(mylist_2)

# 输出插入的所有文档对应的_id值
print(x.inserted_ids)