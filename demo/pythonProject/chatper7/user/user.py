from flask import Flask, Blueprint, render_template

# 创建 Flask 应用实例
app = Flask(__name__)

# 创建蓝图
admin_bp = Blueprint('admin', __name__, template_folder='templates', url_prefix='/admin')
print(admin_bp.root_path)  # 打印蓝图的根路径


# 定义全局函数
def admin_greet(name):
    return f"Hello Admin, {name}!"


# 为蓝图注册全局函数
admin_bp.add_template_global(admin_greet, name='admin_greet')


# 蓝图路由
@admin_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')  # 渲染蓝图模板


# 注册蓝图
# app.register_blueprint(admin_bp, url_prefix='/admin')

# 根路由
@app.route('/user')
def index():
    return "Welcome to the main app!"


if __name__ == "__main__":
    app.run()
