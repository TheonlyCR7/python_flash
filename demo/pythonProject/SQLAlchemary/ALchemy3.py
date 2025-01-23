import hashlib
import json

from flask import Flask, request
from sqlalchemy import create_engine, Table, or_
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

app = Flask(__name__)

# 创建一个引擎，目的是连接到我们的数据库上
engine = create_engine("mysql+pymysql://root:root@192.168.101.63:3306/flask_db", echo=True)
# 打开数据库的连接会话
session = sessionmaker(engine)
# 保证线程安全
db_session = scoped_session(session)
# 获取基类
Base = declarative_base()

class User(Base):
    __table__ = Table("user", Base.metadata, autoload_with=engine)

class Article(Base):
    __table__ = Table("article", Base.metadata, autoload_with=engine)


@app.route("/", methods=["post"])
def my_article():
    username = request.args.get("username")
    all_article = db_session.query(User, Article).filter(User.user_id==Article.user_id).filter(User.username==username).all()
    print(all_article)
    for user,article in all_article:
        print(user)
        print(user.username)

    return "ok"



if __name__ == '__main__':
    app.run()

