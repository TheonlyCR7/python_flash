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

class table_sql:

    def __init__(self, **kwargs):  # 不知道传参数量时
        for k,v in kwargs.items():
            self.__setattr__(k, v)
        print(self.__dict__)

    def insert(self):
        keys = []
        values = []
        for k,v in self.__dict__.items():
            keys.append(k)
            values.append(v)
        sql = "insert into %s(%s) values('%s')" % (self.table_name, ",".join(keys[1:]), "','".join(values[1:]))
        print(sql)
        return MyORM().execute(sql)


if __name__ == '__main__':

    user = table_sql(table_name='user',
                    username='dazhaolaoshi',
                     password='123',
                     nickname="达州老师",
                     picture="1.jpg",
                     job="全栈工程师")
    user.insert()
