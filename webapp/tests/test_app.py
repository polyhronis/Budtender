import unittest
from webapp.app import app, correct_errors, start_webapp

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_start_webapp(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_correct_errors(self):
        result = correct_errors()
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()