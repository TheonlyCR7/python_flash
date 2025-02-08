# tests/test_integration.py
import pytest
from app import create_app
from app.config.config import config
from app.settings import env
from common.response_message import UserMessage, ArticleMessage

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_user_login_and_article_publish(client):
    # 测试用户登录
    login_data = {
        "username": "test@example.com",
        "password": "password123"
    }
    login_response = client.post('/redis/login', json=login_data)
    assert login_response.status_code == 200
    assert login_response.json['status'] == 1000
    assert login_response.json['data'] == "登录成功！"

    # 测试文章发布
    article_data = {
        "title": "Test Article",
        "article_content": "This is a test article.",
        "drafted": 1,
        "label_name": "recommend",
        "article_tag": "test",
        "article_type": "original"
    }
    article_response = client.post('/article/save', json=article_data)
    assert article_response.status_code == 200
    assert article_response.json['status'] == 2003
    assert article_response.json['data'] == "文章保存成功！"
