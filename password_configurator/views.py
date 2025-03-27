"""Views for password_configurator app"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def password_configurator(request: HttpRequest) -> HttpResponse:
    return render(request, "password_configurator/password_configurator.html")
