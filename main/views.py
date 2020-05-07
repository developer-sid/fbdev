from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'main/index.html', {})
