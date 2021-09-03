from django.shortcuts import render


def led(request):
    return render(request, 'base.html', {})
