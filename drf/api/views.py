#from django.shortcuts import render
from rest_framework import viewsets
from .models import test
from .serializers import testserializer
# Create your views here.

class testview(viewsets.ModelViewSet):
    queryset = test.objects.all()
    serializer_class = testserializer