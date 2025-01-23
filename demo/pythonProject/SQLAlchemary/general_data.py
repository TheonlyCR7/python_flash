import random
import string
from sqlalchemy import create_engine, Table
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from datetime import datetime

# 设置数据库连接
engine = create_engine("mysql+pymysql://root:root@192.168.101.63:3306/flask_db", echo=True)
session = sessionmaker(engine)
db_session = scoped_session(session)
Base = declarative_base()

# 定义Article表
class Article(Base):
    __table__ = Table("article", Base.metadata, autoload_with=engine)

# 生成随机邮箱
def generate_random_email():
    domain = random.choice(['example.com', 'test.com', 'mail.com'])
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{username}@{domain}"

# 插入数据
def insert_articles():
    for i in range(100):
        article_id = i + 1
        user_id = generate_random_email()  # 生成随机邮箱作为 user_id
        ipaddr = f"192.168.1.{i+1}"  # 示例 IP 地址
        context = f"This is article number {i+1}."  # 示例内容
        create_time = datetime.now()
        update_time = datetime.now()

        # 创建并保存文章实例
        article = Article(
            article_id=article_id,
            user_id=user_id,
            ipaddr=ipaddr,
            context=context,
            create_time=create_time,
            update_time=update_time
        )
        db_session.add(article)

    # 提交事务
    db_session.commit()
    print("100 articles inserted successfully!")

# 执行插入操作
if __name__ == "__main__":
    insert_articles()
