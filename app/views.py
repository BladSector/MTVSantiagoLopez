from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import ejemplo

# Create your views here.

def home(request):
    return render(request, 'indexstartbootstrap.html')

#Template ejemplo
def template_ejemplo(request):
    #template = loader.get_template('index.html')
    ejemplo1 = ejemplo(nombre='Santi1')
    ejemplo2 = ejemplo(nombre='Santi2')
    ejemplo3 = ejemplo(nombre='Santi3')
    ejemplo1.save()
    ejemplo2.save()
    ejemplo3.save()
    #render = template.render({'lista_ejemplo': [ejemplo1, ejemplo2, ejemplo3)
    #return HttpResponse(render)
    return render(request, 'index.html', {'lista_ejemplo': [ejemplo1, ejemplo2,
    ejemplo3]})
