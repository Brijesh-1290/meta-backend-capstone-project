from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Menu, Booking
from .serializers import BookingSerializer, MenuSerializer
from rest_framework import generics
from rest_framework import viewsets


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
