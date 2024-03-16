from rest_framework import serializers 
from .models import menu, booking, MenuItem
from django.contrib.auth.models import User
from rest_framework import serializers


        
class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = '__all__'
        
class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = '__all__'
        
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']