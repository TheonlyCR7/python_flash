import pymysql

# 建立连接
conn = pymysql.connect(
    host = "192.168.101.62",
    port = 3306,
    user = 'root',
    password= 'root',
    database= 'flask_db',
    charset= 'utf8'
)

# 执行sql语句
sql = "select * from user"
# 实例化一个游标对象
cursor = conn.cursor()
cursor.execute(sql)
# 获取查询结果
result = cursor.fetchall()
print(result)
# 还可以单独打印
for row in result:
    print(row)
# 只打印某一列的数据
for row in result:
    print(row[1])
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
