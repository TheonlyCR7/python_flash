from flask import Flask
from user.routes import user_bp
from order.routes import order_bp

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(user_bp)
app.register_blueprint(order_bp)

@app.errorhandler(404)
def page_not_found(error):
    print(error)
    return "User page not found 404", 404

@app.errorhandler(500)
def internal_server_error(error):
    print(error)
    return "User internal server error 500", 500

if __name__ == "__main__":
    app.run()
