from flask import Blueprint, render_template

index5 = Blueprint('index5', __name__, template_folder='templates', url_prefix='/index5')


@index5.context_processor
def my_context_processor():
    def add_index5(a, b):
        return a+b
    return {"add5":add_index5}

# 定义蓝图内的路由
@index5.route('/')
def index():
    return render_template("index4.html")