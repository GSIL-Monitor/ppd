'''
整理下发标相关，listing 到底落在了mysql的哪个表
userid%128
'''
1111

userids = [50183939,50184057]

a = {}

for userid in userids:
    tableid = str(userid % 128)
    table_name = 'loan_' + tableid
    a[userid] = table_name

print(a)


