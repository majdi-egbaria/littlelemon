from django.contrib.auth.models import User
from django.test import TestCase, Client
from rest_framework.test import APIClient

from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Create User test instance
        self.credentials = {'username': 'testuser', 'password': 'Pass@123'}
        User.objects.create_user(**self.credentials)
        # Create MenuItem test instances
        MenuItem.objects.create(title='IceCream', price=80, inventory=100)
        MenuItem.objects.create(title='Pizza', price=200, inventory=100)
        # Login user
        self.client.login(username='testuser', password='Pass@123')

    def test_getall(self):
        # Retrieve serialized MenuItem instances
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(data=items, many=True)
        serializer.is_valid()
        # Simulate api call
        response = self.client.get('/api/menu-items/')
        # Check if serialized data equals response
        self.assertEquals(serializer.data, response.json())
