"""Views for password_configurator app"""
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from core.password_configurator.password_configurator import generate_password

def password_configurator(request: HttpRequest) -> HttpResponse:
    return render(request, "password_configurator/password_configurator.html")


def generate(request: HttpRequest) -> JsonResponse:
    length = request.POST.get("length")
    nb_uppers = request.POST.get("nb-uppers")
    nb_digits = request.POST.get("nb-digits")
    nb_special_chars = request.POST.get("nb-special-chars")
    print(f"length: {length}, uppers: {nb_uppers}, digits: {nb_digits}, special chars: {nb_special_chars}")
    a = JsonResponse({"password": generate_password(
        length=int(length),
        nb_digits=int(nb_digits),
        nb_uppers=int(nb_uppers),
        nb_special_chars=int(nb_special_chars),
    )})
    print(a)
    return a