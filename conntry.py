
import pymssql


conn = pymssql.connect(host = '172.17.0.19',port = 'XXXX',user = 'XXXX',
                       password = 'XXXX',database = 'XXXX',charset = 'utf8')

sql = "SELECT listingId ,* FROM ppdai.dbo.Listing WITH(NOLOCK) WHERE BorrowerID=50183939 AND StatusID IN(1,2,172)"

cursor = conn.cursor()

list = cursor.execute(sql)
getlist = cursor.fetchall()
for row in getlist:
    print(row)
