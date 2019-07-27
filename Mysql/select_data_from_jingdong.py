#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql

class JD(object):
    def __init__(self):
        # 创建Connection连接
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='jing_dong', charset='utf8')
        # 获得Cursor对象
        self.cursor = self.conn.cursor()

    def __del__(self):
        # 关闭Cursor对象
        self.cursor.close()
        self.conn.close()

    def execute_sql(self,sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)
    def show_all_items(self):
        """显示所有的商品"""
        sql = 'select * from goods;'
        self.execute_sql(sql)

    def show_cates(self):
        sql = 'select name from goods_cates;'
        self.execute_sql(sql)

    def show_brands(self):
        sql = 'select name from goods_brands;'
        self.execute_sql(sql)

    @staticmethod
    def print_menu():
        print("----京东商城----")
        print("1: 所有的商品")
        print("2: 所有的商品分类")
        print("2: 所有的商品品牌分类")
        num = input("请输入功能对应的序号：")
        return num

    def run(self):
        while True:
            num = self.print_menu()
            if num == "1":
                # 查询所有商品
                self.show_all_items()
                pass
            elif num == "2":
                # 查询分类
                self.show_cates()
                pass
            elif num == "3":
                # 查询品牌分类
                self.show_brands()
            else:
                print("输入有误，重新输入...")

def main():
    # 1.创建一个京东商城对象
    jd = JD()

    # 2.调用这个对象的run方法
    jd.run()

if __name__ == '__main__':
    main()

