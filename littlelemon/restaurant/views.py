from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import booking, menu, MenuItem
from .serializers import bookingSerializer, menuSerializer, UserSerializer, MenuItemSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
class bookingview(APIView):
    def get(self, request) :
        items = booking.objects.all()
        # to json or xml you need seriliazer 
        serializer = bookingSerializer (items, many= True)
        return Response(serializer.data) # Return
    def post(self, request) :
        serializer = bookingSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data":serializer.data})
        

    
class menuview(APIView):
    def get(self, request) :
        items = menu.objects.all()
        # to json or xml you need seriliazer 
        serializer = bookingSerializer (items, many= True)
        return Response(serializer.data) # Return
    def post(self, request) :
        serializer = menuSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data":serializer.data})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = booking.objects.all()
    serializer_class = bookingSerializer