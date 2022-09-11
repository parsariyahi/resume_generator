from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from user.models import User

class UserJWTAuthTest(TestCase):
    
    # def setUp(self) -> None:
    #     pass

    def test_register_user(self):
        """
        check '{HOST}/api/auth/register/',
        for registering a user
        """
        data = {
            'username': 'test',
            'full_name': 'test',
            'email': 'test@gmail.com',
            'phone_number': '09909877878',
            'password': 'test',
        }
        url = reverse('register')

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_user_whitout_password(self):
        """
        check '{HOST}/api/auth/register/',
        for registering a user with password=None
        """
        data = {
            'username': 'test',
            'full_name': 'test',
            'email': 'test@gmail.com',
            'phone_number': '09909877878',
        }
        url = reverse('register')

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
