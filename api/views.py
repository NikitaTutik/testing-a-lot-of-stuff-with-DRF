from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import CarSpecsSerializer
from .models import CarSpecs, CarPlan


class CarSpecsViewset(viewsets.ModelViewSet):
    serializer_class = CarSpecsSerializer

    def get_queryset(self):
        cars = CarSpecs.objects.all()
        return cars

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        params_list = params['pk'].split('-')
        cars = CarSpecs.objects.filter(car_brand=params_list[0], car_model=params_list[1])
        serializer = CarSpecsSerializer(cars, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
            car_data = request.data
            new_car = CarSpecs.objects.create(car_plan=CarPlan.objects.get(id=car_data['car_plan']), car_brand=car_data['car_brand'], car_model=car_data['car_model'],
                                              year_of_production=car_data['year_of_production'], car_body=car_data['car_body'],
                                              engine_type=car_data['engine_type'])
            new_car.save()
            serializer = CarSpecsSerializer(new_car)
            return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        loggedin_user = request.user
        if loggedin_user == 'admin':
            car = self.get_object()
            car.delete()
            response_msg = {'message': 'car has been deleted'}
        else:
            response_msg = {'message': 'Not Allowed'}

        return Response(response_msg)



