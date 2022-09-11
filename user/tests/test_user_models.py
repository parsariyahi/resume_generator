from django.test import TestCase

from user.models import User

class UserTest(TestCase) :
    
    def test_create_user_method(self) :
        """
        check 'User.objects.create_user' method,
        for creating normal user.
        """
        data = {
            'username': 'test',
            'full_name': 'test',
            'email': 'test@gmail.com',
            'phone_number': '09909877878',
            'password': 'test',
        }
        user = User.objects.create_user(**data)

        self.assertEqual(user.username, data['username'])
        self.assertNotEqual(user.password, data['password']) #user password should be hashed

    def test_create_user_password_error(self) :
        """
        creating user without password,
        should raise a 'ValueError' exception.
        """
        data = {
            'username': 'test',
            'full_name': 'test',
            'email': 'test@gmail.com',
            'phone_number': '09909877878',
        }

        self.assertRaises(ValueError, User.objects.create_user, **data)
