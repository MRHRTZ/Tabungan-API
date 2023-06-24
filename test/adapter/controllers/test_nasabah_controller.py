import unittest
from app.core.entity.nasabah import CreateNasabah
from app.adapters.controllers.nasabah_controller import NasabahController

class TestUserController(unittest.TestCase):
    def setUp(self):
        self.nasabah_controller = NasabahController()

    def test_create_nasabah(self):
        user_data = {'nama': 'John doe', 'nik': '12345678910', 'no_hp': '0812345678'}
        nasabah = CreateNasabah(**user_data)
        result = self.nasabah_controller.create_nasabah(nasabah)
        self.assertEqual(result['status'], 200)

    def test_save_money(self):
        pass
