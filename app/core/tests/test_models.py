from django.test import TestCase

from django.contrib.auth import get_user_model

from core import models

'''Test email and password vars'''
email='test@test.com'
password='pass123'

def create_sample_user(email=email, password=password):
    """Create a sample user"""
    return get_user_model().objects.create_user(email,password)
class ModelTests(TestCase):

    def test_create_user(self):
        """Test to create a new user with email"""        
        user = get_user_model().objects.create_user(
            email,
            password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password),)

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(email ,"test123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email,
            password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=create_sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

