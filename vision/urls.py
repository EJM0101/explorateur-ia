from django.urls import path
from .views import index, detect

urlpatterns = [
    path('', index, name='vision'),
    path('detect/', detect, name='vision_detect'),
]