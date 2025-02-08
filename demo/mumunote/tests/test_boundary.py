# tests/test_boundary.py
import pytest
from app.app import create_app
from app.config.config import config
from app.settings import env
from common.response_message import UserMessage

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_user_register_password_length(client):
    # 测试密码长度为5（小于最小值6）
    data = {
        "username": "test@example.com",
        "password": "pass",
        "second_password": "pass",
        "ecode": "123456"
    }
    response = client.post('/redis/reg', json=data)
    assert response.status_code == 200
    assert response.json['status'] == 1002
    assert response.json['data'] == "密码长度必须大于等于6"

    # 测试密码长度为6（最小值）
    data = {
        "username": "test@example.com",
        "password": "password",
        "second_password": "password",
        "ecode": "123456"
    }
    response = client.post('/redis/reg', json=data)
    assert response.status_code == 200
    assert response.json['status'] == 1000
    assert response.json['data'] == "注册成功！"

    # 测试密码长度为20（最大值）
    data = {
        "username": "test@example.com",
        "password": "password1234567890",
        "second_password": "password1234567890",
        "ecode": "123456"
    }
    response = client.post('/redis/reg', json=data)
    assert response.status_code == 200
    assert response.json['status'] == 1000
    assert response.json['data'] == "注册成功！"

    # 测试密码长度为21（大于最大值20）
    data = {
        "username": "test@example.com",
        "password": "password12345678901",
        "second_password": "password12345678901",
        "ecode": "123456"
    }
    response = client.post('/redis/reg', json=data)
    assert response.status_code == 200
    assert response.json['status'] == 1002
    assert response.json['data'] == "密码长度必须小于等于20"
