# -*- coding: utf-8 -*-

'''

sqlserver 连接方式 暂停！


已知userid，插入额度, userid 为关键字 只能插入一次
insert into ppdai_RiskControl_pisk.dbo.AppCreditcardAmount (UserId,Amount,InsertTime,UpdateTime,IsActive) values(50183939,20000,'2017-05-02 10:14:26','2017-05-02 10:14:26',1)

select top 10 * from ppdai_RiskControl_pisk.dbo.AppCreditcardAmount where UserId = 50183939

'''

import pymysql
from dbconnect import test_sqlserver_19

userid = 50184057

def add_creditcardAmount(userid):
    db = ' ppdai_RiskControl_pisk.dbo'
    db_connect = test_sqlserver_19(db)

    cur = db.cursor()

    insert_info = "insert into ppdai_RiskControl_pisk.dbo.AppCreditcardAmount (UserId,Amount,InsertTime,UpdateTime,IsActive) values(%d,30000,'2017-05-02 10:14:26','2017-05-02 10:14:26',1)" % userid
    update_info = " update ppdai_RiskControl_pisk.dbo.AppCreditcardAmount set Amount = 50000 where UserId = %d " % userid

    select_info = "select top 10 * from ppdai_RiskControl_pisk.dbo.AppCreditcardAmount where UserId = %d" % userid


    cur.execute(update_info)
    cur.execute(select_info)

    data = cur.fetchall()

    db.commit()
    return  data
add_creditcardAmount(userid)