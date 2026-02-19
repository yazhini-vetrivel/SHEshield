from rest_framework import serializers
from .models import UnsafeArea

class UnsafeAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnsafeArea
        fields = '__all__'
