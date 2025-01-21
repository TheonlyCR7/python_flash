import pymysql
from pymysql.cursors import DictCursor



class MyORM:
    def __init__(self):

        # 建立连接
        conn = pymysql.connect(
            host = "192.168.101.63",
            port = 3306,
            user = 'root',
            password= 'root',
            database= 'flask_db',
            charset= 'utf8',
            cursorclass=DictCursor,  # 使用字典游标
            autocommit=True
        )
        cursor = conn.cursor()
        self.cursor = cursor
        # return self.cursor

    def query_user_all(self):
        sql = "select * from user"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def execute(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

class user:
    table_name = "user"
    def query_all(self):
        sql = "select * from %s" % self.table_name
        return MyORM().execute(sql)
    def query_one(self):
        sql = "select * from %s limit 1" % (self.table_name)
        return MyORM().execute(sql)

if __name__ == '__main__':
    my_orm = MyORM()
    result = my_orm.query_user_all()
    # print(result)
    user = user()
    user_result = user.query_one()
    print(user_result)


        # # 关闭游标
        # cursor.close()
        # # 关闭连接
        # conn.close()
