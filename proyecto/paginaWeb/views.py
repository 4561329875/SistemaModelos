from django.http import HttpResponse
from django.shortcuts import render
from .forms import tablaPruevaForm, tablaVinculadaForm
from .models import tablaPrueva

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def ingresarTabla1(request):
    if request.method == "POST":
        form = tablaPruevaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Guardado")
    else:
        form = tablaPruevaForm()   
    return render(request, "ingresarTabla1.html", {"form": form})

def ingresarTabla2(request):
    if request.method == "POST":
        form = tablaVinculadaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Guardado")
    else:
        form = tablaVinculadaForm()   
    return render(request, "ingresarTabla1.html", {"form": form})
def verTabla1s(request):
    return render(request, "verTabla1.html", {"tablas": tablaPrueva.objects.all()})

def verTabla1Unica(request, id):
    return render(request, "verTablaUnica.html", {"tabla": tablaPrueva.objects.get(id=id).__dict__.items})