from rest_framework import routers
from .views import CarSpecsViewset

router = routers.DefaultRouter()
router.register('car-specs', CarSpecsViewset, basename='car-specs'),
