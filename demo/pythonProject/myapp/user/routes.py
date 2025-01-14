from flask import Blueprint

# 创建蓝图实例
user_bp = Blueprint('user', __name__, url_prefix='/user')

# 定义路由
@user_bp.route('/login')
def login():
    return "User login page"

@user_bp.route('/logout')
def logout():
    return "User logout page"
