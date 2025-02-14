import pytest
from flask import Flask
from app.app import create_app
from common.database import db_connect

@pytest.fixture
def app():
    app = create_app()
    db_session, Base, engine = db_connect()
    Base.metadata.create_all(engine)
    yield app
    Base.metadata.drop_all(engine)

@pytest.fixture
def client(app):
    return app.test_client()

def test_user_registration_success(client):
    response = client.post('/reg', json={
        'username': 'testuser@example.com',
        'password': 'password123',
        'second_password': 'password123',
        'ecode': '123456'
    })
    assert response.status_code == 200
    assert response.json['status'] == 1000
    assert response.json['data'] == 'Registration successful'


def test_registration_with_valid_code(client, redis_client):
    # 步骤1：请求发送验证码
    test_email = "test@example.com"
    client.post('/ecode', json={'email': test_email})

    # 步骤2：从Redis获取实际生成的验证码
    stored_code = redis_client.get(f'email:{test_email}')
    print("stored_code:", stored_code)
    # 步骤3：使用正确验证码注册
    response = client.post('/reg', json={
        'username': test_email,
        'password': 'ValidPass123!',
        'second_password': 'ValidPass123!',
        'ecode': stored_code.decode('utf-8')
    })

    assert response.status_code == 200
    assert response.json['status'] == 1000
    assert '用户注册成功' in response.json['data']



def test_user_registration_password_mismatch(client):
    response = client.post('/reg', json={
        'username': 'testuser@example.com',
        'password': 'password123',
        'second_password': 'password124',
        'ecode': '123456'
    })
    assert response.status_code == 200
    assert response.json['status'] != 1000
    assert response.json['data'] == 'Passwords do not match'

def test_user_registration_invalid_email(client):
    # response = client.post('/reg', json={
    response = client.post('/redis/reg', json={
        'username': 'invalid-email',
        'password': 'password123',
        'second_password': 'password123',
        'ecode': '123456'
    })
    assert response.status_code == 200
    assert response.json['status'] != 1000
    assert response.json['data'] == 'Invalid email format'