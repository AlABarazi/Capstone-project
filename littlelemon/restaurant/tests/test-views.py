from django.test import TestCase
from django.urls import reverse
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from rest_framework.test import APIClient
import json

class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(name="Menu1", description="Description 1")
        MenuItem.objects.create(name="Menu2", description="Description 2")

    def test_getall(self):
        client = APIClient()
        response = client.get(reverse('menu-list'))
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)