from django import forms
from .models import Genero,Ramo,Seccion
from django.forms import ModelForm

class GeneroForm(ModelForm):
    class Meta:
        model=Genero
        fields="__all__"

class RamoForm(ModelForm):
    class Meta:
        model= Ramo
        fields="__all__"

class SeccionForm(ModelForm):
    class Meta:
        model=Seccion
        fields="__all__" 