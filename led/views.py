from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Controller


def led(request):
    template = loader.get_template('base.html')
    context = RequestContext(request, )
    return HttpResponse(template.render({'controllers': Controller.objects.all()}))
