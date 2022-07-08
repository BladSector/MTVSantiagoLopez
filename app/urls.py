from django.urls import path
from .views import base_templates, herencia_ejemplo

urlpatterns = [
    path('', base_templates),
    path('herencia_ejemplo/', herencia_ejemplo)

]
