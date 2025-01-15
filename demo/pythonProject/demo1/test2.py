import os

from flask import Flask, request, abort, session

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.before_request
def before_request():
    url = request.path
    print(url)
    # 白名单
    pass_path = ['/', '/login', 'reg']
    # 后缀名进行放行
    suffix = url.endswith("png") or url.endswith("jpg") or url.endswith("jpeg") or url.endswith("js")

    if url in pass_path or suffix:
        # return "登录成功，放行"
        pass
    else:
        if_login = session.get("islogin")
        if not if_login: # 检查是否已经登录
            return "请登录"

@app.route('/login')
def index():
    session["islogin"] = True
    return "登录成功"

@app.route('/home')
def home():
    return "欢迎访问首页"

if __name__ == "__main__":
    app.run()
