import pytest
from app.app import create_app
from common.database import db_connect
from common.redisdb import redis_connect
from selenium import webdriver

# test_db_connect = db_connect()
# base = test_db_connect.Base

@pytest.fixture(scope='session')
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin1:123@192.168.101.71:3306/flask_db'
    return app

@pytest.fixture(scope='function')
def client(app):
    return app.test_client()

@pytest.fixture(scope='function')
def db_session():
    session, Base, engine = db_connect()
    Base.metadata.create_all(engine)
    yield session
    session.rollback()
    Base.metadata.drop_all(engine)

@pytest.fixture(scope='function')
def redis_client(client):
    client = redis_connect()
    client.flushdb()
    yield client
    client.flushdb()

@pytest.fixture
def selenium_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def mock_email_send(monkeypatch):
    """Mock邮件发送逻辑，仅记录发送行为不实际发送"""
    sent_codes = {}

    def mock_send(email, code):
        sent_codes[email] = code

    # Mock原始发送函数
    monkeypatch.setattr('common.email_utils.send_email', mock_send)

    # 暴露给测试用例访问
    return sent_codes


@pytest.fixture
def captured_code(mock_email_send):
    """获取被Mock捕获的验证码"""
    return mock_email_send