import pymysql
from pymysql.cursors import DictCursor

# 建立连接
conn = pymysql.connect(
    host = "192.168.101.62",
    port = 3306,
    user = 'root',
    password= 'root',
    database= 'flask_db',
    charset= 'utf8',
    cursorclass=DictCursor  # 使用字典游标
)

# 执行sql语句
sql = "select * from user"
# 实例化一个游标对象
cursor = conn.cursor()
cursor.execute(sql)
# 获取查询结果
result = cursor.fetchall()

for row in result:
    print(row["username"])
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
