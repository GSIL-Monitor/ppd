'''
尝试连接sqlserver
搞定
踩了2个坑，一个是port，需要加port，sqlserver要port
另一个是DB：ppdai.dbo，将dbo去掉就可以了
'''

import pymssql


class MSSQL:
    def __init__(self, host,port, user, password, database,charset):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = password
        self.db = database
        self.charset = charset



    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host, port=self.port,user=self.user, password=self.pwd, database=self.db, charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def ExecQuery(self, sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        调用示例：
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        # 查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        """
        执行非查询语句

        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

def main():
## ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
## #返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
## ms.ExecNonQuery("insert into WeiBoUser values('2','3')")

    ms = MSSQL(host = 'xxxxx',port = 'xxxxx',user = 'xxxxx',
                       password = 'xxxxxx',database = 'xxxxx',charset = 'utf8')

    resList = ms.ExecQuery("SELECT listingId ,* FROM ppdai.dbo.Listing WITH(NOLOCK) WHERE BorrowerID=50183939 AND StatusID IN(1,2,172)")

    for row in resList:
        print(row)

if __name__ == '__main__':
    main()
