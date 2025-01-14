import os

from flask import Flask, make_response, request, session
import datetime
from datetime import timedelta

app = Flask(__name__)

# 启动session
app.config['SECRET_KEY'] = os.urandom(24)
# 设置session的有效时间
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)
# 设置session的永久有效
# session.permanent = True
# 设置session的存储位置
app.config['SESSION_TYPE'] = 'filesystem'
# 设置cookie的属性
app.config['SESSION_COOKIE_NAME'] = 'session_cookie'
app.config['SESSION_COOKIE_SECURE'] = True



@app.route('/')
def hello_world():
    return 'Hello, World!1111222'

# 设置 cookie
@app.route('/cookie')
def cookie():
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 将 datetime 转为字符串
    response = make_response(f"Current time is: {time}")
    expires = datetime.datetime.now() + datetime.timedelta(days=1)
    response.set_cookie('username', 'LMC', expires=expires)
    response.set_cookie('sex', 'male')
    response.set_cookie('height', '180')
    return response

# 获取cookie
@app.route('/get_cookie')
def get_cookie():
    # cookie = request.cookies
    get_one = request.cookies.get('username')
    print(get_one)
    cookie_dict = request.cookies.to_dict()
    print(cookie_dict)
    return "获取cookie成功"

# 删除cookie
@app.route('/delete_cookie')
def delete_cookie():
    response = make_response("Cookie has been deleted")
    response.delete_cookie('username')
    # 删除所有
    cookie_dict = request.cookies.to_dict()
    for key in cookie_dict:
        response.delete_cookie(key)
    return response

@app.route('/check_cookie')
def check_cookie():
    username = request.cookies.get('username')
    if username:
        return f"Cookie is still valid: {username}"
    else:
        return "Cookie has expired or does not exist"

# 操作session
@app.route('/set_session')
def set_session():
    pass

# 增加session
@app.route("/add_session")
def add_session():
    session['username'] = 'LMC'
    session['logged_in'] = True
    username = session.get('username')

    return '添加session成功'

@app.route("/get_session")
def get_session():
    print(session)
    username = session.get('username')
    return "获取session成功" + username

@app.route("/delete_session")
def delete_session():
    session.pop('username')
    session.pop('logged_in')
    return "删除session成功"

@app.route("/clear_session")
def clear_session():
    session.clear()
    return "清空session成功"


if __name__ == "__main__":
    app.run()
