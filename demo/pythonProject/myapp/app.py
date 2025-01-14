from flask import Flask
from user.routes import user_bp
from order.routes import order_bp

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(user_bp)
app.register_blueprint(order_bp)

if __name__ == "__main__":
    app.run(debug=True)
