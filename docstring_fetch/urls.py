"""Urls for docstring_fetch app"""

from django.urls import path

from .views import docstring_fetch, compute

urlpatterns = [
    path('', docstring_fetch, name='docstring-fetch'),
    path('compute/', compute, name='compute'),
]