#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
#建立MongoDB数据库连接
myclient = MongoClient('localhost',27017)

#创建数据库
mydb = myclient['test']

#创建集合
mycol = mydb["sites"]


#向集合中插入一条数据
mycol.insert({'name':'xiaowang','age':18,'addr':'Chengdu'})
#向集合中插入多条数据
mycol.insert_many([{'name':'xiaozhang','age':20,'addr':'shanghai'},
                        {'name':'xiaozhao','age': 19, 'addr': 'beijing'}])
#向集合中查询一条数据
res = mycol.find_one({"age": 19})
print(res)

#向集合中更新第一条满足条件的数据
# 参数说明：
# criteria：查询条件
# objNew：update对象和一些更新操作符
# upsert：如果不存在update的记录，是否插入objNew这个新的文档，True为插入，默认为False，不插入。
# multi：默认是false，只更新找到的第一条记录。如果为true，把按条件查询出来的记录全部更新。
mycol.update_one({"age": 19},{"$set": {"age": 100}})
#向集合中更新，如果不存在则插入且只更新第一条
mycol.update({"count":{"$gt":50}},{"$set":{"name":"c5"}},True,False)
# {$inc:{field:value}}的作用是对一个数字字段的某个field增加value
mycol.update({"name":"xiaowang"},{"$inc":{"age":5}})
#向集合中更新所有满足条件的数据
mycol.update_many({"age": 10},{"$set": {"age": 100}})
#向集合中删除第一条满足条件的数据
mycol.delete_one({"age": 10})
#向集合中删除所有满足条件的数据
mycol.delete_many({"age": 18})

#查找集合中所有数据
for item in mycol.find():
    print(item)

#查找集合中单条数据
print(mycol.find_one())

# #删除集合mycol中的所有数据
mycol.remove()
#
# #删除集合mycol
mycol.drop()