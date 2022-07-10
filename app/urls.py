from django.urls import path
from .views import home, crear_santi, listado_santi, about

urlpatterns = [
    path('', home, name= 'home'),
    path('crear_santi/', crear_santi, name= 'crear_santi'),
    path('santis', listado_santi, name= 'listado_santi'),
    path('about/', about, name= 'about'),

]
