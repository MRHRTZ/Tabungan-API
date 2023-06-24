import unittest
from app.adapters.controllers.user_controller import UserController

class TestUserController(unittest.TestCase):
    def setUp(self):
        self.user_controller = UserController()

    def test_create_user(self):
        user_data = {'user_id': 1, 'name': 'John Doe', 'email': 'john@example.com'}
        result = self.user_controller.create_user(user_data)
        self.assertEqual(result['message'], 'User created successfully')

    def test_get_user(self):
        user_id = 1
        result = self.user_controller.get_user(user_id)
        # Lakukan pengujian terhadap hasil yang