from django.urls import path
from .views import home, template_ejemplo

urlpatterns = [
    path('', home),
    path('template_ejemplo/', template_ejemplo)

]
