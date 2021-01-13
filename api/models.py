from django.db import models


class CarPlan(models.Model):
    plan_name = models.CharField(max_length=64)
    years_of_warranty = models.PositiveIntegerField(default=1)
    financial_plan = models.CharField(max_length=20, default='unavailable')

    def __str__(self):
        return self.plan_name


class CarSpecs(models.Model):
    car_plan = models.ForeignKey(CarPlan, on_delete=models.SET_NULL, null=True)
    car_brand = models.CharField(max_length=24)
    car_model = models.CharField(max_length=50)
    year_of_production = models.IntegerField()
    car_body = models.CharField(max_length=24)
    engine_type = models.CharField(max_length=24)

    def __str__(self):
        return self.car_model

