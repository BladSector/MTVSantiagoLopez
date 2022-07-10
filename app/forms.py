from django import forms

class FormSanti(forms.Form):
    nombre = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    fecha_creacion = forms.DateField(required=False)

class BusquedaSanti(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)
