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
def login():
    result = db_session.query(User).all()
    request_data = request.data
    request_data = json.loads(request_data)
    print(request_data)
    user_input_name = request_data["username"]
    user_input_password = request_data["password"]
    print(user_input_name, user_input_password)
    result = db_session.query(User).filter(User.username==user_input_name).first()
    print(result)
    result = db_session.query(User.username, User.password).filter_by(username=user_input_name, password=user_input_password).first()
    # print(result.username)
    if result:
    	return "登陆成功"
    return "用户名不存在"



if __name__ == '__main__':
    app.run()

