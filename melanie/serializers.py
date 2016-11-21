from rest_framework import serializers
from .models import Mole

class MoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mole
        fields = '__all__'

    def create(self, validated_data):
        return Mole.objects.create(**validated_data)