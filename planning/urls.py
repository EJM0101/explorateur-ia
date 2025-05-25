from django.urls import path
from .views import index, calculer

urlpatterns = [
    path('', index, name='planning'),
    path('calculer/', calculer, name='planning_calc'),
]