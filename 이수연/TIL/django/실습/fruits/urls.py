from django.urls import path
from . import fruits

urlpatterns = [
    path('', views.fruits),
]
