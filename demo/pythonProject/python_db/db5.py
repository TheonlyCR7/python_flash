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


class Model:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    # 链式操作来指定查询的列
    def field(self, select_params):
        self.columns = ','.join(select_params)
        return self

    def query(self, **where_params):
        table = self.__class__.__getattribute__(self, 'table_name')
        if hasattr(self, 'columns'):
            sql = 'select %s from %s' % (self.columns, table)
        else:
            sql = 'select * from %s' % table
        if where_params:
            sql = sql + " where "
            for k,v in where_params.items():
                sql = sql + "%s='%s' and " % (k,v)
            sql += ' 1=1 limit 1'
            print(sql)
        else:
            pass
            # sql = "select * from %s limit 1" % table
        return MyORM().execute(sql)

class User(Model):
    table_name = "user"

    def __init__(self, **kwargs):  # 不知道传参数量时
        for k,v in kwargs.items():
            self.__setattr__(k, v)
        # print(self.__dict__)

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
    user = User()
    # result = user.field(['username', 'nickname']).query() # 查询某一列
    # result = user.field(['username', 'nickname']).query(user_id=3)  # 查询某一列
    result = user.query(user_id=3) # 查询某一行
    print(result)