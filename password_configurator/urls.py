"""Urls for password_configurator app"""

from django.urls import path

from .views import generate, password_configurator

urlpatterns = [
    path('', password_configurator, name='password-configurator'),
    path('generate/', generate, name='generate-password'),
]
