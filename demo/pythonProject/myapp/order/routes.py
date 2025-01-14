from flask import Blueprint

# 创建蓝图实例
order_bp = Blueprint('order', __name__, url_prefix='/order')

# 定义路由
@order_bp.route('/list')
def order_list():
    return "Order list page"

@order_bp.route('/detail/<int:order_id>')
def order_detail(order_id):
    return f"Order detail page for order {order_id}"
