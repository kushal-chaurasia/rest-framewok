from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Card
from .serializers import CardSerializers

class CardList(APIView):

    def get(self, request):
        card_detail = Card.objects.all()
        serializer = CardSerializers(card_detail, many = True)
        return Response(serializer.data)

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        expiry = request.POST['expiry']
        cvv = request.POST['cvv']
        card = Card(name = name, number = number, expiry = expiry, cvv = cvv)
        card.save()
    return render(request, 'index.html')