import hashlib
import json

from flask import Flask, request
from sqlalchemy import create_engine, Table
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


@app.route("/", methods=["post"])
def register():
    result = db_session.query(User).all()
    request_data = request.data
    request_data = json.loads(request_data)
    # print(request_data)
    username = request_data["username"]
    password = request_data["password"]

    password = hashlib.md5(password.encode()).hexdigest()
    nickname = request_data["nickname"]
    picture = request_data["picture"]
    insert_data = {
        "username": username,
        "password": password,
        "nickname": nickname,
        "picture": picture
    }
    user = User(**insert_data)
    db_session.add(user)
    # 提交
    db_session.commit()

    return "注册成功"


if __name__ == '__main__':
    app.run()

