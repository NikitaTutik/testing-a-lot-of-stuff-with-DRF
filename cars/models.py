from django.db import models


class Cars(models.Model):
    car_brand = models.CharField(max_length=24)
    car_model = models.CharField(max_length=50)
    year_of_production = models.IntegerField()
    car_body = models.CharField(max_length=24)
    engine_type = models.CharField(max_length=24)

    def __str__(self):
        return self.car_model