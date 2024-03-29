from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

    def setUp(self):
        """Setup which runs before executing any tests"""
        self.client = Client()        
        self.admin_user = get_user_model().objects.create_superuser(
            email= 'admin@test.com',
            password= 'test123'
        )        
        self.client.force_login(self.admin_user)        
        self.user = get_user_model().objects.create_user(
            email= 'test@test.com',
            password='test123',
            name='Test Name'
            )

    def test_list_users(self):
        """ Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.name)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change',args= [self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code,200)

    def test_add_user_page(self):
        """Test that the add user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code,200)