from flask import Flask, make_response, request, session, render_template
from controller.index5 import index5
app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = 'jinja2'

app.register_blueprint(index5)

from controller.index6 import index6
app.register_blueprint(index6)

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/index1')
def index1():
    return "<strong>Hello, World!</strong>"


@app.route('/index2')
def index2():
    with open("templates/index.html") as f:
        html = f.read()
    return html


@app.route('/index3')
def index3():
    return render_template("index3.html")


@app.route('/index4')
def index4():
    countdown_start = 3  # 倒计时的初始值（可以动态修改）
    return render_template('index3.html', countdown_start=countdown_start)


@app.route('/index7')
def index5():
    session['username'] = 'LMC'
    # article = {
    #     'title': 'Flask',
    #     'count': 10,
    #     'content': '<strong>Flask is a micro web framework written in Python.</strong>'
    # }
    # return render_template('index4.html', article=article)
    return render_template('index4.html')


@app.template_filter('add')
def add(input):
    return input + 1


@app.context_processor
def my_context_processor():
    article = {
        'title': 'Flask',
        'count': 10,
        'content': '<strong>Flask is a micro web framework written in Python.</strong>'
    }
    # 返回一个包含article的字典，使其在所有模板中可用
    return dict(article=article)

@app.context_processor
def my_context_processor2():
    def fun(num):
        return num * num
    # 返回一个包含article的字典，使其在所有模板中可用
    return dict(my_add=fun)


def add_fun(input):
    return input + 1


app.jinja_env.globals.update(add_fun=add_fun)

if __name__ == "__main__":
    app.run()
