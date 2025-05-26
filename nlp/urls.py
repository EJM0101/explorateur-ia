from django.urls import path
from .views import index  # Supprimer chat_api

urlpatterns = [
    path('', index, name='nlp'),
]