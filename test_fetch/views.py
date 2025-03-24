from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, "test_fetch/index.html")


def compute(request):
    nb1 = request.POST.get("nb1")
    nb2 = request.POST.get("nb2")
    return JsonResponse({"operation_result": int(nb1) + int(nb2)})
