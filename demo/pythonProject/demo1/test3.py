from flask import Flask, jsonify, abort

app = Flask(__name__)

# 全局500错误处理器
@app.errorhandler(500)
def internal_server_error(error):
    # 可以记录日志，打印错误信息等
    print(f"捕获到 500 错误: {error}")
    return jsonify({"error": "服务器内部错误", "message": str(error)}), 500

# 定义一个路由，用于触发500错误
@app.route('/throwerror')
def throw_error():
    # 抛出一个示例异常，Flask会将其转化为 500 错误
    raise Exception("这是一个模拟的500错误")
    return "这行不会被执行"  # 由于上面抛出异常，这行不会执行

# 定义一个正常的路由
@app.route('/')
def index():
    return "欢迎来到 Flask 应用!"

if __name__ == "__main__":
    app.config['SECRET_KEY'] = 'a_fixed_secret_key'
    app.run()
