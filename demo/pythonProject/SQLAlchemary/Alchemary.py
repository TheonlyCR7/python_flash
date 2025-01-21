from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["post"])
def login():
    return "登陆成功"

if __name__ == '__main__':
    app.run()

