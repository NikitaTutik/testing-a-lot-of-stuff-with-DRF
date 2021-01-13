from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api2/', include('cars.urls')),
    path('api3/', include('posts.urls'))
]
