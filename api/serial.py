from rest_framework import serializers

from api.models import Carta


class CartaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carta
        fields = '__all__'
