from rest_framework import routers
from .views import PostViewset, PostRatesViewset

router = routers.DefaultRouter()
router.register('posts', PostViewset, basename='posts')
router.register('post-rates', PostRatesViewset, basename='post-rates')
