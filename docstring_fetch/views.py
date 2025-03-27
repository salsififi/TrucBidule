from django.http import JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import render


def docstring_fetch(request: HttpRequest) -> HttpResponse:
    return render(request, "docstring_fetch/docstring_fetch.html")


def compute(request: HttpRequest) -> JsonResponse:
    nb1 = request.POST.get("nb1")
    nb2 = request.POST.get("nb2")
    return JsonResponse({"operation_result": int(nb1) + int(nb2)})
