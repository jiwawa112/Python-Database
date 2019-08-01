#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

def main():
    # 打开数据库连接
    conn = pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='jing_dong',charset='utf8')

    # 使用cursor()方法创建一个游标对象cursor
    cursor = conn.cursor()

    # 使用execute()方法执行SQL语句
    cursor.execute('select * from goods;')

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    print("Database version : %s " % data)
    # cursor.fetchone()      该方法获取下一个查询结果集。结果集是一个对象
    # cursor.fetchmany(5)    取多行数据
    # cursor.fetchall()      接收全部的返回结果行

    # 关闭数据库连接
    db.close()
