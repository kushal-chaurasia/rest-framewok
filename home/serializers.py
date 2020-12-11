from rest_framework import fields, serializers
from .models import Card


class CardSerializers(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ('transaction', 'number')
       
