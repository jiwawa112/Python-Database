"""
插入集合
MongoDB 中的一个文档类似 SQL 表中的一条记录。
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


