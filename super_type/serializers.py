from rest_framework import serializers
from .models import SuperType

class SuperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['Hero', 'Villain']
        depth = 1
    
    SuperType_type_id = serializers.IntegerField(write_only=True)