from rest_framework import serializers
from . models import Supers

class supersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['alter_ego', 'primary_ability', 'secondary_ability', 'catch_phrase', 'super_type', 'super_type_id']
        depth = 1

    super_type_id =serializers.IntegerField(write_only=True)