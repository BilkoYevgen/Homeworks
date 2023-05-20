from django.test import TestCase
from .models import User

class UserTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(first_name='Yevgen', last_name='Bilko', age=28)

    def test_create_user(self):
        self.assertTrue(self.user is not None)

    def test_allowed_user(self):
        resp = self.client.get(f'/api/users/{self.user.id}/')
        self.assertEqual(resp.status_code, 200)

    def test_delete_user(self):
        resp = self.client.delete(f'/api/users/{self.user.id}/')
        self.assertEqual(resp.status_code, 204)