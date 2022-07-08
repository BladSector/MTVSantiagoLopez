from django.urls import path
from .views import home, herencia_ejemplo

urlpatterns = [
    path('', home, name= 'home'),
    path('herencia_ejemplo/', herencia_ejemplo, name= 'herencia_ejemplo')

]
