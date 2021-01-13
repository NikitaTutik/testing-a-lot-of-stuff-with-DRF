from rest_framework import serializers
from .models import CarSpecs


class CarSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpecs
        fields = ['id', 'car_plan', 'car_brand', 'car_model', 'year_of_production', 'car_body', 'engine_type']
        depth = 1