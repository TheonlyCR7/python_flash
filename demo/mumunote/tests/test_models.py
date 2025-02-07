import unittest
from app.app import create_app
from model.user import User
from model.article import Article

class ModelTestCase(unittest.TestCase):
    def setUp(self):
        # 创建测试应用
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app_context = self.app.app_context()
        self.app_context.push()
        # 初始化数据库
        from common.database import db_connect
        self.db_session, Base, engine = db_connect()
        Base.metadata.create_all(engine)

    def tearDown(self):
        # 清理数据库
        self.db_session.remove()
        self.app_context.pop()

    def test_user_creation(self):
        user = User(username='test@example.com', password='password')
        self.db_session.add(user)
        self.db_session.commit()
        self.assertIsNotNone(User.find_by_username('test@example.com'))

    def test_article_creation(self):
        user = User(username='test@example.com', password='password')
        self.db_session.add(user)
        self.db_session.commit()
        article = Article(title='Test Article', content='This is a test article', user_id=user.user_id)
        self.db_session.add(article)
        self.db_session.commit()
        self.assertIsNotNone(Article.find_article(1, 'recommend'))

if __name__ == '__main__':
    unittest.main()
