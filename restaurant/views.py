from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)

from .models import Menu, Booking
from .serializers import MenuSerializer , BookingSerializer
from rest_framework.viewsets import ModelViewSet
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(
    RetrieveUpdateAPIView,
    DestroyAPIView
):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer