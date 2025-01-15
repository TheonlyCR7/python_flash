import os

from flask import Blueprint, request, session
from flask import Flask, make_response, request, session
import datetime
from datetime import timedelta

# app = Flask(__name__)
# 创建蓝图实例
user_bp = Blueprint('user', __name__, url_prefix='/user')
# app.config['SECRET_KEY'] = 'a_fixed_secret_key'

# @user_bp.before_request
# def before():
#     if request.path.startswith("/user/v"):
#         pass
#     # elif session.get("islogin"):
#     #     pass
#     else:
#         return "请登录"

# 定义路由
@user_bp.route('/v/login')
def login():
    # session["islogin"] = True
    print("login")
    return "User login page"

@user_bp.route('/logout')
def logout():
    # session.pop("islogin", None)
    return "User logout page"

@user_bp.route("/info")
def info():
    return "User info page"

@user_bp.route("/throwerror")
def throwError():
    raise Exception("User error")
    return "查看用户信息"
