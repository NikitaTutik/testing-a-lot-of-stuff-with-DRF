from rest_framework import serializers
from .models import Cars


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ['id', 'car_brand', 'car_model', 'year_of_production', 'car_body', 'engine_type']