# tests/test_user.py
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

def test_user_register(client):
    # 测试用户注册
    data = {
        "username": "test@example.com",
        "password": "password123",
        "second_password": "password123",
        "ecode": "123456"
    }
    response = client.post('/redis/reg', json=data)
    assert response.status_code == 200
    assert response.json['status'] == 1000
    assert response.json['data'] == "注册成功！"
