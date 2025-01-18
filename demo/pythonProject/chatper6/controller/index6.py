from flask import Blueprint, render_template

index6 = Blueprint('index6', __name__, template_folder='templates', url_prefix='/index6')

# 定义蓝图内的路由
@index6.route('/')
def index():
    return render_template("pre_index.html")

@index6.route('/index_1')
def index1():
    return render_template("article_index.html")