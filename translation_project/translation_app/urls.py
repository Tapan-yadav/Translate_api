# django import
from django.urls import path

#inhouse app import
from .views import translate_text

urlpatterns = [
    path('translate/', translate_text, name='translate_text')
]

