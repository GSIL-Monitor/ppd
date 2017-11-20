# -*- coding: utf-8 -*-

'''
已知userid，插入多个信用卡信息
并打印出该userid下的所有信用卡

可抓包获取userid ，也可查看server库
根据phone 查看userid（sqlserver 20库）
SELECT * from ppdai_user.dbo.UserDetails where MobilePhone = '13774275220'

'''

import pymysql
from dbconnect import test_mysql


userid = 50184057
# userid = 50184046

db = userid %3

table = userid%10

print(db)
print(table)

myconnect_db = 'ppdai_creditpay_%d' % db

insert_info= "INSERT INTO creditbank_accounts_%d VALUES(0,%d,'','梁家辉','6225820000001234',1,10000,0,1,'','2030-01-01 00:00:00','2017-05-22 11:02:55','2017-05-22 11:02:55',1)" % (table,userid)

select_info = "select * from creditbank_accounts_%d where userid =%d " % (table,userid)

db = test_mysql(myconnect_db)
cur = db.cursor()

cur.execute(insert_info)
cur.execute(select_info)

data = cur.fetchall()

db.commit()

# print(data)



for i in data:
    print(i)
