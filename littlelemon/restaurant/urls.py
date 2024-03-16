from django.urls import path
from .views import menuview, bookingview, SingleMenuItemView, msg
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
path( 'menu/', menuview.as_view()),
path('menu/<int:pk>', SingleMenuItemView.as_view()),
path('booking/', bookingview.as_view()),
path('message/', msg),
path('api-token-auth/', obtain_auth_token), # get access token programatically from APIs. POST request so work only using postman or such
]