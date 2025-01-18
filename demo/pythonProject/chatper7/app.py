from flask import Flask, Blueprint, render_template

app = Flask(__name__, template_folder='templates')
print(app.template_folder)  # 打印应用全局的模板路径


def fun(num):
    return num + 1

app.add_template_filter(fun, 'add')

@app.route('/')
def index():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run()
