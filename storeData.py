#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def store_discount(discount_dict):
    sql = "INSERT INTO discount VALUES (NULL, '" + discount_dict['bank'] + "', '" + discount_dict['summary'] + "', '" + discount_dict['description'] \
          + "', '" + discount_dict['begin_time'] + "', '" + discount_dict['end_time'] + "', '" + discount_dict['area'] + "', '" + discount_dict['discount_usage'] \
          + "', '" + discount_dict['discount_detail'] + "', '" + discount_dict['type'] + "', '" + discount_dict['Characteristic'] + "')"
    sql = sql.encode('utf-8')
    print sql
    db = MySQLdb.connect("localhost", "root", "abyjun", "dealbridge")
    cursor = db.cursor()

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except Exception,e:
        # Rollback in case there is any error
        print e
        db.rollback()


    db.close()
