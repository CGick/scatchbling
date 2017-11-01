from rest_framework import serializers
from backscratchers.models import BackScratcher

class BackScratcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackScratcher
        fields = ('name', 'description', 'size', 'price')
