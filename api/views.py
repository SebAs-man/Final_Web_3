from rest_framework import viewsets

from api.models import Carta
from api.serial import CartaSerializer


class CartaViewSet(viewsets.ModelViewSet):
    queryset = Carta.objects.all().order_by('name')
    serializer_class = CartaSerializer
