import unittest
from app.app import create_app

class MainTestCase(unittest.TestCase):
    def test_app_creation(self):
        app = create_app()
        self.assertIsNotNone(app)

if __name__ == '__main__':
    unittest.main()
