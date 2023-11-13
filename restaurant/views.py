from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

def index(request):
    return render(request, 'index.html', {})

# class BookingView(APIView):
#     def get(self, request):
#         items = Booking.objects.all()
#         serializer = BookingSerializer(items, many=True)
#         return Response(serializer.data)

# class MenuView(APIView):
#     def post(self, request):
#         serializer = MenuSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
