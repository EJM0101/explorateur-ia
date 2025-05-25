from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('base/', include('base.urls')),
    path('raisonnement/', include('raisonnement.urls')),
    path('nlp/', include('nlp.urls')),
    path('vision/', include('vision.urls')),
    path('connaissance/', include('connaissance.urls')),
    path('planning/', include('planning.urls')),
    path('robotique/', include('robotique.urls')),
    path('ml/', include('ml.urls')),
]