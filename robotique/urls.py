from django.urls import path
from .views import index, executer

urlpatterns = [
    path('', index, name='robotique'),
    path('executer/', executer, name='robotique_exec'),
]