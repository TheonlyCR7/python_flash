import unittest
from app.app import create_app
from model.user import User
from model.article import Article

class ControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app_context = self.app.app_context()
        self.app_context.push()
        from common.database import db_connect
        self.db_session, Base, engine = db_connect()
        Base.metadata.create_all(engine)
        self.client = self.app.test_client()

    def tearDown(self):
        self.db_session.remove()
        self.app_context.pop()

    def test_user_registration(self):
        response = self.client.post('/reg', json={
            'username': 'test@example.com',
            'password': 'password',
            'second_password': 'password',
            'ecode': '123456'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', response.json['data'])

    def test_article_post(self):
        user = User(username='test@example.com', password='password')
        self.db_session.add(user)
        self.db_session.commit()
        with self.client.session_transaction() as session:
            session['is_login'] = 'true'
            session['user_id'] = user.user_id
        response = self.client.post('/article/save', json={
            'title': 'Test Article',
            'article_content': 'This is a test article',
            'drafted': 1
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', response.json['data'])

if __name__ == '__main__':
    unittest.main()
