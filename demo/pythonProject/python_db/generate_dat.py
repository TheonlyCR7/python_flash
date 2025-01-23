import pymysql
from faker import Faker

# 连接到数据库
connection = pymysql.connect(
    host="192.168.101.63",
    port=3306,
    user='root',
    password='root',
    database='flask_db',
    charset='utf8'
)

cursor = connection.cursor()

# 创建一个 Faker 实例
fake = Faker()

# 构建插入语句
sql = "INSERT INTO user (username, user_id, password, nickname, picture, job) VALUES (%s, %s, %s, %s, %s, %s)"
values = []

for i in range(100):
    username = fake.user_name()         # 生成一个用户名
    user_id = fake.email()              # 生成一个邮箱作为 user_id
    password = fake.password()          # 生成一个密码
    nickname = fake.first_name()        # 生成一个昵称
    picture = f"picture{i + 1}.jpg"    # 生成一个图片文件名
    job = fake.job()                    # 生成一个工作职务
    values.append((username, user_id, password, nickname, picture, job))

# 执行批量插入
cursor.executemany(sql, values)

# 提交事务
connection.commit()

# 关闭游标和连接
cursor.close()
connection.close()

print("100 records have been inserted.")
