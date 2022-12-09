from django import forms
from AppBlog.models import *
 
class RecetaFormulario(forms.Form):
    ingrediente = forms.CharField()
    categoria = forms.CharField()
 
