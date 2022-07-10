from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

from .models import Santi
from .forms import FormSanti
from .forms import BusquedaSanti

# Create your views here.

def base_templates(request):
    return render(request, 'base_templates.html')


def home(request):
    return render(request, 'index_1.html')


def crear_santi(request):

    if request.method == 'POST':
        form = FormSanti(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            fecha = data.get('fecha_creacion')

            santi = Santi(
                nombre=data.get('nombre'),
                edad=data.get('edad'),
                fecha_creacion=fecha if fecha else datetime.now())

            santi.save()

            listado_santi = Santi.objects.all()
            form = BusquedaSanti()
            return render(request, 'listado_santi.html', {'listado_santi':listado_santi, 'form': form})

        else:
            return render(request,'crear_santi.html', {'form': form})

    form_santi = FormSanti()
    return render(request, 'crear_santi.html', {'form': form_santi})

def listado_santi(request):

    nombre_busqueda= request.GET.get('nombre')

    if nombre_busqueda :
        listado_santi = Santi.objects.filter(nombre__icontains=nombre_busqueda)
    else:
        listado_santi = Santi.objects.all()

    form = BusquedaSanti()
    return render(request, 'listado_santi.html', {'listado_santi':listado_santi, 'form': form})

def about(request):
    return render(request, 'about.html')
