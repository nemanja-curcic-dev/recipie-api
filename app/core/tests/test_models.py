from django.test import TestCase
from django.contrib.auth import get_user_model


class TestModels(TestCase):

    def test_create_user_with_email(self):
        """Test creating user with email"""
        email = 'nemanja.curcic@test.com'
        password = 'testpass123'

        user = get_user_model().objects.create_user(email=email,
                                                    password=password)

        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_normalized_email(self):
        """Creating user and normalizing his email address"""
        email = 'nemanja@TESTMAIL.com'
        password = 'testpass123'

        user = get_user_model().objects.create_user(email=email,
                                                    password=password)

        self.assertEquals(user.email, email.lower())

    def test_create_user_has_email(self):
        """User must provide email address"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None,
                                                 password='test123')

    def test_create_superuser(self):
        """Testing of creating a superuser"""
        user = get_user_model().objects.\
            create_super_user(email='test@mail.com',
                              password='test123')

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
