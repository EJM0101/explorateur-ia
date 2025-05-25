from django.urls import path
from .views import index, chat_api

urlpatterns = [
    path('', index, name='nlp'),
    path('chat/', chat_api, name='chat_api'),
]