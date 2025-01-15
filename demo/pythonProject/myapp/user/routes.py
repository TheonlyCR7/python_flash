
from flask import Blueprint

# 创建蓝图实例
user_bp = Blueprint('user', __name__, url_prefix='/user')

# 定义路由
@user_bp.route('/v/login')
def login():
    print("login")
    return "User login page"

@user_bp.route('/logout')
def logout():
    return "User logout page"

@user_bp.route("/info")
def info():
    return "User info page"

@user_bp.route("/throwerror")
def throwError():
    raise Exception("User error")
    return "查看用户信息"
