from django.urls import path
from led import views

urlpatterns = [
    path('', views.led, name='led'),
]
