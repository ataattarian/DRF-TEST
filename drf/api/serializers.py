from rest_framework import serializers
from .models import test

class testserializer(serializers.ModelSerializer):
    class Meta:
        model = test
        fields = '__all__'
        