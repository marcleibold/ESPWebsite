from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse

from .models import Controller


def led(request: HttpRequest) -> HttpResponse:
    return render(request, 'base.html', context={'controllers': Controller.objects.all()})
