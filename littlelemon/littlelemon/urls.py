"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, views
from restaurant.views import BookingViewSet, UserViewSet, MenuItemsView
router = routers.DefaultRouter()

router.register(r'booking', BookingViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
path('admin/', admin.site.urls),
path('api/', include('restaurant.urls')), # api/menu
path('', include(router.urls)),
path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
path('restaurant/',include('restaurant.urls')), # restaurant/menu
path('restaurant/booking/', include(router.urls)),
path('auth/', include('djoser.urls')), 
path('auth/', include('djoser.urls.authtoken')) # # To login, visit the djoser generated URL http://127.0.0.1:8000/auth/token/login/. # Enter the username and password to obtain the token.
# first creat user using admin -> use http://127.0.0.1:8000/auth/token/login/ then enter the user name and pass that you created to get the auth token.
]

