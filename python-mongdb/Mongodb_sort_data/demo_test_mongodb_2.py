import pymongo

myclient = pymongo.MongoClient('127.0.0.1', 27017)
mydb = myclient['Sina']
mycol = mydb["Tweets"]

# 对字段 alexa 按升序排序
mydoc = mycol.find().sort('created_at', -1)
for x in mydoc:
    print(x)