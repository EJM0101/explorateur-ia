from django.urls import path
from .views import index, predict

urlpatterns = [
    path('', index, name='ml'),
    path('predict/', predict, name='ml_predict'),
]