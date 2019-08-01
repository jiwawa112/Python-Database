#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

def main():
    # 打开数据库连接
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong', charset='utf8')

    # 使用cursor()方法创建一个游标对象cursor
    cursor = conn.cursor()

    # 使用execute()方法执行SQL语句
    # 添加一条数据
    sql = 'insert into goods_cates(name) values("硬盘");'

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
    except:
        # 如果发生错误则回滚
        conn.rollback()

    # 关闭数据库连接
    conn.close()