from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Controller


def led(request):
    return render(request, 'base.html', context={'controllers': Controller.objects.all()})
