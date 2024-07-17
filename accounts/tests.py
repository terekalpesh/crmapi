from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import CustomUser

class CustomUserModelTest(TestCase):
    
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User',
            phone='1234567890',
            address='123 Test Street',
            city='Test City',
            state='Test State',
            country='Test Country',
            pincode='123456'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')
        self.assertEqual(self.user.phone, '1234567890')
        self.assertEqual(self.user.address, '123 Test Street')
        self.assertEqual(self.user.city, 'Test City')
        self.assertEqual(self.user.state, 'Test State')
        self.assertEqual(self.user.country, 'Test Country')
        self.assertEqual(self.user.pincode, '123456')

    def test_get_full_name(self):
        self.assertEqual(self.user.get_full_name(), 'Test User')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser@example.com')

