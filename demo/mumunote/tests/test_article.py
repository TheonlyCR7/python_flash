# tests/test_article.py
import pytest
from app.app import create_app
from app.config.config import config
from app.settings import env
from common.response_message import ArticleMessage

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_article_save(client):
    # 测试文章保存
    data = {
        "title": "Test Article",
        "article_content": "This is a test article.",
        "drafted": 0,
        "label_name": "recommend",
        "article_tag": "test",
        "article_type": "original"
    }
    response = client.post('/article/save', json=data)
    assert response.status_code == 200
    assert response.json['status'] == 2003
    assert response.json['data'] == "文章保存成功！"
