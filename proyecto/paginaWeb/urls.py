from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ingresarTabla1/", views.ingresarTabla1, name="ingresarTabla1"),
    path("ingresarTabla2/", views.ingresarTabla2, name="ingresarTabla2"),
    path("verTabla1s/", views.verTabla1s, name="verTabla1s"),
    path("verTabla1Unica/<int:id>/", views.verTabla1Unica, name="verTabla1Unica"),
    
]